import ast

from libs.parser import Tree


class Word:

    @staticmethod
    def flat(_list):
        """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
        return sum([list(item) for item in _list], [])

    def get_all_names(self, tree):
        return [node.id for node in ast.walk(tree)
                if isinstance(node, ast.Name)]

    def get_all_words_in_path(self, path):
        trees = [t for t in Tree.get_trees(path) if t]
        function_names = [f for f in self.flat(
            [self.get_all_names(t) for t in trees])
                          if not (f.startswith('__') and f.endswith('__'))]

        def split_snake_case_name_to_words(name):
            return [n for n in name.split('_') if n]
        return self.flat([split_snake_case_name_to_words(function_name)
                          for function_name in function_names])
