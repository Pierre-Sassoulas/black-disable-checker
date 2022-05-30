"""Check that black is applied everywhere. Used by pre-commit."""

import argparse
import sys
from typing import List, Union

DISABLES_PRAGMAS = {"# fmt: skip", "# yapf: disable", "# fmt: off"}


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
    offending_pragmas = []
    for file_name in args.filenames:
        try:
            with open(file_name, encoding="utf8") as f:
                content = f.read()
            for pragma in DISABLES_PRAGMAS:
                if pragma in content:
                    offending_pragmas.append(pragma)
                    offending_files.append(file_name)
        except UnicodeDecodeError:
            pass
    if offending_files:
        pragmas = "', or '".join(sorted(offending_pragmas))
        print(
            f"Please do not use '{pragmas}' in '{', '.join(offending_files)}',"
            " apply black everywhere.",
            file=sys.stderr,
        )
        sys.exit(-1)
    sys.exit(0)


if __name__ == "__main__":
    main()
