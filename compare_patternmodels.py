import pandas as pd

RECHT_FILENAME = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/patternmodels/strafrecht_patternmodel_good.tab"
BACKGROUND_FILENAME = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/patternmodels/wikicorpus_patternmodel_good.tab"

print('load rechtdf')
recht_df = pd.read_csv(RECHT_FILENAME, delimiter='\t', index_col=False)
print ('load background_df')
background_df = pd.read_csv(BACKGROUND_FILENAME, delimiter='\t', index_col=False)



print (recht_df["CATEGORY"].unique())

recht_ngrams_df = recht_df.loc[recht_df['CATEGORY'] == 'ngram']
recht_ngrams_df = recht_ngrams_df.loc[recht_df['COUNT'] >= 10]
recht_ngrams_df = recht_ngrams_df.loc[recht_df['SIZE'] <= 3]



background_ngrams_df = background_df.loc[background_df["CATEGORY"] == 'ngram']
background_ngrams_df = background_ngrams_df.loc[background_df["COUNT"] >= 100]
background_ngrams_df = background_ngrams_df.loc[background_df["SIZE"] <= 3]

xcount = 0
for index, row in recht_ngrams_df.iterrows():
    ngram = row["PATTERN"]
    freq = row["FREQUENCY"]

    if ngram in background_ngrams_df["PATTERN"].values:
        background_item = background_ngrams_df.loc[background_df["PATTERN"] == ngram]
        background_freq = float(background_item["FREQUENCY"])


        likelyhood_ratio = freq/background_freq

        if likelyhood_ratio >= 5:
            print("{}\t{}".format(ngram, likelyhood_ratio))
            xcount += 1


    #print('{}\t{}'.format(ngram, freq))

print(xcount)





'''

with open(RECHT_FILENAME) as f:
    rechtdata = f.readlines()

with open(BACKGROUND_FILENAME) as f:
    background_data = f.readlines()
'''