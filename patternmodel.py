
class Entry:
    def __init__(self):
        pass

    def line2entry(self, line):
        if type(line) == str:
            line = line.split('\t')

        self.pattern =  line[0]
        self.count =    line[1]
        self.tokens =   line[2]
        self.coverage = line[3]
        self.category = line[4]
        self.size =     line[5]
        self.frequency =    line[6]

        return self

class Patternmodel:
    def __init__(self):
        self.entries = {}

    def read_patternmodel(self, filename):
        print('load patternmodel from {}'.format(filename))
        with open(filename, 'rt') as f:
            data = f.readlines()

        for i, line in enumerate(data):
            line = line.split('\t')
            entry = Entry()
            entry.line2entry(line)
            self.entries[line[0]] = entry

