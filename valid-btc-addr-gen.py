
import os
import sys
from pybitcoin import BitcoinPrivateKey

os.system("clear")

print ("=============================================")
print ("       Valid Bitcoin Address Generator       ")
print ("=============================================")
print ("       Author : Rahat Khan Tusar(rkt)        ")
print ("       Github : https://github.com/r3k4t     ")
print ("=============================================")

private_key = BitcoinPrivateKey()
public_key = private_key.public_key()
print ("Valid BTC Address is :")
print (public_key.address())
