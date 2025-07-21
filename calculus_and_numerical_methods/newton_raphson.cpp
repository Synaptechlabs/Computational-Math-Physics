
/**
 * Newton-Raphson Method for Root Finding
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>

double f(double x) {
    return x*x - 2;
}

double df(double x) {
    return 2*x;
}

double newton(double x0, int max_iter = 20, double tol = 1e-6) {
    double x = x0;
    for (int i = 0; i < max_iter; ++i) {
        double x_new = x - f(x)/df(x);
        if (std::fabs(x_new - x) < tol) return x_new;
        x = x_new;
    }
    return x;
}

int main() {
    std::cout << "Root ≈ " << newton(1.0) << std::endl;
    return 0;
}
