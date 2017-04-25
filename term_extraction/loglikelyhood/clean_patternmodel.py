filename = # Filename of the Patternmodel
outfilename = # Filename of the 'cleaned' Patternmodel

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
