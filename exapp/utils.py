import os
from collections import OrderedDict


def list_py_files(dir_path) -> OrderedDict:
    """
    주어진 디렉토리 구조를 OrderedDict로 나타내며, 각 항목은 (basename, 절대경로) 형태의 튜플로 표현됩니다.

    :param dir_path: 탐색할 디렉토리 경로
    :return: 디렉토리 구조를 나타내는 OrderedDict
    """
    directory_structure = OrderedDict()

    for item in sorted(os.listdir(dir_path)):
        full_path = os.path.abspath(os.path.join(dir_path, item))
        if os.path.isdir(full_path) and not item.startswith("__"):
            dir_files_dict = list_py_files(full_path)
            if len(dir_files_dict) > 0:
                directory_structure[item] = list_py_files(full_path)
        elif item.endswith('.py') and not item.startswith("__"):
            directory_structure[item.replace(".py", "")] = full_path

    return directory_structure
