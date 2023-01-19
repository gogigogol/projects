user_choice = -1                      # zmienna z wartoscią inna niz mozliwe wybory 1 do 5

tasks = []                  # tworzymy liste "zadan"
                      # 1 dodajemy zadanie metodą .append
                           # tasks.append("Posprzątaj biurko") # dodajemy zadanie metodą .append
print()

def show_tasks():      # definiujemy funkcje show_tasks 
     
    task_index = 0                # definiujemy zmienna  pokazujaca numer zadania, 
    for task in tasks:         
        print(task + " [" + str(task_index) + "]")   # wyswietlamuy zadania ,obok task chcemy wyswietlic numer "task_index",musimy uzyć "str" i 
                                              # umieszczasmy go w nawiasie [ ] kwadratowym
        task_index +=1          # zwiekszamy task_index o 1 i przypisujemy te wartosc do zmiennej task_index
    print()
    return
             
def add_task():                               # stworzylismy funkcje dodajaca zadanie i wyswietlajaca "dodano zadanie"
    task = input("Wpisz treść zadania: \n")
    tasks.append(task)                        # dodaje zadanie wpisane przez usera
    print("dodano zadnie") 
    
def delete_task():                          # tworzymy funkcje do usuniecia zadania
    task_index = int(input("Podaj index zadania do usuniecia: ")) 
    if task_index < 0 or task_index > len(tasks) - 1:
        print("zadanie o tym indexie nie istnieje")# warunek ze numer zadania < 0 (taki nie istnieje) lub warunek ze numer zadania jes twiekszy od dlugosci naszych zadan - 1 , bo index liczmy od 0
        return         # nie zwraca zadnej wartosci, konczy wywolanie funkcji
    tasks.pop(task_index)
    print("usunięto zadanie !")

def save_tasks_to_file():                        # tworzymy funkcje zapisywania nowych zadan do pliku tasks.txt
    file = open("tasks.txt",  "w")               # otwiera plik txt  w trybie "w" czyli zapisu, "r" to odczyt , "w+" to zapis odczyt
    for task in tasks:                           # dla zadnia w zadaniach 
        file.write(task+"\n")                   # zpisuje zadanie w nowej lini ("\n)") pliku tasks.txt
    print( "zmiany zostały zapisane!")
    file.close()              # zamykamy dokument
    
def load_tasks_from_file():              # Funkcja laduje zadania z pliku
                
    try:                                 # regula  "try  except " wyjatku, stworzona po to gdbyby ,na początku programu nie mamy jeszcze pliku tasks.txt,
                                        # ktory jest ladowany ponizej , a chcemy uniknac bledu "FileNotFoundError"
        file = open("tasks.txt")         # otwieramy plik 
        for line in file.readlines():        # dla kazdej lini w pliku czyli dla kazdego zadania dodajemy
            
            tasks.append(line.strip())       # dodajemy linie  poniewaz  w save_tasks_to_file dodalismy znak konca lini "\n"
        file.close         
    except FileNotFoundError:            # to wyjątek dla nie znalezionych bo jeszcze nie zdefiniowanych plikow w tym przypadku tasks.txt
                                         # które są ładowane w częsci poniżej     load_tasks_from_file()
        return                         # wychodzimy z funkcji
                      
load_tasks_from_file()           # laduje nam zadania z pliku tasks.txt ( na początku początku dzialania programu tego pliku nie ma,
                                # msuimy wwiec stowrzyc regułę wyjątku w funkcji load_tasks_from_file
             
while user_choice != 5:               # do momentu wybrania przez uzytkownika "5" wykonuje sie petla
    if user_choice == 1:
        show_tasks()            # task zdefiniowana wcześniej  funkcja 
      
    if user_choice == 2:
        add_task()              # funkcja dodawania task zdefiniowana wcześniej 
        
    if user_choice == 3:
        delete_task()
        
    if user_choice == 4:
        save_tasks_to_file()
        
    if user_choice >=6:
        print(" To jest zły numer ! Wybierz numer z listy  1-5 ")   
        
  
       
            
            
    print()                                    # te wszystkie printy sa w petli while  weic beda pojawiac sie ciagle 
    print("1. Pokaż zadania")
    print("2. Dodaj zadania")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")
    print()                                    # daje nam nowa pusta linie dla przejrzystosci 

    user_choice = int(input("wpisz liczbę: "))
    print()
    print()
    
                                         
    
    # zadanie dodatkowe
    # 1. obsluzyc sytuacje wyboru numeru spoza listy 1-5 np 6
    # 2. zamienić listę na set lub dictinary ( w tym przypadku trzeba bedzie zdecydowac w jaki sposob deycydowac o kluczach, zdefinowac klucze lub
    #     lub pozwolic uzytkownikowi na jego wybor
    # 3. pobrać od uzytkownika nazwe pliku w jakim chce przechowywac zadania,  pomyśleć w jaki sposób ten plik odczytać póżniej, 
    #    skąd go pobrać , czy gdzie go stworzyć.
    # 4. Rozszerzyc liste o wykonane i trwajace zadania
    # 5. zmiana foramtu zapisanych zadan np. wykorzystać format "jason"
    # 6. podział zadań na kategorie np. powiązane z domem , z pracą , z rozrywką itp
    # 7. automatyczne zapisywanie przy wyjśćiu z programu
    
    
