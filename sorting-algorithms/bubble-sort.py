
def bubble_sort(_list): 

    for a in range(len(_list)-1 ): 
        for b in range(a+1, len(_list)): 

            if _list[a] > _list[b]:
                temp = _list[a]
                _list[a] = _list[b]
                _list[b] = temp
        break 
    return _list


def main():
    my_list = [5, 4, 0, 1, 3, 0]
    print(bubble_sort(my_list))

if __name__ == "__main__": 
    main()

