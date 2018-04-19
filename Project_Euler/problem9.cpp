#include <iostream>
#include <cmath>
using namespace std;

int find_abc(int s);

int main() {
    int t, n;
    cin >> t;
    for(int i = 0; i < t; ++i) {
        cin >> n;
        cout << find_abc(n) << endl;
    }

    return 0;
}

int find_abc(int s) {
    int c, maximum = -1;
    for(int a = 3; a <= ((s - 3) / 3); a++) {
        for(int b = a+1; b <= ((s - 1 - a) / 2); b++) {
            c = s - a - b;
            if(c*c == (a*a) + (b*b)) {
                int res = a*b*c;
                maximum = res > maximum ? res : maximum;
            }
        }
    }

    return maximum;
}
