#include <stdio.h>
#include <stdlib.h>

void print_pattern(int N) {
    int l, c, len = N*2 - 1;
    for (int i = 0; i < len; ++i) {
        for (int j = 0; j < len; ++j) {
            l = abs(N-i) + (i >= N ? 2 : 0);
            c = abs(N-j) + (j >= N ? 2 : 0);
            printf("%d ", l > c ? l : c);
        }
        printf("\n");
    }
}

int main(int argc, char** argv) {
    int n;
    scanf("%d", &n);
    print_pattern(n);

    return 0;
}
