import sys
import os.path

current_dir = os.path.dirname(os.path.relpath(__file__))
data_dir = current_dir[0:-3]+"Data"
analysis_dir = current_dir[0:-3]+"Analysis"
summary_dir = current_dir[0:-3]+"Summary"
sys.path.append(data_dir)
sys.path.append(analysis_dir)
sys.path.append(summary_dir)

import dataOutput
import check
import dataInput

def main():
    data = dataInput.getData(sys.argv[1:])
    print(f"You entered {len(data)} integers: ", data)
    size = len(data)
    if size < 10:
        check.makeTen(data)
        print(f"After {10-size} random integers are appended: ", data)
    else:
        print(data)
    unique_nums = check.findUnique(data)
    print('These have no duplicates: ', unique_nums)
    dataOutput.printSummary(data)


if __name__ == "__main__":
    main()
