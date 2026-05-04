"""Runtime configuration helpers."""

import os


def require_openai_api_key() -> str:
    """Return OPENAI_API_KEY or raise a clear error message."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            "OPENAI_API_KEY is not set. Export it before running the reviewer."
        )
    return api_key
