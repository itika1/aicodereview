"""LangChain-powered code review chain."""

from langchain_openai import ChatOpenAI

from .prompts import REVIEW_PROMPT


def build_reviewer(model: str = "gpt-4o-mini", temperature: float = 0.1):
    """Build the review chain.

    Args:
        model: OpenAI chat model name.
        temperature: Sampling temperature.

    Returns:
        Runnable chain that accepts {"diff_text": str}.
    """
    llm = ChatOpenAI(model=model, temperature=temperature)
    return REVIEW_PROMPT | llm


def review_diff(diff_text: str, model: str = "gpt-4o-mini") -> str:
    """Run AI review for a git diff and return markdown output."""
    chain = build_reviewer(model=model)
    response = chain.invoke({"diff_text": diff_text})
    return response.content
