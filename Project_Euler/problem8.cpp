#include <iostream>
#include <string>
using namespace std;

int main() {
    int t, n, k;
    string num;
    cin >> t;
    for(int x = 0; x < t; x++) {
        long int previous_biggest = 0;
        int d = scanf("%d %d", &n, &k);
        cin >> num;
        for(int i = 0; i < n - k - 1; i++) {
            long int c = num[i] - '0';
            int j = 1;
            while(j < k) {
                int res = num[i+j] - '0';
                c *= res;
                j++;
            }

            if(c > previous_biggest) {
                previous_biggest = c;
            }
        }
        cout << previous_biggest << endl;
    }

    return 0;
}
