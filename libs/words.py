import ast

from libs import parser
from libs import stat


def get_all_names(tree):
    return [node.id for node in ast.walk(tree)
            if isinstance(node, ast.Name)]


def get_all_words_in_path(path):
    trees = parser.get_trees(path)
    literals = stat.extract_literals([get_all_names(t) for t in trees])
    function_names = [f for f in literals
                      if not (f.startswith('__')
                              and f.endswith('__'))]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    return stat.extract_literals([split_snake_case_name_to_words(function_name)
                                  for function_name in function_names])
