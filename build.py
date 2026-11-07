#!/usr/bin/env python3
"""Static site generator for guohanharryzhang.github.io. Run: python3 build.py"""
import html, pathlib

ROOT = pathlib.Path(__file__).parent
NAME = "Guohan Harry Zhang"
SITE = "https://guohanharryzhang.github.io"
GH = "https://github.com/guohanharryzhang"
LI = "https://www.linkedin.com/in/harrygzhang/"
EMAIL = "gzhang45@jh.edu"
EMAIL2 = "gzhang2006.mg21@gmail.com"
DESC = ("Guohan Harry Zhang, electrical engineering at Johns Hopkins: lab automation, "
        "mixed-signal circuits, embedded firmware and the software that runs them.")

# (dates, organization, role, one-line description, link)
EXPERIENCE = [
    ("Jan 2025 – present", "Luo Research Lab, Johns Hopkins", "Undergraduate Researcher",
     "Helped automate zinc-electrodeposition experiments with OT-2 robotics, NI DAQ control and ultrasonic actuation; "
     "designed the fixtures; automated XRD workflows and ran VASP calculations on the Rockfish cluster.",
     "/work/zinc-electrodeposition-automation/"),
    ("Dec 2024 – present", "Costream (YC S25)", "Member of Technical Staff",
     "One of the first five engineers. Python backend and data pipelines that processed 50,000+ customer interactions; "
     "technical onboarding for three enterprise pilots. Current work is confidential.", None),
    ("Feb 2026 – present", "Scrawl AI", "Creator and developer",
     "Handwriting extraction and rendering engine with web and iOS apps; about 300 paying customers.", "/work/scrawl-ai/"),
    ("May – Jul 2026", "Comillas Pontifical University (ICAI), Madrid", "Research Student",
     "Adaptive decision-boundary search for a neural-network topology study. Research Project I and II graded 10/10.",
     "/work/neural-network-topology/"),
    ("Jun – Aug 2025", "Lucid Motors, Newark CA", "Manufacturing Engineering Intern",
     "Electrical engineering support for EV manufacturing and tooling projects.", None),
    ("Jun – Jul 2023", "Southern California Edison", "Electrical Engineering Intern (Troy Tech)",
     "Design reviews and field inspections of neighborhood power-distribution equipment and substations.", None),
]

TEACHING = [
    ("Jan – May 2026", "Teaching Assistant, Mastering Electronics and Laboratory", "Johns Hopkins University"),
    ("Aug – Dec 2025", "PILOT Leader, Introductory Chemistry", "Johns Hopkins University"),
]

EDUCATION = [
    ("2024 – 2028", "Johns Hopkins University",
     "B.S. Electrical Engineering, minor in Applied Mathematics. GPA 3.8 / 4.0.",
     "Coursework: Mastering Electronics and Laboratory, Introduction to VLSI, Advanced Digital Systems, "
     "Signals and Systems, Electromagnetics, Intermediate Programming (C/C++), Linear Algebra. "
     "In progress: Digital Signal Processing, Robot Sensors and Actuators, Probability and Statistics."),
    ("Summer 2026", "Comillas Pontifical University (ICAI), Madrid",
     "Research Project I and II, 10/10, 8 ECTS.", ""),
]

SKILLS = [
    ("Robotics and automation", "Opentrons OT-2 and API, NI DAQ, LabVIEW, Arduino, sensor integration and calibration"),
    ("Circuits", "Cadence Virtuoso, Spectre, SKILL, CMOS circuit design, DC and transient simulation, Verilog, SystemVerilog, Xilinx FPGA, 74-series logic, breadboarding"),
    ("Programming", "Python, C, C++, MATLAB, TypeScript, Swift, RISC-V assembly, Linux, Git"),
    ("Vision and machine learning", "OpenCV, PaddleOCR, PyTorch, scikit-learn, NumPy, pandas"),
    ("CAD and fabrication", "Autodesk Fusion, SolidWorks, AutoCAD, 3D printing"),
    ("Scientific computing", "VASP, Slurm, Rockfish HPC, pymatgen, XRD analysis, Avizo"),
    ("Backend and product", "FastAPI, Next.js, SwiftUI, Stripe, StoreKit, Docker, Fly.io, Vercel"),
]

