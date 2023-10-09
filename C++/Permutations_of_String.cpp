#include <iostream>
using namespace std;

void printPermutation(string &str, int i) {
    // Base case: If we have reached the end of the string, print it
    if (i >= str.length()) {
        cout << str << " ";
        return;
    }

    // Generate permutations by swapping characters
    for (int j = i; j < str.length(); j++) {
        // Swap characters at positions i and j
        swap(str[i], str[j]);
        
        // Recursively generate permutations for the remaining characters
        printPermutation(str, i + 1);
        
        // Backtrack by swapping characters back to their original positions
        swap(str[i], str[j]);
    }
}

int main() {
    // Prompt the user to enter a string
    cout << "Enter a string to generate permutations: ";
    string str;
    cin >> str;

    // Display the header
    cout << "Permutations of '" << str << "':" << endl;

    int i = 0;
    printPermutation(str, i);
    cout<<endl;

    return 0;
}
