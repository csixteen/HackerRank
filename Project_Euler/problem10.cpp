#include <iostream>
#include <vector>
using namespace std;

vector<int> primes(1000000, 1);
vector<long long int> sums(1000000, 0);

void fill_primes();

int main() {
    fill_primes();
    int t;
    long int n;
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> n;
        cout << sums[n-2] << endl;
    }

    return 0;
}

/*
 * Sieve of Eratosthenes
 * */
void fill_primes() {
    int j, c;
    for(int i = 2; i <= 1000; i++) {
        if(primes[i] == 1) {
            j = i*i, c = 0;
            while(j <= 1000000) {
                primes[j] = 0;
                c++;
                j = i*i + c*i;
            }
        }
    }

    primes.erase(primes.begin(), primes.begin()+2);
    long long int tmp = 0;
    for(int i = 0; i < 999999; i++) {
        if(primes[i] == 1) {
            tmp += i+2;
        }
        sums[i] = tmp;
    }
}
