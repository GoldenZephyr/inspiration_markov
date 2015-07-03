import random


class Markov(object):
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()
        self.generated_phrase = ''

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words

    def triples(self):
        """ Generates triples from the given data string. So if our string were
                        "What a lovely day", we'd generate (What, a, lovely) and then
                        (a, lovely, day).
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 3):
            yield (str.lower(self.words[i]), str.lower(self.words[i + 1]), self.words[i + 2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self, size=25):
        seed = random.randint(0, self.word_size - 3)
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word
        w1 = w1.title()
        gen_words = []
        for i in xrange(size):

            num = random.randint(0, 100)
            if num % 10 == 0:
                w1 = str.upper(w1)
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1.lower(), w2.lower())])
            #if ('.' in w1) | ('!' in w1):
            #    w2 = w2.title()
            #if
        gen_words.append(w2)
        self.generated_phrase = ' '.join(gen_words)
        return ' '.join(gen_words)

    def save(self,path,mode = 'w'):
        with open(path,mode) as fn:
            fn.write(self.generated_phrase)
            fn.write('\n\n\n')
