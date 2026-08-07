# senior.chat — Design System

The visual identity: **a clear day.** Sky above, paper below, olive as the one
committed accent. The product asks people to trust a stranger with a big
decision, so the design leans calm, warm and legible rather than loud.

Two themes ship: **day** (light) and **dusk** (dark). Both are first-class.

---

## Color

Colors are declared once as CSS custom properties on `:root`, redefined under
`@media (prefers-color-scheme: dark)`. Never hardcode a hex in a component —
always reference a token.

### Ground & ink

| Token | Day | Dusk | Use |
|---|---|---|---|
| `--paper` | `#E7E9E1` | `#12170F` | page background below the hero |
| `--paper-2` | `#EFF1E9` | `#171E13` | raised paper panels |
| `--ink` | `#22331C` | `#EDF2E4` | headings, primary text |
| `--ink-soft` | `rgba(34,51,28,.80)` | `rgba(237,242,228,.72)` | body copy |
| `--ink-faint` | `rgba(34,51,28,.70)` | `rgba(237,242,228,.58)` | labels, captions, placeholders |

> `--ink-soft` and `--ink-faint` are **contrast-floored**, not chosen by eye.
> Their alphas are the minimum that clear WCAG AA (4.5:1) on `--paper`. Do not
> lower them. See [Accessibility](#accessibility).

### Brand

| Token | Day | Dusk | Use |
|---|---|---|---|
| `--olive` | `#314216` | `#3A501D` | primary buttons, badges, sent messages |
| `--olive-deep` | `#243310` | `#2C3F15` | hover state for olive |
| `--on-olive` | `#F2F6EA` | `#F2F6EA` | text on olive (9.96:1 — safe) |
| `--sage` | `#65876D` | `#7B9C83` | secondary accent, verified chips |
| `--steel` | `#6494B2` | `#7BA6C2` | tertiary accent, data marks |
| `--focus` | `#3E5A1E` | `#9BC088` | focus rings, success text |

### Sky (hero gradient, top → bottom)

`--sky-1` `#46708D` · `--sky-2` `#6494B2` · `--sky-3` `#87ABC0` ·
`--sky-4` `#B2C3C9` · `--sky-5` `#E4E9E2`
(dusk: `#0A1320` · `#122335` · `#1C3342` · `#2C454F` · `#3B5250`)

Stops sit at `0% / 24% / 48% / 68% / 88%`.

**`--glow`** (`rgba(255,252,238,.60)` day, `rgba(206,226,255,.20)` dusk) is a
haze laid over the sky as `radial-gradient(72% 50% at 50% 31%, var(--glow),
transparent 62%)`. Its geometry is **load-bearing for accessibility**: it lifts
the band behind the hero copy so dark ink clears contrast against a mid-tone
sky, while leaving the blue intact at the very top and near the hills. Changing
its size, position or alpha requires re-checking hero contrast.

### Surfaces

`--glass` / `--glass-strong` / `--glass-brd` — translucent fills for the nav
pill, input field and dashboard, always paired with `backdrop-filter: blur()`.
`--hairline` / `--hairline-soft` — 1px separators. `--card` — solid-ish panels.

### Semantic

Success reads through `--focus`. There is no dedicated error color; form errors
use native browser validation plus `--ink` copy.

---

## Typography

Three families, each with one job. All are **self-hosted as base64 woff2 data
URIs** — no external font requests, so the page renders identically offline and
under a strict CSP.

| Role | Family | Applied to |
|---|---|---|
| Display | **Instrument Serif** (regular + italic) | headlines, section titles, wordmark, big numbers |
| Body | **Manrope** (variable 200–800) | all running text, buttons, nav |
| Utility | **JetBrains Mono** | eyebrows, labels, captions, tabular figures |

Rules:
- Headlines set in Instrument Serif at `clamp(2.9rem, 7.4vw, 5.6rem)`,
  `line-height: 1.02`, `letter-spacing: -.015em`. Emphasis via `<em>` → italic,
  never bold.
- Body copy `clamp(1rem, 1.6vw, 1.16rem)` / `line-height: 1.6`.
- Utility text is uppercase, `.66rem`, `letter-spacing: .15em`. Use `.label`.
- Anywhere digits align in a column, use `font-variant-numeric: tabular-nums`
  (the `.mono` class sets this).

---

## Layout & space

- `.shell` — `max-width: 74rem`, centered, `padding-inline: clamp(1.25rem, 5vw, 3rem)`.
- Sibling groups are spaced with flex/grid `gap`, not per-element margins.
- Corner radii: `999px` for pills and inputs, `1.4–1.6rem` for cards and panels.
- Three shadow depths only: `--shadow-sm` / `--shadow-md` / `--shadow-lg`.
- Wide content scrolls inside its own `overflow-x: auto`; the page body never
  scrolls sideways.

---

## Motion

Motion is used to settle content into place, never to demand attention.

- `.reveal` fades and rises `22px` over `.9s`; `.d1/.d2/.d3` stagger it.
- Ambient canvases (clouds, fireflies) drift slowly and are `aria-hidden`.
- Buttons lift `1px` on hover, scale `.98` on press.

**Every one of these is disabled under `prefers-reduced-motion: reduce`**, where
`.reveal` resolves to its final state immediately.

---

## Accessibility

Non-negotiable, and checked numerically rather than by eye:

- Body text ≥ **4.5:1**; large display text ≥ **3:1**.
- Verified contrast: hero headline **5.36:1**, hero deck **4.81:1**, hero mono
  note **4.54:1**, button label on olive **9.96:1**.
- Every interactive element keeps a visible focus style
  (`:focus-visible { outline: 2px solid var(--focus) }` globally; the input
  wrapper additionally shows a ring on `:focus-within`).
- Forms use **native validation** — no `novalidate`. JS guards on
  `checkValidity()` and defers to `reportValidity()` for messaging.
- Status messages carry `role="status"` and `aria-live="polite"`.
- Decorative canvases, SVG and avatar chips are `aria-hidden="true"`.
- `<html lang="en">` is always set.

---

## Content integrity

The product's entire premise is advice that isn't being sold to you. The page
must hold the same standard.

- **No invented metrics.** No "98% of students…", no live user counts, no
  follower numbers. If it hasn't happened, it doesn't go on the page.
- **No fabricated testimonials.** Quotes are attributed to the team and framed
  as the team's own view, until real users give real ones.
- **Sample UI is labelled as such.** The dashboard and chat mock-ups say
  *example conversation*, and their `aria-label`s say so too.
- **Forward-looking statements are phrased as plans** ("4 cities first", "the
  first cities we're verifying seniors in"), never as current fact.
- Offers must be honourable as written — "First 500 get priority matching" is a
  commitment, so honour it.
