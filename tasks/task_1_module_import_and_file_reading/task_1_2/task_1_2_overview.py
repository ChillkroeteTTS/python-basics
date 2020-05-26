# Hier soll dir ein Überblick über die grundlegendsten Syntax Eigenschaften von Python gegeben werden.
# Du kannst immer wieder hier hin zurückkehren um verschiedene Operationen nachzuschlagen.
# Variablen wurden ja schon in Task 1.1 eingeführt. Sie können die Werte verschiedener Datentype beeinhalten.
# Die wichtigsten Datentypen in Python sind Nummern, Strings, boolsche Werte, Listen, Dicts und Funktionen.
# Funktionen behandeln wir in einem späteren Kapitel noch einmal genauer.

# Boolsche Werte - Können nur die Ausprägung True oder False haben. Sie werden oft zur Steuerung von Programmen benutzt
bool_1 = True

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

# Dicts - Die Kurzform von Dictionary
# ----------------------------------------------------------------------------------------------------------------------
# Dicts kannst du benutzen um Daten zusammenzufassen. Du kannst in ihnen Werte unter einem beliebigen String ablegen.
# Wie in einem Nachschlagewerk eben. Diese Werte können alle Datentypen haben. Du kannst sie also auch schachteln.
# In anderen Programmiersprachen werden diese Konstrukte auch oft Map oder Record bezeichnet.

dict_1 = {}
dict_2 = {'Eine Nummer': number_1}
dict_3 = {'eins bis 3': [1, 2, 3]}
dict_4 = {'geschachtelt': {             # geschachteltes Dictionary mit einem Wert aus einem anderen Dict
    'Eins': dict_2['Eine Nummer']}
}

# If
# ----------------------------------------------------------------------------------------------------------------------

# Hier werden alle Werte auf der Kommandozeile ausgegeben
# ----------------------------------------------------------------------------------------------------------------------
print(bool_1)

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

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
