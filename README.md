# Intuition Process Directory

A web app for families to discover the Intuition Process program, find certified teachers near them, and register for upcoming courses.

**Live site:** https://intuition-process.vercel.app

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Landing page — hero, benefits, and teacher search |
| `/find-teachers?location=...` | Teacher search results (city, state, or "City, ST") |
| `/courses` | All upcoming IP courses across the US |
| `/teachers` | Browse courses grouped by teacher |
| `/<teacher-slug>` | Individual teacher page with their upcoming courses |

### Teacher page examples
- https://intuition-process.vercel.app/chella-kiruthiga-kumar
- https://intuition-process.vercel.app/ankit-desai
- https://intuition-process.vercel.app/dhaneswori-goboori

---

## Features

**Teacher finder** — Families search by city, state abbreviation (CA), full state name (California), or "City, State" format (Newark, CA). If no teacher is in that exact city, the app geocodes it and shows all teachers in the same state.

**Live course data** — Each teacher's page pulls upcoming Intuition Process courses in real time from the Art of Living Unity API, filtered to IP Juniors (5–7), IP Kids (8–12), IP Teens (13–17), and IP Level 2.

**Teacher directory** — 109 certified US teachers sourced from the IP Teachers USA spreadsheet, stored in `static/teachers.json`.

---

## Stack

- **Backend:** Python / Flask
- **Hosting:** Vercel (serverless)
- **Course data:** Art of Living Unity API (`unity.artofliving.org/csapi/courses`)
- **Teacher data:** Google Sheets → `static/teachers.json`
- **Geocoding fallback:** OpenStreetMap Nominatim (no API key required)
- **Fonts:** Cormorant Garamond + Inter (Google Fonts)

---

## Project structure

```
/
├── app.py                  # Flask routes and course-fetching logic
├── static/
│   ├── teachers.json       # 109 US teacher records (name, city, state, phone, email)
│   └── images/
│       └── gallery.jpg     # Photo collage footer
└── templates/
    ├── landing.html        # Main landing page (/)
    ├── teacher.html        # Individual teacher page (/<slug>)
    ├── find_teachers.html  # Teacher search results (/find-teachers)
    ├── by_teacher.html     # Browse by teacher (/teachers)
    └── index.html          # All courses (/courses)
```

---

## Updating teacher data

The teacher list lives in `static/teachers.json`. When the IP Teachers USA Google Sheet is updated, re-export and replace this file. The sheet is at:
https://docs.google.com/spreadsheets/d/1HyfvZ0G_fFouIAFk9mJ19cl62krvTmtd7M4UnpSCIm0
