#include <stdio.h>

int is_divisible(long int n, int e) {
    for(int i = 1; i <= e; i++) {
        if(n % i) return 0;
    }
    return 1;
}

int main() {
    int t, num;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        long int x = 1;
        scanf("%d", &num);
        while(1) {
            if(is_divisible(x, num)) break;
            x++;
        }
        printf("%ld\n", x);
    }
    return 0;
}
