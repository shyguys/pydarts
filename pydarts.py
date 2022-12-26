import sys

from app import PyDartsApp
from window import PyDartsWindow

def main():
    app = PyDartsApp(sys.argv)
    window = PyDartsWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
