# In Oboedencia Veritas

# UVa ID: 10033

# Note: passe the test cases present in problem statement and
#       test cases available on UDebug but get WA on online judge.

def set_reg(reg, ram, d, n):
    reg[d] = n
    reg[d] %= 1000

def add(reg, ram, d, n):
    reg[d] += n
    reg[d] %= 1000

def mult(reg, ram, d, n):
    reg[d] *= n
    reg[d] %= 1000

def set_ds(reg, ram, d, s):
    reg[d] = reg[s]

def add_ds(reg, ram, d, s):
    reg[d] += reg[s]
    reg[d] %= 1000

def mult_ds(reg, ram, d, s):
    reg[d] *= reg[s]
    reg[d] %= 1000

def setreg_dr(reg, ram, d, a):
    reg[d] = int(ram[reg[a]])

def setram_sa(reg, ram, s, a):
    v = str(reg[s])
    while len(v) < 3:
        v = '0' + v

    ram[reg[a]] = v

def goto_ds(reg, ram, d, s):
    if reg[s] != 0:
        return reg[d]
    else:
        return False



instructions = {
    2: set_reg,
    3: add,
    4: mult,
    5: set_ds,
    6: add_ds,
    7: mult_ds,
    8: setreg_dr,
    9: setram_sa,
    0: goto_ds
}


def interpreter(reg, ram):
    i = 0
    icount = 0
    while i < len(ram):
        # print(i, icount, reg, ram[:i+1])
        # input()
        ins, first_arg, second_arg = map(int, ram[i])
        params = (reg, ram, first_arg, second_arg)
        if ins == 1:
            icount += 1
            break
        if ins == 0:
            icount += 1
            move = goto_ds(*params)
            if move:
                i = move
            else:
                i += 1
        if ins > 1:
            i += 1
            icount += 1
            # execute and go to next instruction in sequence
            instructions[ins](*params)

    return icount


ncase = int(input())
input()

for case_count in range(ncase):
    ram = ['000'] * 1000
    reg = [0] * 10

    i = 0
    while True:
        ins = input()
        if ins == '':
            break
        ram[i] = ins
        i += 1

    icount = interpreter(reg, ram)

    print(icount)
    if (case_count+1) == ncase:
        break
    print()

