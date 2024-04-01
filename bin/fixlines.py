# !/usr/bin/python

import os
import re
from pathlib import Path


def get_files():
    for root, _, files in os.walk("."):
        for name in files:
            yield os.path.join(root, name)


def fix_file(file):
    current_paragraph: str = ""
    front_matter = False
    fence = False

    with open(file) as f:
        for line in f:
            if line.startswith("```"):
                fence = not fence
                print(line, end="")
                continue
            if line.startswith("---"):
                front_matter = not front_matter
                print(line, end="")
                continue
            if front_matter or fence:
                print(line, end="")
                continue

            line = line.strip()
            if not line and not current_paragraph:
                continue

            if line:
                current_paragraph += line
            elif current_paragraph:
                current_paragraph = re.sub(pattern, ".\n", current_paragraph)

                print(current_paragraph)
                print()
                current_paragraph = ""
        if current_paragraph:
            current_paragraph = re.sub(pattern, ".\n", current_paragraph)

            print(current_paragraph)
            print()


if __name__ == "__main__":
    p = Path(".")
    files = p.glob("**/*.md")

    fs = [f for f in files if "crushing" in f.as_posix()]
    print(fs)
    pattern = re.compile(r"\.[^\n]")

    # for file in files:
    #    fix_file(file)

    for f in fs:
        fix_file(f)
