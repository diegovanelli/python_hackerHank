from collections import Counter

def ransom_note(magazine, rasom):
    dictionary = Counter()
    line = Counter()
    for word in magazine:
        dictionary[word] += 1
    for word in ransom:
        line[word] += 1
    for word in ransom:
        if line[word]>dictionary[word]:
            return False
    return True


    
if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
