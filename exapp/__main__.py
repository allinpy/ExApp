import argparse

if __name__ == '__main__':
    from .ExampleApp import main as run

    parser = argparse.ArgumentParser(description="ExApp CLI interface")
    parser.add_argument("dir_path", help="directory path contains .py example files")
    args = parser.parse_args()
    run(args.dir_path)
