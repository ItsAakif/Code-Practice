// Program to calculate Gross Salary by Aakif Mudel 
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    // Constants
    const double HRA_RATE = 0.4;    // House Rent Allowance rate (40%)
    const double DA_RATE = 0.2;     // Dearness Allowance rate (20%)

    // Variables
    double basicSalary, grossSalary, hra, da;
    string input;

    // Input: Enter the basic salary
    cout << "Enter the basic salary: ";
    getline(cin, input);

    // Convert input string to a double
    stringstream(input) >> basicSalary;

    // Calculate HRA and DA
    hra = basicSalary * HRA_RATE;
    da = basicSalary * DA_RATE;

    // Calculate Gross Salary
    grossSalary = basicSalary + hra + da;

    // Display the Gross Salary
    cout << "Gross Salary: " << grossSalary << endl;

    return 0;
}
