items = [1, 23, 4, 5]
new_numbers = [i+1 for i in items]
print(new_numbers)


str_data = "abcd"
str_list = [i for i in str_data]
print(str_list)


items = [1, 2, 4, 5]
new_numbers = [i for i in items if (i+1) % 2 == 0]
print(new_numbers)

print("***************************")

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [num*num for num in nums]
print(squared_nums)

# even nums
print(f"{[num for num in nums if num%2==0]}")

# intersection of file1 and file2 data
with open(".\\Day26\\file1.txt") as file:
    file1_data = [int(line) for line in file]

with open(".\\Day26\\file2.txt") as file:
    intersection_data = [int(line) for line in file if int(line) in file1_data]
    print(file.read())

print(intersection_data)
