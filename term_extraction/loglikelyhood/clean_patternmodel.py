import zipfile

PATH = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/corpora/rechtspraaknl_300k/"
ZIPFILE = "readable_patternmodel.zip"
ZIPFILENAME = PATH + ZIPFILE

FILENAME = "total_tokenized.colibri.readablepatternmodel"

OUTFILENAME = PATH + "readablepatternmodel_cleaned.tab"

out = open(OUTFILENAME, 'wt')

i = 0
with zipfile.ZipFile(ZIPFILENAME) as myzip:
    with myzip.open(FILENAME) as myfile:
        for line in myfile:
            line = line.decode("utf-8")
            line = line.split('\t')
            output = ("\t").join(line[:-1]) + '\n'

            out.write(output)
            i += 1

            if i%10000 == 0:
                print("{} lines processed.".format(i))

print("Finished!")
print("{} lines processed".format(i))
out.close()
