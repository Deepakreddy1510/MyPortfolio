"""Build the static pages. Edit shared markup and portfolio content here."""
import shutil
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / 'dist'
PUBLIC = Path(__file__).parent / 'public'
EMAIL = 'deepakreddy1510@gmail.com'
GITHUB = 'https://github.com/Deepakreddy1510'
LINKEDIN = 'https://www.linkedin.com/in/deepak-reddy-53a1a82a6/'
LEETCODE = 'https://leetcode.com/u/Deepakreddy_2005/'

ROOT.mkdir(parents=True, exist_ok=True)
if PUBLIC.exists():
    shutil.copytree(PUBLIC, ROOT, dirs_exist_ok=True)
PROJECTS = [
    dict(number='01', title='AI Data Agent', slug='ai-data-agent', category='Agent workflows', repo=GITHUB+'/AI_Data_Agent', description='A natural-language interface to structured data, with a router coordinating specialized SQL and ETL workflows.'),
    dict(number='02', title='PDF RAG Assistant', slug='pdf-rag-assistant', category='Document retrieval', repo=GITHUB+'/pdf-rag-assistant', description='A multi-document retrieval system that turns PDF collections into grounded answers with traceable page-level evidence.'),
]

def heading(n, category, title):
    return f'<div class="section-heading"><span class="dot-mark" aria-hidden="true"></span><div><div class="eyebrow">SEC_{n} / {category}</div><h2>{title}</h2></div></div>'

def frame(content, title='P Deepak — Build. Integrate. Innovate.', description='P Deepak, an Electrical Engineering student at IIT Hyderabad. Selected work in software, AI systems, and data engineering.'):
    return f'''<!doctype html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="dark light"><title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:type" content="website"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/doto.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="/assets/geist-mono.ttf" as="font" type="font/ttf" crossorigin><script src="/theme.js"></script><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/reference.css"><script src="/site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="identity-link" href="/" aria-label="P Deepak home"><span class="red-mark" aria-hidden="true"></span><span>P DEEPAK / PORTFOLIO</span></a><div class="top-right"><span class="clock" data-clock></span><button class="theme-toggle" aria-label="Switch to light mode"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M20 15.5A8.5 8.5 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z"/></svg></button></div></header><div class="shell">{content}<footer class="footer"><span>© 2026 P Deepak</span><a href="/#connect">Build. Integrate. Innovate.</a></footer></div></body></html>'''

def icon(name):
    path = ROOT / 'assets' / 'icons' / (name + '.svg')
    if path.exists():
        import re
        svg = path.read_text()
        svg = re.sub(r'<title>.*?</title>', '', svg)
        return svg.replace('<svg ', '<svg aria-hidden="true" focusable="false" fill="currentColor" ', 1)
    # A simple graph symbol for LangGraph, rather than an invented brand asset.
    return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M7 6h10M6 8v8m12-8v8M8 18h8M8 8l8 8"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>'

EXTERNAL_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 4h6v6m0-6L10 14M10 5H5v14h14v-5"/></svg>'
MAIL_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="m3 6 9 7 9-7"/></svg>'
RESUME_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 3h8l4 4v14H6zM14 3v5h4M9 12h6m-6 4h6"/></svg>'
TECHNOLOGIES = [
    ('Languages', [('Python','python'),('C++','cplusplus')]),
    ('Backend', [('PostgreSQL','postgresql'),('FastAPI','fastapi')]),
    ('Tools', [('Git','git'),('Docker','docker'),('VS Code','vscode')]),
    ('AI frameworks', [('LangChain','langchain'),('LangGraph','langgraph')]),
    ('Data', [('NumPy','numpy'),('Pandas','pandas'),('Matplotlib','matplotlib')]),
]
def technology(label, asset):
    return f'<span class="technology">{icon(asset)}<span>{label}</span></span>'

