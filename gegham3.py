# Write a python function all even number
# in 10.000 use threading and print time. 

import threading


def print_even_numbers():
    print("List of even numbers:")
    for i in range(0, 51, 2):
        print(i, end=" ")


def print_odd_numbers():
    print("\nList of odd numbers:")
    for i in range(1, 1001, 2):
        print(i, end=" ")


even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)
even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()
