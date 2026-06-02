# Open Source Hardware

All open hardware files for the WorkPod Pro.

## Folders

```
cad/            3D design files
  concept/      Sketches, ideas, early drafts
  source/       Editable CAD (Fusion 360, FreeCAD, SolidWorks)
  step/         STEP files (works in any CAD tool)
  stl/          STL files ready to 3D print
  drawings/     2D drawings, dimensions (PDF)

electronics/    Electrical system
  schematics/   Circuit and wiring diagrams
  pcb/          PCB design files (KiCad, Gerber)
  bom/          Parts list for electronics
  wiring/       Outlet layout, cable routing, pinouts

firmware/       Code for smart controls (lighting, ventilation, sensors)

structure/      Structural engineering files and load calculations

foundation/     Foundation design, leveling specs, anchoring details
```

## Big Files

CAD, STEP, STL, PCB, and PDF files are stored via **Git LFS**.
Run `git lfs install` before cloning.

## Contributing CAD

- Put editable files in `cad/source/` (keep the original: .f3d, .FCStd, .SLDPRT)
- Always export and upload `.step` to `cad/step/`
- Export `.stl` to `cad/stl/` for 3D printing
- File naming: `part-name_v1.step`, `panel-exterior-left_v2.step`
