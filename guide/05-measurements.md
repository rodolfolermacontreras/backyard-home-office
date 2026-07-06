# 5. 📏 Real Measurements (from the CAD)

These numbers come from **measuring the actual STEP CAD files** in [`../cad/pod-core/step/`](../cad/pod-core/step/)
with the tool [`../scripts/measure_step.py`](../scripts/measure_step.py). STEP files store geometry
in **millimeters**; the tool converts to inches/feet.

> 🎯 **Honesty note:** individual CAD parts are modeled in different orientations, so a raw
> bounding box isn't always "length × width × height" in the obvious way. The **headline numbers
> below are cross-checked** against several parts and the designer's published spec, so you can
> trust them for planning and shopping. **Before cutting anything, always open the STEP file and
> confirm the exact dimension you need.**

---

## 🏠 WorkPod Core — headline dimensions

| Measurement | Metric | Imperial | Source |
|-------------|--------|----------|--------|
| **Outer footprint** | ≈ 2.56 m × 3.45 m | **≈ 8.4 ft × 11.3 ft** | floor-bar-front (2552 mm) + floor-bar-side (3455 mm) |
| **Interior floor area** | ≈ 7.4 m² | **≈ 80 sq ft** | published spec (matches footprint minus walls) |
| **Wall height** | ≈ 2.34 m | **≈ 7.7 ft** (7.25 ft interior ceiling) | wall clusters all ≈ 2334–2346 mm |
| **Panel / floor thickness** | ≈ 50 mm | **≈ 2 in** | floor-side panels (50 mm), support bar (60 mm) |
| **Adjustable foot** | 280 mm sq base, ~323 mm tall | **≈ 11 in square, ~12.7 in tall** (adjustable) | adjustable-base part |
| **Foundation feet** | 4 | 4 | Core spec |

**Sanity check:** 8.4 ft × 11.3 ft = ~95 sq ft outer. Subtract the ~2 in walls all around and you
get ≈ **80 sq ft usable** — exactly the published number. ✅

---

## 🪟 Component sizes (useful for planning openings)

| Part | As-modeled size (mm) | Imperial | What it is |
|------|----------------------|----------|------------|
| Adjustable foot | 280 × 323 × 280 | ~11 × 12.7 × 11 in | Leveling foot base |
| Outdoor light | 80 × 180 × 80 | ~3 × 7 × 3 in | Exterior light fixture |
| Vent cover | 192 × 200 × 408 | ~7.6 × 7.9 × 16 in | Ventilation grille |
| Outlet cover | 107 × 218 × 423 | ~4 × 8.6 × 16.6 in | Outlet plate assembly |
| Floor side panel (L) | 1227 × 2418 × 50 | ~48 × 95 × 2 in | Floor edge panel |
| Floor support bar | 2362 × 60 × 30 | ~93 × 2.4 × 1.2 in | Internal floor joist |
| Glass wall (glazing) | 850 × 2262 × ~15 | ~33.5 × 89 in, ~0.6 in thick | Tempered glass leaf |

> Glass thickness in the BOM is **5/16" tempered**. Order glass **to the exact opening** from a
> glass shop (tempered must be cut *before* tempering).

---

## 🧮 Measure any part yourself

The tool is reusable. To check a dimension before you cut:

```powershell
# One part
python scripts/measure_step.py cad/pod-core/step/floor-bar-side_v1.stp

# Several parts at once
python scripts/measure_step.py cad/pod-core/step/door_v1.stp cad/pod-core/step/wall-glass_v1.stp
```

Output shows Width/Depth/Height in mm, cm, inches, and feet. Works on **any** `.stp` file in this
repo (Core, Pro, or Versatile).

> ⚠️ The **assembly** file (`workpod-mini-assembly_v1.stp`) reports an inflated envelope because
> its parts are laid out in an exploded arrangement — use **individual part files** for real sizes.

---

## 📐 What this means for buying materials

- Your foundation pads (pavers) should sit under a **~8.4 ft × 11.3 ft** rectangle, one under each
  of the **4 feet**, roughly at the corners.
- Wall panels are about **7.7 ft tall** — they fit in a standard pickup/trailer laid flat.
- Everything is **~2 in thick** panels — plan storage and a flat, dry staging area.
- Buy the **glass last**, after the wall opening is built, and measure the real hole.

Next → **[cut-list-and-costs.csv](cut-list-and-costs.csv)** (opens in Excel) · or back to the
**[guide index](README.md)**
