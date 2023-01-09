# print("koko")
# print('"ucze sie"\n"\"jezyka"\"')

# print("lekcja1-zmienne")
3
# to jest przyklad wartosci walut
# dolar = 20
# zloty = 37
# zloty_na_dolar = zloty / 4.50
# dolar_na_zloty = dolar * 4.50
# print(zloty , "PLN to", round(zloty_na_dolar ,3) , "USD" )
# print(dolar , "USD to" , round(dolar_na_zloty, 3) , "PLN")

# print("lekcja2-input, i float)")

# cokolwiek = float(input("Wpisz liczbe: "))
# cos = cokolwiek ** 2.0
# print(cokolwiek, "do potegi 2 wynosi", cos)

# mnozna = float(input("Wpisz liczbe : "))
# liczba = mnozna*10
# print(mnozna, "razy 10 wynosi: ", liczba)

# znak konektacji

# imie = input("Prosze, podaj mi swoje imie: ")
# nazwisko = input("Podaj mi rowniez swoje nazwisko:  ")
# print("Dziekuje.")
# print("\nNazywasz sie " + imie + " " + nazwisko + ".")

# print("operator replikacji")

# print("$" + 6*"^" +"$")
# print(("$" + " "*6 +"$\n") *8, end="")
# print("$" + 6*"^" +"$")
# print("$" + 5*" " + "$"*2 )
# test = input( "I jak to wyszło? ")
# print("na pewno"  " " + test + "?") 

# print( " konwersja typu STR")

# bok_a = float(input("Wprowadz dlugosc pierwszego boku: "))
# bok_b = float(input("Wprowadz dlugosc drugiego boku: "))
# print("Dlugosc przeciwprostokatnej wynosi " + str((bok_a**2 + bok_b**2) ** .5))

# a = float(input("podaj liczbe: "))   # tu wprowadź wartość zmiennoprzecinkową dla zmiennej a
# b = float(input("podaj liczbe: "))   # tu wprowadź wartość zmiennoprzecinkową dla zmiennej b
# c = (a+ b)  # tutaj wypisz wynik dodania
# d = (a-b)  # tutaj wypisz wynik odejmowania
# e = (a*b) # tutaj wypisz wynik mnożenia
# f = (a/b)# tutaj wypisz wynik dzielenia
# print( c, (d), e, f)
# print("\nI to by było na tyle!")


# print ("zadanie")
# x = float(input("Wprowadź wartość dla x: "))

# a = (x+(1/x))
# b = (x+(1/a))
# c = (x+(1/b))
# y = 1/c

# print("y =", y)


# h = int(input("Czas startu (godziny): "))
# m = int(input("Czas startu (minuty): "))
# d = int(input("Czas trwania wydarzenia (minuty): "))

# m = m + d # oblicz ogólną liczbę minut
# h = h + m // 60 # znajdź liczbę godzin ukrytych w minutach i zaktualizuj godzinę
# m = m % 60 # prawidłowe minuty w zakresie (0..59)
# h = h % 24 # prawidłowe godziny w zakresie (0..23)
# print(h, ":", m, sep='')

# liczba1 = int(input(" podaj pierwsza liczbe : "))
# liczba2 = int(input(" podaj druga liczbe: "))
# liczba3 = int(input("podaj trzecia liczbe: "))
# najwieksza_liczba = liczba1
# if liczba2 > najwieksza_liczba:
#     najwieksza_liczba = liczba2
# if liczba3 > najwieksza_liczba:
#     najwieksza_liczba = liczba3
# print("najwieksza liczbajest : ", najwieksza_liczba)

# roslina = ("Skrzydłokwiat")
# roslina = input()
# if roslina != ("Skrzydłokwiat"): 
#     print("Nie , ja chce Skrzydłokwiat...!")
#     roslina = input()
# if roslina == ("Skrzydłokwiat"):
#     print("Skrzydłokwiat jest najlepszą rośliną w historii!")


# instrukcja if 
# podatek dochodowy przyklad
# dochod = float(input("Wprowadź swój roczny dochód: "))
# ulga = 556.2

# if dochod <= 85528:
#     podatek = dochod*0.18 - ulga
# if dochod > 85528:
#     podatek = 14839.2 + ((dochod - 85528)*0.32)
# if podatek <= 0:
#     podatek = 0.0
# podatek = round(podatek, 0)


# dochod = float(input("Wprowadź swój roczny dochód: "))
# ulga = 556.2

# if dochod <= 85528:
#     podatek = dochod*0.18 - ulga
# else: dochod > 85528
# podatek =  ((dochod - 85528)*0.32) + 14839.2
# if podatek <= 0:
#     podatek = 0.0
# podatek = round(podatek, 0)
# print("podatek = ", podatek)




