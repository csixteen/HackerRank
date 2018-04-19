#include <stdio.h>
#include <math.h>

long long int largest_factor(long long int n){
    while(!(n % 2)) {n /= 2;}

    if(n == 1) return 2;

    int i = 3;
    for(; i <= sqrt(n); i += 2) {while(!(n % i)) {n /= i;}}

    if(n > 2) return n;
    else return i-2;
}

int main(int argc, char **argv) {
    int t;
    long long int num;
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%lld", &num);
        printf("%lld\n", largest_factor(num));
    }
    return 0;
}
