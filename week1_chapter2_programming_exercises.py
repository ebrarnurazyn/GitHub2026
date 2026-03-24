#PERSONAL INFORMATION
name=input(print("please enter your name"))
address=input(print("please enter your adress"))
telephone_num= input (print("please enter your telephone number"))
college_major=input(print("please enter your college major"))
#SALES PREDICTION
YILLIK_KAZANC=input (int("yıllık kazancı giriinz"))
print(" yıllık karınız:"+YILLIK_KAZANC*23/100)
#Land Calulation
Arazi=input(float("arazinin ölçüsünü giriniz"))
print("arazinin dönümü :"+Arazi/43560)
#Total Purchase
price1=int(input('1.ürünün fiyatini giriniz.'))
price2=int(input('2.ürünün fiyatini giriniz.'))
price3=int(input('3.ürünün fiyatini giriniz.'))
price4=int(input('4.ürünün fiyatini giriniz.'))
price5=int(input('5.ürünün fiyatini giriniz.'))
toplam=price1+price2+price3+price4+price5
ara_toplam=(price1*93/100)+(price2+93/100)+(price3+93/100)+(price4+93/100)+(price5+93/100)
vergi=toplam-ara_toplam
print("ara toplam: \n"+str(ara_toplam)+" vergi: \n"+str(vergi)+" toplam: \n"+str(toplam))

##DISTANCE TRAVELED
print('araba 6 saatte gittiği yol mil/h : '+str(70*6)) 
print('araba 10 saatte gittiği yol mil/h : '+str(70*10)) 
print('araba 15 saatte gittiği yol mil/h : '+str(70*15)) 

##SALES TAXI
tutar=int(input('satin alma tutari giriniz: '))
eyalet_satis_ver=tutar*0.05  
ilce_sat_ver=tutar*0.025
print('tutar: ', str(tutar))
print('eyalet vergisi: ',str(eyalet_satis_ver))
print('ilçe satiş vergisi: ',str(ilce_sat_ver))
print('toplam vergi: ',str(eyalet_satis_ver+ilce_sat_ver))
print('toplam satiş tutari: ',str(tutar+eyalet_satis_ver+ilce_sat_ver))
#MILES PER-GALLON
mesafe=int(input('kat edilen mesafeeyi giriniz(mil): '))
yakit=int(input('kullanilan yakit miktarini giriniz(gallon): '))
mpg=mesafe/yakit
print('aracın mpg değeri: ',str(mpg))

##TIP, TAX AND TOTAL
tutar=int(input('hesap tutarini giriniz: '))
bahsis=tutar*0.18
vergi=tutar*0.07
toplam=tutar+bahsis+vergi
print('toplam: ',str(toplam))
print('bahşiş: ',str(bahsis))
print('vergi: ',str(vergi))

#Celsius to Fahrenheit Temperature Converter
derece=int(input('santigrat cinsinden dereceyi giriniz: '))
fahrenayt=(derece*9/5)+32
print('fahrenayt: ',str(fahrenayt))

#INGREDIENT ADJUSTER
SEKER=1.5
YAG=1
UN=2.75
adet=int(input('kac adet kurabiye yapmak istiyorsunuz: '))
seker=adet/48*(SEKER)
yag=adet/48*(YAG)
un=adet/48*(UN)

print('seker bardak: ',str(seker))
print('yag bardak: ',str(yag))
print('un bardak: ',str(un))

#Lion and Tiger Percentages
kaplan=int(input('hayvanat bahçesindeki kaplan sayisini giriniz: '))
aslan=int(input('hayavanat bahçesindeki aslan sayisisni giriniz: '))
kaplan_o=kaplan/(kaplan+aslan)*100
aslan_o=aslan/(aslan+kaplan)*100
print('aslan orani: %',str(aslan_o))
print('kaplan orani: %',str(kaplan_o))

#Stock Transaction Program
SENET_ADEDI=2000
ALIS=40.00
SATIS=42.75
aliş_ödenen=SENET_ADEDI*ALIS
aliş_kom=ALIS*SENET_ADEDI*3/100
kalan_aliş=aliş_ödenen-aliş_kom
satiş_ödenen=SENET_ADEDI*SATIS
satiş_kom=satiş_ödenen*3/100
kalan_satiş=satiş_ödenen-satiş_kom
kar=kalan_satiş-kalan_aliş
print('aliş kom: $',aliş_kom)
print('aliş ödenen: $',aliş_ödenen)
print('aliş kalan: $',kalan_aliş)
print('satiş kom: $',satiş_kom)
print('satiş ödenen: $',satiş_ödenen)
print('satiş kalan: $',kalan_satiş)
if kar>0:
    print(kar,'$ kadar kar etmiştir joe')
elif kar>=0:
    print('kar etmemiştirt')

#COMPOUND INTEREST
baslangic=int(input('başlangici giriniz: $'))
yillik_faiz=int(input('yillik faiz oraninini giriniz: $'))
faiz_adedi=int(input('Faizin yılda kaç kez bileşik faize tabi tutulacağı (Örneğin, faiz aylık olarak bileşik faize tabi tutuluyorsa 12, üç ayda bir bileşik faize tabi tutuluyorsa 4 girin.)'))
yil=int(input('hesabiniz kaç yil faizde kalacak: '))
para=baslangic*(1+(yillik_faiz/faiz_adedi))**(faiz_adedi*yil)
print('biriken para: $',str(para))


