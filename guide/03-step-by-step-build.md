# 3. 🔨 Step-by-Step Build

Follow these phases in order. Don't skip ahead. Check each box before moving on.

> Assumes the **WorkPod Core** (80 sq ft, 4 feet, flat roof). Pro/Versatile are the same idea
> with more feet/panels. Confirm all dimensions against the CAD in `../cad/pod-core/`.

---

## 🗓️ Overview of phases

```mermaid
flowchart LR
    P1[Phase 1\nSite prep] --> P2[Phase 2\nFeet + level]
    P2 --> P3[Phase 3\nFloor]
    P3 --> P4[Phase 4\nWalls]
    P4 --> P5[Phase 5\nRoof]
    P5 --> P6[Phase 6\nDoor + glass + seal]
    P6 --> P7[Phase 7\nElectrical]
    P7 --> P8[Phase 8\nAC + finish]
```

---

## Phase 1 — Prepare the ground 🌍

- [ ] Confirm your spot meets the **setbacks** from guide 1.
- [ ] Call **811** and wait for utilities to be marked (free).
- [ ] Clear grass/debris where the pod will sit.
- [ ] Roughly level the dirt — it does **not** need to be perfect (the feet adjust up to 5°).
- [ ] Lay a paver + a bit of gravel where each foot will land (a firm pad stops sinking).

**Footprint layout (Core, ≈ 8.4 ft × 11.3 ft outer — measured from CAD, see [guide 5](05-measurements.md)):**

```
        11.3 ft (outer)
   ┌───────────────────────┐
   │ ●                   ● │   ● = adjustable foot (x4)
   │      FLOOR AREA       │
   │   ~80 sq ft interior  │   8.4 ft (outer)
   │ ●                   ● │
   └───────────────────────┘
        DOOR side (front)
```

---

## Phase 2 — Place & level the 4 feet 🦶

This is the **most important step**. A level base = everything else lines up.

- [ ] Set the 4 adjustable feet on their pads in the rectangle above.
- [ ] Put your level (or laser level) across them.
- [ ] Screw each foot up/down until **all four tops are at the same height** and flat.
- [ ] Double-check corner-to-corner (diagonals) so it's square, not a parallelogram.

```
   Adjustable foot (side view)
        ┌───┐  ← top plate (bolts to floor frame)
        │   │
        ╪╪╪╪  ← threaded post: twist to raise/lower
        │   │
       ▄▄▄▄▄  ← base plate on paver
   ────────────  ground
```

✅ **Test:** a ball placed on any foot's top plate shouldn't roll off. All four equal height.

---

## Phase 3 — Floor 🟫

- [ ] Bolt the **floor frame bars** together (front/back/side/support bars) into a rectangle.
- [ ] Bolt the floor frame down onto the 4 feet using the **M12 × 60 mm** bolts.
- [ ] Re-check level now that weight is on the feet. Adjust feet if needed.
- [ ] Lay/attach the **floor panel** onto the frame.

```
   FLOOR FRAME (top view)
   ┌──────front bar──────┐
   │        support      │
   ├─────────bar─────────┤   side bars on left/right
   │                     │
   └──────back bar───────┘
     each corner sits on a foot ●
```

---

## Phase 4 — Walls 🧱

Walls are panels that stand up and bolt to the floor and to each other with **M10 × 40 mm** bolts.

- [ ] Start at one **back corner**. Stand the first wall panel, clamp it, bolt its base to the floor.
- [ ] Add the next panel; bolt the two panels **together** along the seam.
- [ ] Work your way around: back → sides → front. Leave the **door** and **glass** openings.
- [ ] Keep checking each panel is **plumb** (perfectly vertical) with your level.
- [ ] Two people: one holds/plumbs, one bolts.

```
   WALL PANELS bolt at seams (top view)
   back-1 ─┬─ back-2
   left-1  │  right-1
   left-2  │  right-2
        front + DOOR + GLASS
   (each "─┬─" = M10 bolts through the seam)
```

**Wall build-up (why it's warm/quiet) — factory "7-layer" panel, simplified:**

```
   OUTSIDE  →  [ weather skin ] [ insulation foam core ] [ inner panel ]  →  INSIDE
                aluminum/PU              thick foam            finished wall
```
DIY framed equivalent: `siding → sheathing → 2×4 + rigid foam → vapor barrier → interior panel`.

---

## Phase 5 — Roof 🟦

⚠️ Two people. Not on a windy day.

- [ ] Bolt the **roof frame** pieces (front/left/right) on top of the walls.
- [ ] Lift the **4 roof panels** up and bolt them to the frame.
- [ ] Make sure the roof overhangs/edges line up so water runs **off**, not in.
- [ ] Add the **vent cover** opening if your model has a ventilator.

```
   ROOF (flat, slight tilt for drainage)
   ┌───────────────────────┐
   │  panel A  │  panel B   │
   ├───────────┼────────────┤
   │  panel C  │  panel D   │
   └───────────────────────┘
     water drains to one edge →
```

---

## Phase 6 — Door, glass & sealing 🚪🪟

- [ ] Install the **door assembly** + handle/lock. Check it opens/closes freely.
- [ ] Install the **tempered glass wall** in its frame with the seals.
- [ ] Run a bead of **weatherproof sealant** along **every** outside seam: wall-to-wall,
      wall-to-roof, wall-to-floor, around door and glass.
- [ ] Add weatherstripping to the door.

✅ **Water test:** spray the outside with a hose and check inside for leaks. Re-seal any drips.

---

## Phase 7 — Electrical ⚡

👉 See **[04-electrical-wiring.md](04-electrical-wiring.md)** for the full diagram.
Short version:
- [ ] Electrician runs the buried **12/2 UF-B** cable from your house panel to the pod.
- [ ] Wires the **outlets**, **light**, and **ventilator** to a small subpanel/junction.
- [ ] Adds **GFCI** protection and a disconnect.
- [ ] City does the **rough** inspection, then the **final** inspection.

---

## Phase 8 — Comfort & finishing ❄️🪑

- [ ] Install the **mini-split AC** (or set up the portable AC) — El Paso essential.
- [ ] Add the bookshelf / furniture.
- [ ] Run **Ethernet** if you want fast internet.
- [ ] Move in your desk, chair, monitor. **Done! 🎉**

---

## 🧯 Common beginner mistakes (avoid these)

| Mistake | Fix |
|---------|-----|
| Feet not level | Spend the extra hour in Phase 2 — everything depends on it |
| Overtightening bolts | Snug, not gorilla-tight; use a torque wrench if unsure |
| Skipping the water test | Always hose-test before moving electronics in |
| Big glass wall facing **west** | Orient glass north/east to avoid El Paso afternoon heat |
| Wiring it yourself without a permit | Get the electrical permit — it's required and it's for your safety |
| Setting roof panels solo or in wind | Two people, calm day |

Next → **[04-electrical-wiring.md](04-electrical-wiring.md)**
