import os
import argparse
from .ExampleApp import ExampleLoader
import pyqtgraph as pg


def main():
    parser = argparse.ArgumentParser(description="ExApp CLI interface")
    parser.add_argument("dir_path", help="directory path contains .py example files",
                        nargs='?', default=os.getcwd())
    args = parser.parse_args()
    dir_path = args.dir_path

    if dir_path is None or not os.path.isdir(dir_path):
        dir_path = os.getcwd()

    pg.mkQApp()
    loader = ExampleLoader(dir_path)
    loader.ui.exampleTree.setCurrentIndex(
        loader.ui.exampleTree.model().index(0, 0)
    )
    pg.exec()
