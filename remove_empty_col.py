filename = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/patternmodels/wikicorpus_patternmodel.tab"
outfilename = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/patternmodels/wikicorpus_patternmodel_good.tab"

with open(filename, 'rt') as f:
    data = f.readlines()

with open(outfilename, 'wt') as out:
    for i, line in enumerate(data):
        if i == 0:
            print(line.split('\t'))
            out.write(line)
            continue

        line = line.split('\t')
        outlist = line[:2] + line[3:]

        outline = '{}'.format( '\t'.join(outlist))
        out.write(outline)
