import java.util.Scanner;

public class Solution {
    private static int B;
    private static int H;
    private static boolean flag;

    static {
        Scanner in = new Scanner(System.in);
        B = in.nextInt();
        H = in.nextInt();
        if (B > 0 && H > 0) {
            flag = true;
        }
        else {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }

    public static void main(String[] args) {
        if (flag) {
            System.out.println(B * H);
        }
    }
}
