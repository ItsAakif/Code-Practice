#include <iostream>

class Queue {
private:
    static const int max_size = 100;
    int arr[max_size];
    int front, rear;

public:
    Queue() {
        front = rear = -1;
    }

    bool isFull() {
        return (front == 0 && rear == max_size - 1) || (front == rear + 1);
    }

    bool isEmpty() {
        return front == -1;
    }

    void enqueue(int value) {
        if (!isFull()) {
            if (front == -1) {
                front = rear = 0;
            } else if (rear == max_size - 1) {
                rear = 0;
            } else {
                rear++;
            }
            arr[rear] = value;
            std::cout << "Enqueued " << value << " into the queue." << std::endl;
        } else {
            std::cout << "Queue is full! Cannot enqueue more elements." << std::endl;
        }
    }

    void dequeue() {
        if (!isEmpty()) {
            int value = arr[front];
            if (front == rear) {
                front = rear = -1;
            } else if (front == max_size - 1) {
                front = 0;
            } else {
                front++;
            }
            std::cout << "Dequeued " << value << " from the queue." << std::endl;
        } else {
            std::cout << "Queue is empty! Cannot dequeue." << std::endl;
        }
    }

    int peek() {
        if (!isEmpty()) {
            return arr[front];
        } else {
            std::cout << "Queue is empty! No element to peek." << std::endl;
            return -1;
        }
    }
};

int main() {
    Queue queue;

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);

    std::cout << "Front element: " << queue.peek() << std::endl;

    queue.dequeue();
    queue.dequeue();

    std::cout << "Front element: " << queue.peek() << std::endl;

    queue.dequeue();

    return 0;
}
