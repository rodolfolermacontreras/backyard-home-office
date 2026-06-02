# How to Contribute

Thanks for helping. Keep it simple.

## Before You Push

Install Git LFS once. We use it for CAD, STL, STEP, PCB, video, PDF.

```bash
brew install git-lfs       # macOS
sudo apt install git-lfs   # Linux
git lfs install
```

Then `git add` and `git commit` work normally.

## Upload CAD

- Put editable files in `open-source/cad/source/` (keep the original: .f3d, .FCStd, .SLDPRT, etc.)
- Always export and upload a `.step` to `open-source/cad/step/`
- Export `.stl` to `open-source/cad/stl/` for any 3D printable parts
- One folder per part if it has multiple versions

File naming: `part-name_v1.step`, `part-name_v2.step`

## Upload Electronics

- Schematics: PDF + source file (KiCad preferred)
- PCB: include Gerber zip for fab
- Update `open-source/electronics/bom/parts.csv` if you change parts

## Write Assembly Guide

- Use `learn/assembly/README.md`
- Numbered steps. One photo per step.
- Photos in `learn/assembly/photos/`, name them `step-01.jpg`, `step-02.jpg`...

## Share Your Setup

- Add a folder under `setups/community/your-name/`
- Include photos and a `setup.md` describing your config

## Rules

- No big words. Write so a beginner can follow.
- Test before you push.
- Commit messages: short and clear. Example: `add exterior panel STEP v2`
- One topic per Pull Request.

## License of Your Contributions

By sending a Pull Request you agree your contribution is licensed under the
same terms as the project:
- Hardware/CAD/docs: CC BY-NC-SA 4.0
- Code/firmware: PolyForm Noncommercial 1.0.0

See [LICENSE.md](LICENSE.md) for the plain-English summary.

## Issues

Open an Issue if:
- A file is missing or broken
- Instructions don't work
- You want to suggest a feature
- You found a bug

Use the templates in `.github/ISSUE_TEMPLATE/`.
