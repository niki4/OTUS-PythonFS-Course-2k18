import os
import argparse
import collections

from libs import stat

top_size = 200
words = []

cli_parser = argparse.ArgumentParser()
cli_parser.add_argument('-p', '--project', nargs='*', help='Project folder name(s) or path(s) to analyze')
cli_opts = cli_parser.parse_args()

projects = cli_opts.project

if not projects:
    projects = next(os.walk('.'))[1]
    print('No projects to analyze were specified.\nI will analyze all subdirs of current dir:', projects)

for project in projects:
    p_path = os.path.join(os.curdir, project)
    print('-'*30 + '\nAnalyzing', p_path)
    words.extend(stat.get_top_verbs_in_path(p_path))

print('='*30 + '\nTotal %s words, %s unique' % (len(words), len(set(words))))
for word, occurrence in collections.Counter(words).most_common(top_size):
    print(word, occurrence)
