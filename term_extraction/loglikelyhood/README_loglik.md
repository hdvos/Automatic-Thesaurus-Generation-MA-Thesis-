Input to this pipeline is a patternmodel as created by colibri core (van Gompel and van den Bosch, 2016):

1. clean_patternmodel: patternmodels take a lot of space. The last collumn contains all the indexes of this ngram. Removing this collumn drastically reduces the space the file takes.
2. remove_emptycol.py: for some reason there is an empty collumn in the patternmodel. The origin of this empty collumn I cannot trace. Therefore this script removes it.
3. compare_patternmodels.py: computes the likelyhood ratio of the ngrams in the two patternmodels and prints those higher than a given threshold


van Gompel, M., & van den Bosch, A. (2016). Efficient n-gram, skipgram and flexgram modelling with Colibri Core. Journal of Open Research Software, 4(1).
