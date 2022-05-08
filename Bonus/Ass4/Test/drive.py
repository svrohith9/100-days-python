import sys
import os.path

current_dir = os.path.dirname(os.path.relpath(__file__))
ass4_dir = current_dir[0:-4] + "App"
sys.path.append(ass4_dir)

import ass4

print("Assignment 4 begins...")
ass4.main()
print("Assignment 4 ends...")
