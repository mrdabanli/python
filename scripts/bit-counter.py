bits = [] #list of bits
count = int(input("How many bits do you want ?: ")) #number of bits

for bit in range(count):
    print("")
    bits.append(int(input("0/1 ?: "))) #append bits to list

bitCounter = 0 #count the number of 1's
repeatedCount = 0 #count repeated 1's

for bit in bits:
    if bit == 1:
        bitCounter+=1
    if bit == 1 and bitCounter == 2:
        repeatedCount+=1
    if bit == 0:
        bitCounter=0
        
#result
print("\n" + str(bits) + " => " + str(repeatedCount) + "\n")
    
