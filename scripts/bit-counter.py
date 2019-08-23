bits = [] #list of bits
count = int(input("how many bits do you want ?: ")) #1 byte

for bit in range(count):
    print("")
    bits.append(int(input("0/1 ?: ")))

bitCounter = 0
repeatedCount = 0

for bit in bits:
    if bit == 1:
        bitCounter+=1
    if bit == 1 and bitCounter == 2:
        repeatedCount+=1
    if bit == 0:
        bitCounter=0
        
#result
print("\n" + str(bits) + " => " + str(repeatedCount) + "\n")
    
