
/**
 * Taylor Series Approximations for e^x, sin(x), cos(x)
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>

double exp_taylor(double x, int n = 10) {
    double sum = 1.0;
    double term = 1.0;
    for (int i = 1; i <= n; ++i) {
        term *= x / i;
        sum += term;
    }
    return sum;
}

int main() {
    double x = 1.0;
    std::cout << "e^1 ≈ " << exp_taylor(x) << std::endl;
    return 0;
}
