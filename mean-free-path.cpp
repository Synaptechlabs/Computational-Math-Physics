// -----------------------------------------------------------------------------
// Feynman Lectures - Volume I, Chapter 1, Exercise 1-9
// Estimate of Mean Free Path for Air Molecules at STP (with CLI input)
//
// Author: Scott K. Douglass
// Date: 2025-07-20
// Description:
//     Computes mean free path using:
//         λ = 1 / (√2 * π * d² * n)
//     Allows user to press Enter to use default values.
//
// Dependencies: <iostream>, <cmath>, <limits>
// -----------------------------------------------------------------------------

#include <cmath>
#include <iostream>
#include <limits>
#include <string>

double get_input_with_default(const std::string &prompt, double default_value) {
  std::string input;
  std::cout << prompt << " [default: " << default_value << "]: ";
  std::getline(std::cin, input);
  try {
    return input.empty() ? default_value : std::stod(input);
  } catch (...) {
    std::cerr << "Invalid input. Using default.\n";
    return default_value;
  }
}

int main() {
  const double default_d = 3.7e-10; // meters
  const double default_n = 2.7e25;  // m^-3
  const double pi = 3.14159265358979323846;

  double d =
      get_input_with_default("Enter molecular diameter (meters)", default_d);
  double n = get_input_with_default("Enter number density (m^-3)", default_n);

  double lambda = 1.0 / (std::sqrt(2.0) * pi * d * d * n);

  std::cout << "\nEstimated mean free path ≈ " << lambda << " meters\n";

  return 0;
}
