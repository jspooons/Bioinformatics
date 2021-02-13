import pygame
from settings import *


class Game:
    def __init__(self):
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

        pygame.display.flip()


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
    #sequence, minPal = getSequenceAndMinPalandromeLength()
    #comp_seq = getReverseComplement(sequence)
    #findPalandromes(minPal, sequence, comp_seq)

    game = Game()
    while game.running:
        game.new()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()


