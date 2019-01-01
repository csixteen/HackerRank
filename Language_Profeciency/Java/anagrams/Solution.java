import java.util.Scanner;

public class Solution {
    private static boolean isAnagram(String a, String b) {
        if (a == null || b == null || a.length() != b.length())
            return false;

        String aL = a.toLowerCase();
        String bL = b.toLowerCase();
        char[] aFreq = new char[26];
        char[] bFreq = new char[26];

        int offset = (int) 'a';
        for (int i = 0; i < aL.length(); i++) {
            aFreq[((int)aL.charAt(i))-offset] += 1;
            bFreq[((int)bL.charAt(i))-offset] += 1;
        }
        for (int i = 0; i < 26; i++)
            if (aFreq[i] != bFreq[i])
                return false;

        return true;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        System.out.println(isAnagram(a,b) ? "Anagrams" : "Not Anagrams");
    }
}
