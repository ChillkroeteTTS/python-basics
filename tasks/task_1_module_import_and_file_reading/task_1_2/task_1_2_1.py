# Hier kommt deine erste Programmieraufgabe.
# Du kannst die Aufgabe mit dem Wissen aus der Datei task_1_2_overview.py lösen.

# range ist eine Funktion, die dir eine Liste von Nummern zurückgibt. In diesem Fall eine Liste der Zahlen 0-100.
# In Programmiersprachen wird bei solch Funktionen zwischen zwei Verhaltensarten unterschieden: exclusive und inclusive.
# Im wesentlichen beschreibt es nur, ob das angegebene Zahlenintervall den Start oder wie hier Endpunkt mit einbezieht 0-101 oder eben nicht (0-100).
# Pythons range Funktion verhält siuch also exclusive.
eins_bis_hundert = range(0, 101)

# Der folgende Teil enthält eine sogenannte Schleife. Er gibt alle Zahlen von 0-100 aus, die glatt durch 2 teilbar sind.
# All der Code, der eingerückt ist, wird für jedes Element einzeln ausgeführt. Also 100 mal in diesem Fall.
# Codeblöcke werden in Python durch die Einrückung markiert. Verrückst du den untenstehenden COde also wird er nicht mehr funktionieren.
# Andere Programmiersprachen lösen das gleiche Problem oft mit den Klammern {} anstatt durch die Einrückung.
for number in eins_bis_hundert:
    # Eine If-Abfrage steuert den Programmablauf. Wenn das Ergebnis hinter dem if True ergibt, wird der erste Block ausgeführt. Andernfalls der Block hinter dem else.
    if number % 2 == 0: # Der Modulo Operator % berechnet den Rest einer Division. 2.5 % 2 ergibt also 0.5.
        print(number)
    else:
        pass # pass ist in Python ein Platzhalter. DU kannst es benutzten wenn du einen Codeblock erst später befüllen möchtest. In diesem Fall hätte das else und das pass auch komplett weggelassen werden können. Der Effekt wäre derselbe.

# Gib alle durch 2 teilbaren Zahlen von 0 bis -100 aus, ohne die range Methode zu benutzen!
# Verbotene Elemente: range()
# ==================================
for number in eins_bis_hundert:
# ==================================
    if number % 2 == 0:
        print(number)
