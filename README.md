# jessica-yang-site

Personal site for Jessica L. Yang — University of Florida statistics undergraduate,
long/short equity research and quantitative alternative-data work.

## Deploying

`index.html` is a complete, self-contained HTML document. Every asset is inlined as a
data URI — the headshot, the six rendered pitch write-ups, and the six source PDFs the
download buttons hand to the reader. There is no build step and no external asset host.
The only network request the page makes is to Google Fonts.

**Netlify / Vercel / GitHub Pages:** deploy the repository root. Leave the build command
empty and set the publish directory to `.` — there is nothing to compile.

Locally, open `index.html` directly, or:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

## Also published as a Claude Artifact

<https://claude.ai/code/artifact/ff90f50e-91f8-4bdc-a205-5a1299ec21bb>

The Artifact host wraps whatever it is given in its own
`<!doctype html><head>…</head><body>` skeleton, so publishing `index.html` directly
would nest a second document inside the first. Strip it back to a fragment first:

```bash
python3 build_artifact.py     # -> dist/page.html
```

Then publish `dist/page.html`, passing the artifact's existing URL so it updates in
place instead of creating a second artifact. `dist/` is gitignored; `index.html` is the
single source of truth.

## Structure

Five tabs, driven by a small vanilla-JS tablist — arrow-key navigable, last tab
remembered in `localStorage`:

| Tab | Contents |
|---|---|
| Stock pitches | Six long/short theses with targets, horizons, evidence, and the full write-up |
| Quant research | Fama-French 5 + hiring-momentum factor study, open-source repos, ABNB work in progress |
| Writing | Enterprise business and tech reporting for *The Independent Florida Alligator* |
| Experience | Investment banking, real estate, newsroom, student fund |
| Education & toolkit | Degree, methods, certifications, memberships |

## Document viewer

Each pitch card carries a rendered page image of its write-up. Clicking it opens a
full-screen reader with a fit/zoom toggle.

**Download PDF** uses the Claude Artifact `downloads` capability. It appears only when
the viewer's session grants that capability and always asks the viewer to confirm the
save. On Netlify or any ordinary host `window.claude` does not exist, so the buttons
stay hidden and everything else works unchanged — the page previews still open and read
full screen.

Note that anything toggled with the `hidden` attribute must not be given a `display`
value by a class rule, or `hidden` silently loses the cascade. `.lightbox` sets
`display:flex`, so it carries an explicit `.lightbox[hidden]{display:none!important}`
companion rather than depending on a host reset.

## Theming

Light and dark are both designed, driven entirely by CSS custom properties. The palette
is defined on bare `:root`, then redefined under `prefers-color-scheme: dark` (guarded so
an explicit light choice wins) and again under `[data-theme="dark"]`.

## Updating the articles

The *Writing* tab is static. New bylines are added by re-reading
<https://www.alligator.org/staff/jessica-yang> and editing the `.stories` block in
`index.html`.
