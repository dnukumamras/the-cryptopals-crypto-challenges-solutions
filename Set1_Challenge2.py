def xor(buf1,buf2):
	if len(buf2) == len(buf1):
		cipher = bytearray()
        for i in range(len(buf1)):
            cipher.append(chr(buf1[i]^buf2[i]))
        return cipher
        

def main():
    # decode hex encoding to array of bytes 
    buffer1 = bytearray('1c0111001f010100061a024b53535009181c'.decode('hex'))
    buffer2 = bytearray('686974207468652062756c6c277320657965'.decode('hex'))

    # output should be 746865206b696420646f6e277420706c6179
    out = '746865206b696420646f6e277420706c6179'.decode('hex')
    #print out = the kid don't play
    xr = xor(buffer1,buffer2)
    print xr

if __name__ == "__main__":
    main()