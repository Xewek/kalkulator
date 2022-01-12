
print("_"*25)
print(" ")
print(" "*10+"WITAM")
print("_"*25)

#input pobiera info z kolnsoli od uzytkownika


info = input("podaj imię: ")

print("Wiataj " + info + " ciesze się że wróciłeś ^^")

# kalkurator
#int - pełna liczba 
#floaat _wartość 2.5
print("*" * 26)
print(" ")
print(" " *10 + "KALKULATOR")
print(" ")
print("*" * 26)


print(" "*24, "*")
print(" "*24, "*")
print(" "*24, "*")
print(" "*24, "*")

#wynik = {"+": a+c, "-": a-c, "*": a*c, "/": a/c, "**": a**c}
def dodawanie(a,c):
    return a + c
def ode(a,c):
    return a - c
def mno(a,c):
    return a * c
def dzi(a,c):
    return a / c
def pot(a,c):
    return a ** c
def pie(a,c):
    return a // c

print("1.Dodawanie", " "*12, "*")
print("2.odejmowanie", " "*10, "*")
print("3.Mnożenie", " "*13, "*")
print("4.Dzielenie", " "*12, "*")
print("5.Potegowanie", " "*10, "*")
print("6.Pierwiastkowanie", " "*5, "*")
print(" "*24, "*")
print("*" * 26)
print(" ")

wybor = -1
while(wybor != 0):
    wybor = int(input("Witaj " + info + " wybierz działanie podając cyfre z Menu: "))

    a = int(input("podaj pierwszą liczbe: "))
    c = int(input("podaj drugą liczbe: "))

    if wybor==1:
        print(" "*10+"WYNIK")
        print(" "*11, dodawanie(a,c))
    elif wybor==2:
        print(" "*10+"WYNIK")
        print(" "*11, ode(a,c))
    elif wybor==3:
        print(" "*10+"WYNIK")
        print(" "*11, mno(a,c))
    elif wybor==4:
        print(" "*10+"WYNIK")
        print(" "*11, dzi(a,c))
    elif wybor==5:
        print(" "*10+"WYNIK")
        print(" "*11, pot(a,c))
    elif wybor==6:
        print(" "*10+"WYNIK")
        print(" "*11, pie(a,c))
    else:
        print("Error!: wpisany znak operacyjny nie istnieje...")






