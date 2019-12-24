from letter import Letter


class Text:
    def __init__(self, text, font="dejavu/DejaVuSans.ttf", fontsize=10):
        self.text = text
        self.font = "/usr/share/fonts/truetype/{}".format(font)
        self.fontsize = fontsize
        self.array = []
        self.letters = []
        self.render_letters()
        self.fill_array()

    def render_letters(self):
        for char in self.text:
            self.letters.append(Letter(char, self.font))

    def fill_array(self):
        for letter in self.letters:
            for i in range(len(letter.array)):
                if len(self.array) == 8:
                    self.array[i] += letter.array[i]
                else:
                    self.array.append(letter.array[i])




