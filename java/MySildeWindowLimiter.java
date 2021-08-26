import java.util.concurrent.atomic.AtomicInteger;

public class MySildeWindowLimiter {

    /** 限流窗口时间 */
    private long limiterTime;
    /** 滑动窗口数量 */
    private int windowsSize;
    /** 限流数量 */
    private long limiterNumber;
    /** 当前窗口索引 */
    private int nowWindowsIndex;
    /** 滑动窗口时间 */
    private long changeWindowTime;
    /** 滑动窗口 */
    private AtomicInteger[] limitWindows;
    /** 当前通过请求 */
    private AtomicInteger acquireNumber;
    /** 上次请求时间 */
    private long lastReqTime;

    private MySildeWindowLimiter() {}

    public MySildeWindowLimiter(long limiterTime, int windowsSize, long limiterNumber) {
        this.limiterTime = limiterTime;
        this.windowsSize = windowsSize;
        this.limiterNumber = limiterNumber;
        this.nowWindowsIndex = 0;
        this.changeWindowTime = limiterTime / windowsSize;
        this.limitWindows = new AtomicInteger[windowsSize];
        this.acquireNumber = new AtomicInteger(0);
        this.lastReqTime = 0;
        for (int i = 0 ; i < windowsSize ; i++) {
            this.limitWindows[i] = new AtomicInteger(0);
        }
    }

    /**
     * 尝试通过限流
     * @return
     */
    public boolean tryAcquire() {
        // 计算需要移动多少个窗口
        long intervalTime = System.currentTimeMillis() - lastReqTime;
        // 滑动窗口
        sildeWindow((int) (intervalTime / changeWindowTime));
        // 更新此次请求时间
        lastReqTime = System.currentTimeMillis();
        // 计算是否超过最大请求次数
        if (acquireNumber.get() > limiterNumber) {
            return false;
        }
        // 请求放行
        acquireNumber.getAndAdd(1);
        limitWindows[nowWindowsIndex].getAndAdd(1);
        return true;
    }

    /**
     * 移动窗口
     * @param num 移动窗口的数量
     */
    public synchronized void sildeWindow(int num) {
        for (int i = 0 ; i < num ; i++) {
            // 移动一个窗口
            acquireNumber.getAndAdd(-limitWindows[i].get());
            limitWindows[i] = new AtomicInteger(0);
            // 滑动窗口指针后移
            if (nowWindowsIndex == limitWindows.length - 1) {
                nowWindowsIndex = 0;
            } else {
                nowWindowsIndex++;
            }
        }
    }
}