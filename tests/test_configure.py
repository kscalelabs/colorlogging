"""Runs a simple test to ensure that logging configuration works."""

import logging

import colorlogging


def test_configure() -> None:
    colorlogging.configure()

    logger = logging.getLogger("dummy")
    logger.info("Hello, World!")


if __name__ == "__main__":
    # python -m tests.test_configure
    test_configure()
