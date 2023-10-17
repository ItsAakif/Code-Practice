#include <iostream>

class Stack {
private:
    static const int max_size = 100;
    int arr[max_size];
    int top;

public:
    Stack() {
        top = -1;
    }

    bool isFull() {
        return top == max_size - 1;
    }

    bool isEmpty() {
        return top == -1;
    }

    void push(int value) {
        if (!isFull()) {
            arr[++top] = value;
            std::cout << "Pushed " << value << " onto the stack." << std::endl;
        } else {
            std::cout << "Stack overflow! Cannot push more elements." << std::endl;
        }
    }

    void pop() {
        if (!isEmpty()) {
            std::cout << "Popped " << arr[top--] << " from the stack." << std::endl;
        } else {
            std::cout << "Stack is empty! Cannot pop." << std::endl;
        }
    }

    int peek() {
        if (!isEmpty()) {
            return arr[top];
        } else {
            std::cout << "Stack is empty! No element to peek." << std::endl;
            return -1;
        }
    }
};

int main() {
    Stack stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    std::cout << "Top element: " << stack.peek() << std::endl;

    stack.pop();
    stack.pop();

    std::cout << "Top element: " << stack.peek() << std::endl;

    stack.pop();

    return 0;
}
