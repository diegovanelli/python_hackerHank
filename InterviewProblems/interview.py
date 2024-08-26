from collections import Counter

a= [5,1,2,4,4,2,1,6,5,6,3]
counter = Counter(a)
retorno = [key for key, value in counter.items() if value == 1]
print(retorno[0])