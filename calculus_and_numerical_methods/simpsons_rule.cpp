
/**
 * Simpson's Rule for Numerical Integration
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>

double f(double x) {
    return std::sin(x);  // Example function
}

double simpson(double a, double b, int n) {
    if (n % 2 != 0) n++; // Ensure even number of intervals
    double h = (b - a) / n;
    double result = f(a) + f(b);
    for (int i = 1; i < n; i += 2)
        result += 4 * f(a + i * h);
    for (int i = 2; i < n; i += 2)
        result += 2 * f(a + i * h);
    return result * h / 3;
}

int main() {
    std::cout << "Approx ∫sin(x) from 0 to π ≈ " << simpson(0, M_PI, 100) << std::endl;
    return 0;
}
