// integer_factorization.cpp - Naive prime factorization.
// Author: Scott

#include <iostream>
using namespace std;

void factorize(int n) {
    cout << "Prime factors of " << n << ": ";
    for (int i = 2; i*i <= n; ++i) {
        while (n % i == 0) {
            cout << i << " ";
            n /= i;
        }
    }
    if (n > 1) cout << n;
    cout << endl;
}

int main() {
    int n = 100;
    cout << "Enter number to factor (default 100): ";
    string input;
    getline(cin, input);
    if (!input.empty()) n = stoi(input);

    factorize(n);
    return 0;
}
