'''
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.
'''

def main():
	hex_encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	hexD = bytearray(hex_encoded.decode('hex'))
	Singlebyte_XOR_cipher(hexD)

#print hex_encoded.decode('hex')

'''
How? Devise some method for "scoring" a piece of English plaintext. 
Character frequency is a good metric. Evaluate each output and choose the one with the best score.


Logic: hex_encoded has been XOR'd against a single character. Hexadecimal is one byte. That is 8 bits. 
So need to iterate all possible  00000000 to 11111111. That is 0 to 255 inclusive. So write a function that xor's hex_encoded with every possible key.
Count number of human readable text for each iteration. That is number of alphabets [a-z or A-Z]
'''


def Singlebyte_XOR_cipher(hexStr):
	All_possible = []
	for i in range(256):
		pt = [chr(y^i) for y in hexStr]
		All_possible.append([len(filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' ', pt)), ''.join(pt), i])
	ans = max(All_possible, key=lambda x: x[0] )
	print "Key is: " + hex(ans[2])
	print "Message is: " + ans[1]
	#print ans[2]

if __name__ == "__main__":
    main()