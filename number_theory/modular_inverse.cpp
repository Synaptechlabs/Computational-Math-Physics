// modular_inverse.cpp - Compute modular inverse using the Extended Euclidean Algorithm.
// Author: Scott

#include <iostream>
using namespace std;

int extended_euclidean(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    int x1, y1;
    int g = extended_euclidean(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int mod_inverse(int a, int m) {
    int x, y;
    int g = extended_euclidean(a, m, x, y);
    if (g != 1)
        return -1;  // No inverse
    return (x % m + m) % m;
}

int main() {
    int a = 3, m = 11;
    cout << "Enter number (default 3): ";
    string input;
    getline(cin, input);
    if (!input.empty()) a = stoi(input);

    cout << "Enter modulus (default 11): ";
    getline(cin, input);
    if (!input.empty()) m = stoi(input);

    int inv = mod_inverse(a, m);
    if (inv == -1)
        cout << "No modular inverse exists for " << a << " mod " << m << endl;
    else
        cout << "Modular inverse of " << a << " mod " << m << " = " << inv << endl;
    return 0;
}
