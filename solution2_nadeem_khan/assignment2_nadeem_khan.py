# Assignment 2

## Course: MET CS 566 - Analysis of Algorithm.
### BU ID: U03225602
### Name: Nadeem Khan

def find_maximum(sub_arr):
    max_el = sub_arr[0]
    max_el_idx = 0
    for i in range(0, len(sub_arr)):
        if sub_arr[i] > max_el:
            max_el = sub_arr[i]
            max_el_idx = i
    return {"max_el": max_el, "idx": max_el_idx}


def max_sort(arr):

    for i in range(0, len(arr)):
        max_el_idx = find_maximum(arr[0: len(arr) - i])["idx"]

        # swap operation
        arr[len(arr) - 1 - i], arr[max_el_idx] = arr[max_el_idx], arr[len(arr) - 1 - i]

    return arr


if __name__ == '__main__':
    print(max_sort([5, 4, 3, 2, 1]))

    print(max_sort([7, 1, 8, 3, 9]))

    print(max_sort([72, 1, 8, 3, 10]))
