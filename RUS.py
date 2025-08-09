def Povtor_slov():

    a = 1
    word = input(
        "ПрИвЕт, это програма преднозначенна для создания ёлочек из слов. Введите слово:\n"
    )
    b = int(input("Введите колчиство слоёв в ёлке: \n"))
    while a <= b:
        print(word * a)
        a += 1
        print("|")
    if a == b + 1:
        a = 1
        Povtor_slov()


Povtor_slov()
