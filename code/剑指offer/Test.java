public class Test {

    // 加密规则 (具体规则忘掉了。。。)
    public static final int[] ENCRYPTION = {5, 4, 3, 2, 1};

    public static int[] change(int[] data) {
        int[] res = new int[data.length];
        for (int i = 0 ; i < data.length ; i++) {
            res[i] = Test.ENCRYPTION[data[i] - 1];
        }
        return res;
    }
    
}