# rok = int(input("Wprowadź rok: "))

# przez400 = rok % 400
# przez4 = rok % 4
# przez100 = rok % 100
# if rok <= 1581:
#     print("Nie w kalendarzu gregorianskim")
# elif przez400 ==0:
#     print("rok przestepny")
# elif przez4 == 0:
#         print("rok przestepny")
# elif przez100 != 0:
#     print("rok przestepny")
# else:
#     print("rok zwykly")
    
    
    
# rok = int(input("Wprowadź rok: "))

# przez400 = rok % 400
# przez4 = rok % 4
# przez100 = rok % 100
# if rok <= 1581:
#     print("Nie w kalendarzu gregorianskim")
# elif przez400 !=0:
#     print(f"{rok} to rok zwykly")
# elif przez4 != 0:
#         print(f"{rok} to rok zwykly")
# elif przez100 != 0:
#     print(f"{rok} to rok zwykly")
# else:
#     print(f"{rok} to rok przestepny") 
    
     
    # "f" to funkcja wywolujaca zmienna "rok" ktora zawierac sie musi w {}
    
    # bedziemy przechowywac obecnie najwieksza liczbe tutaj
# najwiekszaLiczba = -999999999

# # wprowadz pierwsza wartosc
# liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zatrzymac: "))

# # jesli liczba nie jest rowna -1, bedziemy kontynuowac
# while liczba != -1:
#     # czy liczba jest wieksza niz najwiekszaLiczba?
#     if liczba > najwiekszaLiczba:
#         # tak, uaktualnij najwiekszaLiczba
#         najwiekszaLiczba = liczba
#     # wprowadz nastepna liczba
#     liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zatrzymac: "))

# # wyswietl najwiekszaLiczba
# print("Najwieksza liczba wynosi:", najwiekszaLiczba)

# tajny_numer = 777

# print(
# """
# +================================+
# | Witaj w mojej grze, mugolu!    |
# | Wprowadź liczbę całkowitą      |
# | i zgadnij, jaki numer          |
# | wybrałem dla ciebie.           |
# | Jaki jest więc sekretny numer? |
# +================================+
# """)
# liczba = int(input("Wpisz tajny numer:",   ))
# while liczba != 777:
#     print("Nie, to nie jest ta liczba, którą wybrałem dla Ciebie. Spróbuj ponownie!", )
#     liczba = int(input("Wpisz tajny numer:",   ))
#     if liczba == tajny_numer:
#         print(" tak jest, to jest tajny numer!")


# import time # LINIA I
# for i in range(1, 6):
#     print( i, "MIssissippi",  )


# # Napisz pętlę for, która liczy do pięciu.
#     # Ciało pętli: wyświetl w oknie konsoli numer iteracji i słowo "Mississippi".
#     time.sleep(1) # LINIA II
# for i in range (1):    
#     print("Ready or not , here i come!")
# # Napisz funkcję print, która wyświetli wiadomość końcową.

# najwieksza_liczba = -99999999
# licznik = 0

# liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zakonczyc: "))

# while liczba != -1:
#     if liczba == -1:
#         continue
#     licznik += 1

#     if liczba > najwieksza_liczba:
#         najwieksza_liczba = liczba
#     liczba = int(input("Wprowadz liczbe lub wpisz -1, aby zakonczyc: "))

# if licznik:
#     print("Najwieksza liczba wynosi", najwieksza_liczba)
# else:
#     print("Nie wprowadzono zadnej wartosci.")
  
    
# slowo = "pumpernikiel"
# slowo = input("wpisz nazwę ciastka:")
# while slowo != "pumpernikiel":
#     if slowo == "pumpernikiel":
#         break
#     if slowo != "pumpernikiel":
#         slowo = input("wpisz nazwę ciastka:")
# if slowo:
#     print("Udało Ci się opuśćić pętlę")



name = "Konrad"
print(len(name)) #pokazuje ilsc znakow w nazwie zmiennej
print(name.capitalize()) #zamienia z  duzej litery
print(name.upper()) #zamienia na duze litery

print(name.lower()) #zamienia na male litery

print(name[0]) #pokazuje pierwszy znak w zmiennej

channel = "jak nauczyć się programowania" #metoda split(rozdzielenia)
print(channel.split(" "))

join_string = " "  #metoda join  łaczenia
print(join_string.join(['jak', 'Nauczyć', "się", 'pythona']))

print(name.startswith("K"))
print(name.startswith("k"))
print(name.endswith("K"))
print(name.strip("a,E,I,o,U"))













