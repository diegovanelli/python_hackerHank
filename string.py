# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = 'qA4'

    print(s)
    has_alphanum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    for i in s:
        print(i)
        if i.isalnum():
            has_alphanum = True
        if i.isalpha():
            has_alpha = True
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
    print(has_alphanum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)