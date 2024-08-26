def count_substring(string, sub_string):
    count = 0
    idx = 0
    while string.find(sub_string, idx, len(string)) > -1:
        count += 1
        idx = string.find(sub_string, idx, len(string)) + 1
                
    return count

if __name__ == '__main__':
    string = 'BlUeBe1Bl*fjal9jkl'
    sub_string = 'Bl'
    
    count = count_substring(string, sub_string)
    print(count)