#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_palindrome(long int n) {
    long int reversedInteger = 0, remainder, originalInteger = n;
    while(n != 0) {
        remainder = n % 10;
        reversedInteger = reversedInteger*10 + remainder;
        n /= 10;
    }
    return originalInteger == reversedInteger;
}

int main() {
    int t, num;
    scanf("%d", &t);
    for(int z = 0; z < t; z++) {
        scanf("%d", &num);
        long int pal = 0;
        for(int i = 100; i < 1000; i++) {
            for(int j = 100; j < 1000; j++) {
                long int x = i*j;
                if(is_palindrome(x) && (x > pal) && (x < num)) {
                    pal = x;
                }
            }
        }
        printf("%ld\n", pal);
    }
    return 0;
}
