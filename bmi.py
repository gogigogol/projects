print()
print("oblicz swoje BMI", "\n" )

waga = float(input("Podaj swoja wage [kg]: ")) #tworzymy zmienną "waga" typu float
wzrost = float(input("Podaj swoj wzrost [m]: ")) #kolejna zmianna typu float
bmi = waga / (wzrost**2) #obliczamy bmi wg wzoru
if (waga ,wzrost) == ZeroDivisionError:
    print("podana wartość jest nieprawidłowa")
if(bmi < 18): #klasyczne użycie ifa
    print("Masz niedowage")
elif(bmi > 25): #jeżeli bmi < 18 to sprawdź czy jest większe od 25
    print("Masz nadwage")

        
else: #żaden warunek nie jest spełniony więc pozostaje to
    print("Waga jest prawidlowa")
print("Twoje BMI wynosi", bmi) #wypisanie "bmi"
print()