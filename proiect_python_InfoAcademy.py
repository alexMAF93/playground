#!/usr/bin/env python3


from datetime import datetime
import pygal, smtplib, re

class Stoc:
    """Tine stocul unui depozit"""
    tot_categ = 0
    tot_prod = 0
    categorii = list()
    produse = list()
    categ_prod = {}

    def __init__(self, prod, categ, um='Buc', sold=0):
        self.prod = prod			# parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  		# fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold			# al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = {}					# fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = {}					# pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = {}
        Stoc.tot_prod += 1		    # la fiecare instantiere se calculeaza numarul produselor si al categ
        Stoc.produse.append(prod)           # populam lista cu produse

        if categ not in Stoc.categorii:     # populam lista cu categorii, daca nu exista (unicitate)
            Stoc.tot_categ += 1
            Stoc.categorii.append(categ)
            Stoc.categ_prod[categ] = {prod}
        else:
            Stoc.categ_prod[categ].add(prod)

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold += self.cant          # recalculam soldul dupa fiecare tranzactie
        if self.d.keys():               # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.i[cheie] = self.cant       # introducem valorile in dictionarele de intrari si data
        self.d[cheie] = self.data

    def iesi(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        #   datetime.strftime(datetime.now(), '%Y%m%d') in Python 3.5
        self.data = data
        self.cant = cant
        self.sold -= self.cant
        if self.d.keys():
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.e[cheie] = self.cant       # similar, introducem datele in dictionarele iesiri si data
        self.d[cheie] = self.data

    def fisap(self):
        print('Fisa produsului ' + self.prod + ': ' + self.um)
        print('----------------------------')
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
        print('----------------------------')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
        print('----------------------------')
        print('Stoc actual       ' + str(self.sold).rjust(10))
        print('----------------------------\n')


    def mail_export(self):
        """
        Trimite fisa produsul pe mail
        catre o adresa de mail introdusa
        de utilizator.
        """
        username = 'user@magazin.ro'
        parola = 'parolasmechera'
        expeditor = 'user@magazin.ro'
        mesaj = str(self.fisap()) # pentru ca functia fisap nu returneaza nimic, trebuie folosita functia str() pentru a stoca intr-o variabila textul
        try:
            smtp_ob = smtplib.SMTP('mail.magazin.ro:25')
            smtp_ob.login(username, parola)
            smtp_ob.sendmail(expeditor, destinatar, mesaj)
            print('Mesaj expediat cu succes!')
        except:
            print('Mesajul nu a putut fi expediat!')


fragute = Stoc('fragute', 'fructe', 'kg')       # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litru')
ceasuri = Stoc('ceasuri', 'ceasuri')
fragute.intr(100)
fragute.iesi(73)
fragute.intr(100)
fragute.iesi(85)
fragute.intr(100)
fragute.iesi(101)
ceasuri.intr(23)
ceasuri.iesi(12)
ceasuri.intr(31)
ceasuri.iesi(22)
lapte.intr(1500)
lapte.iesi(975)
lapte.intr(1200)
lapte.iesi(1490)
lapte.intr(1000)
lapte.iesi(1200)


class Mag1(Stoc):
    """Subclasa a clasei Stoc"""
    def __init__(self, p, c, u, x, y, z = 7):
        self.x = x
        self.y = y
        super().__init__(p,c,u)

    def perisabilitati(self, procent):
        '''Calculeaza valoarea perisabilitatilor si o scade din sold (iesire)'''
        s = 0
        for k,v in self.i.items():
            s += v
        p = int(s * procent / 100 + .99)
        self.iesi(p)


pepeni = Mag1('pepeni', 'fructe', 'kg', 'xpepeni', 'ypepeni')
pepeni.intr(2500)
pepeni.intr(1800)
pepeni.iesi(3972)
tabla = Mag1('tabla', 'mat_constr', 'kg', 'x', 'y')
tabla.intr(1000, '20170501')
tabla.iesi(877, '20170502')
tabla.intr(1500, '20170505')
tabla.iesi(1001)
tabla.intr(500)
tabla.perisabilitati(.5)


l = [fragute, lapte, ceasuri, tabla, pepeni] # lista cu instantele


def afisare_produse():
    """
    Afiseaza lista cu produsele disponibile
    atunci cand utilizatorul trebuie sa aleaga
    un produs despre care ii vor fi afisate anumite informatii
    """
    lista_produse = "" # incepem cu un sir gol, in care vom adauga numele produselor
    for i in l:
        lista_produse += i.prod + " " # separate de spatiu
    print("Produsele disponibile sunt: " + lista_produse)
    return lista_produse


def produse(produs):
    """
    Afiseaza fisa produsului; daca utilizatorul
    introduce un produs care nu exista
    va primi pe ecran un mesaj de eroare
    """
    ver = 0 # variabila cu care verificam daca produsul exista
    for i in l:
        if produs == i.prod: # daca exista, apelam metoda fisap
            i.fisap()
            ver = 1
    if ver == 0:
        print("Eroare: Produsul cautat nu se gaseste in baza noastra de date!")


def situatie_grafica(produs):
    """
    Creeaza un fisier svg care contine
    un grafic cu valorile de intrare / iesire
    pentru o anumita data, pentru un anumit
    produs
    """
    ver = 0 # variabila cu care verificam daca produsul exista
    lista_intrari = []
    lista_iesiri = []
    for i in l:
        if produs == i.prod:
            ver = 1 # daca produsul cautat se afla printre cele care exista, variabila asta va fi 1
            zi = input("Introduceti ziua: ")
            luna = input("Introduceti luna: ")
            an = input("Introduceti anul: ")
            if len(zi) < 2: # pentru a nu fi nevoit sa introducem zilele mai mici de 10 sub forma asta: 0x
                zi = '0'+zi
            if len(luna) < 2: # la fel ca la zi
                luna = '0'+luna
            if len(an) < 4: # la fel ca la zi, doar ca anul poate fi introdus din 2 cifre
                an = '20'+an
            data1 = an + " " + luna + " " + zi # data pentru care vrem sa vedem tranzactiile
            data_situatie = data1.replace(" ", "-")
            var1 = [] # din cauza ca pot fi introduse mai multe intrari/iesiri in aceeasi zi, vom folosi o lista care tine cheile dictionarului
            for j in i.d: # dictionarul cu date calendaristice, de unde luam cheia
                if i.d[j] == data_situatie.replace("-",""):
                    var1.append(j)
            for j in var1:
                if j in i.i: # dictionarul cu operatiunile de intrare
                    lista_intrari.append(i.i[j])
                if j in i.e: # dictionarul cu operatiunile de iesire
                    lista_iesiri.append(i.e[j])
            if len(lista_intrari) == 0 and len(lista_iesiri) == 0: # daca listele sunt goale, nu avem ce afisa
                print("Eroare : Nu exista suficiente date pentru generarea graficului")
            else:
                bar = pygal.Bar(x_title='', y_title='Valoare')
                bar.title = 'Situatie intrari/iesiri pentru ' + produs + ' in data de ' + data_situatie
                bar.add('Intrari', lista_intrari)
                bar.add('Iesiri', lista_iesiri)
                nume = produs + "_situatie_intrari_iesiri.svg" # numele sub care va fi salvat fisierul svg
                bar.render_to_file(nume)
                print("Grafic generat cu succes")
    if ver == 0: # in cazul in care produsul cautat nu este gasit, afiseaza un mesaj de eroare
        print("Eroare: Produsul cautat nu se gaseste in baza noastra de date!")


def situatie_mail(produs):
    """
    Apeleaza metoda mail_export
    a instantei clasei Stoc,
    daca aceasta exista
    """
    cnt = 0 # variabila cu care verificam daca produsul exista
    for i in l:
        if produs == i.prod: # daca produsul este gasit, apeleaza metoda mail_export
            i.mail_export()
            cnt += 1 # si incrementeaza variabila
    if cnt == 0:
        print("Produsul nu se gaseste in baza noastra de date")


def mail_alert(valoare, produs):
    """"
    Trimite un mail atunci cand
    valoarea stocului unui produs
    scade sub o anumita valoare
    """
    if produs.sold < valoare:
        print("Stoc critic pentru " + produs.prod + "\nTrimitere mail de alerta ...")
        username = 'user@magazin.ro'
        parola = 'parolasmechera'
        expeditor = 'user@magazin.ro'
        destinatar = 'patron@magazin.com'
        mesaj = "ALERTA!!! Stocul de " + produs.prod + " se epuizeaza. Sold disponibil: " + str(produs.sold)
        try:
            smtp_ob = smtplib.SMTP('mail.magazin.ro:25')
            smtp_ob.login(username, parola)
            smtp_ob.sendmail(expeditor, destinatar, mesaj)
            print('Mesaj expediat cu succes!')
        except:
            print('Mesajul de alerta nu a putut fi expediat!')


def cautare_produse(alegere):
    """
    Cauta produsele dupa nume
    sau tranzactiile dupa valoarea lor
    """
    if alegere.isalpha(): # verificam daca alegerea facuta este una dintre cele prezentate
        print("Optiune invalida !!!\nVa rugam sa alegeti dintre optiunile prezentate.")
        cautare_produse(input(" --> ")) # in cazul in care nu a fost introdus un numar de la tastatura, functia se auto apeleaza
    if alegere.isnumeric(): # alegerea trebuie sa fie neaparat un numar
        alegere = int(alegere)
        if alegere == 1: # pentru 1 se va realiza cautarea dupa nume
            lista_gasite = [] # lista in care vor fi adaugate produsele care se potrivesc pattern-ului
            patternu = ".*" + input("Introduceti numele / o parte din numele produsului cautat: ") + ".*"
            for i in l:
                p = re.match(patternu, i.prod,re.IGNORECASE) # nu este case sensitive
                if p:
                    lista_gasite.append(i.prod)
            if len(lista_gasite) > 0: # daca exista elemente in lista, acestea vor fi afisate
                print("Au fost gasite urmatoarele produse:")
                for i in lista_gasite:
                    print("==> " + i)
            else:
                print("Nu au fost gasite produse cu acest nume")
        elif alegere == 2: # pentru 2, se va cauta dupa valoarea tranzactiei
            valoare = input("Introduceti valoare cautata: ")
            if valoare.isnumeric(): # valoarea tranzactiei trebuie sa fie un numar
                cnt1 = 0  # variabile folosite pentru a determina daca nu au fost gasite tranzactii de intrare / iesire de o anumita valoare
                cnt2 = 0
                for i in l:
                    lista_gasite_intrari = []
                    lista_gasite_iesiri = []

                    for v in i.i:
                        patternu = "^" + valoare + "$" # pentru a nu avea rezultate inexacte. De exemplu, daca introducem 10, sa nu gaseasca si valori de genul 100, 910, 2310231
                        p = re.match(patternu, str(i.i[v]))
                        if p:
                            rezultat = "In data de " + str(i.d[v])[0:4] + "-" + str(i.d[v])[4:6] + "-" + str(i.d[v])[6:] + " s-au efectuat tranzactii in valoare de " + str(i.i[v])
                            lista_gasite_intrari.append(rezultat) # daca se potriveste vreo valoare din operatiunile de intrare, aceasta este adaugata in lista
                    if len(lista_gasite_intrari) > 0: # Daca lista nu este goala vor fi afisate datele in care au avut loc tranzactiile
                        cnt1+=1
                        print("\nPentru produsul: " + i.prod)
                        print("Operatiuni de intrare:")
                        for j in set(lista_gasite_intrari): # am folosit set pentru a elimina duplicatele
                            print(j)
                        print("*"*30)
                    for v in i.e:
                        patternu = "^" + valoare + "$"
                        p = re.match(patternu, str(i.e[v]))
                        if p:
                            rezultat = "In data de " + str(i.d[v])[0:4] + "-" + str(i.d[v])[4:6] + "-" + str(i.d[v])[6:] + " s-au efectuat tranzactii in valoare de " + str(i.e[v])
                            lista_gasite_iesiri.append(rezultat)
                    if len(lista_gasite_iesiri) > 0:
                        cnt2+=1
                        print("\nPentru produsul: " + i.prod)
                        print("Operatiuni de iesire:")
                        for j in set(lista_gasite_iesiri):
                            print(j)
                        print("*"*30)
                if cnt1 == 0: # daca aceste variabile sunt 0, inseamna ca nu au fost gasite tranzactii
                    print("Nu au fost gasite tranzactii de intrare cu aceasta valoare")
                if cnt2 == 0:
                    print("Nu au fost gasite tranzactii de iesire cu aceasta valoare")
            else:
                print("EROARE : Introduceti valori numerice") # daca este introdusa o valoare non-numerica, afiseaza un mesaj de eroare
                cautare_produse('2') # si se apeleaza singura
        else:
            print("Optiune invalida !!!") # la fel si daca nu este 1 sau 2
            cautare_produse(input(" --> "))


dict_alerta = {lapte: 30, fragute: 40, pepeni: 300, ceasuri: 30, tabla: 1000} # dictionar care contine valorile la care sunt trimise alertele
for v in dict_alerta:
    mail_alert(dict_alerta[v], v)


opt = ""
while opt != 0:
    print("Meniu principal")
    print("\nAlegeti din optiunile de mai jos:")
    print("Fisa produs".ljust(25) +" --> 1")
    print("Situatie intrari / iesiri".ljust(25) +" --> 2")
    print("Export situatii".ljust(25) +" --> 3")
    print("Cautare produs".ljust(25) + " --> 4")
    print("Iesire din Meniu".ljust(25) +" --> 0")
    opt = int(input(" ->> "))
    if opt == 1:
        afisare_produse()
        produse(input("Numele produsului: "))
    elif opt == 2:
        afisare_produse()
        situatie_grafica(input("Numbele produsului: "))
    elif opt == 3:
        print("Veti primi pe adresa de mail exportul ...")
        destinatar = input("Introduceti adresa dumneavoastra de email: ")
        afisare_produse()
        situatie_mail(input("Numele produsului: "))
    elif opt == 4:
        print("Alegeti din optiunile de mai jos:")
        print("Cautare dupa nume ".ljust(33) + " --> 1 ")
        print("Cautare dupa valoarea tranzactiei".ljust(33) + " --> 2 ")
        cautare_produse(input(" --> "))
    elif opt == 0:
        print("La revedere!!!")
        break
    else:
        print("Optiune invalida")
