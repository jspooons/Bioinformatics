def equal(str, arr):
    for i in range(len(str) - 1):
        if str[i] == arr[i]:
            continue
        else:
            return False

    return True


def getSequenceAndMinPalandromeLength():
    # min = 6
    minPal = int(input("Enter a minimum palandrome length: \n"))

    #sequence = input("Enter your sequence: \n")
    #print('\n')
    #sequence = 'AAATTTATAGAAGAGTCTAGACATG'
    sequence = 'AAATTT'
    sequence.replace(" ", "")
    sequence.upper()

    return sequence, minPal


def getReverseComplement(sequence):
    len_seq = len(sequence)

    comp_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp_seq = []

    for i in range(len_seq):
        base = sequence[i]
        comp_base = comp_dict.get(base)
        comp_seq.append(comp_base)

    return comp_seq


def findPalandromes(minPal, sequence, comp_seq):
    len_seq = len(sequence)

    palandromes_and_pos = []
    # palandromes = []
    for j in range(len_seq - minPal+1):
        l = minPal
        while l + j <= len_seq:
            if equal(sequence[j:l + j], list(reversed(comp_seq[j:l + j]))):
                palandromes_and_pos.append([sequence[j:l + j], j + 1, l])
                # palandromes.append(sequence[j:l+j])
            l += 1

    print('Printing list [[palandrome, position]... ]\n')
    print(palandromes_and_pos)


def main():
    sequence, minPal = getSequenceAndMinPalandromeLength()
    comp_seq = getReverseComplement(sequence)
    findPalandromes(minPal, sequence, comp_seq)


if __name__ == "__main__":
    main()
