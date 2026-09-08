# jessica-yang-site

Personal site for Jessica L. Yang — University of Florida statistics undergraduate,
long/short equity research and quantitative alternative-data work.

**Live:** published as a Claude Artifact at
<https://claude.ai/code/artifact/ff90f50e-91f8-4bdc-a205-5a1299ec21bb>

## What's here

`index.html` is the entire site — a single self-contained file. Every asset is inlined
as a data URI: the headshot, the six rendered pitch write-ups, and the six source PDFs
that the download buttons hand to the reader. There is no build step and no external
asset host. The only network request the page makes is to Google Fonts.

Open it directly in a browser, or serve the directory:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

## Structure

Five tabs, driven by a small vanilla-JS tablist (arrow-key navigable, last tab
remembered in `localStorage`):

| Tab | Contents |
|---|---|
| Stock pitches | Six long/short theses with targets, horizons, evidence, and the full write-up |
| Quant research | Fama-French 5 + hiring-momentum factor study, open-source repos, ABNB work in progress |
| Writing | Enterprise business and tech reporting for *The Independent Florida Alligator* |
| Experience | Investment banking, real estate, newsroom, student fund |
| Education & toolkit | Degree, methods, certifications, memberships |

## Document viewer

Each pitch card carries a rendered page image of its write-up. Clicking it opens a
full-screen reader with a fit/zoom toggle. The **Download PDF** control uses the Claude
Artifact `downloads` capability, so it appears only when the viewer's session grants it
and always asks the viewer to confirm the save. Outside that runtime the button stays
hidden and the rest of the page works unchanged.

## Theming

Light and dark are both designed, driven entirely by CSS custom properties. The palette
is defined on bare `:root`, then redefined under `prefers-color-scheme: dark` (guarded so
an explicit light choice wins) and again under `[data-theme="dark"]`.

## Updating the articles

The *Writing* tab is static. New bylines are added by re-reading
<https://www.alligator.org/staff/jessica-yang> and editing the `.stories` block in
`index.html`, then republishing.
