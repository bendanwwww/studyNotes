public class MyLock extends MyAbstractQueuedSynchronizer {

    public boolean getLock() {
        return compareAndSetState(0, 1);
    }

    public boolean releaseLock() {
        return compareAndSetState(1, 0);
    }

    public static void main(String[] args) {
        MyLock lock = new MyLock();
        // 获取锁
        lock.tryGetLock();
        System.out.println("run");
        // 释放锁
        lock.tryReleaseLock();
    }

}