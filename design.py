import textwrap

u = input()
u = u.split(' ')
s = '.|.'
n = int(u[0])
m = int(u[1])
x = 1
y = int(n/2)+1
for i in range(1, n+1):
    p = int((m - len(s))/2)
    if (i < y):
        x = x+2
        print('-'*p + s + '-'*p)
    if (i == y):
        text = 'WELCOME'
        j = int((m - len(text))/2)
        print('-'*j + text + '-'*j)
        x = x-2
    if (i > y):
        x = x-2
        print('-'*p + s + '-'*p)
    s = '.|.'*x

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ---------WELCOME---------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------