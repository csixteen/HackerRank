import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        String r = new StringBuilder(s).reverse().toString();
        System.out.println(s.compareTo(r) == 0 ? "Yes" : "No");
    }
}
