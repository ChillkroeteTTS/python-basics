minus_hundert_bis_hundert = range(-100, 100)

# Schreibe jede Zahl die größer oder gleich 0  und kleiner als 11 ist unter einem beliebigen String in das Dictionary.
# Die Ausgabe sollte also ein dictionary mit den Zahlen 0 bis 10 enthalten.
dict = {}
for number in minus_hundert_bis_hundert:
# ==================================
    if number >= 0 and number < 11:
        dict[str(number)] = number
# ==================================

print(dict)
