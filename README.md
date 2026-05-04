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
| 1 | `HEAD` | docs: rewrite README with setup guide and 10-commit history |
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

## License

Private project (`"private": true` in `package.json`). Adjust if you publish the repo.
