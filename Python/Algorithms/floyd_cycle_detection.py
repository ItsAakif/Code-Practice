class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    tortoise = head
    hare = head

    while hare is not None and hare.next is not None:
        tortoise = tortoise.next        # Move tortoise one step
        hare = hare.next.next          # Move hare two steps

        if tortoise == hare:           # Meeting point found, indicating a cycle
            return True

    return False

# Example usage:
# Create a linked list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

has_cycle_detected = has_cycle(node1)
print("Cycle detected:", has_cycle_detected)
