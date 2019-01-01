import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            String s = in.next();
            try {
                long x = (new Long(s)).longValue();
                System.out.println(s + " can be fitted in:");
                if(x >= -128 && x <= 127) 
                    System.out.println("* byte");
                if(x >= -32768 && x <= 32767) 
                    System.out.println("* short");
                if(x >= -2147483648 && x <= 2147483647)
                    System.out.println("* int");
                if(x >= -Math.pow(2,63) && x <= Math.pow(2,63)-1)
                    System.out.println("* long");
            }
            catch(Exception e) {
                System.out.println(s + "can't be fitted anywhere.");
            }
        }
    }
}
