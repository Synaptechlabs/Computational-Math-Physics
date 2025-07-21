
/**
 * Finite Difference Approximation
 * Approximates the derivative of a function using forward difference.
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>
#include <functional>

double f(double x) {
    return std::sin(x);  // Example function
}

double finite_difference(double x, double h) {
    return (f(x + h) - f(x)) / h;
}

int main() {
    double x = M_PI / 4;
    double h = 1e-5;
    std::cout << "f'(" << x << ") ≈ " << finite_difference(x, h) << std::endl;
    return 0;
}
