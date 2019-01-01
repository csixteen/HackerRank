import java.util.Scanner;

public class Solution {
    private static void series(int a, int b, int n) {
        int acc = a;
        for (int i = 0; i < n; i++) {
            acc += ((int)Math.pow(2, i)) * b;
            System.out.format("%d ", acc);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        for (int i = 0; i < q; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            series(a, b, n);
        }
    }
}
