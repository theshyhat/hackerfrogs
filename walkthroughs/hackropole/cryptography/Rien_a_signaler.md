# URL
https://hackropole.fr/en/challenges/crypto/fcsc2024-crypto-rien-a-signaler/
# Concept
* Incorrect implementation of RSA cryptosystem
# Method of solve
* there are two files to interact with, `rien-a-signaler.py` and `output.txt`
* the Python script is the one that created the text file, and we notice something off about it:
```Python
import json
from Crypto.Util.number import getPrime, bytes_to_long

def keygen(n = 1024):
        p = getPrime(n)
        q = getPrime(n)
        n = p * q
        e = 2 ** 16 + 1
        d = pow(e, -1, (p - 1) * (q - 1))
        sk = (d, n)
        pk = (e, n)
        return pk, sk

# Read the flag as an integer
m = bytes_to_long(open("flag.txt", "rb").read())

# Generate RSA keys
sk, pk = keygen()

# Encrypt the flag
c = pow(m, pk[0], pk[1])

# Output public key and ciphertext
d = {
        "e": pk[0],
        "n": pk[1],
        "c": c,
}
print(json.dumps(d, indent = 4))
```
* specifically, the private key and the public key are reversed:
```Python
def keygen(n = 1024):
        p = getPrime(n)
        q = getPrime(n)
        n = p * q
        e = 2 ** 16 + 1
        d = pow(e, -1, (p - 1) * (q - 1))
        sk = (d, n)
        pk = (e, n)
        return pk, sk

sk, pk = keygen()
```
* this means that the ciphertext was created using the `d` value instead of the `e` value
* since the `d` value was used to encrypt, we can use the `e` value to decrypt, the opposite of the usual `e` to encrypt and `d` to decrypt
* this Python script gets the job done:
```Python
from Crypto.Util.number import long_to_bytes

N = 15796942747309728499758004731551695370913663306666035509299434642801916886496898004446545897149657535285268305926374338100837909963511256277964036962044387829939281166102731090331978991280163210213940391251452338553405036351243486418991475381065523778778374159216111211039724992140348798301914302441933569705494577465736752087544176074475722982600742085989140379907623574747713824460161103249270448563714176784913386788071348191510218812659925461534747629228752452045853041012162619056264262054391967199115369336548943331022933845667724296738334370747384492830658154258526863726939357154899976616849634493499797766299
d = 2 ** 16 + 1
c = 8974868290281688737233990325600894780715849339628541493919631966007477856153771121147897587192029426714635875587384109624607194486211852465796766441066196469272988076202321557112300294463883797708163984188107199926745938577562219282934551167072277621808474131345695591468145868455419473050498493285402336637848596791275101533878984692539165395918338275186762268105380646876795842765910627488934075701761752437069042340873474933889573307306539126206460702731582652544213958040586038088129224761895431978602343177304095553828090049657631935349611981192723124744317395844933142968117051307548448128268941861109853064071

def rsa_decrypt():
    m = pow(c, d, N)
    pt = long_to_bytes(m)
    print("Decrypted message:", pt)

rsa_decrypt()
```
