from funcs import *

locations = get_locations('locations')

pmr = PatternModel()
backgroundpm = pmr.read_patternmodel(locations['Background_corpus'])
pmr.threshold = 1000
legalpm = pmr.read_patternmodel(locations['Legal_corpus'])

print(len(legalpm.keys()))