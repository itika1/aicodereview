# AI Code Review Assistant (LangChain + OpenAI API)

This project is an **AI code review assistant** that reviews git diffs and outputs structured markdown feedback.

## What it does

- Reads a git diff from `stdin` or a diff file
- Uses LangChain + OpenAI chat model for review
- Produces consistent sections:
  - High-level summary
  - Bugs/logic risks
  - Security concerns
  - Performance concerns
  - Maintainability suggestions
  - Next actions

## Install

### Option A: local editable install (recommended)

```bash
pip install -e .
```

### Option B: dependencies only

```bash
pip install -r requirements.txt
```

## CLI usage

Set API key first:

```bash
export OPENAI_API_KEY="your_api_key"
```

Review staged changes:

```bash
git diff --staged | ai-code-review
```

Review a diff file:

```bash
ai-code-review --diff-file sample.diff
```

Use another model:

```bash
ai-code-review --model gpt-4o
```

## Use as a Python package in another repository

Yes. You can import and use it directly.

### 1) Install from this repo path

```bash
pip install "git+https://<your-git-host>/<org>/aicodereview.git"
```

_or for local path during development:_

```bash
pip install -e /path/to/aicodereview
```

### 2) Call from Python

```python
from ai_code_reviewer import review_diff

diff_text = """diff --git a/app.py b/app.py
+print('hello')
"""

report = review_diff(diff_text, model="gpt-4o-mini")
print(report)
```

## Developer notes

Main package files:
- `ai_code_reviewer/cli.py`
- `ai_code_reviewer/reviewer.py`
- `ai_code_reviewer/prompts.py`
