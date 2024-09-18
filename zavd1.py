def delete():
    A = list(map(int, input("Введіть список: ").split()))
    print("Введений список:", A)

    result = [A[i] for i in range(len(A)) if i % 2 != 0]

    print("Cписок після видалення елементів з парними індексами:", result)
    return result

delete()
