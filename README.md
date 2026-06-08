# Autonomous WorkPod

![Autonomous WorkPod](pod_banner.png)

Your office is 5 steps from the house. Plug one cable, skip permits, enter deep work.

## What is this?

Open hardware for a backyard office pod. Below permit threshold. One plug. No slab.

Whether you're learning, customizing, or building your own version — the files are here.

## Pod Lineup

| | [WorkPod Core](cad/pod-core/) | [WorkPod Pro](cad/pod-pro/) | [WorkPod Versatile](cad/pod-versatile/) |
|---|---|---|---|
| Floor area | 80 sqft | 102 sqft | 105 sqft |
| Ceiling height | 7.25' flat | 6.8'–9.3' sloped | 7.25' flat |
| Foundation | 4 adjustable feet | 6 adjustable feet | 6 adjustable feet |
| Weight capacity | 2.3 tons | 2.9 tons | 2.9 tons |
| Outlets | 2 wall | 2 wall + 1 floor | 5 wall |
| Lighting | 1 ceiling light | 1 ceiling light | 4 ceiling lights |
| Ethernet | 2 ports | — | 2 ports |
| Ventilator | — | Yes | Yes |
| Glass walls | 1 | 1 | 3 |
| Comfort range | — | 45–100°F | 45–100°F |
| Installation | 1–2 days | 1–2 days | 1–2 days |

All models: single outdoor cable from house, no excavation, no concrete, 5° slope tolerance, 7-layer wall system.

## Repo Layout

```
cad/                  3D design files
  pod-pro/            WorkPod Pro
    step/             STEP files (opens in any CAD tool)
    stl/              STL files for 3D printing
  pod-versatile/      WorkPod Versatile
    step/
    stl/
  pod-core/           WorkPod Core
    step/
    stl/

electronics/          Electrical system
  bom/                Electronics parts list

bom/                  Full bill of materials (all parts, prices, links)
```

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

- Hardware, CAD, docs — **[CC BY-NC-SA 4.0](LICENSE)**
- Firmware, code — **[PolyForm Noncommercial 1.0.0](LICENSE-CODE)**

Plain-English summary: **[LICENSE.md](LICENSE.md)**
