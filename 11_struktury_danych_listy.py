names_list = []                             # pusta lista
names_list.append("Kamil")                  #append dodaje nam element do listy
names_list.append("Mariusz")
print(names_list) 


names_list = ["Kamil", "Mariusz"]              # inny spospob zapisania listy
print(names_list)
names_list.reverse()                           # odwraca liste
for name in names_list:                        # dla kazdego imienia w liscie(names_list)
    print(name)
    
names_list = ["Kamil", "Mariusz", "Adam"]   
names_list.sort()                             # sortuje nam liste
for name in names_list:                       # dla kazdego imienia w liscie(names_list)
    print(name)
    
    
names_list = ["Kamil", "Mariusz", "Adam", "Kamil"] 
print(names_list[0])                            # wyswietla pierwszy element listy



names_list = ["Kamil", "Mariusz", "Adam", "Kamil"] 
print(names_list.count("Kamil"))                  # count wyswietla ile razy element jest na liscie


print(len(names_list))                            # len  wysietla dlugosc list tzn ile elementow jest w liscie
print(names_list.pop(0))           # pop zwraca element z listy i jednoczesnie go usuwa
print(names_list)
names_list.remove("Kamil")   # usuwa element z listy (ale tylko pierwszy o tej nazwie Kamil )

names_list.sort()                   # sortuje liste 


names_list.clear()           # usuwa wszystkie elementy z listy
names_list.sort(reverse=True)       # sortowanie odwrotne
print(names_list)


