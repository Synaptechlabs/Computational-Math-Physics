// -----------------------------------------------------------------------------
// [Project Name] - [Topic / Problem]
// [Short Description of what this script does]
//
// Author: Scott K. Douglass
// Date: YYYY-MM-DD
// Description:
//     [Describe the formula used, physical constants, units, etc.]
//
// Dependencies: <iostream>, <cmath>, <string>, ...
// -----------------------------------------------------------------------------

#include <cmath>
#include <iostream>
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
  // Define constants
  const double pi = 3.14159265358979323846;

  // Get user input
  double example_value = get_input_with_default("Enter example quantity", 1.0);

  // Perform calculation
  double result = example_value * pi; // Replace with real formula

  // Output result
  std::cout << "\nResult: " << result << "\n";

  return 0;
}
