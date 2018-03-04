import os
import argparse
from collections import Counter

from libs import stat

top_size = 200
words = []


def load_projects(projects_list=None):
    if not projects_list:
        projects_list = next(os.walk('.'))[1]
        print('No projects to analyze were specified. Analyzing all subdirs of current dir:', projects_list)
    return projects_list


def clone_from_git(git_repository_link=None):
    if git_repository_link and git_repository_link.endswith('.git'):
        os.system("git clone %s" % git_repository_link)
        return True


if __name__ == '__main__':
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-p', '--project', nargs='*', help='Project folder name(s) or path(s) to analyze')
    cli_opts = cli_parser.parse_args()

    projects = load_projects(cli_opts.project)

    for project in projects:
        if project not in os.listdir():
            print("No %s found on local drive." % project)
            if not clone_from_git(input('Provide .git link to clone project from Git (or hit Enter to skip): ')):
                continue

        p_path = os.path.join(os.curdir, project)
        print('-' * 30 + '\nAnalyzing', p_path)
        words.extend(stat.get_top_verbs_in_path(p_path))

    print('=' * 30 + '\nTotal %s words, %s unique' % (len(words), len(set(words))))
    for word, occurrence in Counter(words).most_common(top_size):
        print(word, occurrence)
