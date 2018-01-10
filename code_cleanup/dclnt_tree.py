import ast
import os


class Tree:

    @staticmethod
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

    @classmethod
    def get_trees(cls, path, with_filenames=False, with_file_content=False):
        trees = []
        py_files = cls.get_files(path)
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
        print('trees generated', len(trees))
        return trees
