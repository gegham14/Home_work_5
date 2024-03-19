import threading


def print_even_numbers():
    print("List of even numbers:")
    for i in range(0, 50, 2):
        print(i, end=" ")


def print_odd_numbers():
    print("\nList of odd numbers:")
    for i in range(1, 1001, 2):
        print(i, end=" ")


# Create threads for printing even and odd numbers
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)
# Start the threads
even_thread.start()
odd_thread.start()
# Wait for the threads to complete
even_thread.join()
odd_thread.join()
