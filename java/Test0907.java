import java.util.ArrayList;
import java.util.List;

public class Test0907 {

    public static void main(String[] args) {
        int[][] data = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
        Test0907.print(data);
    }

    public static void print(int[][] data) {
        List<String> printIndex = new ArrayList<>();
        // 0: 右 1: 下 2: 左 3: 上
        int state = 0;
        int c = 0;
        int r = 0;
        boolean needPrint = true;
        for (;;) {
            if (printIndex.size() == data.length * data[0].length) {
                break;
            }
            if (needPrint) {
                System.out.println(data[c][r]);
                printIndex.add(c + "," + r);
            }
            needPrint = true;
            if (state == 0) {
                if (r + 1 < data[c].length && !printIndex.contains(c + "," + (r + 1))) {
                    r += 1;
                    continue;
                } else {
                    state = 1;
                }
            }
            if (state == 1) {
                if (c + 1 < data.length && !printIndex.contains((c + 1) + "," + r)) {
                    c += 1;
                    continue;
                } else {
                    state = 2;
                }
            }
            if (state == 2) {
                if (r - 1 >= 0 && !printIndex.contains(c + "," + (r - 1))) {
                    r -= 1;
                    continue;
                } else {
                    state = 3;
                }
            }
            if (state == 3) {
                if (c - 1 >= 0 && !printIndex.contains((c - 1) + "," + r)) {
                    c -= 1;
                    continue;
                } else {
                    state = 0;
                    needPrint = false;
                }
            }
        }
    }
    
}

/**
 * 
 * 顺时针循环遍历打印二维数组，
 * [
 * [1,2,3,4],
 * [5,6,7,8],
 * [9,10,11,12]
 * ],输出1 2 3 4 8 12 11 10 9 5 6 7
 */