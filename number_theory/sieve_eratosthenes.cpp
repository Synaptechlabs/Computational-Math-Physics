// sieve_eratosthenes.cpp - Generate prime numbers up to N using the Sieve of Eratosthenes.
// Author: Scott

#include <iostream>
#include <vector>
using namespace std;

void sieve(int n) {
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p*p <= n; ++p)
        if (is_prime[p])
            for (int i = p*p; i <= n; i += p)
                is_prime[i] = false;

    cout << "Primes up to " << n << ": ";
    for (int i = 2; i <= n; ++i)
        if (is_prime[i]) cout << i << " ";
    cout << endl;
}

int main() {
    int n = 100;
    cout << "Generate primes up to (default 100): ";
    string input;
    getline(cin, input);
    if (!input.empty()) n = stoi(input);

    sieve(n);
    return 0;
}
