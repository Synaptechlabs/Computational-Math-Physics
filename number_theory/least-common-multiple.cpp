/*
 * Least Common Multiple Calculator (LCM)
 *
 * This program computes the Least Common Multiple (LCM) of two or more integers.
 * It uses the Euclidean algorithm to find the Greatest Common Divisor (GCD),
 * and then applies the formula: LCM(a, b) = |a * b| / GCD(a, b)
 *
 * Features:
 * - Accepts command-line input of space- or comma-separated integers.
 * - Uses standard input if no command-line arguments are provided.
 * - Validates user input and reports errors.
 *
 * Author: Scott
 * Date: 2025-07-20
 */

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cctype>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return std::abs(a);
}

int lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return std::abs(a * b) / gcd(a, b);
}

int lcm_list(const std::vector<int>& nums) {
    if (nums.empty()) return 0;
    int result = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        result = lcm(result, nums[i]);
    }
    return result;
}

std::vector<int> parse_input(const std::string& input) {
    std::vector<int> numbers;
    std::string cleaned;
    for (char ch : input) {
        if (ch == ',') cleaned += ' ';
        else cleaned += ch;
    }

    std::istringstream iss(cleaned);
    std::string token;
    while (iss >> token) {
        try {
            numbers.push_back(std::stoi(token));
        } catch (...) {
            std::cerr << "❌ Invalid input: '" << token << "' is not an integer.\n";
            exit(1);
        }
    }
    return numbers;
}

int main() {
    std::string input;
    std::cout << "Enter integers (space or comma separated, default: 12 18 30): ";
    std::getline(std::cin, input);

    std::vector<int> numbers = input.empty() ? std::vector<int>{12, 18, 30} : parse_input(input);
    int result = lcm_list(numbers);

    std::cout << "LCM(";
    for (size_t i = 0; i < numbers.size(); ++i) {
        std::cout << numbers[i];
        if (i != numbers.size() - 1) std::cout << ", ";
    }
    std::cout << ") = " << result << std::endl;

    return 0;
}
