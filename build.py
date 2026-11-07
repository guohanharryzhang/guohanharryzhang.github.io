#!/usr/bin/env python3
"""Static site generator for guohanharryzhang.github.io. Run: python3 build.py"""
import html, os, pathlib, shutil

ROOT = pathlib.Path(__file__).parent
GH = "https://github.com/guohanharryzhang"
EMAIL = "gzhang45@jh.edu"
EMAIL2 = "gzhang2006.mg21@gmail.com"
NAME = "Guohan Harry Zhang"
SITE = "https://guohanharryzhang.github.io"

CURRENT = [
    ("Luo Research Lab, Johns Hopkins", "Undergraduate Researcher", "Spring 2025 to present",
     "Automating zinc-electrodeposition experiments: OT-2 robotics, NI DAQ controls, ultrasonic actuation, 3D-printed fixtures, XRD and DFT.", "/work/zinc-electrodeposition-automation/"),
    ("Costream (YC S25)", "Member of Technical Staff", "Dec 2024 to present",
     "Python backend and data pipelines for audio-AI sales analysis; onboarding for enterprise pilots. Current work is confidential.", None),
    ("Scrawl AI", "Creator and developer", "Feb 2026 to present",
     "Handwriting extraction and rendering engine with web and iOS apps, about 300 paying customers.", "/work/scrawl-ai/"),
]

PAST = [
    ("Comillas Pontifical University (ICAI), Madrid", "Research Student", "May to Jul 2026", "/work/neural-network-topology/"),
    ("Lucid Motors, Newark CA", "Manufacturing Engineering Intern", "Jun to Aug 2025", None),
    ("Johns Hopkins University", "Teaching Assistant, Mastering Electronics", "Jan to May 2026", None),
    ("Southern California Edison", "Electrical Engineering Intern (Troy Tech)", "Jun to Jul 2023", None),
]

