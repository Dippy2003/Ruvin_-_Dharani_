# Dharani & Ruvin — Wedding Invitation

A small **React + Vite** app that hosts a full-page wedding invitation. The invitation itself is a static HTML file served from `public/` and shown inside an accessible iframe so you can deploy it like any static site (Netlify, Vercel, GitHub Pages, etc.).

## Features

- **React 19** shell with fast **Vite 8** dev server and production builds  
- **Full-viewport iframe** for the invitation HTML — update copy and design without touching React  
- **Google Fonts** loaded in the root HTML for consistent typography in the shell  
- **ESLint** configured for React and hooks  

## Prerequisites

- [Node.js](https://nodejs.org/) 20+ (LTS recommended)  
- npm (comes with Node)  

## Getting started

```bash
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`).

### Build & preview

```bash
npm run build
npm run preview
```

## Project layout

| Path | Role |
|------|------|
| `public/wedding-invitation.html` | The invitation page (must exist for the iframe in `App.jsx`) |
| `src/App.jsx` | Renders the invitation in a full-page iframe |
| `src/App.css` | Layout for the iframe (e.g. crop / full-bleed styling) |
| `index.html` | App shell, title, and font links |

If `public/wedding-invitation.html` is missing locally, add your exported invitation file there so the dev server can serve it.

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start dev server with HMR |
| `npm run build` | Production build to `dist/` |
| `npm run preview` | Serve the production build locally |
| `npm run lint` | Run ESLint |

## Tech stack

