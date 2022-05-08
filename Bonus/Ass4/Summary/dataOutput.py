import sys
import os.path

current_dir = os.path.dirname(os.path.relpath(__file__))
analysis_dir = current_dir[0:-7] + "Analysis"
sys.path.append(analysis_dir)

import check

def printSummary(data):
    print("Summary:")
    unique_list = check.findUnique(data)
    for i in unique_list:
        print(f"{i} (1)")
    for item in data:
        if item not in unique_list:
            print(f"{item} ({data.count(item)})")
            unique_list.append(item)


if __name__ == "__main__":
    test_data = [2, 2, -1, -71, 0, 0, 2, 2, 0, 0, 345, 345, 678]
    printSummary(test_data)
