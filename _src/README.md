Sources for the four variant mockups. Output files in `variants/` are generated and self-contained.
Rebuild all: `cd variants/_src && for f in bp hx md xe; do python3 ${f}2.py; done`
`data.js, core.js, s1-s3.js, engine.css` are the shared engine; `*2.py` are the per-variant skins and home layouts.
