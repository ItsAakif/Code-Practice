#include <iostream>
#include <string>

using namespace std;

// Function to check if a string is a palindrome
bool isPalindrome(const string& str) {
    int left = 0;           // Initialize a pointer for the left end of the string
    int right = str.length() - 1; // Initialize a pointer for the right end of the string
    
    // Iterate while the left pointer is less than the right pointer
    while (left < right) {
        // If characters at the left and right pointers are different, it's not a palindrome
        if (str[left] != str[right]) {
            return false;
        }
        ++left;     // Move the left pointer to the right
        --right;    // Move the right pointer to the left
    }
    
    return true; // If the loop completes without finding a mismatch, it's a palindrome
}

int main() {
    string input;
    
    // Prompt the user to enter a string
    cout << "Enter a string: ";
    cin >> input;
    
    // Check if the input is a palindrome and display the result
    if (isPalindrome(input)) {
        cout << input << " is a palindrome." << endl;
    } else {
        cout << input << " is not a palindrome." << endl;
    }
    
    return 0;
}