''' This is a small project of implementing RSA Algorithm '''

class RSAenc_dec:
    def __init__(self, p, q):
        self.n = p * q
        self.m = (p - 1) * (q - 1)
        self.public_key, self.private_key = self.generate_keys()
        
    # Calculate the GCD 
    def pgcd(self, a, b):
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        return b
    
    # Check if a and b are relatively prime numbers
    def premiers(self, a, b):
        return self.pgcd(a, b) == 1
    
    #Gathering intermediate values using Euclide algorithm
    def liste_valeurs(self, a, b):
        L, r = [], a % b
        while r != 0:
            r = a % b
            L.append((a, b))
            a = b
            b = r
        return L

    # return the (u,v) solutions of the Bezout equation ax+by=1
    def coiff_bizout(self, a, b):
        u, v = 1, 0
        for i in self.liste_valeurs(a, b)[::-1]:
            u, v = v, u - (i[0] // i[1]) * v
        return u, v
    
    # Generate public and private keys using Bizout equation
    def generate_keys(self):
        for k in range(self.m - 1, 2, -1):
            if self.premiers(k, self.m):
                d, v = self.coiff_bizout(k, self.m)
                if 2 < d < self.m:
                    break
        return [(self.n, k), (self.n, d)]
    
    # binary conversion
    def binaire(self, n):
        B = []
        while n != 0:
            B.append(n % 2)
            n = n // 2
        return B[::-1]
    # Calculate power using Logarithmic time complexity log(n) algorithm
    def puissance(self, x, B):
        p = 1
        for i in range(len(B)):
            p = p ** 2
            if B[i] == 1:
                p = p * x
        return p
    
    # RSAencryption return the Encrypted text using ASCII Caracters and public key
    def RSAencryption(self, text):
        C = []
        T = [ord(i) for i in text]

        for i in range(len(text)):
            C.append(chr(self.puissance(T[i], self.binaire(self.public_key[1])) % self.n))
        return ''.join(C)
    
    # RSAdecryption return the original text using private key
    def RSAdecryption(self, C):
        return ''.join([chr(self.puissance(ord(C[i]), self.binaire(self.private_key[1])) % self.n) for i in range(len(C))])

#EXEMPLE
p=719
q=127

rsa = RSAenc_dec(p, q)

text="CYBERSECURITY FOR EVER"

#---Encryption
encrypted_text = rsa.RSAencryption(text)
print('Encrypted:', encrypted_text)

#---Decryption
decrypted_text = rsa.RSAdecryption(encrypted_text)
print('Decrypted:', decrypted_text)



