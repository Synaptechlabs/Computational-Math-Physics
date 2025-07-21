// triangle_area_heron.cpp - Compute the area of a triangle using Heron's formula.
// Author: Scott

#include <iostream>
#include <cmath>
using namespace std;

double heron_area(double a, double b, double c) {
    double s = (a + b + c) / 2.0;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

int main() {
    double a = 3, b = 4, c = 5;
    string input;

    cout << "Enter side a (default 3): ";
    getline(cin, input);
    if (!input.empty()) a = stod(input);

    cout << "Enter side b (default 4): ";
    getline(cin, input);
    if (!input.empty()) b = stod(input);

    cout << "Enter side c (default 5): ";
    getline(cin, input);
    if (!input.empty()) c = stod(input);

    double area = heron_area(a, b, c);
    cout << "Area of triangle = " << area << endl;
    return 0;
}
