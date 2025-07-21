// chinese_remainder_theorem.cpp - Solve system of congruences using CRT.
// Author: Scott

#include <iostream>
#include <vector>
using namespace std;

int mod_inverse(int a, int m) {
    int m0 = m, t, q;
    int x0 = 0, x1 = 1;

    if (m == 1) return 0;

    while (a > 1) {
        q = a / m;
        t = m;

        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0) x1 += m0;
    return x1;
}

int chinese_remainder(vector<int> num, vector<int> rem) {
    int prod = 1;
    for (int n : num) prod *= n;

    int result = 0;
    for (int i = 0; i < num.size(); ++i) {
        int pp = prod / num[i];
        result += rem[i] * mod_inverse(pp, num[i]) * pp;
    }
    return result % prod;
}

int main() {
    vector<int> num = {3, 5, 7};
    vector<int> rem = {2, 3, 2};

    cout << "Solving system: x ≡ 2 mod 3, x ≡ 3 mod 5, x ≡ 2 mod 7" << endl;
    int result = chinese_remainder(num, rem);
    cout << "Solution x = " << result << endl;
    return 0;
}