PROJECTS = [
 dict(slug="zinc-electrodeposition-automation", title="Zinc electrodeposition automation", tag="hardware",
  kicker="Luo Research Lab, Johns Hopkins | Spring 2025 to present",
  one="OT-2 robot, NI DAQ waveform and valve control, ultrasonic actuation and custom fixtures; 300% higher synthesis throughput.",
  intro="Professor Yuting Luo's group studies zinc-ion batteries. The deposition experiments were slow because every trial needed a person to handle additives, run the pumps and swap electrodes. I helped turn that into an automated workflow.",
  results=[("300%","higher synthesis throughput"),("50+","experimental trials on the automated setup"),("80%","shorter hardware-iteration lead time")],
  work=["Integrated Opentrons OT-2 robotics with ultrasonic actuation so deposition cycles run without manual handling.",
        "Wrote the Python/NI DAQ routines for ultrasonic waveform generation and pressure-valve sequencing used across 50+ trials.",
        "Designed and 3D-printed the experimental fixtures and housings in Autodesk Fusion, which is where the 80% lead-time cut came from.",
        "Helped automate the XRD characterization workflow and ran VASP surface-energy and adsorption calculations for three zinc facets on the Rockfish cluster."],
  figures=[("lab_setup.jpg","Electrodeposition setup in the lab. Laboratory photograph."),
           ("lab_layout.jpg","Team setup and experiment sequence: additive handling, pumps, electrode storage and the deposition cycle. Slide credited to Peilin Li."),
           ("lab_controls.png","Team OT-2 control interface showing coordinated experiment settings. Slide credited to Peilin Li; my contributions are listed above.")],
  tools="Python, NI DAQ, Opentrons OT-2 and API, Autodesk Fusion, 3D printing, LabVIEW, Arduino, VASP, Slurm",
  links=[("vasp-flow on GitHub", GH+"/vasp-flow"),("xrd-indexer on GitHub", GH+"/xrd-indexer")]),

 dict(slug="ultrasonic-transducer-enclosure", title="Ultrasonic transducer and driver-board enclosure", tag="hardware",
  kicker="Luo Research Lab | January 2026",
  one="Fusion enclosure with a driver-board cavity, wire openings and a transducer support; assembly and cutaway views.",
  intro="The ultrasonic transducer and its driver board sat loose on the bench. I designed an enclosure that holds the board, routes the wiring and supports the transducer at the working position, and presented the design to the lab.",
  results=[],
  work=["Modeled the enclosure in Autodesk Fusion with a driver-board cavity, wire openings and a transducer support.",
        "Produced assembly and cutaway views for the lab review in January 2026.",
        "Not yet fabricated; printing and fit checks are the next step."],
  figures=[("transducer_assembly.png","Assembly view."),("transducer_cutaway.png","Cutaway showing the board cavity and transducer support.")],
  tools="Autodesk Fusion, 3D printing", links=[]),

 dict(slug="cmos-keyword-spotting", title="CMOS keyword-spotting circuits", tag="hardware",
  kicker="Introduction to VLSI, Johns Hopkins | Spring 2026 | Team project with Andrew Chae",
  one="Mixed-signal keyword detector in gpdk045: shift registers, current-mode banks and a threshold stage, simulated in Spectre.",
  intro="A schematic-level audio keyword detector. Two 1,024-stage shift registers feed weighted current-mode banks, and a threshold block flags a matched pattern. Designed in Cadence Virtuoso and simulated in Spectre with the gpdk045 kit.",
  results=[("755 mV","matched input"),("272 mV","anti-matched input"),("526 mV","all taps active")],
  work=["Implemented transmission gates, inverters and flip-flops, then built the two 1,024-stage shift registers.",
        "Built the current-mode bank subcells, bias circuits, the threshold block and the integration testbench.",
        "Wrote Cadence SKILL generators for the tap cells, weighted branches and a net-label testbench so the repetitive cells were scripted rather than hand-drawn.",
        "Helped map MATLAB-derived weights onto bias domains and debug integration.",
        "The four-bank extension passed schematic and DC checks; disk limits on the course server stopped the full transient run. No layout or fabricated chip."],
  figures=[("cmos_four_bank.png","Team schematic from the final report: two shift-register paths feed four current-mode banks and the threshold stage."),
           ("cmos_matched_test.png","Matched-pattern simulation of the 16-tap demonstration bank, settling near 755 mV.")],
  tools="Cadence Virtuoso, Spectre, SKILL, gpdk045, DC and transient simulation",
  links=[("cmos-kws-skill on GitHub", GH+"/cmos-kws-skill")]),

 dict(slug="zero-set-finder", title="Black-box zero-set sampler", tag="software",
  kicker="Independent research project | May to June 2026",
  one="Active-learning Gaussian process that finds where an unknown function crosses zero with 10 to 90 times fewer evaluations.",
  intro="Given a function you can only evaluate point by point, find the surface where it equals zero. Three versions: Sobol seeding with bisection, a gradient-rescue variant, and an active-learning Gaussian-process surrogate that picks the next query by the U-score |mu|/sigma and validates every returned point on the real function.",
  results=[("11x to 92x","fewer function evaluations than the sampling baseline, n = 2 to 6"),("1e-8","boundary residual |F| in all dimensions")],
  work=["Implemented all three samplers plus a shared bisection and Sobol toolkit in about 200 lines each.",
        "Built the benchmark and figure scripts, pytest suites and the write-up with the derivations.",
        "Documented the limits: smoothness assumption of the Matern kernel and the cubic GP cost above a few thousand points."],
  figures=[("fig_v3_vs_v2.png","Evaluations and wall time, v2 vs v3, on the unit sphere in 2 to 6 dimensions."),
           ("demo_v3_walkthrough.png","v3 on x^2 + y^2 - 3: Sobol seeds, active-learning rounds, extracted boundary.")],
  tools="Python, NumPy, SciPy, scikit-learn, matplotlib, pytest",
  links=[("zero-set-finder on GitHub", GH+"/zero-set-finder")]),

 dict(slug="neural-network-topology", title="Neural-network decision-boundary topology", tag="software",
  kicker="Comillas Pontifical University (ICAI), Madrid | May to July 2026",
  one="Adaptive boundary search (Sobol, Gaussian-process uncertainty, bisection) inside a PyTorch and GUDHI topology pipeline.",
  intro="A team study of the topology of decision boundaries learned by small ReLU networks. Networks are trained on known geometries, their boundaries are extracted, and persistent homology summarizes the result.",
  results=[("1,000","random 2-8-1 ReLU networks in the stored experiment"),("892","with stable detected boundaries; 736 had one component, 154 two, 2 three")],
  work=["Developed the adaptive boundary search using Sobol sampling, Gaussian-process uncertainty and bisection.",
        "Contributed to PyTorch training with seeded, checkpointed and resumable experiments, and to GUDHI persistent-homology analysis.",
        "Resolution checks do not prove exact topology; results depend on domain, sampling resolution and filtration scale. The team repository is private."],
  figures=[], tools="Python, PyTorch, scikit-learn, GUDHI, NumPy", links=[]),

 dict(slug="scrawl-ai", title="Scrawl AI", tag="software",
  kicker="Sole creator, developer and operator | Launched 2026 | About 300 paying customers",
  one="Extracts your handwriting from your own work, solves uploaded problems and renders the solutions in your handwriting. Web and iOS.",
  intro="Scrawl takes photos or PDFs of a user's handwritten work, builds a personal glyph library, and renders typed or solved content back in that handwriting, including equations and diagrams. I built the extraction and rendering engines, the web and iOS apps, billing, hosting and the marketing.",
  results=[("~300","paying customers"),("2","clients, Next.js and SwiftUI, on one FastAPI backend")],
  work=["Extraction: PaddleOCR line detection, OpenCV glyph splitting and vision-model crop classification into editable per-user libraries.",
        "Rendering: LaTeX and PyMuPDF layout drives glyph placement; correlated variation in slant, spacing and baseline; stretched brackets, fraction bars and redrawn vector paths for diagrams.",
        "Backend: asynchronous job pool with stage timing and failure categories, glyph and raster caches, parallel crop classification.",
        "Billing: Stripe and StoreKit entitlements with atomic credit reservations and idempotent purchase grants; pytest and XCTest coverage for timeouts, duplicate payment events and race conditions.",
        "Discovery: crawlable sample pages, JSON-LD, sitemaps, RSS and llms.txt."],
  figures=[("scrawl_circuit_example.png","Demo output: a circuit rendered in a user's handwriting. Not customer data."),
           ("scrawl_equation_detail.png","Demo output: equation detail.")],
  tools="Python, FastAPI, Next.js, TypeScript, SwiftUI, PaddleOCR, OpenCV, PyMuPDF, Stripe, StoreKit, Docker, Fly.io, Vercel",
  links=[("scrawlai.app","https://scrawlai.app/")]),

 dict(slug="vasp-flow", title="vasp-flow: DFT workflow CLI for an HPC cluster", tag="software",
  kicker="Luo Research Lab | March to October 2026",
  one="Interactive CLI that takes a Materials Project structure to a submitted, monitored VASP job on the Rockfish cluster.",
  intro="Running density-functional-theory calculations by hand meant juggling structure files, four VASP inputs, a Slurm script and SSH. vasp-flow walks through those steps, explains each one, and handles upload, submission and status checks.",
  results=[],
  work=["Materials Project search and structure fetch, POSCAR/KPOINTS/INCAR generation from presets, POTCAR assembly on the cluster.",
        "SSH and SCP transport with sbatch submission and squeue parsing; resumable per-job progress.",
        "Used for the zinc surface-energy and adsorption study across three facets."],
  figures=[], tools="Python, pymatgen, paramiko, Slurm, VASP", links=[("vasp-flow on GitHub", GH+"/vasp-flow")]),

 dict(slug="cansat-payload", title="CanSat competition payload", tag="hardware",
  kicker="AstroJays / SEDS JHU | Team contributor",
  one="C/C++ firmware for sensor processing, flight-event logging and RF telemetry; accelerometer, barometer and GPS integration.",
  intro="A soda-can-sized payload for the CanSat competition. I worked on the sensor and firmware side of the team.",
  results=[],
  work=["Integrated and calibrated accelerometer, barometer and GPS measurements for descent and impact monitoring.",
        "Wrote C/C++ firmware for sensor-data processing, flight-event logging and RF telemetry."],
  figures=[], tools="C, C++, microcontrollers, RF telemetry, sensor calibration", links=[]),

 dict(slug="smaller-projects", title="Smaller projects", tag="software",
  kicker="Course and side projects",
  one="XRD pattern indexer with local LLMs, a bidirectional-LSTM fake-news classifier, and a 74-series baseball scoreboard.",
  intro="",
  results=[],
  work=["XRD indexer: parses PANalytical XRDML files, detects peaks with SciPy, characterizes patterns with a local LLM and supports semantic search over a library. Built for triaging lab diffraction data.",
        "Fake news classifier, co-developed: PyTorch bidirectional LSTM on GloVe embeddings, about 94% test accuracy, served through FastAPI with a UMAP embedding explorer.",
        "Baseball scoreboard, Digital Systems Fundamentals: finite-state machine for balls, strikes and outs built from 74-series logic and seven-segment displays."],
  figures=[], tools="",
  links=[("xrd-indexer", GH+"/xrd-indexer"),("fake-news-detector", GH+"/fake-news-detector")]),
]

