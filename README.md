# Army National Guard Recruiter — Interview Questions

A simple study app to flip through Army National Guard recruiter interview questions. No answers are provided; use it to practice answering out loud.

## Setup

1. **Install:** No dependencies. Python 3 is used only to build the question list from markdown.

2. **Build:** After editing `questions.md`, run:
   ```bash
   python3 build_html.py
   ```
   This parses `questions.md` and injects the questions into `index.html`.

3. **Use:** Open `index.html` in a browser (or host on GitHub Pages). Use **Next Question** to move through cards, **Show Answer** as a reminder that there’s no answer key (practice out loud), and **Mark Needs Review** to flag questions. Filter by category in the deck select (Ctrl/Cmd+click for multiple).

## Files

- `questions.md` — Source questions (## sections = categories, - bullets = questions).
- `parse_questions.py` — Parser for the questions-only markdown format.
- `build_html.py` — Injects parsed questions into `index.html`.
- `index.html` — Single-page app (study mode only; no test mode).

## Moving to your repo

The project is in `army-guard-recruiter-questions/` inside this workspace. Copy the contents of that folder into your new GitHub repo (or clone the repo and copy these files in), then run `python3 build_html.py` if you change `questions.md`. Enable GitHub Pages on the repo and set the source to the branch that contains `index.html` (and optionally set the root to `/` or `/docs` depending on where `index.html` lives).
