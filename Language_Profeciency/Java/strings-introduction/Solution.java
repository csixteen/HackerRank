import java.util.Scanner;

public class Solution {
    private static String capitalize(String s) {
        return s.substring(0,1).toUpperCase() + s.substring(1);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();

        System.out.println(a.length() + b.length());
        System.out.println(a.compareTo(b) > 0 ? "Yes" : "No");
        System.out.println(capitalize(a) + " " + capitalize(b));
    }
}
