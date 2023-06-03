import argparse
import logging

import pydarts.gui.app

PROG = "pydarts"
PRETTY_PROG = "PyDarts"


class PyDarts():
    def __init__(self):
        self.args = self._parse_args()
        self._configure_logging()
        self.app = pydarts.gui.app.Root(PRETTY_PROG)

    def run(self):
        self.app.mainloop(self.args.debug)

    def _parse_args(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(prog=PROG)
        parser.add_argument(
            "-d", "--debug",
            dest="debug",
            help="highlight widgets and print debugging information",
            action="store_true"
        )
        return parser.parse_args()

    def _configure_logging(self):
        level = logging.DEBUG if self.args.debug else logging.INFO
        logging.basicConfig(
            level=level,
            format="[%(asctime)s - %(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )
