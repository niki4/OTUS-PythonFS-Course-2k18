import ast
import os
import collections

import nltk
nltk.download('averaged_perceptron_tagger')


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = nltk.pos_tag([word])
    print('pos_info', pos_info)
    return pos_info[0][1] == 'VB'


def get_files(path):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for file in filenames:
            if file.endswith('.py'):
                py_files.append(os.path.join(dirpath, file))
                if len(py_files) == 100:
                    break
    print('total %s files' % len(py_files))
    return py_files


def get_trees(path, with_filenames=False, with_file_content=False):
    trees = []
    py_files = get_files(path)
    for filename in py_files:
        with open(filename, encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print('trees generated')
    return trees


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]
    function_names = [f for f in flat([get_all_names(t) for t in trees])
                      if not (f.startswith('__') and f.endswith('__'))]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    return flat([split_snake_case_name_to_words(function_name)
                 for function_name in function_names])


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    functions = [f for f in flat([[node.name.lower() for node in ast.walk(t) if isinstance(
        node, ast.FunctionDef)] for t in trees]) if not (f.startswith('__') and f.endswith('__'))]
    print('functions extracted', list(functions))
    verbs = flat([get_verbs_from_function_name(function_name)
                  for function_name in functions])
    print('verbs extracted', list(verbs))
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    t = get_trees(path)
    nms = [f for f in flat([[node.name.lower() for node in ast.walk(t)
                             if isinstance(node, ast.FunctionDef)] for t in t])
           if not (f.startswith('__') and f.endswith('__'))]
    return collections.Counter(nms).most_common(top_size)


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
