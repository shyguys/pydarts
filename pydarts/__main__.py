import sys

import pydarts.app


def main():
    app = pydarts.app.PyDarts(sys.argv[1:])
    app.run()


if __name__ == "__main__":
    main()
