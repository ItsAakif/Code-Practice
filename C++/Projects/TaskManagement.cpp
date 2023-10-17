#include <iostream>
#include <vector>
#include <string>

struct Task {
    std::string description;
    bool isCompleted;
};

int main() {
    std::vector<Task> tasks;

    while (true) {
        std::cout << "\nTask Management Application" << std::endl;
        std::cout << "1. Add a task" << std::endl;
        std::cout << "2. List tasks" << std::endl;
        std::cout << "3. Quit" << std::endl;
        std::cout << "Enter your choice: ";

        int choice;
        std::cin >> choice;

        if (choice == 1) {
            Task newTask;
            std::cout << "Enter task description: ";
            std::cin.ignore();
            std::getline(std::cin, newTask.description);
            newTask.isCompleted = false;
            tasks.push_back(newTask);
            std::cout << "Task added." << std::endl;
        } else if (choice == 2) {
            if (tasks.empty()) {
                std::cout << "No tasks in the list." << std::endl;
            } else {
                std::cout << "Tasks:" << std::endl;
                for (size_t i = 0; i < tasks.size(); ++i) {
                    std::cout << i + 1 << ". " << tasks[i].description;
                    if (tasks[i].isCompleted) {
                        std::cout << " (Completed)";
                    }
                    std::cout << std::endl;
                }
            }
        } else if (choice == 3) {
            std::cout << "Exiting the Task Management Application. Goodbye!" << std::endl;
            break;
        } else {
            std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    return 0;
}
