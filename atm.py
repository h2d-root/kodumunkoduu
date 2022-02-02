def atm() :
    bakiye = 500
    sifre = 0
    sifreSor = int(input("lütfen şifrenizi giriniz \n:"))

    if sifre == sifreSor :
        islem = int(input("para yatır = 1\npara çek = 2 \nbakiye sorgulama = 3 \n:"))
        if islem == 1 :
            yatirilacakTutar = int(input("yatırılacak tutarı giriniz \n:"))
            bakiye = bakiye + yatirilacakTutar
            print("yeni bakiye {}".format(bakiye))
        elif islem == 2 :
            cekilecekTutar = int(input("ne kadar para çekmek istersiniz \n:"))
            kalan = bakiye - cekilecekTutar
            if kalan < 0 :
                print("yetersiz bakiye :/")
            elif kalan > 0:
                bakiye = bakiye - cekilecekTutar
                print("yeni bakiye {}".format(bakiye))
            else : 
                print("geçersiz işlem")
        elif islem == 3:
            print(bakiye)
        else:
            print("geçersiz işlem")
    else :
        print("şifre yanlış :/")
    return

atm()