import argparse
import logging

import modules.app


def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s - %(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

def parse_args() -> argparse.Namespace:
    prog = "pydarts"
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False,
        dest="enable_debugging", help="highlight widgets and be verbose"
    )
    return parser.parse_args()

def main():
    configure_logging()
    args = parse_args()
    app = modules.app.App(enable_debugging=args.enable_debugging)
    app.mainloop()
