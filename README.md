# Autonomous WorkPod Pro

<img width="1462" height="542" alt="Autonomous WorkPod Pro" src="https://github.com/user-attachments/assets/workpod-pro-hero" />

Your office is 5 steps from the house. Plug one cable, skip permits, enter deep work.

## What is this?

Open hardware for a backyard office pod. 102 sqft. Below permit threshold. One plug. No slab.

Whether you're learning, customizing, or building your own version — the files are here.

## Repo Layout

```
thinking/           Design philosophy, research notes, vision docs
  research/         User research, environmental studies
  design/           Design decisions, material choices
  vision/           Long-form thinking about the future of remote work

classics/           Archive of past designs and notable community builds
  designs/          Previous pod versions and concepts
  builds/           Notable community builds

learn/              How to build, install, and live in a WorkPod Pro
  assembly/         Step-by-step installation guide
    photos/         Installation photos (step-01.jpg, step-02.jpg...)
    videos/         Video walkthroughs (links or files)
  specs/            Spec sheets, dimensions, materials
  images/           Diagrams and reference images

open-source/        All open hardware files
  cad/              3D design files
    concept/        Sketches, early drafts, ideation
    source/         Editable CAD (Fusion 360, FreeCAD, SolidWorks)
    step/           STEP files (opens in any CAD tool)
    stl/            STL files for 3D printing
    drawings/       2D drawings, dimensions (PDF)
  electronics/      Electrical system
    schematics/     Wiring diagrams, circuit diagrams
    pcb/            PCB design files (KiCad, Gerber)
    bom/            Parts list for electronics
    wiring/         Wiring diagrams, outlet layout, pinouts
  firmware/         Code for smart controls (lighting, ventilation, sensors)
  structure/        Structural engineering files, load calculations
  foundation/       Foundation design, leveling details

setups/             Real builds and configurations from the community
  photos/           Setup photos
  videos/           Walkthroughs and tours
  community/        Community submitted setups

bom/                Full bill of materials (all parts, prices, links)
tools/              Scripts and helper tools
```

## Key Specs

| | |
|---|---|
| Floor area | 102 sqft |
| Ceiling height | 6.8' to 9.3' |
| Comfort range | 45–100°F |
| Glass | 5/16" tempered |
| Insulation layers | 6 |
| Foundation | 6 adjustable feet, 5° slope, 2.9 ton capacity |
| Electrical | 3 outlets, 1 ceiling light, 1 ventilator, 2 Ethernet ports |
| Installation | 1–2 days, no slab required |

## Big Files: Git LFS

This repo uses **Git LFS** for CAD, STL, STEP, PCB, video, and PDF files.
Install LFS once before cloning or pushing:

```bash
brew install git-lfs     # macOS
git lfs install
git clone https://github.com/autonomous-ai/autonomous-pod.git
```

## Want to Build One?

1. Read [learn/assembly/README.md](learn/assembly/README.md)
2. Get the parts from [bom/](bom/)
3. Review structural files in [open-source/structure/](open-source/structure/)
4. Follow the foundation guide in [open-source/foundation/](open-source/foundation/)
5. Flash any smart controls from [open-source/firmware/](open-source/firmware/)

## Want to Contribute?

- Share your build in [setups/](setups/)
- Upload CAD to [open-source/cad/source/](open-source/cad/source/) with STEP export
- Add installation photos to [learn/assembly/photos/](learn/assembly/photos/)
- Open an Issue if something is broken or unclear

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

- Hardware, CAD, docs → **[CC BY-NC-SA 4.0](LICENSE)**
- Firmware, code → **[PolyForm Noncommercial 1.0.0](LICENSE-CODE)**

Plain-English summary: **[LICENSE.md](LICENSE.md)**
