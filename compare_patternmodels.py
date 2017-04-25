import pandas as pd

RECHT_FILENAME = #Legal corpus name
BACKGROUND_FILENAME = #Background corpus name

print('load rechtdf')
recht_df = pd.read_csv(RECHT_FILENAME, delimiter='\t', index_col=False)
print ('load background_df')
background_df = pd.read_csv(BACKGROUND_FILENAME, delimiter='\t', index_col=False)

print (recht_df["CATEGORY"].unique())

recht_ngrams_df = recht_df.loc[recht_df['CATEGORY'] == 'ngram']  # select only N-grams (no skipgrams)
recht_ngrams_df = recht_ngrams_df.loc[recht_df['COUNT'] >= 10]   # The ngram must occur at least 10 times in the legal corpus
recht_ngrams_df = recht_ngrams_df.loc[recht_df['SIZE'] <= 3]     # the maximum size of n-grams



background_ngrams_df = background_df.loc[background_df["CATEGORY"] == 'ngram']   # select only N-grams (no skipgrams)
background_ngrams_df = background_ngrams_df.loc[background_df["COUNT"] >= 10]   # The ngram must occur at least 10 times in the legal corpus
background_ngrams_df = background_ngrams_df.loc[background_df["SIZE"] <= 3]      # the maximum size of n-grams

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
