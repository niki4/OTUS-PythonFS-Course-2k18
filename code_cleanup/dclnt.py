import ast
import os
import collections

from code_cleanup.dclnt_tree import Tree

import nltk
nltk.download('averaged_perceptron_tagger')


tree_inst = Tree()


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def is_verb(word):
    if not word:
        return False
    pos_info = nltk.pos_tag([word])
    return pos_info[0][1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def get_all_words_in_path(path):
    trees = [t for t in tree_inst.get_trees(path) if t]
    function_names = [f for f in flat([get_all_names(t) for t in trees])
                      if not (f.startswith('__') and f.endswith('__'))]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    return flat([split_snake_case_name_to_words(function_name)
                 for function_name in function_names])


def get_top_verbs_in_path(path, words_count=10):
    trees = [t for t in tree_inst.get_trees(path) if t]
    functions = [f for f in flat([[node.name.lower() for node in ast.walk(t) if isinstance(
        node, ast.FunctionDef)] for t in trees]) if not (f.startswith('__') and f.endswith('__'))]
    print('functions extracted', len(functions))
    verbs = flat([get_verbs_from_function_name(function_name)
                  for function_name in functions])
    print('verbs extracted', len(verbs))
    return collections.Counter(verbs).most_common(words_count)


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_top_functions_names_in_path(path, words_count=10):
    trees = tree_inst.get_trees(path)
    nms = [f for f in flat([[node.name.lower() for node in ast.walk(t)
                             if isinstance(node, ast.FunctionDef)] for t in trees])
           if not (f.startswith('__') and f.endswith('__'))]
    return collections.Counter(nms).most_common(words_count)


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
    words += get_top_verbs_in_path(p_path)

top_size = 200

print('total %s words, %s unique' % (len(words), len(set(words))))
for word, occurrence in collections.Counter(words).most_common(top_size):
    print(word, occurrence)
