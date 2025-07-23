/*
 * Greatest Common Divisor Calculator (GCD)
 *
 * This program computes the Greatest Common Divisor (GCD) of two or more integers
 * using the Euclidean algorithm. It accepts input via standard input, with
 * support for both space-separated and comma-separated integers.
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
        int tmp = b;
        b = a % b;
        a = tmp;
    }
    return std::abs(a);
}

int gcd_list(const std::vector<int>& nums) {
    if (nums.empty()) return 0;
    int result = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        result = gcd(result, nums[i]);
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
    std::cout << "Enter integers (space or comma separated, default: 48 18 30): ";
    std::getline(std::cin, input);

    std::vector<int> numbers = input.empty() ? std::vector<int>{48, 18, 30} : parse_input(input);
    int result = gcd_list(numbers);

    std::cout << "GCD(";
    for (size_t i = 0; i < numbers.size(); ++i) {
        std::cout << numbers[i];
        if (i != numbers.size() - 1) std::cout << ", ";
    }
    std::cout << ") = " << result << std::endl;

    return 0;
}
