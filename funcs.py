import zipfile


def get_locations(filename = 'locations.txt'):
    with open (filename, 'rt') as f:
        lines = f.readlines()
        locationdict = {line.split("=")[0].strip():line.split("=")[1].strip() for line in lines}
        f.close()
    return locationdict


class entry:
    def __init__(self):
        pass



class PatternModel:
    def __init__(self, encoding = 'utf-8', threshold = 100):
        self.encoding = encoding
        self.threshold = threshold

    def read_patternmodel(self, location):
        pm_dict = {}
        zf = zipfile.ZipFile(location, 'r')
        for filename in zf.namelist():
            data = zf.read(filename)
            data = data.decode(self.encoding).split('\n')
            for i, line in enumerate(data):
                line = line.split('\t')

                if not i == 0 and len(line[0]) > 0 and int(line[1]) > self.threshold:
                    pm_dict[line[0]] = {'freq':int(line[1])}

        self.location = location
        self.nrtokens = sum(pm_dict.values())
        self.nrtypes = len(pm_dict.items())
        self.patternstats = pm_dict

    def compute_refreqs(self):
        relfreqdict = {}
        for word, count in self.patternstats:
            self.patternstats[word]['relfreq'] = count/self.nrtokens


