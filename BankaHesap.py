class Hesap():
    def __init__(self, ad, borc=0.0, bakiye=0.0):
        self.ad = ad
        self.bakiye = bakiye
        self.borc = borc

    def paraYatir(self, miktar):
        self.bakiye+=miktar
        print("Para yatırma işlemi başarılı.")
        self.bakiyeGoster(False)
        
    def paraCek(self, miktar):
        if(miktar > self.bakiye):
            raise ValueError("İşlem başarısız!, yetersiz bakiye.")
        self.bakiye-=miktar
        print("Hesabınızdan {0}₺ para çekildi.".format(miktar)) 
        self.bakiyeGoster(False)

    def baskaHesabaParaYatir(self, hesap, miktar):
        if miktar > self.bakiye:
            raise ValueError("İşlem başarısız!, yetersiz bakiye")
        self.bakiye-=miktar
        print("{0} hesabına {1}₺ gönderildi.".format(hesap.ad, miktar))
        self.bakiyeGoster(False)  

    def borcOde(self, miktar):
        self.borc -= miktar
        print("İşlem başarılı. Kalan borç: {0}₺.".format(self.borc))

    def bakiyeGoster(self, ilk_giris):
        if ilk_giris == True:
            print("Hoş geldiniz, {0} \nBakiyeniz: {1}₺.".format(self.ad, self.bakiye))
        else:
            print("Bakiyeniz: {0}₺.".format(self.bakiye))

hesap1 = Hesap("Okan Dabanlı")
hesap1.bakiyeGoster(True) #ATM giriş ekranı karşılaması
hesap1.borc = 250
hesap1.borcOde(140)
hesap1.paraYatir(1500)
hesap1.paraCek(650)

hesap2 = Hesap("Hakan Dabanlı")
hesap2.bakiyeGoster(True) #ATM giriş ekranı karşılaması

hesap1.baskaHesabaParaYatir(hesap2, 400) #Hesaba para yatır.
        