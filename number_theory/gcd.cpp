// gcd.cpp - Compute the Greatest Common Divisor (GCD) using the Euclidean algorithm.
// Author: Scott

#include <iostream>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    int a = 12, b = 18;
    cout << "Enter first integer (default 12): ";
    string input;
    getline(cin, input);
    if (!input.empty()) a = stoi(input);

    cout << "Enter second integer (default 18): ";
    getline(cin, input);
    if (!input.empty()) b = stoi(input);

    cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << endl;
    return 0;
}
