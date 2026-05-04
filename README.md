# AI Code Review Assistant (LangChain + OpenAPI)

This project is a starter implementation of an **AI code review assistant** built with:

- **LangChain** for orchestration
- **OpenAI API** ("OpenAPI" likely intended as OpenAI API)
- **Git diff ingestion** to review changed files

## Features

- Reads a git diff from stdin or a file
- Uses a structured review prompt to produce:
  - Summary of changes
  - Potential bugs / risks
  - Security concerns
  - Performance concerns
  - Actionable suggestions
- Outputs markdown for easy posting to PR comments

## Quickstart

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key:

```bash
export OPENAI_API_KEY="your_api_key"
```

4. Run against current staged diff:

```bash
git diff --staged | python -m src.main
```

5. Or review a diff file:

```bash
python -m src.main --diff-file sample.diff
```

## Project Structure

- `src/main.py` - CLI entrypoint
- `src/reviewer.py` - LangChain review chain
- `src/prompts.py` - Prompt template

## Notes

- This is intentionally simple and can be extended with:
  - Repository-aware context retrieval
  - Severity scoring
  - Auto-fix suggestions
  - PR platform integration (GitHub/GitLab)
