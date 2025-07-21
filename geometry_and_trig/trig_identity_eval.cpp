// trig_identity_eval.cpp - Evaluate basic trig identities given an angle in degrees.
// Author: Scott

#include <iostream>
#include <cmath>
using namespace std;

const double DEG2RAD = M_PI / 180.0;

int main() {
    double angle_deg = 45.0;
    string input;

    cout << "Enter angle in degrees (default 45): ";
    getline(cin, input);
    if (!input.empty()) angle_deg = stod(input);

    double rad = angle_deg * DEG2RAD;
    cout << "sin^2 + cos^2 = " << pow(sin(rad), 2) + pow(cos(rad), 2) << endl;
    cout << "tan = " << tan(rad) << ", cot = " << 1.0 / tan(rad) << endl;
    return 0;
}
