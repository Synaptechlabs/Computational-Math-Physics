
/**
 * 4th Order Runge-Kutta Method for Solving ODEs
 * dy/dx = f(x, y)
 * Author: Scott Douglass
 * License: MIT
 */

#include <iostream>
#include <cmath>

double f(double x, double y) {
    return x + y;  // Example: dy/dx = x + y
}

double runge_kutta(double x0, double y0, double h, double x_end) {
    while (x0 < x_end) {
        double k1 = h * f(x0, y0);
        double k2 = h * f(x0 + h/2, y0 + k1/2);
        double k3 = h * f(x0 + h/2, y0 + k2/2);
        double k4 = h * f(x0 + h, y0 + k3);
        y0 += (k1 + 2*k2 + 2*k3 + k4)/6;
        x0 += h;
    }
    return y0;
}

int main() {
    std::cout << "Approx y(1) ≈ " << runge_kutta(0, 1, 0.1, 1.0) << std::endl;
    return 0;
}
