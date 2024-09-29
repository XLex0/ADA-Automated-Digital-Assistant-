import Levenshtein
import re

def comparaLevenshtein(original, comparacion):
        distancia = Levenshtein.distance(original, comparacion)
        return distancia


            

        
if __name__ == '__main__':
        pass