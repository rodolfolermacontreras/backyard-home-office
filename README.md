# Autonomous WorkPod Pro

<img width="1462" height="542" alt="Autonomous WorkPod Pro" src="https://github.com/user-attachments/assets/workpod-pro-hero" />

Your office is 5 steps from the house. Plug one cable, skip permits, enter deep work.

## What is this?

Open hardware for a backyard office pod. 102 sqft. Below permit threshold. One plug. No slab.

Whether you're learning, customizing, or building your own version — the files are here.

## Repo Layout

```
cad/                3D design files
  step/             WorkPod Pro — STEP files (opens in any CAD tool)
  stl/              WorkPod Pro — STL files for 3D printing
  studio-pod/       Studio Pod variant
    step/
    stl/

electronics/        Electrical system
  bom/              Electronics parts list

bom/                Full bill of materials (all parts, prices, links)
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

## Want to Contribute?

- Upload CAD to [cad/](cad/) with STEP export
- Open an Issue if something is broken or unclear

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

- Hardware, CAD, docs → **[CC BY-NC-SA 4.0](LICENSE)**
- Firmware, code → **[PolyForm Noncommercial 1.0.0](LICENSE-CODE)**

Plain-English summary: **[LICENSE.md](LICENSE.md)**
