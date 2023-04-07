def has_common_member(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10):
    """
    This function takes 10 lists as input and returns True if they have at least one common member.
    """
    for element in list1:
        if element in list2 or element in list3 or element in list4 or element in list5 or element in list6 or element in list7 or element in list8 or element in list9 or element in list10:
            return True
    return False

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

if has_common_member(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10):
    print("TRUE")
else:
    print("FALSE")
    
    
has_common_member (list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
