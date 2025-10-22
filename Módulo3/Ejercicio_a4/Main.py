'''
Dada la siguiente instancia y sus atributos, crea
una clase que la instancie.
np2005 = Nobel ("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)
'''
from Nobel import Nobel
if __name__ == '__main__':
    np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
    print(np2005.category, np2005.year, np2005.winner)