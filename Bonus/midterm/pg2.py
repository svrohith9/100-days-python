import sys


def retrieve():
    main_list = []
    for i in sys.argv[1:]:
        main_list.append(int(i))
    return main_list


def removeEven(main_list):
    list_odd_nums = []
    for i in main_list:
        if i % 2 > 0:
            list_odd_nums.append(i)
    return list_odd_nums


def extraLast(main_list, num):
    if num > 0:
        end_num = main_list[-1]
        for i in range(0, num):
            main_list.append(end_num)
    return main_list


main_list = retrieve()
print("You entered {len(list_data)} integers which become a list: ", main_list)
print("original list after calling removeEven:", main_list)
list_odd = removeEven(main_list)
print("return of removeEven", list_odd)
appended_list = extraLast(main_list, 3)
print("original list after calling extraLast: ", appended_list)
