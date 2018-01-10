import os
import collections

from code_cleanup.dclnt_stat import Statistic

import nltk
nltk.download('averaged_perceptron_tagger')


stat = Statistic()

top_size = 200
words = []
projects = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]
for project in projects:
    p_path = os.path.join(os.curdir, project)
    words += stat.get_top_verbs_in_path(p_path)

print('total %s words, %s unique' % (len(words), len(set(words))))
for word, occurrence in collections.Counter(words).most_common(top_size):
    print(word, occurrence)
