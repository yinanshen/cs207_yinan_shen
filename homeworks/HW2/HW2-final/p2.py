from collections import Counter
import matplotlib.pyplot as plt

def languages(filename):
    file = open(filename, "r+")
    thelist = file.read().strip().split('\n')
    countlist = Counter(thelist)
    language_count = {}
    for key, value in countlist.items():
        language_count[key] = value
    print(language_count)
    return language_count

Result = languages('languages.txt')

the_figure = plt.figure()
x_coords = range(len(Result))
freqs = list(Result.values())
plt.bar(x_coords, freqs)
plt.xticks(x_coords, list(Result.keys()))
plt.show()
the_figure.savefig('P2.png')
