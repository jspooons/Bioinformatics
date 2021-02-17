from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from math import floor

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


def getSequenceAndMinPalandromeLength():
    minPal = 6
    #minPal = int(input("Enter a minimum palandrome length: \n"))

    #sequence = input("Enter your sequence: \n")
    #print('\n')
    #sequence = 'AAATTTATAGAAGAGTCTAGACATG'
    sequence = 'GAAATTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG'
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
    palandrome_data = []
    # palandromes = []
    for j in range(len_seq - minPal+1):
        l = minPal
        while l + j <= len_seq:
            if equal(sequence[j:l + j], list(reversed(comp_seq[j:l + j]))):
                palandromes_and_pos.append([sequence[j:l + j], j + 1]) # palandrome and position
                palandrome_data.append([j+1, l]) # position of a palandrome and the length of it
                # palandromes.append(sequence[j:l+j])
            l += 1

    print('Printing list [[palandrome, position]... ]\n')
    print(palandromes_and_pos)

    return palandrome_data


def renderTextCenteredAt(text, font, colour, x, y, d, allowed_width, info, img):
    # first, split the text into words
    words = list(text)

    # now, construct lines out of these words
    lines = []
    lines_ = []
    counter = 0
    # TO DO: counter for counting letter position
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            counter+=1
            #print(counter)
            for i in range(len(info)):
                if (info[i][0] == counter):
                    line_words[len(line_words)-1] = line_words[len(line_words)-1]

            line_words.append(words.pop(0))
            #print(line_words)
            #if (len(line_words) == 0):


            fw, fh = font.getsize(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)
    #print(lines)
    #lines[0][0] = lines[0][0]+'\u0332'
    #test = [['d','d']]
    #test[0][0] = test[0][0]+'e'+'d'
    #print(test)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    ty=0
    for line in lines:
        line_len = len(line)



        fw, fh = font.getsize(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset
        #font.set_underline(True)

        d.text((tx, ty), line, font=font, fill=BLACK)

        y_offset += fh

    return img, ty+fh+5


def findLargestChar(chars, font):
    largest = chars[0]

    for i in range(1, len(chars) - 1):
        if font.getsize(chars[i]) > font.getsize(largest):
            largest = chars[i]

    return largest


def checkFit(width, height, text, font, largest):
    largest_size = font.getsize(largest)
    length = len(text)

    width_amount = floor(width/largest_size)
    height_amount = floor(height/largest_size)

    if width_amount * height_amount <= length:
        return False

    return True, width_amount, height_amount


def optimise(no_chars):
    cols = 1;
    rows = 1;

    while (no_chars > cols * rows):
        cols += 1;
        if (no_chars > cols * rows):
            rows += 1;
        else:
            break


def drawText(sequence, seq_info, width, height, colour, background):
    img = Image.new('RGB', (width, height), color=background)

    fnt = ImageFont.truetype('/Library/Fonts/arial.ttf', 20)
    d = ImageDraw.Draw(img)

    img2 = img.crop((0,0,width,height))
    img2.save('pil_text_font.png')
    img2.show()


def main():
    sequence, minPal = getSequenceAndMinPalandromeLength()
    comp_seq = getReverseComplement(sequence)
    palandrome_data = findPalandromes(minPal, sequence, comp_seq)


if __name__ == "__main__":
    main()