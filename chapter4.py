#bugcollector
toplam=0
for day in range (1,6,1):
    hata_sayisi=int(input("hata sayisi giriniz: "))
    toplam+=hata_sayisi
print('toplam hata sayisi: ',toplam)
#calories burned
toplam=0
for calori in range(10,31,5):
    toplam+=4.2*calori
    print('yakilan kalori: ',toplam)

#BUDGET ANALYSIS
BUDGET=int(input("bütçeyi girin: "))
toplam=0
for day in range(1,30,1):
    toplam+=int(input("harcadiğiniz mikatari girin: "))
if(BUDGET>toplam):
    print("bütçenin altinda harcama yaptiniz")
elif(BUDGET<toplam):
    print("Fazla harcama yaptiniz ")
else:
    print("bütçeniz bitti")
#DISTANCE TRAVELLED
hour=int(input("saati giriniz"))
speed=int(input(" hizi giriniz"))
for n in range(hour):
    distance=speed*n
    print(" saat    ",n,         "disatance travelled: ",distance)
#AVRAGE RAINFALL
toplam=0
yil=int(input("öğrenmek istediğiniz yağiş yilini giriniz: "))
for i in (1,yil):
    for j in range(12):
        yagis=int(input('yağiş miktarini giriniz.: '))
        toplam+=yagis
print(yil," yil kadar ygğiş miktari: ",toplam)
#Celsius to Fahrenheit table
for c in range(21):
    f=c*9/5+32
    print(c," derece, ",f," fahrenheit: ")
#pennies for pay
gun=int(input(" hesaplamak istediğiniz gün sayisini giriniz: "))
toplam=0
print("gün           toplam")
print("---------------------")
for i in range(1,gun+1):
    toplam+=2*i
    print(i,"           ",toplam)
print("toplam maaş: ",toplam)
#sum of numbers
n=0
while(n>=0):
    n=int(input("bir sayi giriniz: "))
    if n>0:
        print(n)
    else :print("geçersiz giriş")
print("döngü kirildi")
#ocean levels
level=0
for i in range(25):
    level+=i*1.6
    print(level)
#tuition increase
price=8000
for i in range(1,10):
    price+=int(price*0.03)
    print(i,". dönemin ücreti: ",price)
##faktöriyel
n=int(input("sayi gir: "))
fak=1
top=0
for i in range(1,n+1):
    fak*=i
print(fak)