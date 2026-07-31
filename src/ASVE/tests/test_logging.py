"""
Tests for ASVE logging utilities.

These tests validate runtime observability behavior.
"""

from __future__ import annotations

import logging

from asve.utils.logging import get_logger, configure_logging


def test_logger_creation() -> None:
    """
    Logger factory should return a logger.
    """
    logger = get_logger(
        "asve.test",
    )

    assert isinstance(
        logger,
        logging.Logger,
    )


def test_logger_name_is_preserved() -> None:
    """
    Logger should retain requested name.
    """
    logger = get_logger(
        "asve.pipeline",
    )

    assert (
        logger.name
        == "asve.pipeline"
    )


def test_logging_configuration() -> None:
    """
    Logging configuration should execute.
    """
    result = configure_logging()

    assert result is None


def test_logger_emits_messages(
    caplog,
) -> None:
    """
    Logger should emit records.
    """
    logger = get_logger(
        "asve.test",
    )

    with caplog.at_level(
        logging.INFO,
    ):
        logger.info(
            "verification started",
        )

    assert (
        "verification started"
        in caplog.text
    )


def test_logger_supports_errors(
    caplog,
) -> None:
    """
    Logger should capture error events.
    """
    logger = get_logger(
        "asve.test",
    )

    with caplog.at_level(
        logging.ERROR,
    ):
        logger.error(
            "verification failed",
        )

    assert (
        "verification failed"
        in caplog.text
    )
