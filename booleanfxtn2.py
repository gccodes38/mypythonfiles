# List of numbers

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
list5 = [13, 14, 15]
list6 = [16, 17, 18]
list7 = [19, 20, 21]
list8 = [22, 23, 24]
list9 = [25, 26, 27]
list10 = [28, 29, 30]

# getting the common elements 
common = set(list1) & set(list2) or set(list1) & set(list3) or set(list1) & set(list4) or set(list1)\
        & set(list5) or set(list1) & set(list6) or set(list1) & set(list7) or set(list1) & set(list8)\
        or set(list1) & set(list9) or set(list1) & set(list10) or set(list2) & set(list3) or set(list2)\
        & set(list4) or set(list2) & set(list5) or set(list2)& set(list6) or set(list2) & set(list7)\
        or set(list2) & set(list8) or set(list2)& set(list9) or set(list2) & set(list10)\
        or set(list3) & set(list4) or set(list3)& set(list5) or set(list3) & set(list6) or set(list3)& set(list7)\
        or set(list3) & set(list8) or set(list3)& set(list9) or set(list3) & set(list10) or set(list4)& set(list5)\
        or set(list4) & set(list6) or set(list4)& set(list7) or set(list4) & set(list8) or set(list4)& set(list9)\
        or set(list4) & set(list10) or set(list5)& set(list6) or set(list5) & set(list7) or set(list5)& set(list8)\
        or set(list5) & set(list9) or set(list5)& set(list10) or set(list6) & set(list7) or set(list6)& set(list8)\
        or set(list6) & set(list9) or set(list6)& set(list10) or set(list7) & set(list8) or set(list7)& set(list9)\
        or set(list7) & set(list10) or set(list8)& set(list9) or set(list8) & set(list10) or set(list9)& set(list10)

if common:
    print(bool(common))
else:
    print(bool())
