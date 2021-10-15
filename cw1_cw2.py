# # Cwiczenie 1
# Zad 1
a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
literka1 = "a"
literka2 = "b"
# # Zad 2
d = len(a)
print(d)
b = a.count(literka1)
c = a.count(literka2)
print(b)
print("W tekście jest {0} liter a  oraz {1} liter b.". format(b, c))
# Zad 3
zad3 = "Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate."
print('{:10}'.format(zad3))
print('{:^10}'.format(zad3))
print('{:.5}'.format(zad3))
print('{:10.5}'. format(zad3))


# Zad 4
zmienna_typu_string = "bllalalallalalla"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())
# Zad 5
ewelina = "Ewelina Wesolowska"
zad5 = (ewelina[1:].capitalize())
print(zad5)
# Zad 6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1 = lista[0:4]
lista2 = lista[5:10]
print(lista1, lista2)
# Zad 7
lista3 = lista1 + lista2
print(lista3)
liczba = 0
lista3.insert(0, liczba)

print(lista3)
new_list = lista3.copy()
new_list.sort(reverse=True)
print(new_list)
# # Zad 8
listakrotek = [(145863, "Ewelina Wesołowska"), (123455, "Slawomir Hucz"), (234537, "Jan Jurkowski")]
# Zad 9
slowniklistykrotek = { n for n in listakrotek}
print(slowniklistykrotek)
#
# # Zad 10
lista10 = [1234564844, 355555123, 3333443123, 1234564844]
final_new_menu = list(set(lista10))

print(final_new_menu)
# Zad 11
for i in range(11):
    print(i)

#12
zad12 = [range(100, 20, 5)]
zad12.reverse()
print(zad12)

#Ćwiczenie 2
# Zad 1
a_list = [0, 1, 2, 3, 4, 5, 6, 7]
b_list = [10, 20, 30, 40, 50]
def funkcja1 (a_list, b_list):
    lista = []
    for x, y in zip(a_list, b_list):
        if a_list[x] % 2 == 0:
            lista.append(x)
        else:
            lista.append(y)
    return lista

print(funkcja1(a_list, b_list))

# # Zad 2
dictionary = {}
def funkcja2(data_text):
    x = data_text.upper()
    y = data_text.lower()
    dictionary = {'length': len(data_text), 'letters': list(data_text), 'big_letters': x, 'small_letters': y }
    return dictionary

print(funkcja2('Kamsm ssffdf weedvgkgkg'))

# Zad 3
text = 'ewelina wesolowska'
letter = 'w'
def funkcja3(text, letter):
    counter = 0
    for i in text:
        if i==letter:
            counter +=1
    return counter

print(funkcja3(text, letter))
# # Zad 4
def convert_to_fahrenheit(celsius):
    c = float(celsius)
    f = c * 9 / 5 + 32
    k = float(273.15 + c)
    r =float((c + 273.15) * 1.8)
    print (f, k, r)

convert_to_fahrenheit(12)

# Zad 5
class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        a = self.x + self.y
        return a
    def difference (self):
        a = self.x - self.y
        return a
    def multiply(self):
        a = self.x * self.y
        return a
    def divide(self):
        if (self.y == 0):
            a = "You can't divide by zero!"
        else:
            a = self.x / self.y
        return a

x = Calculator(2,3)
print(x.divide())
print(x.add())
# Zad 6
class ScienceCalulator(Calculator):
    def power(self):
        a = self.x ** self.y
        return a

y = ScienceCalulator(4,5)
print(y.power())
# # Zad 7
tekst ="koteł"
def odtylu(tekst):
    odwrotny = tekst[::-1]
    return odwrotny
print(odtylu(tekst))
