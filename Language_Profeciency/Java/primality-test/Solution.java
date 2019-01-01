import java.util.Scanner;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String n = in.next();
        BigInteger i = new BigInteger(n);
        System.out.println(i.isProbablePrime(1) ? "prime" : "not prime");
    }
}
