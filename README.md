# [Note Book](https://tristanedu.github.io/note-book/)

This repository contains my personal wiki built with [MkDocs](https://www.mkdocs.org/) and hosted on [GitHub](https://github.com/TristanEDU/note-book).

**The docs are best read [online](https://tristanedu.github.io/note-book/).**

## Building the documentation

Install the dependencies and start the development server:

```bash
pdm install  # or `pip install -r requirements.txt`
pdm run mkdocs serve
```

Visit <http://127.0.0.1:8000/> to preview the site locally. To generate the static site run:

```bash
pdm run mkdocs build
```

## Creating Notes

Reusable note templates live in the `templates/` directory. They contain
placeholders like `{{date}}`, `{{job}}` and `{{client}}` which you can replace
after copying a file.

- `templates/daily.md` – daily log template.
- `templates/job/README.md` – job overview page.
- `templates/job/client-profile.md` – client details sheet.
- `templates/job/meeting-notes.md` – meeting agenda and notes.
- `templates/job/project-plan.md` – track tasks and milestones.
- `templates/job/proposal-draft.md` – draft proposals or quotes.

To create a new daily entry you might run:

```bash
cp templates/daily.md docs/Timeline/$(date +%Y-%m-%d).md
```

## Contributing

Found a mistake or want to add new content? Feel free to open a pull request or [file an issue](https://github.com/TristanEDU/note-book/issues/new).

## Thank you

If you enjoy this project you can also check out my [other projects](https://github.com/TristanEDU).

[![CC0](https://img.shields.io/badge/license-CC0-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://creativecommons.org/publicdomain/zero/1.0/)
