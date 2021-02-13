import pygame
from settings import *

# longest sequence length is 666 (pygame will do a 18x37 window for the window size i have made)

class Game:
    def __init__(self, sequence, info):
        self.sequence = sequence
        self.info = info

        pygame.init()

        # Create a screen and a clock
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

        self.running = True
        # Load assets like textures and audio
        self.load_data()

    def load_data(self):
        pass

    def new(self):

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()

            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        None

    def draw(self):
        self.screen.fill(LIGHTGREY)
        #pygame.display.set_caption(f"{self.clock.get_fps():.2F} FPS")

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Arial', 30)
        #textsurface = myfont.render(self.sequence, False, (0, 0, 0))
        renderTextCenteredAt(self.sequence, myfont, BLACK, 450, 0, self.screen, 900, self.info)
        #self.screen.blit(textsurface, (0, 0))

        pygame.display.flip()


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
    sequence = 'GAATTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG'
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


def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width, info):
    # first, split the text into words
    words = list(text)
    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        line_len = len(line)



        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset
        #font.set_underline(True)

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh


def main():
    sequence, minPal = getSequenceAndMinPalandromeLength()
    comp_seq = getReverseComplement(sequence)
    palandrome_data = findPalandromes(minPal, sequence, comp_seq)

    game = Game(sequence, palandrome_data)
    while game.running:
        game.new()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()


