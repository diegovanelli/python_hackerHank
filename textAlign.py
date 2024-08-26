def print_formatted(number):
    s = ""
    l = len(bin(number).replace('0b', ''))
    format = '{:>'+ str(l) +'}'
    for i in range(1, number+1):
        s += format*4 +"\n".format(i, oct(i).replace('0o', ''), str(hex(i)).replace('0x', '').upper(), bin(i).replace('0b', '')) 
    print(s)

if __name__ == '__main__':
    n = 2
    print_formatted(n)

