#include <iostream>
#include <vector>
using namespace std;

vector<int> current_primes;
int is_prime(int n);

int main(){
    int t, num, candidate, count;
    current_primes.push_back(2);
    current_primes.push_back(3);
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> num;
        if(num <= current_primes.size()) {
            cout << current_primes[num-1] << endl;
        }
        else {
            candidate = current_primes.back();
            count = current_primes.size()+1;
            while(count <= num) {
                candidate += 2;
                if(is_prime(candidate)) {
                    current_primes.push_back(candidate);
                    count++;
                }
            }
            cout << candidate << endl;
        }
    }

    return 0;
}

int is_prime(int n){
    for(vector<int>::iterator it = current_primes.begin(); it != current_primes.end(); ++it) {
        if(!(n % *it)) {
            return 0;
        }
    }
    return 1;
}
