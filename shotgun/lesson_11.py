# coding:utf-8
import sys
import logging
import argparse
import os
from datetime import datetime

_DESCRIPTION = "This scripts runs various tests to demostrate efficient use of the Shotgun Python API."

def _run(args):
    """
    A boilerplate function to add code to.

    :param dict args: Arguments that control script behavior
    """
    logging.info("Running.")

def _set_up_parser():
    """
    :return: dict of args
    """
    # Initialize a command-line argument parser
    parser = argparse.ArgumentParser(
        description=_DESCRIPTION,
    )

    # add an argument to the parser.
    parser.add_argument(
        "-r",
        "--run",
        help="Run this script.",
        action="store_true",
        required=False,
    )
    # Split out script usage if no argument are passed
    if len(sys.argv)<2:
        logging.info("Usage: %s --help" % __file__)
        sys.exit()

    # Resolve parser arguments
    # vars() 函数返回对象object的属性和属性值的字典对象
    return vars(parser.parse_args())


def _set_up_logging():
    """
    Create logs directory and sets up logging-related stuffs.

    """
    # Create a logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Create a datestamp var for stamping the logs
    datestamp = datetime.now().strftime("%Y_%m_%d_%H-%M-%S")

    log = os.path.join(
        "logs","%s_%s.log" % (
            list(os.path.splitext(__file__))[0],
            datestamp,
        )
    )

    # set the logging level
    logging_level = logging.DEBUG

    # set up our logging
    logging.basicConfig(
        filename=log,
        level=logging_level,
        format="%(levelname)s: %(asctime)s: %(message)s",
    )

    logging.getLogger().addHandler(logging.StreamHandler())

if __name__ == "__main__":

    # Initialize our logger and create related floder/files.
    _set_up_logging()

    # Parser our user input and toss it in a dict.
    args = _set_up_parser()

    start = datetime.now()
    _run(args)
    logging.info(
        "_run function took %s to complate." % str(datetime.now()-start)
    )
