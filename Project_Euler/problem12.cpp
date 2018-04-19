#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

#define PRIMES_SIZE 65500
vector<int> primes;

void fill_primes();
long int find_triangle(int n);

int main(int argc, char **argv) {
    fill_primes();
    int t, num;
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> num;
        cout << find_triangle(num) << endl;
    }

    return 0;
}

void fill_primes() {
    vector<int> aux(PRIMES_SIZE*11, 1);
    int j, c;
    for(int i = 2; i <= 256; i++) {
        if(aux[i] == 1) {
            j = i*i, c = 0;
            while(j <= PRIMES_SIZE*11) {
                aux[j] = 0;
                c++;
                j = i*i + c*i;
            }
        }
    }

    aux.erase(aux.begin(), aux.begin()+2);

    for(int i = 0, j = 0; i < PRIMES_SIZE*11 && j < PRIMES_SIZE; i++) {
        if(aux[i] == 1) {
            primes.push_back(i+2);
            j++;
        }
    }
}

long int find_triangle(int lim) {
    if(lim == 1)
        return 3;

    long int n = 3;
    int n1, dn1, i, exponent, counter = 0, dn = 2;
    while(counter <= lim) {
        n += 1;
        n1 = n;
        if(!(n1 % 2)) n1 /= 2;
        dn1 = 1;
        for(i = 0; i < PRIMES_SIZE; i++) {
            if(primes[i]*primes[i] > n1) {
                dn1 *= 2;
                break;
            }

            exponent = 1;
            while(!(n1 % primes[i])) {
                exponent++;
                n1 /= primes[i];
            }
            if(exponent > 1)
                dn1 *= exponent;
            if(n1 == 1)
                break;
        }
        counter = dn*dn1;
        dn = dn1;
    }

    return n*(n-1)/2;
}
