def get_even_list(l):
    l = [
        a
        for a in l
            if a% 2 == 0
    ]
    return l
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")