HONORS = ["USACO Gold", "AIME qualifier", "CyberPatriot national semifinalist", "National Merit Scholar", "Eagle Scout"]

# thumb: (source asset, "cover" for photos or "fit" for diagrams)
PROJECTS = [
 dict(slug="zinc-electrodeposition-automation", title="Zinc electrodeposition automation", tag="Lab automation", featured=True,
  thumb=("lab_setup.jpg", "cover"),
  kicker="Luo Research Lab, Johns Hopkins | Spring 2025 to present",
  one="OT-2 robot, NI DAQ waveform and valve control, ultrasonic actuation and custom fixtures. 300% higher synthesis throughput.",
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

 dict(slug="scrawl-ai", title="Scrawl AI", tag="Product", featured=True,
  thumb=("scrawl_circuit_example.png", "fit"),
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

 dict(slug="cmos-keyword-spotting", title="CMOS keyword-spotting circuits", tag="Circuits", featured=True,
  thumb=("cmos_four_bank.png", "fit"),
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

 dict(slug="zero-set-finder", title="Black-box zero-set sampler", tag="Numerical methods", featured=True,
  thumb=("demo_v3_walkthrough.png", "fit"),
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

 dict(slug="ultrasonic-transducer-enclosure", title="Ultrasonic transducer and driver-board enclosure", tag="Mechanical design", featured=False,
  thumb=("transducer_assembly.png", "fit"),
  kicker="Luo Research Lab | January 2026",
  one="Fusion enclosure with a driver-board cavity, wire openings and a transducer support; assembly and cutaway views.",
  intro="The ultrasonic transducer and its driver board sat loose on the bench. I designed an enclosure that holds the board, routes the wiring and supports the transducer at the working position, and presented the design to the lab.",
  results=[],
  work=["Modeled the enclosure in Autodesk Fusion with a driver-board cavity, wire openings and a transducer support.",
        "Produced assembly and cutaway views for the lab review in January 2026.",
        "Not yet fabricated; printing and fit checks are the next step."],
  figures=[("transducer_assembly.png","Assembly view."),("transducer_cutaway.png","Cutaway showing the board cavity and transducer support.")],
  tools="Autodesk Fusion, 3D printing", links=[]),

 dict(slug="neural-network-topology", title="Neural-network decision-boundary topology", tag="Research software", featured=False, thumb=None,
  kicker="Comillas Pontifical University (ICAI), Madrid | May to July 2026",
  one="Adaptive boundary search (Sobol, Gaussian-process uncertainty, bisection) inside a PyTorch and GUDHI topology pipeline.",
  intro="A team study of the topology of decision boundaries learned by small ReLU networks. Networks are trained on known geometries, their boundaries are extracted, and persistent homology summarizes the result.",
  results=[("1,000","random 2-8-1 ReLU networks in the stored experiment"),("892","with stable detected boundaries; 736 had one component, 154 two, 2 three")],
  work=["Developed the adaptive boundary search using Sobol sampling, Gaussian-process uncertainty and bisection.",
        "Contributed to PyTorch training with seeded, checkpointed and resumable experiments, and to GUDHI persistent-homology analysis.",
        "Resolution checks do not prove exact topology; results depend on domain, sampling resolution and filtration scale. The team repository is private."],
  figures=[], tools="Python, PyTorch, scikit-learn, GUDHI, NumPy", links=[]),

 dict(slug="vasp-flow", title="vasp-flow: DFT workflow CLI for an HPC cluster", tag="Scientific computing", featured=False, thumb=None,
  kicker="Luo Research Lab | March to October 2026",
  one="Interactive CLI that takes a Materials Project structure to a submitted, monitored VASP job on the Rockfish cluster.",
  intro="Running density-functional-theory calculations by hand meant juggling structure files, four VASP inputs, a Slurm script and SSH. vasp-flow walks through those steps, explains each one, and handles upload, submission and status checks.",
  results=[],
  work=["Materials Project search and structure fetch, POSCAR/KPOINTS/INCAR generation from presets, POTCAR assembly on the cluster.",
        "SSH and SCP transport with sbatch submission and squeue parsing; resumable per-job progress.",
        "Used for the zinc surface-energy and adsorption study across three facets."],
  figures=[], tools="Python, pymatgen, paramiko, Slurm, VASP", links=[("vasp-flow on GitHub", GH+"/vasp-flow")]),

 dict(slug="cansat-payload", title="CanSat competition payload", tag="Embedded", featured=False, thumb=None,
  kicker="AstroJays / SEDS JHU | Team contributor",
  one="C/C++ firmware for sensor processing, flight-event logging and RF telemetry; accelerometer, barometer and GPS integration.",
  intro="A soda-can-sized payload for the CanSat competition. I worked on the sensor and firmware side of the team.",
  results=[],
  work=["Integrated and calibrated accelerometer, barometer and GPS measurements for descent and impact monitoring.",
        "Wrote C/C++ firmware for sensor-data processing, flight-event logging and RF telemetry."],
  figures=[], tools="C, C++, microcontrollers, RF telemetry, sensor calibration", links=[]),

 dict(slug="smaller-projects", title="Smaller projects", tag="Course and side projects", featured=False, thumb=None,
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

CSS = """
:root{--bg:#faf8f3;--fg:#1b1a17;--muted:#6c6961;--line:#e2ded4;--accent:#2d5d7b;--soft:#f1eee6;--figbg:#fff;color-scheme:light}
@media(prefers-color-scheme:dark){:root{--bg:#131312;--fg:#e8e5de;--muted:#9b988f;--line:#2b2a27;--accent:#8cb9d9;--soft:#1d1c1a;--figbg:#f4f2ec;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;padding:0 20px;font-feature-settings:"cv11","ss01"}
main{max-width:740px;margin:0 auto;padding:56px 0 72px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline;text-underline-offset:3px}
.serif,h1,h3,.feat h3{font-family:Newsreader,Georgia,"Times New Roman",serif;font-weight:500;letter-spacing:-.005em}
h1{font-size:44px;line-height:1.08;margin:0 0 14px;text-wrap:balance}
h2{display:flex;align-items:center;gap:16px;font-size:12px;line-height:1;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--muted);margin:60px 0 20px}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
h3{font-size:20px;line-height:1.3;margin:0}h3 a{color:var(--fg)}h3 a:hover{color:var(--accent)}
p{margin:0 0 12px}
.lede{font-size:19px;line-height:1.5;margin:0 0 14px;max-width:62ch}
.meta{font-size:14px;color:var(--muted);margin:0 0 18px}
.meta span+span::before{content:"·";margin:0 8px}
.links{display:flex;flex-wrap:wrap;gap:8px 10px;margin:0;font-size:14px}
.links a{border:1px solid var(--line);border-radius:3px;padding:5px 11px;color:var(--fg)}
.links a:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.links a.primary{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.links a.primary:hover{opacity:.85}
.feat{display:grid;grid-template-columns:216px 1fr;gap:6px 26px;padding:22px 0;border-top:1px solid var(--line);align-items:start}
.feat:first-of-type{border-top:0}.feat:last-of-type{border-bottom:1px solid var(--line)}
.feat img{width:100%;aspect-ratio:4/3;object-fit:cover;border:1px solid var(--line);border-radius:3px;background:var(--figbg);grid-row:1/4;display:block}
.feat .tag{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.feat p{font-size:15px;color:var(--fg);margin:2px 0 0;max-width:60ch}
.list{margin:0;padding:0;list-style:none}
.list li{display:grid;grid-template-columns:1fr auto;gap:2px 16px;padding:13px 0;border-top:1px solid var(--line)}
.list li:first-child{border-top:0}.list li:last-child{border-bottom:1px solid var(--line)}
.list .tag{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);white-space:nowrap;padding-top:4px}
.list p{grid-column:1/-1;font-size:15px;color:var(--muted);margin:0}
.rows{margin:0}
.row{display:grid;grid-template-columns:150px 1fr;gap:2px 20px;padding:14px 0;border-top:1px solid var(--line)}
.row:first-child{border-top:0}.row:last-child{border-bottom:1px solid var(--line)}
.row .when{color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums;padding-top:3px}
.row .org{font-weight:600;font-size:16px}
.row .role{color:var(--muted);font-size:14px}
.row p{font-size:15px;margin:4px 0 0;max-width:60ch}
.row .role,.row p{grid-column:2}
dl.skills{display:grid;grid-template-columns:200px 1fr;gap:0 20px;margin:0}
dl.skills dt{font-weight:600;font-size:14px;padding:10px 0;border-top:1px solid var(--line)}
dl.skills dd{margin:0;font-size:15px;color:var(--fg);padding:10px 0;border-top:1px solid var(--line)}
dl.skills dt:first-of-type,dl.skills dd:first-of-type{border-top:0}dl.skills dt:last-of-type,dl.skills dd:last-of-type{border-bottom:1px solid var(--line)}
.honors{display:flex;flex-wrap:wrap;gap:6px 0;padding:0;margin:0;list-style:none;font-size:15px}
.honors li+li::before{content:"·";color:var(--muted);margin:0 10px}
.contact{font-size:17px}
.crumb{font-size:14px;color:var(--muted);margin:0 0 36px;display:flex;gap:10px}
.kicker{color:var(--muted);font-size:14px;margin:0 0 22px}
.results{display:flex;flex-wrap:wrap;gap:12px 36px;margin:0 0 24px;padding:16px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.results div b{display:block;font-family:Newsreader,Georgia,serif;font-weight:500;font-size:28px;line-height:1.1;letter-spacing:-.01em;font-variant-numeric:tabular-nums}
.results div span{font-size:13px;color:var(--muted)}
ul.work{padding-left:18px;margin:0 0 20px}ul.work li{margin:0 0 8px;max-width:64ch}
figure{margin:26px 0}figure img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:3px;background:var(--figbg)}
figcaption{font-size:13px;color:var(--muted);margin-top:8px;max-width:64ch}
.tools{font-size:14px;color:var(--muted)}
.next{margin-top:48px;padding-top:18px;border-top:1px solid var(--line);font-size:15px;display:flex;justify-content:space-between;gap:16px}
footer{margin-top:64px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 18px}
@media(max-width:640px){h1{font-size:34px}.feat{grid-template-columns:1fr}.feat img{grid-row:auto;margin-bottom:6px}.row{grid-template-columns:1fr}.row .role,.row p{grid-column:1}dl.skills{grid-template-columns:1fr}dl.skills dt{border-top:1px solid var(--line);padding-bottom:0}dl.skills dd{border-top:0;padding-top:4px}dl.skills dt:last-of-type{border-bottom:0}}
"""

def esc(s): return html.escape(s)

def page(title, body, path="/", description=DESC):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:type" content="website">
<link rel="canonical" href="{SITE}{path}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css"></head><body><main>
{body}
<footer><span>{NAME}</span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="mailto:{EMAIL2}">{EMAIL2}</a><a href="{GH}">GitHub</a><a href="{LI}">LinkedIn</a><span>Updated November 2026</span></footer>
</main></body></html>"""

def thumb_path(p):
    return f"/assets/thumbs/{p['slug']}.jpg" if p.get("thumb") else None

def index():
    feats = "".join(
        f'<article class="feat"><img src="{thumb_path(p)}" alt="" loading="lazy">'
        f'<span class="tag">{esc(p["tag"])}</span><h3><a href="/work/{p["slug"]}/">{esc(p["title"])}</a></h3>'
        f'<p>{esc(p["one"])}</p></article>' for p in PROJECTS if p["featured"])
    more = "".join(
        f'<li><h3><a href="/work/{p["slug"]}/">{esc(p["title"])}</a></h3><span class="tag">{esc(p["tag"])}</span>'
        f'<p>{esc(p["one"])}</p></li>' for p in PROJECTS if not p["featured"])
    exp = "".join(
        f'<div class="row"><span class="when">{esc(w)}</span><span class="org">{esc(o)}</span><span class="role">{esc(r)}</span>'
        f'<p>{esc(d)}{(" <a href=%s>Read more</a>" % href) if href else ""}</p></div>' for w, o, r, d, href in EXPERIENCE)
    teach = "".join(
        f'<div class="row"><span class="when">{esc(w)}</span><span class="org">{esc(r)}</span><span class="role">{esc(o)}</span></div>'
        for w, r, o in TEACHING)
    edu = "".join(
        f'<div class="row"><span class="when">{esc(w)}</span><span class="org">{esc(o)}</span><span class="role">{esc(d)}</span>'
        f'{("<p>%s</p>" % esc(c)) if c else ""}</div>' for w, o, d, c in EDUCATION)
    skills = "".join(f'<dt>{esc(a)}</dt><dd>{esc(b)}</dd>' for a, b in SKILLS)
    honors = "".join(f'<li>{esc(h)}</li>' for h in HONORS)
    body = f"""
<header><h1>{NAME}</h1>
<p class="lede">Electrical engineering student at Johns Hopkins. I build lab automation and measurement setups, mixed-signal circuits, embedded firmware, and the software that runs them.</p>
<p class="meta"><span>B.S. 2028, Applied Mathematics minor</span><span>Baltimore, MD</span><span>U.S. citizen</span><span>Available Summer 2027</span></p>
<div class="links"><a class="primary" href="/assets/Guohan_Zhang_Resume.pdf">Resume (PDF)</a><a href="/assets/Guohan_Zhang_Portfolio.pdf">Engineering portfolio</a><a href="{GH}">GitHub</a><a href="{LI}">LinkedIn</a><a href="mailto:{EMAIL}">Email</a></div></header>
<h2>Selected work</h2>{feats}
<h2>More projects</h2><ul class="list">{more}</ul>
<h2>Experience</h2><div class="rows">{exp}</div>
<h2>Education</h2><div class="rows">{edu}</div>
<h2>Skills</h2><dl class="skills">{skills}</dl>
<h2>Teaching</h2><div class="rows">{teach}</div>
<h2>Honors</h2><ul class="honors">{honors}</ul>
<h2>Contact</h2><p class="contact">Looking for Summer 2027 internships in electrical, manufacturing, robotics, semiconductor and software engineering. Open to relocation anywhere in the United States.</p>
<p class="contact"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="mailto:{EMAIL2}">{EMAIL2}</a></p>"""
    return page(NAME, body)

def work(p, nxt):
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
{('<p>%s</p>' % links) if links else ""}
<p class="next"><a href="/">All work</a><a href="/work/{nxt["slug"]}/">Next: {esc(nxt["title"])} →</a></p>"""
    return page(f'{p["title"]} · {NAME}', body, path=f"/work/{p['slug']}/", description=p["one"])

def make_thumbs():
    try:
        from PIL import Image
    except ImportError:
        print("Pillow missing; thumbnails not regenerated"); return
    out = ROOT / "assets" / "thumbs"; out.mkdir(exist_ok=True)
    W, H = 864, 648
    for p in PROJECTS:
        if not p.get("thumb"): continue
        src, mode = p["thumb"]
        dst = out / f"{p['slug']}.jpg"
        if dst.exists() and dst.stat().st_mtime > (ROOT / "assets" / src).stat().st_mtime: continue
        im = Image.open(ROOT / "assets" / src).convert("RGB")
        if mode == "cover":
            s = max(W / im.width, H / im.height)
            im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
            l, t = (im.width - W) // 2, (im.height - H) // 2
            im = im.crop((l, t, l + W, t + H))
        else:
            pad = 56
            s = min((W - 2 * pad) / im.width, (H - 2 * pad) / im.height)
            im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
            canvas = Image.new("RGB", (W, H), (255, 255, 255))
            canvas.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
            im = canvas
        im.save(dst, "JPEG", quality=86, optimize=True)
        print("thumb", dst.name, dst.stat().st_size // 1024, "KB")

def main():
    make_thumbs()
    (ROOT / "style.css").write_text(CSS.strip() + "\n")
    (ROOT / "index.html").write_text(index())
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    for i, p in enumerate(PROJECTS):
        d = ROOT / "work" / p["slug"]; d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(work(p, PROJECTS[(i + 1) % len(PROJECTS)]))
    print("built", 1 + len(PROJECTS), "pages")

if __name__ == "__main__":
    main()
