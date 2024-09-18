def reverse_list():
    A = list(map(int,input("Введіть список: ").split()))
    print("Введений список: ", A)

    A.reverse()
    print("Cписок у зворотньому напрямку:", A)
    return A


reverse_list()