with open('chiffrat.txt', 'r') as file:
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

common = ["E","N","I","S","R","A","T","D","H","U","L","C","G","M","O","B","W","F","K","Z","P","V","J","Y","X","Q"]
key = [0] * 26

absolute2=absolute.copy()

for x in range(26):
    maxamount = max(absolute2)
    maxindex = absolute2.index(maxamount)
    key[maxindex] = common[x]
    absolute2[maxindex] = -1

#Manuelle swaps nach menschlichem ansehen vom loesungstext:


# LIE -> DIE; D <-> L
        
a, b = key.index('D'), key.index('L')
key[a], key[b] = key[b], key[a]

# DIOITALES -> DIGITALES;  O <-> G

a, b = key.index('O'), key.index('G')
key[a], key[b] = key[b], key[a]

# RIOHESHEIT -> SICHERHEIT; R <-> S, O <-> C

a, b = key.index('R'), key.index('S')
key[a], key[b] = key[b], key[a]
a, b = key.index('O'), key.index('C')
key[a], key[b] = key[b], key[a]

# ZESENTUICH -> WESENTLICH; Z <-> W, U <-> L

a, b = key.index('Z'), key.index('W')
key[a], key[b] = key[b], key[a]
a, b = key.index('U'), key.index('L')
key[a], key[b] = key[b], key[a]

# INBRASTRUZTUREN -> INFRASTRUKTUREN; B <-> F, Z <-> K
        
a, b = key.index('B'), key.index('F')
key[a], key[b] = key[b], key[a]
a, b = key.index('K'), key.index('Z')
key[a], key[b] = key[b], key[a]

# ZUBLIC-KEJ-KRJZTOGRAFIE -> PUBLIC-KEY-KRYPTOGRAFIE; Z <-> P, J <-> Y

a, b = key.index('Z'), key.index('P')
key[a], key[b] = key[b], key[a]
a, b = key.index('J'), key.index('Y')
key[a], key[b] = key[b], key[a]

# VU -> ZU; V <-> Z

a, b = key.index('Z'), key.index('V')
key[a], key[b] = key[b], key[a]

# JUANTENCOMPUTERN -> QUANTENCOMPUTERN; Q <-> J
a, b = key.index('Q'), key.index('J')
key[a], key[b] = key[b], key[a]

# XAHREN -> JARHREN; X <-> J
a, b = key.index('X'), key.index('J')
key[a], key[b] = key[b], key[a]

print("")
print("The Key is:")
print(key)


loesung = ""
for c in f:
    for x in range(26):
        if ord(c) == x+65:
            loesung += key[x]
    if ord(c) < 65 or ord(c) >= 65+26:
        loesung += c

print(loesung)

