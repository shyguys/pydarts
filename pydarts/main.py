import sys

from PySide6.QtCore import QCommandLineOption, QCommandLineParser
from PySide6.QtWidgets import QApplication

import pydarts
from pydarts.widgets.main_window import MainWindow


def parse(app) -> None:
    parser = QCommandLineParser()
    parser.addHelpOption()
    version_option = QCommandLineOption(
        ["v", "version"],
        "Show version and exit.",
    )
    parser.addOption(version_option)
    debug_option = QCommandLineOption(
        ["d", "debug"],
        "Write debug messages to stdout.",
    )
    parser.addOption(debug_option)
    parser.process(app)
    pydarts.configure_logging(parser.isSet(debug_option))
    if parser.isSet(version_option):
        print(pydarts.__version__)
        sys.exit()
    return None


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("pydarts")
    app.setApplicationDisplayName("PyDarts")
    app.setApplicationVersion(pydarts.__version__)
    parse(app)
    window = MainWindow()
    window.show()
    app.exec()
    return None
