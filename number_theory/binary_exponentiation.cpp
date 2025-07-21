// binary_exponentiation.cpp - Compute (base^exp) % mod efficiently.
// Author: Scott

#include <iostream>
using namespace std;

long long binpow(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) result = result * base % mod;
        base = base * base % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    long long base = 2, exp = 10, mod = 1000;
    string input;

    cout << "Enter base (default 2): ";
    getline(cin, input);
    if (!input.empty()) base = stoll(input);

    cout << "Enter exponent (default 10): ";
    getline(cin, input);
    if (!input.empty()) exp = stoll(input);

    cout << "Enter modulus (default 1000): ";
    getline(cin, input);
    if (!input.empty()) mod = stoll(input);

    cout << "(" << base << "^" << exp << ") % " << mod << " = " << binpow(base, exp, mod) << endl;
    return 0;
}
