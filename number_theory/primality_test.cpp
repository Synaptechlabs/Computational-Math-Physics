// primality_test.cpp - Check if a number is prime using trial division.
// Author: Scott

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); ++i)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int n = 29;
    cout << "Enter integer to test (default 29): ";
    string input;
    getline(cin, input);
    if (!input.empty()) n = stoi(input);

    if (is_prime(n))
        cout << n << " is prime." << endl;
    else
        cout << n << " is not prime." << endl;
    return 0;
}