social = ''.join(f'<a class="icon-box" href="{url}" aria-label="{label}" title="{label}">{icon(asset)}</a>' for label,asset,url in [('GitHub','github',GITHUB),('LinkedIn','linkedin',LINKEDIN),('LeetCode','leetcode',LEETCODE)])
project_tech = [['Python','LangChain','LangGraph','PostgreSQL','Pandas'],['Python','PostgreSQL','pgvector','Sentence Transformers','CrossEncoder']]
project_options = ''.join(f'''<button type="button" role="option" id="project-option-{i}" data-project-select="{i}" aria-selected="{'true' if i==0 else 'false'}" tabindex="{'0' if i==0 else '-1'}"><span class="option-number">PRJ_{p['number']}</span><span class="option-title">{p['title']}</span><span class="option-tags"><span>{project_tech[i][0]}</span><span>{project_tech[i][1]}</span></span></button>''' for i,p in enumerate(PROJECTS))
projects = ''.join(f'''<article class="project-panel" id="project-{p['number']}" role="tabpanel" aria-labelledby="project-tab-{i}" tabindex="0"><div class="project-toolbar"><span class="project-meta">PRJ_{p['number']}</span><div class="project-links"><a class="icon-box" href="{p['repo']}" aria-label="{p['title']} on GitHub" title="Source code">{icon('github')}</a><a class="icon-box" href="/{p['slug']}.html" aria-label="Explore {p['title']}" title="Explore project">{EXTERNAL_ICON}</a></div></div><h3 class="project-title"><a href="/{p['slug']}.html">{p['title']}</a></h3><p class="project-description">{p['description']}</p><div class="project-tags">{''.join('<span>'+t+'</span>' for t in project_tech[i])}</div></article>''' for i,p in enumerate(PROJECTS))
tabs = ''.join(f'<button id="project-tab-{i}" role="tab" type="button" aria-label="View project {i+1}: {p["title"]}" aria-controls="project-{p["number"]}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}" data-project-select="{i}"><span></span></button>' for i,p in enumerate(PROJECTS))
marquee_content = ''.join(technology(label, asset) for _,items in TECHNOLOGIES for label,asset in items)
skills = ''.join(f'<div><dt>{category}</dt><dd>'+''.join(technology(label,asset) for label,asset in items)+'</dd></div>' for category,items in TECHNOLOGIES)
connect = ''.join(f'<a class="connect-link" href="{url}"><span class="connect-name">{icon(asset)} {label}</span><span aria-hidden="true">↗</span></a>' for label,asset,url in [('GitHub','github',GITHUB),('LinkedIn','linkedin',LINKEDIN),('LeetCode','leetcode',LEETCODE)])
home=f'''<main id="main">
<section class="section hero" aria-labelledby="name"><div class="hero-id"><div class="portrait"><img src="/assets/profile.png" alt="P Deepak’s black-and-white illustrated avatar with round glasses" width="100" height="100" fetchpriority="high"></div><div><div class="eyebrow">SEC_01 / ID</div><h1 id="name">P Deepak</h1><p class="positioning">Build. Integrate. Innovate.</p></div></div><div class="hero-about" id="about" role="region" aria-label="About"><h2 class="about-label">About</h2><p class="intro">Building AI applications and data-driven systems by integrating AI with data using Python, LangChain, LangGraph, and PostgreSQL.</p></div><div class="hero-actions"><a class="outline-link" href="mailto:{EMAIL}">{MAIL_ICON} Contact</a><a class="outline-link" href="#resume-note" data-resume aria-controls="resume-note">{RESUME_ICON} Resume</a></div><div class="social-row"><span class="social-label">SOCIAL</span><div class="social-links">{social}</div></div><nav class="mini-nav" aria-label="Portfolio sections"><a href="#about">About</a><a href="#experience">Experience</a><a href="#work">Work</a><a href="#connect">Connect</a></nav></section>
<section class="section experience" id="experience">{heading('02','PRACTICE','Experience')}<div class="role-heading"><h3 class="compact-title">Data Engineering Intern</h3><span class="role-location">Remote</span></div><div class="role-meta"><span>Diagonal Matrix</span><span>UK startup</span></div><ul class="experience-details"><li>Developed a YAML-driven data-modeling accelerator to automate model generation, synthetic data creation, and PostgreSQL loading.</li><li>Connected the generated PostgreSQL data to existing JAI SQL Agent workflows for AI-assisted analysis.</li><li>Improved consistency, traceability, and validation across the data-modeling workflow.</li></ul></section>
<section class="section" id="work">{heading('03','WORK','PROJECTS')}<details class="project-picker"><summary><span class="picker-label">PROJECT</span><span class="picker-title" id="selected-project-title">AI Data Agent</span><span class="picker-count" id="selected-project-count">01/02</span><svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4 6 4 4 4-4" fill="none" stroke="currentColor"/></svg></summary><div class="project-options" role="listbox" aria-label="Choose a project">{project_options}</div></details><div class="project-panels">{projects}</div><div class="project-status"><span class="project-progress" aria-hidden="true"></span><span id="project-position" aria-live="polite">01 OF 02</span></div><div class="project-tabs" role="tablist" aria-label="Projects">{tabs}</div></section>
<section class="section" id="tools">{heading('04','TOOLS','TECH STACK')}<div class="tools-ticker"><div class="ticker-window" aria-hidden="true"><div class="ticker-track"><div class="ticker-group">{marquee_content}</div><div class="ticker-group">{marquee_content}</div></div></div><button class="ticker-toggle" type="button" aria-label="Pause moving tools" aria-pressed="false" title="Pause moving tools"><svg class="pause-icon" aria-hidden="true" viewBox="0 0 16 16" fill="currentColor"><path d="M4 3h2v10H4zm6 0h2v10h-2z"/></svg><svg class="play-icon" aria-hidden="true" viewBox="0 0 16 16" fill="currentColor"><path d="m5 3 8 5-8 5z"/></svg></button></div><dl class="skills">{skills}</dl></section>
<section class="section" id="activity">{heading('05','ACTIVITY','GITHUB')}<p class="activity-error" id="activity-loading" role="status">Loading public activity…</p><div id="activity-content" hidden><div class="activity-stats"><div><span class="stat-label">Contributions</span><strong id="activity-total"></strong></div><div><span class="stat-label">Best day</span><strong id="activity-best"></strong><small> contributions</small></div><div><span class="stat-label">Active days</span><strong id="activity-days"></strong><small> days</small></div></div><div class="calendar-frame"><div class="heatmap-scroll"><div class="calendar-inner"><div class="calendar-months" aria-hidden="true" id="calendar-months"></div><div class="heatmap" id="heatmap" role="img"></div></div></div><div class="calendar-legend" aria-hidden="true"><span>Less</span><i></i><i data-level="1"></i><i data-level="2"></i><i data-level="3"></i><i data-level="4"></i><span>More</span></div></div></div><div class="activity-bottom"><a href="{GITHUB}">○ @Deepakreddy1510</a><span id="activity-period">Public GitHub activity</span></div><div class="activity-updated" id="activity-updated"></div><noscript><p class="activity-error">View public contributions on the GitHub profile linked above.</p></noscript></section>
<section class="section" id="education">{heading('06','BACKGROUND','Education')}<div class="education"><div>Indian Institute of Technology Hyderabad<small>B.Tech · Electrical Engineering</small></div><span class="year">Expected 2027</span></div></section>
<section class="section connect" id="connect">{heading('07','LINKS','Connect')}<p>Open to interesting conversations and collaboration opportunities. Let's build something remarkable.</p><div class="connect-links">{connect}<a class="connect-link" href="mailto:{EMAIL}"><span class="connect-name">{MAIL_ICON} Email</span><span aria-hidden="true">↗</span></a><a class="connect-link" href="#resume-note" data-resume aria-controls="resume-note"><span class="connect-name">{RESUME_ICON} Resume</span><span aria-hidden="true">↗</span></a></div><p class="email-line"><a href="mailto:{EMAIL}">{EMAIL}</a></p><noscript><p class="resume-note">Resume coming soon. Please contact me by email.</p></noscript><div class="resume-note" id="resume-note" tabindex="-1" hidden>Resume coming soon. <a href="mailto:{EMAIL}">Contact me by email ↗</a></div></section></main>'''
def write_page(filename, content):
    (ROOT / filename).write_text(content)
    if PUBLIC.exists():
        (PUBLIC / filename).write_text(content)

