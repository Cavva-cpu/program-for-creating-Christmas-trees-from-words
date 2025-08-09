#Code On Python
def Povtor_slov():

    a = 1
    word = input(
        "Hello, this program is designed to create Christmas trees from words. Enter the word:\n "
    )
    b = int(input("Enter the number of layers in the tree:\n"))
    while a <= b:
        print(word * a)
        a += 1
        print("|")
    if a == b + 1:
        a = 1
        Povtor_slov()


Povtor_slov()
