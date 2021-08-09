import java.lang.reflect.Field;

import sun.misc.Unsafe;

public abstract class MyAbstractQueuedSynchronizer {

    // 队列node结构
    class AqsQueueNode {

        /** 线程等待状态 (0: 执行中 1: 阻塞中 2: 已废弃) */
        private int waitState;
        /** 等待线程 */
        private Thread queueThread;
        /** 前置节点 */
        private AqsQueueNode prev;
        /** 后置节点 */
        private AqsQueueNode next;
        /** 下一个等待节点 */
        private AqsQueueNode nextWait;

        public int getWaitState() {
            return waitState;
        }
    
        public void setWaitState(int waitState) {
            this.waitState = waitState;
        }
    
        public Thread getQueueThread() {
            return queueThread;
        }
    
        public void setQueueThread(Thread queueThread) {
            this.queueThread = queueThread;
        }
    
        public AqsQueueNode getPrev() {
            return prev;
        }
    
        public void setPrev(AqsQueueNode prev) {
            this.prev = prev;
        }
    
        public AqsQueueNode getNext() {
            return next;
        }
    
        public void setNext(AqsQueueNode next) {
            this.next = next;
        }
    
        public AqsQueueNode getNextWait() {
            return nextWait;
        }
    
        public void setNextWait(AqsQueueNode nextWait) {
            this.nextWait = nextWait;
        }

    }

    /** 资源锁定状态 */
    protected volatile int lockState;
    /** 等待队列头 */
    private AqsQueueNode head;
    /** 等待队列尾 */
    private AqsQueueNode tail;
    /** cas操作类 */
    private static final Unsafe unsafe;

    private static final long lockStateOffset;
    private static final long headOffset;
    private static final long tailOffset;

    static {
        try {
            // 获取unsafe类
            Field field = Unsafe.class.getDeclaredField("theUnsafe");
            field.setAccessible(true);
            unsafe = (Unsafe) field.get(null);
            // 获取域偏移量
            lockStateOffset = unsafe.objectFieldOffset(MyAbstractQueuedSynchronizer.class.getDeclaredField("lockState"));
            headOffset = unsafe.objectFieldOffset(MyAbstractQueuedSynchronizer.class.getDeclaredField("head"));
            tailOffset = unsafe.objectFieldOffset(MyAbstractQueuedSynchronizer.class.getDeclaredField("tail"));
        } catch(Exception e) {
            throw new Error(e);
        }
    }

    /**
     * 获取锁逻辑
     */
    abstract boolean getLock();

    /**
     * 释放锁逻辑
     */
    abstract boolean releaseLock();

    /**
     * 尝试获取锁
     */
    protected void tryGetLock() {
        // 若无法获取锁 则加入等待队列
        if (!getLock()) {
            // LockSupport.park();
            // 阻塞线程
            unsafe.park(false, 0L);
            // 加入等待队列
            addThreadInAqsQueue(Thread.currentThread());
        }
    }

    /**
     * 尝试释放
     */
    protected void tryReleaseLock() {
        // 释放锁
        releaseLock();
        // 从等待队列中获取一个等待线程并唤醒
        getWaitThreadInAqsQueue();
    }

    /**
     * 加入等待队列
     * @param currentThread
     */
    private void addThreadInAqsQueue(Thread currentThread) {
        // 初始化节点
        AqsQueueNode newTail = new AqsQueueNode();
        newTail.setQueueThread(currentThread);
        newTail.setWaitState(1);
        AqsQueueNode t = this.tail;
        // 保证一定插入成功
        for (;;) {
            // 若队列为空
            if (t == null) {
                if (compareAndSetHead(head, newTail)) {
                    this.head = newTail;
                    return;
                }
            } else {
                if (compareAndSetTail(t, newTail)) {
                    t.setNext(newTail);
                    newTail.setPrev(t);
                    return;
                }
            }
        }
    }

    /**
     * 从等待队列里获取一个等待线程
     * @return
     */
    private void getWaitThreadInAqsQueue() {
        // 从头结点遍历 找到一个阻塞线程
        AqsQueueNode node = head;
        while (node != null) {
            if (node.getWaitState() == 1) {
                break;
            }
        }
        // 尝试获取锁
        if (node != null) {
            if (getLock()) {
                // 唤醒线程
                unsafe.unpark(node.getQueueThread());
                // 移除节点
                node.prev.next = node.next;
            }
        }
    }

    /**
     * 修改锁标志位
     * @param expect
     * @param update
     * @return
     */
    protected final boolean compareAndSetState(int expect, int update) {
        return unsafe.compareAndSwapInt(this, lockStateOffset, expect, update);
    }

    /**
     * 修改等待队列尾
     * @param expect
     * @param update
     * @return
     */
    protected final boolean compareAndSetTail(AqsQueueNode expect, AqsQueueNode update) {
        return unsafe.compareAndSwapObject(this, tailOffset, expect, update);
    }

    /**
     * 修改等待队列头
     * @param expect
     * @param update
     * @return
     */
    protected final boolean compareAndSetHead(AqsQueueNode expect, AqsQueueNode update) {
        return unsafe.compareAndSwapObject(this, headOffset, expect, update);
    }
}