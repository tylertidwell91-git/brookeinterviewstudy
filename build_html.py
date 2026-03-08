"""
Build index.html: read questions.md, parse, inject JSON into index.html.
"""
import json
from pathlib import Path

from parse_questions import MARKDOWN_PATH, parse_markdown_questions

HTML_PATH = (Path(__file__).resolve().parent / "index.html").resolve()


def main():
    if not MARKDOWN_PATH.exists():
        raise SystemExit(f"Markdown file not found: {MARKDOWN_PATH}")

    text = MARKDOWN_PATH.read_text(encoding="utf-8")
    questions_data = parse_markdown_questions(text)
    if not questions_data:
        raise SystemExit("No questions parsed from markdown file.")

    if not HTML_PATH.exists():
        raise SystemExit(f"HTML file not found: {HTML_PATH}")

    html = HTML_PATH.read_text(encoding="utf-8")
    marker = "const questions ="
    start = html.find(marker)
    if start == -1:
        raise SystemExit("Could not find 'const questions =' in HTML file.")
    end = html.find("];", start)
    if end == -1:
        raise SystemExit("Could not find end of questions array (' ];') in HTML file.")
    end += 2

    new_array = "const questions = " + json.dumps(questions_data, indent=2, ensure_ascii=False) + ";"
    updated = html[:start] + new_array + html[end:]
    HTML_PATH.write_text(updated, encoding="utf-8")
    print(f"Updated {HTML_PATH.name} with {len(questions_data)} questions from {MARKDOWN_PATH.name}.")


if __name__ == "__main__":
    main()
