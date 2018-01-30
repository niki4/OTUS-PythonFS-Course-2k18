import ast
import collections

from libs import parser

import nltk
nltk.download('averaged_perceptron_tagger')


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_top_verbs_in_path(path, words_count=10):
    trees = [t for t in parser.get_trees(path) if t]
    functions = [f for f in flat(
        [[node.name.lower() for node in ast.walk(t)
          if isinstance(node, ast.FunctionDef)] for t in trees])
                 if not (f.startswith('__') and f.endswith('__'))]
    print('%s functions extracted' % len(functions))
    verbs = flat(
        [get_verbs_from_function_name(function_name)
         for function_name in functions])
    print('%s verbs extracted' % len(verbs))
    return collections.Counter(verbs).most_common(words_count)


def get_top_functions_names_in_path(path, words_count=10):
    trees = parser.get_trees(path)
    nms = [f for f in flat(
        [[node.name.lower() for node in ast.walk(t)
          if isinstance(node, ast.FunctionDef)] for t in trees])
           if not (f.startswith('__') and f.endswith('__'))]
    return collections.Counter(nms).most_common(words_count)


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_')
            if is_verb(word)]


def is_verb(word):
    if not word:
        return False
    pos_info = nltk.pos_tag([word])
    return pos_info[0][1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
