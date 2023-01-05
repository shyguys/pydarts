import argparse

from modules.app import App


def parse_args() -> argparse.Namespace:
    prog = "pydarts"
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False,
        dest="enable_debugging", help="highlight widgets and be verbose"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    app = App(enable_debugging=args.enable_debugging)
    app.mainloop()
    