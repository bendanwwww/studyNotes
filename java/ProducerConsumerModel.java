/**
 * 生产者消费者模型
 * 
 * @author liushuoyang03
 */
public class ProducerConsumerModel {

    private static int stock = 0;
    private static int maxStock = 10;
    private static Object lock = new Object();

    public void producer() throws InterruptedException {
        Thread.sleep(10);
        synchronized(lock) {
            if (stock >= maxStock) {
                System.out.println("producer wait " + stock);
                lock.wait();
            } else {
                stock++;
                System.out.println("producer add " + stock);
                lock.notify();
            }
        }
    }

    public void consumer() throws InterruptedException {
        Thread.sleep(10);
        synchronized(lock) {
            if (stock <= 0) {
                System.out.println("consumer wait " + stock);
                lock.wait();
            } else {
                stock--;
                System.out.println("consumer delete " + stock);
                lock.notify();
            }
        }
    }

    public static void main(String[] args) {
        ProducerConsumerModel producerConsumerModel = new ProducerConsumerModel();
        for (int i = 0 ; i < 50 ; i++) {
            new Thread(new ProducerThread(producerConsumerModel)).start();
        }
        for (int i = 0 ; i < 50 ; i++) {
            new Thread(new ConsumerThread(producerConsumerModel)).start();
        }
    }
}

class ProducerThread implements Runnable {

    private ProducerConsumerModel producerConsumerModel;

    public ProducerThread(ProducerConsumerModel producerConsumerModel) {
        this.producerConsumerModel = producerConsumerModel;
    }

    @Override
    public void run() {
        try {
            producerConsumerModel.producer();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

class ConsumerThread implements Runnable {

    private ProducerConsumerModel producerConsumerModel;

    public ConsumerThread(ProducerConsumerModel producerConsumerModel) {
        this.producerConsumerModel = producerConsumerModel;
    }

    @Override
    public void run() {
        try {
            producerConsumerModel.consumer();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}