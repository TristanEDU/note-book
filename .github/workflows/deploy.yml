name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - main  # or your default branch

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material mkdocs-gen-nav-plugin

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install mkdocs mkdocs-material mkdocs-gen-nav-plugin pyyaml==6.0.2 cython
