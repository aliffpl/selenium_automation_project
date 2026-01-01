# Git Cleanup Instructions

Follow these steps to remove sensitive data and local artifacts from your Git history before pushing to GitHub.

1) Remove files/directories from the current working tree and stop tracking them:

   git rm -r --cached .venv
   git rm -r --cached .pytest_cache
   git rm -r --cached *.log
   git commit -m "chore: remove local artifacts from repo"

2) Add or update `.gitignore` (ensure these entries exist):

   .venv/
   .pytest_cache/
   __pycache__/
   *.log
   reports/

3) Rewrite Git history to purge sensitive files (choose one):

- Using `git filter-repo` (recommended):

  # Install: pip install git-filter-repo
  git filter-repo --invert-paths --paths .venv --paths .pytest_cache --paths path/to/file_with_sensitive_data

- Using BFG Repo Cleaner:

  # Download BFG jar and run:
  java -jar bfg.jar --delete-folders .venv --delete-folders .pytest_cache --delete-files "*private*" --replace-text replacements.txt
  git reflog expire --expire=now --all && git gc --prune=now --aggressive

4) Force-push cleaned history to remote (BE CAREFUL):

   git push --force --all
   git push --force --tags

5) After push, ask collaborators to re-clone the repo (their local history will be incompatible).

Notes:
- Rewriting history is destructive. Back up your repo first.
- `git filter-repo` is faster and safer than BFG for complex filters.
