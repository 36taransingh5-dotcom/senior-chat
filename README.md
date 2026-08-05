# senior.chat — waitlist

Waitlist landing page for senior.chat: verified 1:1 conversations with current
students abroad, for Indian students evaluating study-abroad options.

Live: https://senior-chat-waitlist.vercel.app

## Structure

- `index.html` — the built, deployable page (fonts embedded as base64 data URIs,
  no build step needed to serve it as-is).
- `src/template.html` — the source template, with `{{MANROPE}}` / `{{JBM}}`
  placeholders instead of inlined font data.
- `fonts/` — the two embedded font files (Manrope variable, JetBrains Mono).
- `src/build.py` — regenerates `index.html` from `src/template.html` + `fonts/`.

## Editing

Edit `src/template.html`, then rebuild:

```bash
python3 src/build.py
```

This overwrites `index.html` with the placeholders replaced by the current font
files. Commit both the template and the rebuilt `index.html`.

## Deploying

Static site, no build step required by the host.

```bash
npx vercel deploy --prod
```
