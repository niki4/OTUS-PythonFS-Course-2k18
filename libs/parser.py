import ast
import os


def get_files(path):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for file in filenames:
            if file.endswith('.py'):
                py_files.append(os.path.join(dirpath, file))
    print('%s files in total' % len(py_files))
    return py_files


def get_trees(path):
    trees = []
    py_files = get_files(path)
    for filename in py_files:
        with open(filename, encoding='utf-8') as file:
            tree = ast.parse(file.read())
            trees.append(tree)
    return trees
