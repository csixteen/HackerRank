import java.util.Scanner;

public class Solution {
    private static String getSmallestAndLargest(String s, int k) {
        String smallest = s;
        String largest = "";

        for (int i = 0; i <= s.length() - k; i++) {
            String tmp = s.substring(i, i + k);
            if (tmp.compareTo(smallest) < 0) {
                smallest = tmp;
            }
            if (tmp.compareTo(largest) > 0) {
                largest = tmp;
            }
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int k = in.nextInt();
        in.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
