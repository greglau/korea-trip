# Korea Trip Planner PWA

Interactive itinerary and map for the Korea trip — Gyeongju, Busan, Andong, Seoul (ICML), Sokcho/Seoraksan.

**Dates:** July 3–14, 2025 (12 Days)

## Features
- Interactive Leaflet map with route lines and spot markers
- 12-day detailed itinerary with sights, food, accommodation, and tips
- Naver Maps integration for navigation in Korea
- KTX booking link (Let's Korail)
- PWA support — works offline after first load
- Mobile-responsive with draggable sidebar

## Files
- `index.html` — Main page
- `data.js` — All 12 days of itinerary data with GPS coordinates
- `app.js` — Map rendering, sidebar logic, route drawing
- `styles.css` — Styling (light theme)
- `manifest.json` — PWA manifest
- `sw.js` — Service worker for offline caching

## Running Locally
Open `index.html` in a browser. For full PWA functionality (service worker), serve via HTTP:
```bash
python3 -m http.server 8000
# Then open http://localhost:8000
```

## Data Format
Each day in `data.js` contains:
- `day`, `date`, `title` — Basic info
- `distance`, `time` — Travel stats
- `sights` — HTML with descriptions, ticket info, hours
- `accommodation` — Hotel name and booking links
- `food` — Restaurant recommendations with HTML
- `practical` — Tips and warnings
- `spots` — Array of {name, type, lat, lng} for map markers
