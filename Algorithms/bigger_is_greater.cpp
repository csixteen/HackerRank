#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string find_bigger(string s);

int main() {
    int t;
    string s;
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> s;
        cout << find_bigger(s) << endl;
    }

    return 0;
}

string find_bigger(string s){
    if((s.size() == 1) || (count(s.begin(), s.end(), s[0]) == s.size())) {
        return "no answer";
    }

    string s2(s);
    do {
        if(s2 > s) return s2;
    } while(next_permutation(s2.begin(), s2.end()));

    return "no answer";
}
