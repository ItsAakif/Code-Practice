#include <iostream>
#include <vector>

std::vector<int> quick_sort(std::vector<int> arr) {
    if (arr.size() <= 1) {
        return arr;
    } else {
        int pivot = arr[0];
        std::vector<int> less_than_pivot, greater_than_pivot;
        for (size_t i = 1; i < arr.size(); ++i) {
            if (arr[i] <= pivot) {
                less_than_pivot.push_back(arr[i]);
            } else {
                greater_than_pivot.push_back(arr[i]);
            }
        }
        std::vector<int> sorted_list;
        sorted_list = quick_sort(less_than_pivot);
        sorted_list.push_back(pivot);
        std::vector<int> right_sorted = quick_sort(greater_than_pivot);
        sorted_list.insert(sorted_list.end(), right_sorted.begin(), right_sorted.end());
        return sorted_list;
    }
}

int main() {
    std::string user_input;
    std::cout << "Enter a list of numbers separated by spaces: ";
    std::getline(std::cin, user_input);

    std::vector<int> input_list;
    int num;
    std::istringstream iss(user_input);
    while (iss >> num) {
        input_list.push_back(num);
    }

    std::vector<int> sorted_list = quick_sort(input_list);

    std::cout << "Sorted list: ";
    for (int number : sorted_list) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}

