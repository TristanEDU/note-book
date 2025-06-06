---
name: github pages

on:
  push:
    branches:
      - main
  schedule:
    - cron: 11 06 * * *

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          # Number of commits to fetch. 0 indicates all history.
          # Default: 1
          fetch-depth: 0
      - uses: pdm-project/setup-pdm@main
        name: Setup Python and PDM
        with:
          python-version: 3.9

      - name: Install build tools for Python packages
        run: pip install --upgrade pip setuptools wheel cython
        
      - name: Install dependencies
        run: make install

      - name: Update requirements
        run: make update

      - name: Run the formatters
        run: make format

      - name: Make the newsletters
        run: make build-newsletters

      - name: Commit files
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add pdm.lock
          git add .
          git diff-index --quiet HEAD \
            || git commit -m "chore: update dependency, publish newsletters and add the not by ai badge"

      - name: Make the site
        run: make build-docs

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          deploy_key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
          publish_dir: ./site
