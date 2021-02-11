#min = 6
min = int(input("Enter a minimum palandrome length: \n"))

sequence = input("Enter your sequence: \n")
print('\n')
#sequence = 'TAGAAGAGTCTAGACATG'
sequence.replace(" ", "")
sequence.upper()
len_seq = len(sequence)


comp_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
comp_seq = []

palandromes_and_data = []
palandromes = []

for i in range(len_seq-1):
    base = sequence[i]
    comp_base = comp_dict.get(base)
    comp_seq.append(comp_base)

def equal(str, arr):
    for i in range(len(str)-1):
        if str[i] == arr[i]:
            continue
        else:
            return False

    return True

for j in range(len_seq-min):
    l = min
    while l+j < len_seq:
        if equal(sequence[j:l+j], list(reversed(comp_seq[j:l+j]))):
            palandromes_and_data.append([sequence[j:l+j], j+1])
            #palandromes.append(sequence[j:l+j])
        l += 1

print('Printing list [[palandrome, position]... ]\n')
print(palandromes_and_data)