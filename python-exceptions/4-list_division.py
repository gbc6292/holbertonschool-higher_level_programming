#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    NewList = []
    for a in range(list_length):
        try:
            division = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            NewList.append(division)
    return NewList