- [React 19](https://react.dev/)  
- [Vite 8](https://vite.dev/)  
- [ESLint 9](https://eslint.org/) with `eslint-plugin-react-hooks`  

---

## Recent commits (10)

Newest first. Rows 1–8 match `git log` on this branch; rows 9–10 summarize template setup that shipped with the earliest feature commits. Row 1 uses `HEAD` so the hash stays accurate after rebases or amends.

| # | Hash | Message |
|---|------|---------|
| 1 | `HEAD` | docs: add Vercel deployment and family invite links |
| 2 | `2ddad3d` | add crop |
| 3 | `f7ad7d9` | new |
| 4 | `41a9de8` | Merge origin/main; keep updated invitation HTML |
| 5 | `9e9c766` | Update wedding invitation content and directions link |
| 6 | `efaee0c` | feat: add deployable React invitation project |
| 7 | `5e289c4` | Delete wedding-invitation.html |
| 8 | `0ac15c7` | Add wedding invitation HTML file |
| 9 | — | chore: scaffold Vite 8 + React 19 + ESLint (template baseline) |
| 10 | — | chore: configure `@vitejs/plugin-react` and app shell fonts |

To refresh this table after new commits:

```bash
git log --oneline -10
```

## Live site

Production deployment: [https://ruvin-dharani-gixh.vercel.app/](https://ruvin-dharani-gixh.vercel.app/)

## Personalized invite links

Guest names are encrypted in the `?guest=` query parameter (AES-GCM). Generate new links with:

```bash
python scripts/generate_invite_links.py \
  --base-url "https://ruvin-dharani-gixh.vercel.app/" \
  --secret "A1b2C3d4E5f6G7h8J9k0L1m2N3p4Q5r6" \
  --name "Guest Name Here"
```

For a list of names (one per line), use `--input guests.txt`. The secret must match `SECRET_KEY` in `public/wedding-invitation.html`.

### Family & friends (Vercel)

- `Mr & Mrs Aththanayaka` — `https://ruvin-dharani-gixh.vercel.app/?guest=8SfHiVj5lfDFAj63.FwSBfn_JtY4PaOgEYS3pWNtAJJW_qU66qBGL-9pDUEEkUxdWtQ`
- `Mr & Mrs Kapila` — `https://ruvin-dharani-gixh.vercel.app/?guest=qI8QQNIzyPGH6U4O.If5h9SUnu-kyIXmWPds5PqNKYCf9VZqSygpRKLDEmA`
- `Mrs Chamari` — `https://ruvin-dharani-gixh.vercel.app/?guest=JIXh4pIq7afW2LEM.JILQ80OjKULy1QEoHyERYMuTLxBsGkuz3Sh2`
- `Mrs Renuka (Chuti)` — `https://ruvin-dharani-gixh.vercel.app/?guest=CfIxDVRXYzQc9vUd.ATe3poiZbz9gPnSGuMWX3FIjHqgCTPA10SouMXntx86geA`
- `Mr Kavishka Weerasuriya` — `https://ruvin-dharani-gixh.vercel.app/?guest=06-viGfyfGgqtAJv.OK-qjcnSLatCwNM6Dr9MJaetM3Apb-mDG0lsGXf5SzhXnvvUdj9u`
- `Mr & Mrs Manoj` — `https://ruvin-dharani-gixh.vercel.app/?guest=kN43ZHZ_Ig6uy8TG.rLbTalkxmQF9P-4lASS6exJARwUg5evz4iULsZG7`

### Earlier batch (ruvindharani.live)

- `Mr. Chatura Perera` — `https://ruvindharani.live/?guest=Vfh0CkFKgXNkYVVw.xJ6SR4k4lmSY-I4a516-NYovaq_DD5i0-M1o6ZkpLygutg`
- `Harsha Ramanayake` — `https://ruvindharani.live/?guest=oq1DMPz0YK2CXkPq.I-wTQOZzYlAXxBrpzvqrvfpEOGCvLRCgFSe7UrwXwgrf`
- `Duleema Hettige` — `https://ruvindharani.live/?guest=9Y9zJmx9TRt0JfIo.2zx-xTiCrR9cjs6GQM80F4CLXwWn5dReFv1JwgthYA`
- `Ridmi Manarandi` — `https://ruvindharani.live/?guest=GjzKjU3g4KThUbC6.Mhs9VD-GzYpiStWSPGYPbxRJhBOiQMRKsmX9X7Q5Rw`
- `Dinuka Gayan` — `https://ruvindharani.live/?guest=qcMZ99VP6jsULsa6.rwS3kaLGu2zZMTM1AK5D1KTBP5TZl6RN99gHxA`
- `Chamika Roshan` — `https://ruvindharani.live/?guest=1PKY4eqfklOUKhI-.GHKRyC7cPFOtzJptc5Ol1P5eEqHGn7eCgIRFc-f5`
- `Kalindu Lakshan` — `https://ruvindharani.live/?guest=Kf5x4ALddwwvDWDz.ABEdMdUWz07rnm5B9_eFla0lrq9XIltBWa20ZCn32w`
- `Dinoshkaran` — `https://ruvindharani.live/?guest=6hCeV2m7ezu4tRRk.p3CKAjSH2HTwNUZTB0CvEN-_36aKI5nqwa2b`
- `Gayan Hatharasinghe` — `https://ruvindharani.live/?guest=3eCtdjl-J7ihwH5n.PQ6sjKMfVpZo2buv4IvB74HIqy1l-isWIXPa5tJ-qH53LI4`
- `Hasini Kanchana` — `https://ruvindharani.live/?guest=M4HcHcrsTP8a2ylO.hUTAg5o6yLFMtdCWIT5J2VdUWPsLBFrDBcUTBlbJKQ`
- `Thihara Kumarasinghe` — `https://ruvindharani.live/?guest=y4jK0eFDkE819EGF.5KfPgrFqP98IDAiIheGIuDuJDElDLz-qBO8OlvjxhNhSqtQz`
- `Kaushalya Senarathne` — `https://ruvindharani.live/?guest=qZOdDBzfa6_IxYiu.-pYIW0PgR6MxrqXgqWdblccAoiDvzsboZrm9ZRvwJ7Cg01QF`
- `Tharuka Ruwan` — `https://ruvindharani.live/?guest=XwFYWEwTfPQCRPAf.ZNsdgj-y1kqoOYBHl5wCzEy0Wdi7RtgJiEj9ciA`
- `Chamodi Vimodya` — `https://ruvindharani.live/?guest=lNFjWQPiPG5N3KOa.Bn9iGemFgIaSOWdSoAhQoXo-cOrSjDiS6PDdD4EYKw`
- `Hasindu Chandeepa` — `https://ruvindharani.live/?guest=zA1VINvgbSgkemzp.DUte-16PFW0_QIop_HroAbyoOV1PqFRADlXgLYw-iBDT`
- `Upulini Akki & Daham Aiya` — `https://ruvindharani.live/?guest=wU84cBojxS03fY-v._NiLjK5UScp0goOFSH-ItJwIRox8YAGHka33xx7usJf0u7GYKxEoqJc`
- `Loku Akki` — `https://ruvindharani.live/?guest=KLDAlts9xnUN9Yxp.GfxKF3Z3xm8EEdAxc2YpMA7nSKTxtB159g`
- `Raveen` — `https://ruvindharani.live/?guest=Am8kogcPzx-IV-iZ.BJlOl-rfW1MTTmhDjgUfmdDmSkyRvA`
- `Chandupa Lokuliyana` — `https://ruvindharani.live/?guest=C7YJkU3Mshail-Tf.WkGI--fgSx2EcBeyQ_EgyGHdBC_3YLcT-TEOK0opQg27064`

## License

Private project (`"private": true` in `package.json`). Adjust if you publish the repo.
