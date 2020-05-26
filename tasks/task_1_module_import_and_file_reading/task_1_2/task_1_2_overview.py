# Hier soll dir ein Überblick über die grundlegendsten Syntax Eigenschaften von Python gegeben werden.
# Du kannst immer wieder hier hin zurückkehren um verschiedene Operationen nachzuschlagen.
# Variablen wurden ja schon in Task 1.1 eingeführt. Sie können die Werte verschiedener Datentype beeinhalten.
# Die wichtigsten Datentypen in Python sind Nummern, Strings, boolsche Werte, Listen, Dicts und Funktionen.
# Funktionen behandeln wir in einem späteren Kapitel noch einmal genauer.

# Boolsche Werte - Können nur die Ausprägung True oder False haben. Sie werden oft zur Steuerung von Programmen benutzt
bool_1 = True
bool_2 = True and False # Logisches UND, Beide Seiten des 'and' müssen true sein, damit das Ergebnis true ist.
bool_3 = True or False  # Logisches ODER, s reicht wen neine Seite des 'or' true ist, damit der Gesamtausdruck true wird.
bool_4 = 5 == 5         # Logisches prüfen auf Gleichheit
bool_5 = 5 != 5         # Logisches prüfen auf Ungleicheit
bool_6 = 5 >= 4         # Logisches prüfen auf größer oder gleich
bool_7 = not (5 >= 4)   # Ausdrücke in Klammern werden zuerst ausgeführt! In diesem Fall ist 5 >= 4 zwar True, das not vor der Klammer negiert das Ergebnis allerdings. Der Gesamtausdruck ist also False

# Nummern
# ----------------------------------------------------------------------------------------------------------------------
number_1 = 3
number_2 = -5.5 # Eine negative Zahl mit Nachkommastelle
number_3 = number_1 + number_2  # Simple Addition
number_4 = number_1 - number_2  # Simple Subtraktion

# Strings
# ----------------------------------------------------------------------------------------------------------------------
string_1 = 'Hello World!'

# Listen
# ----------------------------------------------------------------------------------------------------------------------
list_1 = []  # Liste ohne Inhalt
list_2 = [number_1]  # Liste mit einem Element
# Liste mit zwei Element unterschiedlicher Datentypen. In viele Programmiersprachen wäre das gar nicht möglich!
# In der Regel ist das allerdings auch keine gute Idee, da es so leicht zu Fehlern bei der Verarbeitung der Liste führen kann.
list_3 = [number_3, string_1]
list_4 = [number_1, number_2]
list_5 = [number + 1 for number in list_4] # Dieses Konsturkt nennt sich 'List Comprehension'. In diesem Fall wird jeder Nummer aus list_4 mit 1 addiert. Die Werte in list_4 bleiben unverändert! Nur list_5 enthält die addierten Werte
list_6 = [number + 1 for number in list_4 if number > number_1] # Hier werden in das Ergebnis der List Comprehesion, nur Werte aufgenommen für die der Ausdruck hinter dem if True ergibt. Nur number_2 wird also mit 1 addiert.

# Dicts - Die Kurzform von Dictionary
# ----------------------------------------------------------------------------------------------------------------------
# Dicts kannst du benutzen um Daten zusammenzufassen. Du kannst in ihnen Werte unter einem beliebigen String ablegen.
# Wie in einem Nachschlagewerk eben. Die Strings werden auch Keys genannt, die Werte Values. Die Values können von jedem Datentyp sein. Du kannst also auch ein Dict in ein Dict schachteln.
# In anderen Programmiersprachen werden diese Konstrukte auch oft Map oder Record bezeichnet.

dict_1 = {}
dict_2 = {'Eine Nummer': number_1}
dict_3 = {'eins bis 3': [1, 2, 3]}
dict_4 = {'geschachtelt': {             # geschachteltes Dictionary mit einem Wert aus einem anderen Dict
    'Eins': dict_2['Eine Nummer']}
}

# Hier werden alle Werte auf der Kommandozeile ausgegeben
# ----------------------------------------------------------------------------------------------------------------------
print(bool_1)
print(bool_2)
print(bool_3)
print(bool_4)
print(bool_5)
print(bool_6)
print(bool_7)

print(number_1)
print(number_2)
print(number_3)
print(number_3)

print(string_1)

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(list_6)

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
