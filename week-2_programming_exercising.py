#Day of the week
number_of_day=int(input('Enter the number of day: '))
if number_of_day==1:
    print('Monday')
elif number_of_day==2:
    print('Tuesday') 
elif number_of_day==3:
    print('Wednesday')   
elif number_of_day==4:
    print('Thursaday')          
elif number_of_day==5:
    print('Friday')   
elif number_of_day==6:
    print('saturday')   
elif number_of_day==7:
    print('sunday')   
else:print('Error')                
#Areas of rectangles
length_first=float(input("Enter your first rectangle's length: "))
high_first=float(input("Enter your first rectangle's high: "))
length_second=float(input("Enter your second rectangle's length: "))
high_second=float(input("Enter your second rectangle's high: "))
first_rectangle_area=length_first*high_first
second_rectnagle_area=length_second*high_second
print('first rectangle: ',first_rectangle_area,' second rectangle area: ',second_rectnagle_area)
if first_rectangle_area>second_rectnagle_area:
    print('first rectangle is bigger than second rectangle')
elif first_rectangle_area<second_rectnagle_area:
    print('second rectangle is bigger than first rectangle')
else:print('these rectangles are equal')
###Age Classifier
age=int(input('enter your age: '))
if age<=1:
    print('Infant')
elif age>=1 and age<13:
    print('child')    
elif age>=13 and age<20:
    print('teenage')
elif age>=20:
    print('adult' )
else:print('error')           
#Roman Numerals
number=int(input('enter a number 1 trough 10: '))
if number==1:
    print('I')
elif number==2:
    print('II')
elif number==3:
    print('III')        
elif number==4:
    print('IV')
elif number==5:
    print('V')
elif number==6:
    print('VI')  
elif number==7:
    print('VII')
elif number==8:
    print('VIII')
elif number==9:
    print('IX')
elif number==1:
    print('X')
else:print('error')
mass=int(input('enter your mass'))
weight=mass*9.8
if weight>=500:
    print('çok ağır')
elif weight<=100:
    print('Çok hafif')
else:print(weight)
##Magic dates
day=int(input('enter the day'))
month=int(input('enter the month'))
year=int(input('enter the year'))
if month*day==year:
    print(month,'/',day,'/',year)
else:print('not magic day')    
#Hot dog cookout calculator çalışmıyor!!!!
per_person_hotdog=int(input('Enter the per person hotdog: '))
person=int(input('Katılacak kişşi sayısını giriniz: '))
hotdog=(per_person_hotdog*person)
bread=(per_person_hotdog*person)
artan_hotdog=hotdog%10
artan_ekmek=bread%8
if artan_hotdog!=0:
    pHotdog=(hotdog/10)+1
    print('hotdog paket sayısı : ',pHotdog)
else:
    print('hotdog artmadı ',int(hotdog/10),' adet paket hotdog lazım') 
print(' artan hotdog sayısı : ',artan_hotdog)   
if artan_ekmek!=0:
    pBread=(bread/8)+1
    print('ekmek paket sayısı : ',pBread)
else:
    print('ekmek artmadı ',int(bread/8),' adet paket ekmek lazım')   
print(' artan ekmek sayısı: ',artan_ekmek)   
##COLOR MIXER çalışmıyor!!! kuramadım
color1=input('bir renk giriniz: ')
color2=input('bir renk giriniz: ')
if color1=='kirmizi' and color1=='sari' and color1=='mavi' and color2=='kirmizi'and color2=='sari'and color2=='mavi':
    
    if color1=='kirmizi' and color2=='mavi':
       print('mor')  
    elif color1=='kirmizi'and color2=='sari':
        print('turuncu') 
    elif color1=='mavi'and color2=='sari':
        print('yeşil')
else:
    print('geçersiz giriş')

#ROULETTE WHEEL COLORS
sayi=int(input('bir sayi girini(0-36): '))

if sayi==0:
    print('yeşil')
elif sayi>0 and sayi<11:
    if sayi%2==0:
        print('kirmizi')  
    else: print('siyah')
elif sayi>10 and sayi<=18:
    if sayi%2==0:
        print('kirmizi')  
    else: print('siyah')
elif sayi>=19 and sayi<=28:
    if sayi%2==0:
        print('siyah')  
    else: print('kirmizi')
elif sayi>=29 and sayi<=36:
    if sayi%2==0:
        print('kirmizi')  
    else: print('siyah')
else :
    print('gecersiz giriş')
print ('oyun bitti')

##MONEY COUNTING GAME  detay bilmiyorum
#BOOK CLUB POINTS
kitap_s=int(input('satin aldiğiniz kitap sayisini giriniz: '))
if kitap_s==0:
    print('0 puan kazandiniz.')
elif kitap_s==2:
    print('5 puan kazandiniz')
elif kitap_s==4:
    print('15 puan kazandiniz')
elif kitap_s==6:
    print('30 puan kazandiniz')
elif kitap_s>=8:
    print('60 puan kazandiniz')
else: print('geçersiz giriş')

#SOFTWARE SALES
paket_s=int(input('almak istediğiniz paket sayisini giriniz: '))
if paket_s>=10 and paket_s<=19:
    print((paket_s*99*90/100),'$ dolar ödeyin')
elif paket_s>=20 and paket_s>=49:
    print((paket_s*99*80/100),'$ dolar ödeyin')
elif paket_s>=50 and paket_s<=99:
    print((paket_s*99*70/100),'$ dolar ödeyin')
elif paket_s>=100:
    print((paket_s*99*60/100),'$ dolar ödeyin')
else:print(paket_s*99,' $ ödeyin indirim bulunmamaktadir')

#SHIPPING CHARGES
giris=int(input('miktari girin: '))
if giris<=2:
    print(giris*1.5,'$ öde')
elif giris>2 and giris>=6:
    print(giris*3,'$ öde')
elif giris>6 and giris<=10:
    print(giris*4,'$ öde')
elif giris>10:
    print(giris*4.75,'$ öde')

##TIME CALCULATOR
zaman=int(input('zamani girin saniye cinsinden: '))
if zaman<60:
    print(zaman%60,'saniye')
elif zaman>=60 and zaman<3600:
    dakika=zaman/60
    print(zaman%60,' saniye ',dakika,' dakika')
elif zaman>=3600 and zaman<86400:
    saat=zaman/3600
    dakika=(zaman%3600)/60
    saniye=zaman%3600
    print('saat',saat,'dakika',dakika,'saniye',saniye)
elif zaman>=86400:
    gün=zaman/86400
    saat=(zaman%86400)/60/60
    dakika=(zaman%86400)/60
    saniye=zaman%86400
    print('gün',gün,'saat',saat,'dakika',dakika,'saniye',saniye)

# FEBRUARY DAYS
yil=int(input('yili giriniz: '))
if yil%4==0:
    print('artik yildir')
else:print('artik yil değildir')

#Wİ-Fİ DIAGNOSTIC TREE
komut=input('Reboot the computer and try to connect.')
if(komut=='no'):
    print('Reboot the router and try to connect.')
    komut1=input('Did that fix the problem?')
    if (komut1=='no'):
        print('Make sure the cables between the router and modem are plugged in firmly.')
        komut2=input('Did that fix the problem?')
        if(komut2=='no'):
            print('Move the router to a new location.')
            komut3=input('did that fix the problem?')
            if(komut3=='no'):
                print('get a new router')
            else:
                print('finish')
        else:
            print('finish')
    else:
        print('finish')
else:
    print('finish')
