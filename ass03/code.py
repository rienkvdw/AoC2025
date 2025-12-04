# assignment 3
import time

ts = time.time()
# uitlezen text bestandje
with open('ass03/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    banks = inputstring.splitlines()

tr = time.time()
# part 1
joltages1 = []
for bank in banks:
    dig1 = max(bank[0:-1])
    id1 = bank.index(dig1)
    dig2 = max(bank[id1+1:len(bank)])
    joltages1.append(int(dig1)*10+int(dig2))
print("The sum of joltages for part 1 is " + str(sum(joltages1))) # correcte waarde is 17166

t1 = time.time()

# part 2
# wow het is een functie, bijna alsof dit een recursive iets is en anders je echt veel te hard beunt
def findjoltage(bank, id, dig, sum):
    value = max(bank[id+1:len(bank)-dig])
    id_nxt = bank[id+1:len(bank)-dig].index(value)+id+1
    sum += int(value)*(10**dig)
    if dig != 0:
        dig -= 1
        return findjoltage(bank, id_nxt, dig, sum)
    else:
        return sum
# hier alleen nog ff de functie callen
joltages2 = [findjoltage(bank,-1,11,0) for bank in banks]

print("The sum of joltages for part 2 is " + str(sum(joltages2))) # correcte waarde is 169077317650774

t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**6//1)) + " us;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")
# average van 10 runs is ongeveer
# kost 130 us, 1200 us, 4500 us, 5700 us