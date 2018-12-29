import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();
        for (int i = 1; i <= 10; i++) {
            System.out.format("%d x %d = %d%n", N, i, N*i);
        }
    }
}
