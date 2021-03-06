"""Check that black is applied everywhere. Used by pre-commit."""

import argparse
import sys
from typing import List, Union


def main(argv: Union[List[str], None] = None) -> int:
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        metavar="FILES",
        help="File names to modify",
    )
    args = parser.parse_args(argv)
    offending_files = []
    for file_name in args.filenames:
        try:
            with open(file_name, encoding="utf8") as fp:
                if "# fmt: off" in fp.read():
                    offending_files.append(file_name)
        except UnicodeDecodeError:
            pass
    if offending_files:
        print(
            f"Please do not use '# fmt: off' in {', '.join(offending_files)}, apply black everywhere."
        )
        sys.exit(-1)
    sys.exit(0)


if __name__ == "__main__":
    main()
