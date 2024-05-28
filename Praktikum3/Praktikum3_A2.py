# %% [markdown]
# Das Chiffrat encrypted.bin (Binärdatei) ist mit RC4 verschlüsselt worden, der Schlüssel ist unbekannt. Ihre Aufgabe ist es, den Klartext wiederzugewinnen. Gehen Sie dafür wie folgt vor:
# (a) Schreiben Sie eine Software für die Ver- und Entschlüsselung mit dem Stromchiffre RC4.
# (b) Nutzen Sie Ihre RC4-Software für einen Brute-Force-Angriff auf den Chiffrattext. Starten Sie hierfür mit den Annahmen, dass
# (i) der Schlüsselraum klein ist und (ii) alle verwendeten Schlüsselbytes Kleinbuchstaben (ASCII-Code) sind. Gehen Sie auch diesmal wieder davon aus, dass der Klartext ein Text einer natürlichen Sprache ist.
# 
# Implementierung, die man Copy Paste machen kann
# https://github.com/manojpandey/rc4/blob/master/rc4-3.py

# %%
## Read in files
# Read in chiffrat
en = open('encryptedbin.sec', 'rb')
encrypt = en.read()


# %% [markdown]
# RC4 Verschlüsselung Implementierung

# %%
# Will use codecs, as 'str' object in Python 3 doesn't have any attribute 'decode'
import codecs


def initalize(key):
    #initalize is for initializing the key 

    #convert a single unicode character into its integer represntation
    key = [ord(c) for c in key]
    keylength = len(key)

    #make a list 
    S = list(range(256))
    
    
    j = 0
    for i in range(256):
        t = key[i % keylength]
        j = (j + S[i] + t) % 256
        #swap values
        S[i], S[j] = S[j], S[i]
    return S

def get_keystream(key):
    #get the keystream 

    S = initalize(key)
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % 256]
        yield K

def crypt_logic(text, key):
    #key needs to be in keystream already

    #make array for result
    result = []

    #for the entire text xor with keystream
    for counter in text:
       #xor the two strings
       #xored = chr(counter ^ (next(key)))
       xored = ("%02X" % (counter ^ (next(key))))
       result.append(xored)
    result = ''.join(result)
    #result is in hexform
    return result



def natural_language(result):
    #try making it an ascii string
    try:
        n_result = codecs.decode(result, 'hex_codec').decode('ASCII')
        #bei ä geht das nicht, weil kein ASCII Zeichen
        print(n_result)
        return(n_result)
    except:
        #if not ascii does not work out, reset xored
        #return 'try again'
        pass

def RC4_decrypt(ciphertext, key):
    #process of decrypting with RC4

    keystream = get_keystream(key)

    #make ascii ciphertext into hexcoded ciphertext
    #ciphertext = codecs.decode(ciphertext, 'hex_codec')
    
    res = crypt_logic(ciphertext, keystream)

    #try making it into natural language
    result = natural_language(res)
    return result


def RC4(ciphertext, key):
    #process of encrypting with RC4

    #convert a single unicode character into its integer represntation
    ciphertext = [ord(c) for c in ciphertext]

    #initialize and get keystream
    keystream = get_keystream(key)
    encrypt_text = crypt_logic(ciphertext, keystream)
    return encrypt_text


#test_text = 'TEST'
#test_key = 'Key'
#test_text ='BBF316E8D940AF0AD3'
#print(RC4_decrypt(test_text, test_key))


# %%
import itertools
from itertools import product
import string

#generate key from a... to z...
def generate_key_num(length):
    for combination in product(string.ascii_lowercase, repeat=length):
        yield list(combination)

def get_keys(length):
    keys = []
    key_generator = generate_key_num(length)
    
    #test
    #for i in key_generator:
      #  print (i)
    
    while True:
        try:
            keys.append(next(key_generator))
        except:
            break
    return keys

i = 2
for i in range(1, 6):
    print(i)
    canidates = get_keys(i)

    for j in canidates:
        #make array of characters into a string to use as a key
        key = ''.join(str(c) for c in j)
        print(key)
        RC4_decrypt(encrypt, key)
    


# %% [markdown]
# 5
# aaaaa
# aaaab
# aaaac
# aaaad
# aaaae
# aaaaf
# aaaag
# aaaah
# aaaai
# aaaaj
# aaaak
# aaaal
# aaaam
# aaaan
# aaaao
# aaaap
# aaaaq
# aaaar
# aaaas
# aaaat
# aaaau
# aaaav
# aaaaw
# aaaax
# aaaay
# aaaaz
# aaaba
# aaabb
# aaabc
# aaabd
# aaabe
# aaabf
# aaabg
# aaabh
# aaabi
# aaabj
# aaabk
# aaabl
# aaabm
# aaabn
# aaabo
# aaabp
# aaabq
# aaabr
# aaabs
# aaabt
# aaabu
# aaabv
# aaabw
# aaabx
# aaaby
# aaabz
# aaaca
# aaacb
# aaacc
# aaacd
# aaace
# aaacf
# aaacg
# aaach
# aaaci
# aaacj
# aaack
# aaacl
# aaacm
# aaacn
# aaaco
# aaacp
# aaacq
# aaacr
# aaacs
# aaact
# aaacu
# aaacv
# aaacw
# aaacx
# aaacy
# aaacz
# aaada
# aaadb
# aaadc
# aaadd
# aaade
# aaadf
# aaadg
# aaadh
# aaadi
# aaadj
# aaadk
# aaadl
# aaadm
# aaadn
# aaado
# aaadp
# ...
# oxqju
# oxqjv
# oxqjw
# oxqjx
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...


