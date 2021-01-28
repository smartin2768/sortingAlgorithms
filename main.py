# This is a sample Python script.

import sys
import time
import os
#import bubble_sort as sort
#import quick_sort as sort
#import merge_sort as sort
#import selection_sort as sort
import builtin_sort as sort


def main():

    input_file = sys.argv[1]
    with open(input_file) as reader:
        input_text = reader.read()
    integer_list = input_text.split()

    print(f"Sorting Begins Now!")
    timer = time.time()
    sorted_list = sort.sort(integer_list)
    print(f"Sorting Has Finished: {time.time()-timer}")

    # Remove output file if it already exists
    if os.path.exists("output.txt"):
        os.remove("output.txt")

    f = open("output.txt", "w")
    f.write(str(sorted_list))
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