HONORS = "USACO Gold · AIME qualifier · CyberPatriot national semifinalist · National Merit Scholar · Eagle Scout"

CSS = """
:root{--bg:#22272e;--fg:#cdd9e5;--muted:#8b98a5;--line:#444c56;--accent:#6cb6ff;--soft:#2d333b;--figbg:#f4f4f4;color-scheme:dark}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;padding:0 20px}
main{max-width:700px;margin:0 auto;padding:60px 0 72px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline;text-underline-offset:3px}
h1{font-size:30px;line-height:1.15;margin:0 0 6px;letter-spacing:-.01em}
h2{display:flex;align-items:center;gap:16px;font-size:12px;line-height:1;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--muted);margin:56px 0 18px}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
h3{font-size:17px;font-weight:600;margin:0;line-height:1.35}
h3 a{color:var(--fg)}h3 a:hover{color:var(--accent)}
p{margin:0 0 12px}
.lede{font-size:18px;line-height:1.55;margin:14px 0 6px}
.meta{font-size:14px;color:var(--muted);margin:0 0 18px}
.meta span+span::before{content:"\\00b7";margin:0 8px}
.links{display:flex;flex-wrap:wrap;gap:6px 18px;margin:10px 0 0;font-size:15px}
.row{display:grid;grid-template-columns:1fr auto;gap:2px 16px;padding:14px 0;border-top:1px solid var(--line)}
.row:first-of-type{border-top:0}.row:last-of-type{border-bottom:1px solid var(--line)}
.row .when{color:var(--muted);font-size:14px;white-space:nowrap;font-variant-numeric:tabular-nums;padding-top:2px}
.row .role{color:var(--muted);font-size:14px;grid-column:1/-1}
.row .desc{grid-column:1/-1;font-size:15px;margin:4px 0 0}
ol.projects{list-style:none;padding:0;margin:0;counter-reset:p}
ol.projects li{display:grid;grid-template-columns:30px 1fr auto;gap:3px 12px;padding:14px 0;border-top:1px solid var(--line);counter-increment:p}
ol.projects li:first-child{border-top:0}ol.projects li:last-child{border-bottom:1px solid var(--line)}
ol.projects li::before{content:counter(p,decimal-leading-zero);color:var(--muted);font-variant-numeric:tabular-nums;font-size:13px;padding-top:4px}
ol.projects .one{grid-column:2/-1;font-size:15px;color:var(--muted);margin:0}
.tag{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:5px;white-space:nowrap}
.filters{display:flex;gap:18px;margin:0 0 6px;font-size:13px}
.filters button{font:inherit;background:none;color:var(--muted);border:0;border-bottom:1px solid transparent;padding:2px 0;cursor:pointer;letter-spacing:.02em}
.filters button:hover{color:var(--fg)}
.filters button[aria-pressed=true]{color:var(--fg);border-bottom-color:var(--fg)}
li.hide{display:none!important}
.honors{display:flex;flex-wrap:wrap;gap:6px 0;padding:0;margin:0;list-style:none;font-size:15px}
.honors li+li::before{content:"\\00b7";color:var(--muted);margin:0 10px}
.contact{font-size:17px}
.crumb{font-size:14px;color:var(--muted);margin:0 0 36px;display:flex;gap:10px}
.kicker{color:var(--muted);font-size:14px;margin:0 0 22px}
.results{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px 28px;margin:0 0 24px;padding:16px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.results div b{display:block;font-weight:600;font-size:24px;line-height:1.1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.results div span{font-size:13px;color:var(--muted)}
ul.work{padding-left:18px;margin:0 0 20px}ul.work li{margin:0 0 8px}
figure{margin:26px 0}figure img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:3px;background:var(--figbg)}
figcaption{font-size:13px;color:var(--muted);margin-top:8px}
.tools{font-size:14px;color:var(--muted)}
footer{margin-top:64px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 18px}
@media(max-width:600px){h1{font-size:26px}.row{grid-template-columns:1fr}.row .when{white-space:normal}ol.projects li{grid-template-columns:30px 1fr}.tag{grid-column:2;padding-top:0}}
"""

