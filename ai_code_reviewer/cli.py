"""CLI for AI code review assistant."""

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

from .config import require_openai_api_key
from .reviewer import review_diff


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI code review assistant")
    parser.add_argument(
        "--diff-file",
        type=Path,
        default=None,
        help="Path to a git diff file. If omitted, read diff from stdin.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model name (default: gpt-4o-mini).",
    )
    return parser.parse_args()


def read_diff(diff_file: Path | None) -> str:
    if diff_file:
        return diff_file.read_text(encoding="utf-8")
    return sys.stdin.read()


def main() -> None:
    load_dotenv()
    args = parse_args()
    require_openai_api_key()

    diff_text = read_diff(args.diff_file)
    if not diff_text.strip():
        raise SystemExit("No diff provided. Pipe git diff or use --diff-file.")

    review_markdown = review_diff(diff_text=diff_text, model=args.model)
    print(review_markdown)


if __name__ == "__main__":
    main()
