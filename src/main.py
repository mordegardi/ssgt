import sys

from copy_static_files import copy_static
from generate_page import generate_pages_recursive


def main():
    args = sys.argv

    basepath = "/"

    if len(args) > 2:
        basepath = args[1]

    copy_static("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)


main()
