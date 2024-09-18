def search():
    A = input("Введіть текст: ")
    B = A.lower()
    print("Текст:", B)

    letter_set = set([char for char in B if char.isalpha()])

    punctuation_marks = {'.', ',', ';', ':', '!', '?', '-', '(', ')', '"', "'"}

    punctuation_count = sum(1 for char in B if char in punctuation_marks)

    print("Множина літер:", letter_set)
    print("Кількість розділових знаків:", punctuation_count)


search()
