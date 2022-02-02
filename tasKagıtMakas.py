from random import randint
x = 2
while x == 2:
    print("taş kağıt makas oyununa hoşgeldiniz :)")
    secim = {1: "taş", 2: "kağıt", 3: "makas"}
    pc = randint(1, 3)
    oyuncu = int(input("1 = taş \n2 = kağıt\n3 = makas\n seçimin\n:"))
    print("pc'nin hamlesi {}".format(secim[pc]))
    print("oyuncu'nun hamlesi {}".format(secim[oyuncu]))
    if pc == oyuncu:
        print("berabere")
    elif pc == 2 and oyuncu == 1:
        print("pc kazandı")
    elif pc == 1 and oyuncu == 3:
        print("pc kazandı")
    elif pc == 3 and oyuncu == 2:
        print("pc kazandı")
    else:
        print("oyuncu kazandı")
    x = int(input("tamam ise 1\n devam ise 2\n:"))
print("görüşmek üzere :)")