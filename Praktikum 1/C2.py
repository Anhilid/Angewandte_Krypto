with open('chiffrat2.txt', 'r') as file:
    f = file.read()
print(f)

absolute = [0] * 26
relative = [0] * 26

for x in range(26):
    anzahl = 0
    for c in f:
        if ord(c) == x+65:
            anzahl = anzahl+1
    absolute[x]=anzahl
    
for x in range(26):
    relative[x] = absolute[x]/len(f)    


print("Absolute values are:")
print(absolute)
print("Relative values are:")
print(relative)

Koinzidenzindex = 0.
for x in range(26):
    Koinzidenzindex += absolute[x]*(absolute[x]-1)
Koinzidenzindex /= len(f)*(len(f)-1)

Erwartungswert = 0.076
print("Koinzidenzindex ist:")
print(Koinzidenzindex)

print("Erwartungswert ist:")
print(Erwartungswert)

Koinzidenzindexe = [0.]*20
for i in range(20):
    fAufgeteilt = ""
    for c in range(len(f)):
        if c%(i+1)==0:
            fAufgeteilt += f[c]

    absolute2 = [0] * 26
    for x in range(26):
        anzahl = 0
        for c in fAufgeteilt:
            if ord(c) == x+65:
                anzahl = anzahl+1
        absolute2[x]=anzahl

    Koinzidenzindex2 = 0.
    for x in range(26):
        Koinzidenzindex2 += absolute2[x]*(absolute2[x]-1)
    Koinzidenzindex2 /= len(fAufgeteilt)*(len(fAufgeteilt)-1)
    Koinzidenzindexe[i] = abs(Koinzidenzindex2-0.076)

closest = min(Koinzidenzindexe)

print("Fuer Schluessellaenge " + str(Koinzidenzindexe.index(closest)+1) + ":")
print("Abweichung von " + str(closest))

Keylength = (Erwartungswert-1/26)


