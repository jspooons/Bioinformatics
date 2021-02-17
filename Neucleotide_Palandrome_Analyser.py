from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from math import floor
import tkinter as tk
from functools import partial

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHTGREY = (220, 220, 220)





def equal(str, arr):
    for i in range(len(str) - 1):
        if str[i] == arr[i]:
            continue
        else:
            return False

    return True


def getSequenceAndMinPalandromeLength(minPal, sequence):
    #minPal = 6
    #minPal = int(input("Enter a minimum palandrome length: \n"))

    #sequence = input("Enter your sequence: \n")
    #print('\n')
    #sequence = 'AAATTTATAGAAGAGTCTAGACATG'
    #sequence = 'GAAATTTAAAAAAAAAATTTAAAATTTG'
    sequence.replace(" ", "")
    sequence.upper()

    return sequence, int(minPal)


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
    palandrome_data = []
    # palandromes = []
    for j in range(len_seq - minPal+1):
        l = minPal
        while l + j <= len_seq:
            if equal(sequence[j:l + j], list(reversed(comp_seq[j:l + j]))):
                palandromes_and_pos.append([sequence[j:l + j], j + 1])  # palandrome and position
                palandrome_data.append([j+1, l])  # position of a palandrome and the length of it
                # palandromes.append(sequence[j:l+j])
            l += 1

    print('Printing list [[palandrome, position]... ]\n')
    print(palandromes_and_pos)

    return palandrome_data


def findLargestChar(chars, font):
    largest = chars[0]

    for i in range(1, len(chars) - 1):
        if font.getsize(chars[i]) > font.getsize(largest):
            largest = chars[i]

    return largest


def checkFit(width, height, text, font, largest):
    largest_size = font.getsize(largest)
    length = len(text)

    width_amount = floor(width/largest_size[0])
    height_amount = floor(height/largest_size[1])

    if length > ((floor(width_amount/2) + 1) * height_amount):  # too big (letters over fill)
        return 0, -1, -1
    elif length < ((floor(width_amount/2) + 1) * (height_amount-1)) + 1:  # too small (letters under fill)
        return 1, -1, -1
    else:
        return 2, width_amount, height_amount


# tries to optimise for a square grid of letters
def optimise(num_elems):
    cols = 1;
    rows = 1;

    while (num_elems > cols * rows):
        cols += 1;
        if (num_elems > cols * rows):
            rows += 1;
        else:
            break

    return cols, rows


def getPos_column(matrix, i):
    return [row[i]-1 for row in matrix]


def getLen_column(matrix):
    return [row[1] for row in matrix]


def drawText(sequence, seq_info, width, height, colour, background):
    img = Image.new('RGB', (width, height), color=background)
    d = ImageDraw.Draw(img)
    fit = -1
    fontsize = 8
    allowed_num_cols = 0
    allowed_num_rows = 0
    w = 0
    h = 0
    fnt = ''
    pal_positions = getPos_column(seq_info,0)
    pal_lengths = getLen_column(seq_info)

    while fit != 2:
        fnt = ImageFont.truetype('/Library/Fonts/arial.ttf', fontsize)
        largest = findLargestChar(['A', 'T', 'C', 'G'], fnt)
        w, h = fnt.getsize(largest)

        fit, allowed_num_cols, allowed_num_rows = checkFit(width, height, sequence, fnt, largest)

        if fit == 0:
            fontsize -= 1
        elif fit == 1:
            fontsize += 1

    counter = 0
    for i in range(allowed_num_rows):
        for j in range(allowed_num_cols):
            if j % 2 == 0:
                if (counter== len(sequence)):
                    break

                if counter in pal_positions:
                    d.text((j * w, i * h), sequence[counter], font=fnt, fill=RED)
                    subfontsize = floor(fontsize/4)
                    subfnt = ImageFont.truetype('/Library/Fonts/arial.ttf', subfontsize)
                    d.text((j * w +w, i * h +h*0.8), str(counter+1), font=subfnt, fill=BLUE)
                    d.text((j * w + w, i * h), str(pal_lengths[counter]), font=subfnt, fill=GREEN)
                else:
                    d.text((j * w, i * h), sequence[counter], font=fnt, fill=colour)

                counter += 1

    img.save('pil_text_font.png')
    img.show()


def run(minPal, sequence):
    sequence, minPal = getSequenceAndMinPalandromeLength(minPal, sequence)
    comp_seq = getReverseComplement(sequence)
    palindrome_data = findPalandromes(minPal, sequence, comp_seq)
    drawText(sequence, palindrome_data, 900, 600, BLACK, LIGHTGREY)


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.canvas = tk.Canvas(self.root, width=400, height=450, relief='raised')
        self.canvas.pack()

        self.setup()

    def setup(self):
        label1 = tk.Label(self.root, text='Nucleotide Palindrome Analyser')
        label1.config(font=('helvetica', 14))
        self.canvas.create_window(200, 25, window=label1)

        label2 = tk.Label(self.root, text='Min palindrome length:')
        label2.config(font=('helvetica', 10))
        self.canvas.create_window(200, 100, window=label2)

        entry1 = tk.Entry(self.root)
        self.canvas.create_window(200, 140, window=entry1)

        label3 = tk.Label(self.root, text='Nucleotide sequence:')
        label3.config(font=('helvetica', 10))
        self.canvas.create_window(200, 240, window=label3)

        entry2 = tk.Entry(self.root)
        self.canvas.create_window(200, 280, window=entry2)

        button1 = tk.Button(text='Get Palindromes', command=lambda: run(entry1.get(), entry2.get()), bg='brown',
                            fg='white',
                            font=('helvetica', 9, 'bold'))
        self.canvas.create_window(200, 380, window=button1)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
