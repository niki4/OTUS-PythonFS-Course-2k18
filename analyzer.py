import os
import sys
import collections

from libs.stat import Statistic

stat = Statistic()

top_size = 200
words = []
if len(sys.argv) > 1:
    projects = sys.argv[1:]            # If there target folder in command line, use it...
    print('Analyzing these projects:', sys.argv[1:])
else:
    projects = next(os.walk('.'))[1]  # ...otherwise scan for folders in current script location
    print('No projects to analyze specified.\nGoing over current dir:', projects)

for project in list(projects):
    p_path = os.path.join(os.curdir, project)
    words += stat.get_top_verbs_in_path(p_path)

print('total %s words, %s unique' % (len(words), len(set(words))))
for word, occurrence in collections.Counter(words).most_common(top_size):
    print(word, occurrence)
