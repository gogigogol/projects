# # funkcja główna programu
# def main():
#     print("Witaj świecie!") # ta funkcja wypisuje napis
#     # wiersz poniżej wczytuje dane z klawiatury
#     pobrany_napis = input()
#     print("Twój napis to: " + pobrany_napis)
# # uruchomienie funkcji głównej
# if __name__ == "__main__":
#     main()
def main():
    x = 7
    y = 3 
    suma = x + y
    print("Dodawanie: " + str(suma))
    
    roznica = x - y
    print ("Odejmowanie: " + str(roznica))
    
    iloczyn = x * y
    print("Mnozenie: " + str(iloczyn))
    
    iloraz = x / y
    print("dzielenie: " + str(iloraz))
    
    reszta = x % y
    print("reszta: " + str(reszta))
    

if __name__ == "__main__":
    main()
    