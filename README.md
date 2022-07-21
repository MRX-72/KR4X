# KR4X
Advanced File and string encryption and decryption 

# Installation
``` git clone https://github.com/MRX-72/KR4X ```
> 
``` cd KR4X ```
> 
``` pip3 install -r requirements.txt ```
> 
``` bash setup.sh ```
> 
> Type: ``` Krax.py -h ``` for usage and commands

# Examples
> 
> Original Content
```
[Mrx@System]$ cat confidential.txt
Mrx here

Password: H1DENP455W0RD

secret_code: PasMrxHxKrax
```
> 
> Encrypted Content
> 
``` 
[Mrx@System]$ Krax.py -f confidential.txt -E --aes

[HASHER] > Encrypted =>  confidential.txt
[HASHER] > KEY       =>  4Uwdmp9_A8n6o1jPOWBCXP0rXW8kK1kKcBV1r8DoGQ8=

[Mrx@System]$ cat confidential.txt
gAAAAABi2XhORo8314mD2xKrnBbKCPE1dr79HTcmwlarkobVi13vjAsIqbv1khA-EIzhUWy_Okm86fB8td6--NMv8mPj3bYL70gOI9l9ijo94foOAHR6BX35IsPwlltBnZi0OjLEtmiK0frdHFOOADh9beoLdOh9Rw==

```
> 
> Decryption
> 
``` 
[Mrx@System]$ Krax.py -f confidential.txt -D --key 4Uwdmp9_A8n6o1jPOWBCXP0rXW8kK1kKcBV1r8DoGQ8= --aes

[HASHER] > Decrypted =>  confidential.txt
[HASHER] > KEY       =>  4Uwdmp9_A8n6o1jPOWBCXP0rXW8kK1kKcBV1r8DoGQ8=

[Mrx@System]$ cat confidential.txt
Mrx here

Password: H1DENP455W0RD

secret_code: PasMrxHxKrax
```
> Explore further by hashing passwords and string
