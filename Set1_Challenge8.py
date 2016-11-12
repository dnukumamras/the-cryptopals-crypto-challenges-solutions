'''

Detect AES in ECB mode
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; 
the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

'''
def AES_ECB_detect(ciphertext, blockSize):
  block_count = len(ciphertext)/blockSize
  for i in range(block_count):
    for j in range(i+1,block_count):
      if ciphertext[i*blockSize:(i+1)*blockSize] == ciphertext[j*blockSize:(j+1)*blockSize]:
        return True
  return False

def main():
	for ct in open('8.txt'):
	  ct = ct.strip()
	  if AES_ECB_detect(ct.decode("hex"), 16):
	    print ct
	    #print ct.decode("hex")

	 #d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a

if __name__ == "__main__":
	main()