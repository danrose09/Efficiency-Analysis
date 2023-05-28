# Author: Daniel Rosenberg
# GitHub username: danrose09
# Date: 05/20/2023
# Description: Project 8b sort_timer

import time
import random
import functools
from matplotlib import pyplot


def sort_timer(timed_func):
    """Decorator function that times how long it takes a function to run"""

    @functools.wraps(timed_func)
    def wrapper(*args, **kwargs):
        """Wrapper function that computes the time taken to run timed_func function"""

        starting_time = time.perf_counter()
        timed_func(*args, **kwargs)
        ending_time = time.perf_counter()

        elapsed_time = ending_time - starting_time

        return elapsed_time

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(decorated_sort_func_1, decorated_sort_func_2):
    """Takes two decorated sort functions as parameters. Randomly generates a list of 1000 numbers
    and then makes a separate copy of the list. Then it times how long it takes bubble sort and
    insertion sort to sort one copy each. Next it repeats this process for 2000, 3000 and up to
    10000. Numbers must be integers between 1 and 10000. Finally, plots data on a line graph."""

    list_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    func_timer_1_data = []
    func_timer_2_data = []

    for list_length in list_lengths:
        random_list = []

        for i in range(1, list_length + 1):
            random_list.append(random.randint(1, 10000))

        random_list_copy = list(random_list)

        func_timer_1 = decorated_sort_func_1(random_list)
        func_timer_2 = decorated_sort_func_2(random_list_copy)

        func_timer_1_data.append(func_timer_1)
        func_timer_2_data.append(func_timer_2)

    pyplot.plot(list_lengths, func_timer_1_data, 'ro--', linewidth=2, label='Insertion Sort')
    pyplot.plot(list_lengths, func_timer_2_data, 'go--', linewidth=2, label='Bubble Sort')
    pyplot.xlabel("Random List Length")
    pyplot.ylabel("Time to Run Function in Seconds")
    pyplot.legend(loc='upper left')
    pyplot.show()

    return


compare_sorts(insertion_sort, bubble_sort)
