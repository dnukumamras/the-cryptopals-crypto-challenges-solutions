'''
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
'''
def main():
    with open('4.txt') as f:
        cipher = " ".join(line.strip() for line in f)  

    Detect_single_character_XOR(cipher)


def Detect_single_character_XOR(hexStr):
    lines = hexStr.split()
    All_possible = []
    for line in lines:
        l = bytearray(line.decode('hex'))
        for i in range(256):
            pt = [chr(y^i) for y in l]
            All_possible.append([len(filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' ', pt)), ''.join(pt), i])
    
    ans = max(All_possible, key=lambda x: x[0])

    #print "Key is: " + hex(ans[2])
    print "Message is: " + ans[1]


if __name__ == "__main__":
    main()