def page(title, body, depth=0, path="/", description=None):
    description = description or f"{NAME}, electrical engineering at Johns Hopkins: lab automation, mixed-signal circuits, embedded firmware and backend software."
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:type" content="website">
<link rel="canonical" href="{SITE}{path}">
<link rel="stylesheet" href="/style.css?v=5"></head><body><main>
{body}
<footer><span>{NAME}</span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="mailto:{EMAIL2}">{EMAIL2}</a><a href="{GH}">GitHub</a><a href="https://www.linkedin.com/in/harrygzhang/">LinkedIn</a><span>Updated November 2026</span></footer>
</main></body></html>"""

def esc(s): return html.escape(s)

def index():
    cur = "".join(
        f'<div class="row"><h3>{esc(o)}</h3><span class="when">{esc(w)}</span><span class="role">{esc(r)}</span>'
        f'<p class="desc">{esc(d)}{(" <a href=%s>Read more</a>" % href) if href else ""}</p></div>'
        for o, r, w, d, href in CURRENT)
    past = "".join(
        f'<div class="row"><h3>{esc(o)}</h3><span class="when">{esc(w)}</span><span class="role">{esc(r)}{(" · <a href=%s>details</a>" % href) if href else ""}</span></div>'
        for o, r, w, href in PAST)
    proj = "".join(
        f'<li data-tag="{p["tag"]}"><h3><a href="/work/{p["slug"]}/">{esc(p["title"])}</a></h3><span class="tag">{p["tag"]}</span>'
        f'<p class="one">{esc(p["one"])}</p></li>' for p in PROJECTS)
    body = f"""
