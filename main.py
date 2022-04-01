#1.	Izdrukāt visus skaitļus no 1 lidz dotajam skaitlim.
"""
n = int(input("Izdrukāt skaitli no 1 līdz: "))
for i in range(1, n+1):
  print(i)
"""
#2.	Stabiņā viens zem otra jāizvada vārds CIKLS x reizes.
"""
x = int(input("Cik reizes jūs vēlaties ievadīt vārdu CIKLS: "))
for i in range(1, x+1):
  print("CIKLS")
"""
#3.	Stabiņā viens zem otra jāizvada nolasītais vārds x reizes.
"""
vards = str(input("Kādu vārdu jūs vēlaties izdrukāt: "))
x = int(input("Cik reizes jūs vēlaties šo vārdu ievadīt: "))
for i in range(1, x+1):
  print(vards)
"""
#4.	Izdrukāt mazāko skaitli vienu zem otra tik reizes, cik liels ir lielākais skaitlis.
"""
x = int(input("Ievadi mazāko skaitli: "))
n = int(input("Ievadi lielāko skaitli: "))
for i in range(1, n+1):
  print(x)
"""
#5.	Izvaddatu vienīgajā rindā jāizvada visu pēc kārtas veselu skaitļu summa no a līdz b, ieskaitot skaitļus a un b
"""
sum = 0
a = int(input("Ievadiet skaitli a: "))
b = int(input("Ievadiet skaitli b: "))
for i in range(a, b+1):
  sum = sum + i
print(sum)
"""
#6.	Izvaddatu vienīgajā rindā jāizvada visu pēc kārtas veselu skaitļu reizinānujms no a līdz b, ieskaitot skaitļus a un b
"""
a = int(input("Ievadiet skaitli a: "))
b = int(input("Ievadiet skaitli b: "))
multi = a
for i in range(a, b):
  multi = multi * (i+1)
print("Reizinājums ir: ", multi)
"""
#7.	Jāizvada cik reižu meklējamais cipars x atrodas skaitļos no otrās rindiņas līdz beigām.
"""
while (True):
  Skaits = 0
  a = int(input("Ievadiet sākuma skaitli: "))
  b = int(input("Ievadiet beigu skaitli: "))
  x = int(input("Ievadiet ciparu, kuru jūs vēlaties atrast: "))
  for i in range(a+1, b+1):
    sk = i
    while sk > 0:
      atl = sk % 10
      sk = int(sk/10)
      if atl == x:
        Skaits += 1
        print(Skaits, ". Skaitlis ", i, "satur ", atl)
  print ("Kopā atrasti: \"", Skaits, "cipari ", x)
  atkartot = str(input("Atkrtot? (Y/N): "))
  if atkartot != "Y" and atkartot != "y":
    break
"""
#8.	Ievada skaitli, izdrukāt cik veselu pāra skaitļu, kuri mazāki par ievadīto skaitli.
"""
Skaits = 0
b = int(input("Ievadiet beigu skaitli: "))
for i in range(1, b):
  if i % 2 == 0:
    Skaits += 1
print(Skaits)
"""
#9.	Izrēķināt ievadītā skaitļa ciparu summu.
"""
ievadits = input("Ievadiet naturālu skaitli: ")
try:
  Skaitlis = int(ievadits) 
  if Skaitlis > 0:
    #raise Exception()
    Sum = 0
    while Skaitlis > 0:
      atl = Skaitlis % 10
      Skaitlis = int(Skaitlis/10)
      Sum = Sum + atl
    print(Sum)
  else:
    print("Nav ievadīts naturāls skaitlis!")
except:
  print("Nav ievadīts naturāls skaitlis!")
"""