write_page('index.html', frame(home))

def flow(items):
    return '<div class="flow">'+'<b aria-hidden="true">→</b>'.join('<span>'+escape(s)+'</span>' for s in items)+'</div>'

details=[
f'''<section class="section"><h2>The problem</h2><p>Working with structured data often means switching between SQL queries and data-preparation scripts. This project gives both tasks a shared natural-language entry point.</p></section>
<section class="section"><h2>The approach</h2><p>A router classifies each request and hands it to a specialized SQL or ETL analyst. LangGraph coordinates the workflows, while tools connect them to databases and datasets.</p>{flow(['User request','Router','SQL / ETL analyst','Tools','Data sources'])}<h3>SQL workflow</h3><p>The question is curated, database context is retrieved, and SQL is generated. A safety-validation step checks the query before execution; the result is then turned into an answer.</p>{flow(['Question','Context','Generate SQL','Validate','Execute','Answer'])}<h3>ETL workflow</h3><p>The analyst selects extraction or transformation tools, uses dataset context to generate Pandas transformations, and saves the resulting output.</p>{flow(['Request','Extract / load','Transform with Pandas','Output'])}</section>
<section class="section"><h2>Implementation notes</h2><div class="detail-grid"><div><h3>Separate responsibilities</h3><p>Routing, SQL analysis, and ETL each have a distinct workflow, keeping task-specific tools and logic together.</p></div><div><h3>Validation before execution</h3><p>The SQL workflow includes a safety check intended to reject destructive statements. The check runs before database execution.</p></div></div></section>
<section class="section"><h2>Main technologies</h2><p class="tech-line">Python · LangChain · LangGraph · PostgreSQL · Pandas</p></section>''',
f'''<section class="section"><h2>The problem</h2><p>An answer over a collection of PDFs is useful only when its supporting evidence can be found. This project preserves the connection between an answer, the source document, and its page.</p></section>
<section class="section"><h2>The approach</h2><h3>Index the documents</h3><p>Text is extracted page by page and split into tokenizer-aware chunks that stay within page boundaries. Sentence Transformers creates embeddings, stored alongside text and page metadata in PostgreSQL with pgvector.</p>{flow(['PDF','Extract','Page-aware chunks','Embeddings','pgvector'])}<h3>Retrieve, then answer</h3><p>Dense retrieval finds candidate passages. A CrossEncoder reranks them, and the strongest evidence is supplied to the language model. Source labels connect the answer back to the PDF and page.</p>{flow(['Question','Retrieve','Rerank','LLM','Answer + evidence'])}</section>
<section class="section"><h2>Designed around evidence</h2><div class="detail-grid"><div><h3>Traceable sources</h3><p>Document names, page numbers, and retrieved passages stay connected throughout the pipeline.</p></div><div><h3>Insufficient evidence</h3><p>The assistant is instructed to refuse when the documents do not support an answer. Retrieved candidates are not displayed as supporting evidence for a refusal.</p></div><div><h3>Focused evaluation</h3><p>Retrieval is evaluated separately from answer generation, so the quality of evidence selection can be assessed independently.</p></div><div><h3>Retrieval and reranking</h3><p>The default path combines exact dense search with CrossEncoder reranking. Experimental retrieval paths are separate from this default.</p></div></div></section>
<section class="section"><h2>Main technologies</h2><p class="tech-line">Python · PostgreSQL · pgvector · Sentence Transformers · CrossEncoder</p></section>'''
]
for i,p in enumerate(PROJECTS):
    other=PROJECTS[1-i]
    body=f'''<main id="main"><header class="detail-header"><a class="back-link" href="/#work">← Projects</a><div class="eyebrow">PROJECT {p['number']} / {p['category']}</div><h1>{p['title']}</h1><p>{p['description']}</p><a class="outline-link" href="{p['repo']}">View on GitHub <span aria-hidden="true">↗</span></a></header><div class="detail-content">{details[i]}</div><a class="next-project" href="/{other['slug']}.html"><div><span>EXPLORE PROJECT {other['number']}</span><strong>{other['title']}</strong></div><span aria-hidden="true">↗</span></a></main>'''
    write_page(p['slug'] + '.html', frame(body, p['title'] + ' — P Deepak', p['description']))
write_page('404.html', frame('<main id="main" class="section"><div class="eyebrow">404 / PAGE NOT FOUND</div><h1>Wrong turn.</h1><p>This page is not available.</p><a class="outline-link" href="/">Back to portfolio ↗</a></main>', 'Page not found — P Deepak'))