<header><h1>{NAME}</h1>
<p class="lede">Electrical engineering at Johns Hopkins (B.S. 2028, Applied Mathematics minor, GPA 3.8). I build lab automation and measurement setups, mixed-signal circuits, embedded firmware, and the backends that run them. U.S. citizen, based in Baltimore.</p>
<div class="links"><a href="/assets/Guohan_Zhang_Resume.pdf">resume ↗</a><a href="/assets/Guohan_Zhang_Portfolio.pdf">engineering portfolio ↗</a><a href="{GH}">github ↗</a><a href="https://www.linkedin.com/in/harrygzhang/">linkedin ↗</a></div></header>
<h2>Currently</h2>{cur}
<h2>Projects</h2>
<div class="filters" role="group" aria-label="Filter projects"><button aria-pressed="true" data-f="all">All</button><button aria-pressed="false" data-f="hardware">Hardware</button><button aria-pressed="false" data-f="software">Software</button></div>
<ol class="projects">{proj}</ol>
<h2>Previously</h2>{past}
<h2>Honors</h2><ul class="honors">{"".join(f"<li>{esc(h)}</li>" for h in HONORS.split(" · "))}</ul>
<h2>Say hi</h2><p class="contact">Open to Summer 2027 internships in electrical, manufacturing, robotics, semiconductor and software roles, anywhere in the United States.</p>
<p class="contact"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="mailto:{EMAIL2}">{EMAIL2}</a></p>
<script>
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>{{
 const f=b.dataset.f;document.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 document.querySelectorAll('ol.projects li').forEach(li=>li.classList.toggle('hide',f!=='all'&&li.dataset.tag!==f));}}));
</script>"""
    return page(NAME, body)

def work(p):
    res = "".join(f'<div><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in p["results"])
    figs = "".join(f'<figure><img src="/assets/{f}" alt="{esc(c)}" loading="lazy"><figcaption>{esc(c)}</figcaption></figure>' for f, c in p["figures"])
    links = " · ".join(f'<a href="{u}">{esc(t)}</a>' for t, u in p["links"])
    body = f"""<p class="crumb"><a href="/">{NAME}</a><span>/</span><span>{esc(p["tag"])}</span></p>
<h1>{esc(p["title"])}</h1><p class="kicker">{esc(p["kicker"])}</p>
{('<p class="lede">%s</p>' % esc(p["intro"])) if p["intro"] else ""}
{('<div class="results">%s</div>' % res) if res else ""}
<h2>What I did</h2><ul class="work">{"".join(f"<li>{esc(w)}</li>" for w in p["work"])}</ul>
{figs}
{('<p class="tools"><b>Tools:</b> %s</p>' % esc(p["tools"])) if p["tools"] else ""}
{('<p>%s</p>' % links) if links else ""}"""
    return page(f'{p["title"]} · {NAME}', body, depth=2, path=f"/work/{p['slug']}/", description=p["one"])

def main():
    (ROOT / "style.css").write_text(CSS.strip() + "\n")
    (ROOT / "index.html").write_text(index())
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    for p in PROJECTS:
        d = ROOT / "work" / p["slug"]; d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(work(p))
    print("built", 1 + len(PROJECTS), "pages")

if __name__ == "__main__":
    main()
