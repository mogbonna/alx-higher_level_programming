#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_result = []
    for i in range(list_length):
        try:
            l3 = my_list_1[i] / my_list_2[i]
            my_result.append(l3)
        except IndexError:
            print("out of range")
            my_result.append(0)
        except ZeroDivisionError:
            my_result.append(0)
            print("division by 0")
        except TypeError:
            my_result.append(0)
            print("wrong type")
        finally:
            pass
    return (my_result)
