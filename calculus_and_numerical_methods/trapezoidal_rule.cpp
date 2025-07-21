
/**
 * Trapezoidal Rule for Numerical Integration
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>

double f(double x) {
    return std::sin(x);  // Example function
}

double trapezoidal(double a, double b, int n) {
    double h = (b - a) / n;
    double result = 0.5 * (f(a) + f(b));
    for (int i = 1; i < n; ++i)
        result += f(a + i * h);
    return result * h;
}

int main() {
    std::cout << "Approx ∫sin(x) from 0 to π ≈ " << trapezoidal(0, M_PI, 100) << std::endl;
    return 0;
}
