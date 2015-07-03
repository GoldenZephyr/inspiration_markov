import random

class Markov(object):

        def __init__(self, open_file):
                self.cache = {}
                self.open_file = open_file
                self.words = self.file_to_words()
                self.word_size = len(self.words)
                self.database()


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

                for i in range(len(self.words) - 2):
                        yield (self.words[i], self.words[i+1], self.words[i+2])

        def doubles(self):

            if len(self.words) < 2:
                return

            for ii in xrange(len(self.words) - 1):
                yield (self.words[ii],self.words[ii + 1])

        def database(self):
                for word,next_word in self.doubles():
                        key = word
                        if key in self.cache:
                                self.cache[key].append(next_word)
                        else:
                                self.cache[key] = [next_word]

        def generate_markov_text(self, size=25):
                seed = random.randint(0, self.word_size-3)
                seed_word = self.words[seed]
                w1 = seed_word
                gen_words = []
                for i in xrange(size):
                        gen_words.append(w1)
                        w1 = random.choice(self.cache[w1])
                gen_words.append(w1)
                return ' '.join(gen_words)