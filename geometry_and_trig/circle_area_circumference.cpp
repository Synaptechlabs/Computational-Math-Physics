// circle_area_circumference.cpp - Compute area and circumference of a circle from radius.
// Author: Scott

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double r = 1.0;
    string input;

    cout << "Enter radius (default 1.0): ";
    getline(cin, input);
    if (!input.empty()) r = stod(input);

    double area = M_PI * r * r;
    double circ = 2 * M_PI * r;

    cout << "Area = " << area << ", Circumference = " << circ << endl;
    return 0;
}
