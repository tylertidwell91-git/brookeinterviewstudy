"""
Parse questions-only markdown: ## Section headers and - bullet lines.
No answers or options; output shape matches STUDYXL (options=[], answer="", explanation="").
"""
import re
from pathlib import Path

MARKDOWN_PATH = (Path(__file__).resolve().parent / "questions.md").resolve()


def parse_markdown_questions(text: str):
    """Parse ## section headers and '-' bullet lines into question records."""
    lines = text.splitlines()
    questions = []
    current_chapter = ""
    question_num = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Section header: ## Category Name
        if re.match(r"^##\s+.+", stripped):
            # Trim "## " and use as chapter
            current_chapter = re.sub(r"^##\s+", "", stripped).strip()
            continue
        # Question: - Question text (must be under a section)
        if stripped.startswith("- ") and current_chapter:
            prompt = stripped[2:].strip()
            if not prompt:
                continue
            question_num += 1
            questions.append(
                {
                    "chapter": current_chapter,
                    "number": question_num,
                    "prompt": prompt,
                    "options": [],
                    "answer": "",
                    "explanation": "",
                }
            )
    return questions
