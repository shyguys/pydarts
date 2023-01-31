import argparse
import logging

from pydarts.gui import appwindow

class PyDarts():
    def __init__(self):
        self.args = self._parse_args()
        self.app = appwindow.AppWindow("PyDarts")

    def run(self):
        self.app.run(self.args.debug)

    def _parse_args(self) -> argparse.Namespace:
        prog = "pydarts"
        parser = argparse.ArgumentParser(prog=prog)

        parser.add_argument(
            "-d", "--debug", action="store_true", default=False,
            dest="debug", help="highlight widgets and be verbose"
        )

        return parser.parse_args()

    def _configure_logging(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s - %(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )
