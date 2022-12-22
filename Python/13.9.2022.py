import random

def prva_uloha(smallest, highest, how_many):
      #Zadanie: Sám si zapíšeš koľko random čísel chceš a od koľko po koľko.
    
      zoznam = []
      
      if smallest < highest:
            for num in range(how_many):
                totaly_random = random.randint(smallest, highest)
                zoznam.append(totaly_random)
            return print(*zoznam)
            
      else:
            return print("TY PRIMITIV!")

prva_uloha(int(input("Zadaj najmenšie číslo: ")), int(input("Zadaj najväčšie číslo: ")), int(input("Zadaj počet koľko čísel chceš vygenerovať: ")))
