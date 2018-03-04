import ast
import collections

from libs import parser

import nltk
nltk.download('averaged_perceptron_tagger')


def extract_literals(raw_words):
    extracted_literals = [word for sublist in raw_words for word in sublist]
    return extracted_literals


def get_top_verbs_in_path(path, words_count=10):
    trees = parser.get_trees(path)
    functions = [f for f in extract_literals([[node.name.lower() for node in ast.walk(t)
                                               if isinstance(node, ast.FunctionDef)] for t in trees])
                 if not (f.startswith('__') and f.endswith('__'))]
    verbs = extract_literals([get_verbs_from_function_name(function_name)
                              for function_name in functions])
    print('%s verbs extracted' % len(verbs))
    return collections.Counter(verbs).most_common(words_count)


def get_top_functions_names_in_path(path, words_count=10):
    trees = parser.get_trees(path)
    nms = [f for f in extract_literals([[node.name.lower() for node in ast.walk(t)
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
