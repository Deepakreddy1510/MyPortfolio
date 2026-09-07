# P Deepak portfolio

A dependency-free static portfolio with shared page generation, local fonts, a compact project selector, two project details pages, and light/dark theme preferences.

## Editing

- Edit content and shared HTML in `generate.py`, then run `python generate.py`.
- Styles live in `dist/styles.css` and `dist/reference.css`; interaction behavior is in `dist/site.js`.
- Replace `dist/assets/profile.png` to update the avatar.
- When the actual resume is supplied, save it as `dist/assets/resume.pdf` and set `RESUME_URL` to `/assets/resume.pdf` in `dist/site.js`. The placeholder is honest and does not link to a missing file.
- GitHub contributions load from https://github-contributions-api.jogruber.de/v4/Deepakreddy1510?y=last on page load, every five minutes while visible, and when returning after five minutes. This public API scrapes GitHub and caches data for up to one hour. Failures are labeled honestly and retried; no bundled snapshot is used. Counts and calendar dates come from the same response.


Serve the contents of `dist` from the root of a static web host. No runtime server, API key, or JavaScript package installation is required. Pages and navigation render without JavaScript; theme preferences and activity visualization use JavaScript. Project write-ups reflect the supplied brief and the public repository READMEs, not an independent code audit.

## Sources

- Visual reference studied interactively: https://tabrez.ai.studio/ (layout, typography, theme toggle and project selector). No code, personal content, photographs, or proprietary assets copied.
- Public project descriptions: https://github.com/Deepakreddy1510/AI_Data_Agent and https://github.com/Deepakreddy1510/pdf-rag-assistant
- Fonts: Doto and Geist Mono from Google Fonts, licensed under the SIL Open Font License; licenses retained in `licenses/`.
- Profile illustration supplied by the user.

The homepage follows the supplied reference screenshots: a 720px desktop frame, a Social icon row, project dropdown and paging controls, moving technology strip with pause and reduced-motion support, and a GitHub calendar with three summary cells. About is part of section 01; Experience, Projects, Tools, GitHub, Education, and Connect are sections 02–07.

Technology and social icons use Simple Icons v13 (VS Code from v11) and Devicon v2.16.0 (Matplotlib); their license notices are retained beside the assets. LangGraph uses a generic graph symbol.
