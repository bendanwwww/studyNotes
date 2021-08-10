import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class MyThreadExecutorPool {

    /** 核心池大小 */
    private int coreSize;
    /** 最大池大小 */
    private int maxSize;
    /** 拒绝策略 */
    private RejectedExecutionHandler rejectedHandler;
    /** 线程池等待队列 */
    private BlockingQueue<Thread> executorQueue;
    /** 线程池集合 */
    private Map<ExecutorThread, Thread> executorThreadMap;

    public MyThreadExecutorPool(int coreSize, int maxSize, BlockingQueue executorQueue, 
                                RejectedExecutionHandler rejectedHandler) {
        this.coreSize = coreSize;
        this.maxSize = maxSize;
        this.rejectedHandler = rejectedHandler;
        this.executorQueue = executorQueue;
        // 初始化线程池
        this.executorThreadMap = new HashMap<>();
        for (int i = 0 ; i < this.coreSize ; i++) {
            ExecutorThread et = new ExecutorThread(false, executorQueue);
            Thread t = new Thread(et);
            this.executorThreadMap.put(et, t);
            t.start();
        }
        // 初始化一个回收多余线程的线程
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    for (ExecutorThread et : new HashSet<>(executorThreadMap.keySet())) {
                        if (et.getIsExtra() && et.tryLock()) {
                            et.lock();
                            et.stop();
                            et.unlock();
                            executorThreadMap.remove(et);
                        }
                    }
                }
            }
        }).start();
    }

    /**
     * 提交任务
     * @param t
     */
    public void execut(Thread t) throws Exception {
        // 放入等待队列中
        if (!executorQueue.offer(t)) {
            // 若 等待队列已满
            // 若 超过最大池大小 执行拒绝策略 否则新开线程执行
            if (executorThreadMap.size() >= this.maxSize) {
                rejectedHandler.reject(t);
            } else {
                ExecutorThread et = new ExecutorThread(true, t, executorQueue);
                Thread newThread = new Thread(et);
                executorThreadMap.put(et, newThread);
                t.start();
            }
        }
    }

    // 拒绝策略接口
    interface RejectedExecutionHandler {
        // 拒绝策略
        void reject(Thread t);
    }

    // 线程池线程类
    class ExecutorThread implements Runnable {

        /** 立刻执行任务 */
        private Thread firstTask;
        /** 是否为额外线程 */
        private boolean isExtra;
        /** 是否需要运行 */
        private boolean isRun = true;
        /** 等待队列 */
        private BlockingQueue<Thread> executorQueue;
        /** 线程是否正在执行 锁 */
        private Lock runLock = new ReentrantLock();

        public ExecutorThread(boolean isExtra, BlockingQueue<Thread> executorQueue) {
            this.isExtra = isExtra; 
            this.executorQueue = executorQueue;
        }

        public ExecutorThread(boolean isExtra, Thread firstTask, BlockingQueue<Thread> executorQueue) {
            this.isExtra = isExtra; 
            this.firstTask = firstTask; 
            this.executorQueue = executorQueue;
        }

        @Override
        public void run() {
            // 先执行需要立刻执行的任务
            if (firstTask != null) {
                lock();
                firstTask.run();
                firstTask = null;
                unlock();
            }
            // 轮询任务
            while (isRun) {
                try {
                    Thread runThread = executorQueue.take();
                    lock();
                    runThread.run();
                    unlock();
                } catch(Exception e) {
                    e.printStackTrace();
                }
            }

        }

        public boolean getIsExtra() {
            return isExtra;
        }

        public void setIsExtra(boolean isExtra) {
            this.isExtra = isExtra; 
        }

        public void lock() {
            runLock.lock();
        }

        public boolean tryLock() {
            return runLock.tryLock();
        }

        public void unlock() {
            runLock.unlock();
        }

        public void stop() {
            System.out.println("超出核心池大小 丢弃线程");
            this.isRun = false;
        }        

    }

    public static void main(String[] args) {
        MyThreadExecutorPool threadPool = new MyThreadExecutorPool(5, 10, new ArrayBlockingQueue(5), t -> {
            System.out.println("任务被丢弃");
        });
        for (int i = 0 ; i < 30 ; i++) {
            int index = i;
            try {
                threadPool.execut(new Thread(new Runnable() {
                    @Override
                    public void run() {
                        System.out.println("任务" + index + "执行 " + Thread.currentThread().getName());
                        try {
                            Thread.sleep(3000);
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                }));
            } catch(Exception e) {
                e.printStackTrace();
            }
        }
    }
}