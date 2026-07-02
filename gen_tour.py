#!/usr/bin/env python3
"""Generate tour_package.html for korea-trip PWA."""

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Korea Trip — Gyeongju • Busan • Seoul • Sokcho (12 Days) | Professional Tour Package</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #334155; background-color: #f8fafc; margin: 0; padding: 0; }
    .header { background: linear-gradient(rgba(15,23,42,0.7), rgba(15,23,42,0.7)), url('https://images.unsplash.com/photo-1538485399081-7191377e8241?auto=format&fit=crop&w=1600&q=80') center/cover; color: white; padding: 60px 20px; text-align: center; }
    .header h1 { margin: 0 0 10px 0; font-size: clamp(1.5rem, 5vw, 2.5rem); }
    .header p { margin: 0; font-size: 1.1rem; opacity: 0.9; }
    .layout { display: flex; max-width: 1200px; margin: 0 auto; padding: 20px; gap: 30px; }
    .sidebar { width: 260px; flex-shrink: 0; }
    .sidebar-nav { position: sticky; top: 20px; background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); max-height: calc(100vh - 40px); overflow-y: auto; padding-bottom: 60px; }
    .sidebar-nav h3 { margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; color: #1e293b; }
    .sidebar-nav ul { list-style: none; padding: 0; margin: 0; }
    .sidebar-nav li { margin-bottom: 8px; }
    .sidebar-nav a { display: block; text-decoration: none; color: #475569; padding: 6px 10px; border-radius: 6px; transition: all 0.2s; font-size: 0.9rem; }
    .sidebar-nav a:hover, .sidebar-nav a.active { background: #eff6ff; color: #2563eb; font-weight: 500; }
    .content { flex-grow: 1; min-width: 0; }
    .summary-card { background: white; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-top: 4px solid #2563eb; }
    .summary-card h2 { margin-top: 0; color: #1e293b; }
    .day-card { background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border-left: 4px solid #3b82f6; scroll-margin-top: 20px; }
    .day-header { display: flex; flex-wrap: wrap; gap: 10px; justify-content: space-between; align-items: baseline; margin-bottom: 15px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }
    .day-title { font-size: 1.25rem; font-weight: 600; color: #0f172a; }
    .day-meta { display: flex; gap: 15px; font-size: 0.9rem; color: #64748b; }
    .meta-item i { color: #3b82f6; margin-right: 5px; }
    .history-box { background-color: #fdf8f6; border-left: 4px solid #d97706; padding: 12px; border-radius: 0 8px 8px 0; margin-bottom: 15px; color: #475569; font-size: 0.95rem; line-height: 1.6; }
    .history-box i { color: #d97706; margin-right: 5px; }
    .details-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px; background: #f8fafc; padding: 15px; border-radius: 8px; }
    .detail-item { font-size: 0.95rem; }
    .detail-label { font-weight: 600; color: #475569; display: block; margin-bottom: 3px; }
    .schedule { margin-top: 20px; }
    .schedule h4 { margin: 0 0 10px 0; color: #1e293b; }
    .schedule ul { margin: 0; padding-left: 20px; color: #475569; }
    .schedule li { margin-bottom: 8px; }
    .note-box { background: #eff6ff; border: 1px solid #bfdbfe; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
    .note-box h3 { margin-top: 0; color: #1e3a8a; }
    .fab { display: none; position: fixed; bottom: 20px; right: 20px; background: #2563eb; color: white; width: 56px; height: 56px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.3); justify-content: center; align-items: center; font-size: 24px; cursor: pointer; z-index: 1000; border: none; }
    .mobile-menu-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 998; }
    .mobile-menu { position: fixed; bottom: -100%; left: 0; right: 0; background: white; border-radius: 20px 20px 0 0; padding: 20px 20px 40px 20px; z-index: 999; transition: bottom 0.3s ease-in-out; box-shadow: 0 -4px 10px rgba(0,0,0,0.1); max-height: 85vh; overflow-y: auto; }
    .mobile-menu.open { bottom: 0; }
    .mobile-menu-close { position: absolute; top: 15px; right: 20px; font-size: 24px; color: #64748b; cursor: pointer; background: none; border: none; }
    @media (max-width: 768px) { .layout { flex-direction: column; padding: 10px; } .sidebar { display: none; } .fab { display: flex; } .header { padding: 30px 15px; } .header h1 { font-size: 1.8rem; } }
    @media print { @page { margin: 1cm; } .fab, .sidebar, .mobile-menu-overlay, .actions, .mobile-menu { display: none !important; } .layout { display: block; padding: 0; max-width: 100%; } .content { width: 100%; } body { background: white; font-size: 12pt; color: black; } .header { padding: 20px 0; background: none; color: black; border-bottom: 2px solid black; } .header h1 { font-size: 24pt; color: black; } .day-card { page-break-inside: avoid; border: 1px solid #ddd; box-shadow: none; padding: 15px; margin-bottom: 20px; } .summary-card { border: 1px solid #ddd; box-shadow: none; padding: 15px; margin-bottom: 20px; } .details-grid { display: block; background: none; padding: 0; } .detail-item { margin-bottom: 10px; } .history-box { background: none; border-left: 2px solid #555; padding-left: 10px; color: #333; } a { text-decoration: none; color: black; } }
  </style>
</head>
<body>

<div class="header">
  <h1>Korea Trip — Gyeongju, Busan, Seoul & Sokcho (12 Days)</h1>
  <p>Professional Itinerary · July 3–14, 2025</p>
</div>

<div class="layout">
  <div class="sidebar">
    <div class="sidebar-nav">
      <h3>Navigation</h3>
      <ul id="desktop-nav">
<li><a href="#day1">Day 1 (Gyeongju)</a></li>
<li><a href="#day2">Day 2 (Bulguksa → Busan)</a></li>
<li><a href="#day3">Day 3 (Haedong Yonggungsa → Andong)</a></li>
<li><a href="#day4">Day 4 (Hahoe → Seoul)</a></li>
<li><a href="#day5">Day 5 (ICML Day 1)</a></li>
<li><a href="#day6">Day 6 (ICML Day 2)</a></li>
<li><a href="#day7">Day 7 (ICML Day 3)</a></li>
<li><a href="#day8">Day 8 (ICML Day 4 → Sokcho)</a></li>
<li><a href="#day9">Day 9 (Seoraksan)</a></li>
<li><a href="#day10">Day 10 (Naksansa & Falls)</a></li>
<li><a href="#day11">Day 11 (Coastal Leisure)</a></li>
<li><a href="#day12">Day 12 (Departure)</a></li>
<li><a href="#notes">Key Notes</a></li>
      </ul>
    </div>
  </div>

  <div class="mobile-menu-overlay" id="mobileOverlay"></div>
  <div class="mobile-menu" id="mobileMenu">
    <button class="mobile-menu-close" id="closeMenuBtn"><i class="fa-solid fa-xmark"></i></button>
    <h3 style="margin-top:0; border-bottom:1px solid #e2e8f0; padding-bottom:10px;">Navigation</h3>
    <ul class="sidebar-nav" style="box-shadow:none; padding:0;" id="mobile-nav">
<li><a href="#day1">Day 1 (Gyeongju)</a></li>
<li><a href="#day2">Day 2 (Bulguksa → Busan)</a></li>
<li><a href="#day3">Day 3 (Haedong Yonggungsa → Andong)</a></li>
<li><a href="#day4">Day 4 (Hahoe → Seoul)</a></li>
<li><a href="#day5">Day 5 (ICML Day 1)</a></li>
<li><a href="#day6">Day 6 (ICML Day 2)</a></li>
<li><a href="#day7">Day 7 (ICML Day 3)</a></li>
<li><a href="#day8">Day 8 (ICML Day 4 → Sokcho)</a></li>
<li><a href="#day9">Day 9 (Seoraksan)</a></li>
<li><a href="#day10">Day 10 (Naksansa & Falls)</a></li>
<li><a href="#day11">Day 11 (Coastal Leisure)</a></li>
<li><a href="#day12">Day 12 (Departure)</a></li>
<li><a href="#notes">Key Notes</a></li>
    </ul>
  </div>

  <div class="content">
    <div class="summary-card">
      <h2><i class="fa-solid fa-map"></i> Trip Overview</h2>
      <p>A 12-day journey through Korea's cultural heartland and eastern coast. Starting in the ancient capital of Gyeongju (Silla kingdom), moving to Busan's coastal energy, spending four conference days at ICML in Seoul with cultural excursions, then heading north to Sokcho for Seoraksan National Park's dramatic granite peaks and East Sea coastline. July is peak summer — expect heat, humidity, and the monsoon season (jangma) in late July.</p>
      <div class="actions" style="margin-top: 20px; display: flex; align-items: center; gap: 10px;">
        <a href="index.html" target="_blank" style="display: inline-block; padding: 12px 20px; background: #f59e0b; color: white; border-radius: 8px; text-decoration: none; font-weight: bold; text-align: center; border: none; cursor: pointer; flex: 1;"><i class="fa-solid fa-map-location-dot"></i> Interactive Map</a>
        <button onclick="window.print()" style="padding: 12px 15px; background: #e2e8f0; color: #475569; border-radius: 8px; border: none; cursor: pointer; font-weight: bold; font-size: 0.9rem;" title="Print"><i class="fa-solid fa-print"></i></button>
        <button onclick="window.close()" style="padding: 12px 15px; background: #e2e8f0; color: #475569; border-radius: 8px; border: none; cursor: pointer; font-weight: bold; font-size: 0.9rem;" title="Close"><i class="fa-solid fa-xmark"></i></button>
      </div>
    </div>

'''

# Day cards data - each day is a tuple of (id, title, weather, distance, time, history, sights, hotel, food, hours, schedule_items)
days = [
    {
        "id": 1,
        "title": "Day 1 (2025-07-03): Incheon → Singyeongju — Arrival & Gyeongju Historic Core",
        "weather": "🌤️ 24-30°C (Warm/Humid)",
        "distance": "~380km (AREX + KTX)",
        "time": "~5h transit",
        "history": '<i class="fa-solid fa-scroll"></i> <b>The Ancient Capital of Silla</b><br>Gyeongju (경주) was the capital of the Silla Kingdom for over 900 years (57 BC – 935 AD). Often called "the museum without walls," the entire city is dotted with UNESCO-listed tombs, temple ruins, and palace foundations. The 23 grass mounds of Daereungwon are intact royal tombs — not ruins, but smooth hills rising from the suburban streetscape. The city\'s density of heritage sites per square kilometre is unmatched in Korea.',
        "sights": '🌟 Daereungwon Tomb Complex (대릉원) | 🌟 Hwangridan-gil Street (황리단길) | 🌟 Donggung Palace & Wolji Pond (동궁과 월지/안압지)',
        "hotel": '✅ Gyeongju Hwangnamkwan Hanok Hotel (Booked)',
        "food": 'Hwangnam-ppang (red bean bun) at Choi Yeonghwa Ppang | Hyanghwajeong for cockle bibimbap',
        "hours": '🌟 Daereungwon: 7:00–22:00 (summer) | 🌟 Wolji Pond: 7:00–22:00 (illuminated at night) | Tickets: ₩3,000 each',
        "schedule": [
            ("09:00 – 10:30", "Arrive Incheon Airport (ICN). Clear immigration, collect luggage. Purchase T-money card at airport station and top up ₩50,000."),
            ("10:30 – 11:30", "Take AREX (Airport Railroad Express) from Incheon Airport to Seoul Station. Regular train takes ~43 min; express takes ~35 min."),
            ("11:30 – 12:00", "Transfer at Seoul Station to KTX platform. Walk time between AREX and KTX platforms is ~5 min."),
            ("12:00 – 13:00", "KTX Seoul Station → Singyeongju. Journey time ~1h 20min. Book in advance via Korail — July is peak season."),
            ("13:00 – 13:45", "Arrive Singyeongju Station. Take taxi to hotel (approx. 20 min, ₩15,000–20,000). Drop bags at hotel."),
            ("14:00 – 15:30", "Walk to Daereungwon Tomb Complex (대릉원). Explore the 23 grass mounds and Cheonmachong royal tomb interior. Allow 1–1.5 hours."),
            ("15:30 – 16:30", "Stroll Hwangridan-gil Street (황리단길). Coffee at a hanok-style cafe, buy warm Hwangnam-ppang (red bean buns) from Choi Yeonghwa Ppang — the original shop on this street."),
            ("16:30 – 17:30", "Return to hotel for a rest. July heat is intense; midday recovery is essential."),
            ("17:30 – 19:00", "Walk to Donggung Palace & Wolji Pond (월지). The illuminated pavilions reflected in the pond are one of Korea's best night views. Stay for sunset and illumination."),
            ("19:00 – 20:30", "Dinner at Hyanghwajeong (향화정) — long-standing local favourite for cockle bibimbap and seafood pancake. Arrive early or expect a queue."),
            ("20:30 – 21:30", "Return to hotel. Early rest — full day tomorrow."),
        ],
    },
    {
        "id": 2,
        "title": "Day 2 (2025-07-04): Bulguksa & Seokguram → Busan — Mountain Sanctuaries & Coast",
        "weather": "🌤️ 25-31°C (Warm/Humid)",
        "distance": "~70km (Bus + KTX)",
        "time": "Full day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Silla\'s Spiritual Masterpieces</b><br>Bulguksa (불국사, "Temple of the Buddha Land") and Seokguram (석굴암) are the twin crowning achievements of Silla-era Buddhist art, both UNESCO World Heritage Sites. Bulguksa\'s stone staircases and twin pagodas are precisely positioned on a terrace above the forest. Seokguram\'s granite rotunda houses Korea\'s finest 8th-century seated Buddha — the geometry of the chamber channels light onto the face from a single hidden aperture.',
        "sights": '🌟 Bulguksa Temple (불국사) | 🌟 Seokguram Grotto (석굴암)',
        "hotel": '✅ Hotel Foret Premier Nampo, Busan (Booked)',
        "food": 'Yeonhwa Baru (Buddhist vegan set near Bulguksa) | Mytoury Dwaeji Gukbap (pork rice soup) | Gukje Milmyeon',
        "hours": '🌟 Bulguksa: 7:00–18:30 (summer) | 🌟 Seokguram: 8:00–18:00 (timed entry, fills fast in July) | Tickets: ₩6,000 each',
        "schedule": [
            ("07:30 – 08:15", "Early breakfast at hotel. Pack light day bag (keep heavy luggage at hotel — you'll return tonight)."),
            ("08:15 – 09:00", "Taxi to Bulguksa Temple entrance. Allow time for the long stone staircase (Cheongungyo/Baegungyo) — it's steep and exposed to July sun."),
            ("09:00 – 11:30", "Explore Bulguksa (불국사). Read the spatial geometry of the twin pagodas, the stone terrace, and the main halls. Allow 2–2.5 hours."),
            ("11:30 – 12:00", "Bus 12 from Bulguksa to Seokguram (runs every ~30 min, 15-min ride). <b>CRITICAL:</b> Seokguram has timed-entry slots of ~10 min each. Peak July = long queues. Go straight there."),
            ("12:00 – 13:00", "Seokguram Grotto (석굴암). The granite rotunda and seated Buddha. Allow the full 10-min viewing slot."),
            ("13:00 – 14:00", "Lunch at Yeonhwa Baru (연화바루) — Joseon-era Buddhist vegan set meal near Bulguksa. ₩20,000 pp. Book in advance."),
            ("14:00 – 15:00", "Taxi back to hotel, collect luggage. Walk or taxi to Singyeongju Station."),
            ("15:00 – 16:00", "KTX Singyeongju → Busan. Journey time ~20 min."),
            ("16:00 – 17:00", "Arrive Busan Station. Taxi to hotel in Nampo-dong (approx. 10 min, ₩8,000–12,000). Drop bags."),
            ("17:00 – 18:30", "Explore Nampo-dong area. Walk to BIFF Square, Jagalchi Market exterior. Grab eomuk (fish cake) at dockside stalls."),
            ("18:30 – 20:00", "Dinner at Mytoury or Ssangdoongi — Busan's signature Dwaeji Gukbap (pork rice soup). Michelin Bib Gourmand. Rich bone broth, perfect for July heat."),
            ("20:00 – 21:00", "Evening walk along Nampo-dong streets. Gukje Milmyeon (국제밀면) for cold noodles if still hungry."),
        ],
    },
    {
        "id": 3,
        "title": "Day 3 (2025-07-05): Haedong Yonggungsa → Andong — Coastal Temple & Hahoe Village",
        "weather": "🌤️ 26-32°C (Hot/Humid)",
        "distance": "~200km (KTX + Bus)",
        "time": "Full day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Where the Mountain Meets the Sea</b><br>Haedong Yonggungsa (해동 용궁사, "Dragon Palace Temple by the Sea") is one of Korea\'s rare coastal temples — built on rocky cliffs overlooking the East Sea, it was constructed in 1376 during the Goryeo Dynasty. The temple\'s main hall sits directly above crashing waves, a dramatic fusion of Buddhist architecture and natural seascape. Andong\'s Hahoe Folk Village (하회마을) is a UNESCO-listed Joseon-era village where the Ryu clan has lived for over 600 years, preserving traditional hanok architecture and the masked dance drama tradition.',
        "sights": '🌟 Haedong Yonggungsa Temple (해동 용궁사) | 🌟 Hahoe Folk Village (하회마을)',
        "hotel": '✅ Andong Hahoe Hanok Stay (Booked)',
        "food": 'Andong Sundubu-jjigae (Andong soft tofu stew) | Hahoe traditional Korean meal',
        "hours": '🌟 Haedong Yonggungsa: 6:00–23:00 (summer, open late) | 🌟 Hahoe Village: 9:00–18:00 (free entry) | Museum: ₩3,000',
        "schedule": [
            ("07:30 – 08:15", "Early breakfast at hotel. Pack day bag."),
            ("08:15 – 09:00", "Taxi to Busan Station. KTX Busan → Donghae (approx. 1h, ₩25,000). Book in advance."),
            ("09:00 – 10:30", "KTX Busan → Donghae Station. Arrive ~10:30."),
            ("10:30 – 11:00", "Taxi from Donghae Station to Haedong Yonggungsa (approx. 15 min, ₩8,000–12,000)."),
            ("11:00 – 13:00", "Explore Haedong Yonggungsa (해동 용궁사). Walk the cliffside paths, see the main hall perched above waves. The coastal setting is unique in Korea — most temples are mountain-secluded."),
            ("13:00 – 14:00", "Lunch at a nearby seafood restaurant in Donghae. Fresh East Sea fish, sashimi, and grilled mackerel."),
            ("14:00 – 15:30", "KTX Donghae → Andong (approx. 45 min, ₩18,000). Arrive ~16:00."),
            ("15:30 – 16:00", "Taxi from Andong Station to Hahoe Village (approx. 15 min, ₩8,000–12,000)."),
            ("16:00 – 18:30", "Explore Hahoe Folk Village (하회마을). UNESCO-listed Joseon-era village. Walk the traditional hanok streets, visit the Andong Mask Museum (₩3,000), and see the Namsan Mountain backdrop. The village is free to enter; museums have small fees."),
            ("18:30 – 19:30", "Check into Andong Hahoe Hanok Stay. Traditional Korean guesthouse experience."),
            ("19:30 – 21:00", "Dinner at a local restaurant — Andong Sundubu-jjigae (안동 순두부 찌개), the city's signature dish. Spicy soft tofu stew with beef, seafood, and vegetables."),
        ],
    },
    {
        "id": 4,
        "title": "Day 4 (2025-07-06): Hahoe Morning → Seoul — Traditional Culture & ICML Prep",
        "weather": "🌤️ 25-31°C (Hot/Humid)",
        "distance": "~280km (KTX)",
        "time": "~3h transit",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Morning Mist Over Hahoe</b><br>Hahoe Village is best visited early — the morning light on the traditional hanok roofs and the Namsan Mountain backdrop creates one of Korea\'s most photographed scenes. The village was a model Joseon-era Confucian settlement, where the Ryu clan maintained strict social hierarchies and elaborate ritual traditions. The Hahoe Talchum (masked dance drama) is designated as a UNESCO Intangible Cultural Heritage — the masks represent different social classes, from yangban (aristocrats) to commoners and women.',
        "sights": '🌟 Hahoe Village (morning walk) | 🌟 Andong Folk Museum',
        "hotel": '✅ Hotel Skypark Myeongdong 2, Seoul (Booked)',
        "food": 'Andong Jjim (Andong steamed chicken) | Myeongdong Kyoja for kalguksu',
        "hours": '🌟 Hahoe Village: 9:00–18:00 | Andong Folk Museum: 9:00–17:30 (closed Mon)',
        "schedule": [
            ("07:00 – 08:30", "Early morning walk through Hahoe Village. Best light for photos, fewer crowds. Walk the riverside path and visit the Yangdong Village area (nearby, also UNESCO-listed)."),
            ("08:30 – 09:30", "Breakfast at the hanok guesthouse — traditional Korean breakfast with rice, soup, and banchan (side dishes)."),
            ("09:30 – 10:00", "Taxi to Andong Station."),
            ("10:00 – 11:30", "KTX Andong → Seoul. Journey time ~1h 30min. Book in advance via Korail."),
            ("11:30 – 12:30", "Arrive Seoul Station. Taxi to hotel in Myeongdong (approx. 15 min, ₩10,000–15,000). Drop bags."),
            ("12:30 – 14:00", "Lunch in Myeongdong. Try Andong Jjim (안동찜닭, 'Andong chicken') — a spicy-sweet braised chicken dish that originated in Andong. Myeongdong Kyoja (명동교자) for kalguksu (hand-cut noodles)."),
            ("14:00 – 16:00", "ICML conference prep. Visit the venue (check location), collect badge, review schedule. Set up laptop and presentation materials."),
            ("16:00 – 17:30", "Explore Myeongdong shopping district. Cosmetics, street food, and souvenir shopping. Try hotteok (sweet pancake) from a street vendor."),
            ("17:30 – 19:00", "Early dinner. Try Samgyetang (삼계탕, ginseng chicken soup) — a traditional Korean summer dish believed to boost energy during hot weather. Samgyetang is served year-round but especially popular in July."),
            ("19:00 – 20:30", "Evening walk along Cheonggyecheon Stream (청계천). The illuminated stream is a popular evening stroll spot in Seoul. Rest your feet."),
        ],
    },
]

def day_card(d):
    items = "".join(f'<li><b>{t}</b>: {desc}</li>' for t, desc in d["schedule"])
    return f'''      <div id="day{d['id']}" class="day-card">
        <div class="day-header">
          <div class="day-title">{d['title']}</div>
          <div class="day-meta">
            <div class="meta-item" style="color:#d97706; background:#fffbeb; padding:2px 8px; border-radius:12px; font-weight:bold; border:1px solid #fef3c7;">{d['weather']}</div>
            <div class="meta-item"><i class="fa-solid fa-road"></i> {d['distance']}</div>
            <div class="meta-item"><i class="fa-solid fa-clock"></i> {d['time']}</div>
          </div>
        </div>

        <div class="history-box">{d['history']}</div>

        <div class="details-grid">
          <div class="detail-item">
            <span class="detail-label"><i class="fa-solid fa-camera"></i> Key Sights</span>
            {d['sights']}
          </div>
          <div class="detail-item">
            <span class="detail-label"><i class="fa-solid fa-bed"></i> Accommodation</span>
            <span style="color: #e11d48; font-weight: 500;">{d['hotel']}</span>
          </div>
          <div class="detail-item">
            <span class="detail-label"><i class="fa-solid fa-utensils"></i> Food</span>
            {d['food']}
          </div>
          <div class="detail-item">
            <span class="detail-label"><i class="fa-solid fa-clock"></i> Opening Hours</span>
            {d['hours']}
          </div>
        </div>

        <div class="schedule">
          <h4><i class="fa-solid fa-list-check"></i> Timeline</h4>
          <ul>{items}</ul>
        </div>
      </div>

'''

# Days 1-4
for d in days:
    html += day_card(d)

# Days 5-7: ICML Conference days in Seoul
days_567 = [
    {
        "id": 5,
        "title": "Day 5 (2025-07-07): ICML Day 1 — Conference & Seoul Evening",
        "weather": "🌤️ 26-32°C (Hot/Humid)",
        "distance": "Local (Myeongdong area)",
        "time": "Conference day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Seoul — Korea\'s Dynamic Capital</b><br>Seoul is a city of contrasts: 600 years of Joseon Dynasty palaces sit alongside glass skyscrapers and neon-lit streets. The city\'s six major royal palaces — Gyeongbokgung, Changdeokgung, Changgyeonggung, Deoksugung, Jongmyo, and Gyeonghuigung — form one of the world\'s greatest concentrations of pre-modern East Asian architecture. ICML 2025 brings the global ML community to Seoul, adding a modern layer to this ancient crossroads.',
        "sights": '🌟 ICML Conference Venue | 🌟 Gyeongbokgung Palace (evening option)',
        "hotel": '✅ Hotel Skypark Myeongdong 2, Seoul (Booked)',
        "food": 'ICML catering/workshop meals | Gwangjang Market for bibimbap and bindaetteok',
        "hours": '🌟 ICML: Full day (check schedule) | 🌟 Gyeongbokgung: 9:00–18:00 (free on Wed evenings)',
        "schedule": [
            ("08:30 – 09:00", "Breakfast at hotel. Head to ICML venue."),
            ("09:00 – 12:30", "ICML Day 1 — Keynote sessions, parallel talks. Check the conference app for your target papers and schedule."),
            ("12:30 – 14:00", "Lunch at ICML venue or nearby. Network with researchers from around the world."),
            ("14:00 – 17:30", "ICML Day 1 — Continued sessions, poster sessions. Visit posters in the afternoon slot."),
            ("17:30 – 19:00", "ICML Day 1 — Evening sessions or social hour. Attend the welcome reception if scheduled."),
            ("19:00 – 20:30", "Dinner at Gwangjang Market (광장시장). Try bibimbap, bindaetteok (mung bean pancake), and tteokbokki. One of Seoul's oldest and largest traditional markets."),
            ("20:30 – 21:30", "Return to hotel. Rest for tomorrow."),
        ],
    },
    {
        "id": 6,
        "title": "Day 6 (2025-07-08): ICML Day 2 — Conference & Cultural Excursion",
        "weather": "🌤️ 26-33°C (Hot/Humid)",
        "distance": "Local + Namsan",
        "time": "Conference day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Namsan — Seoul\'s Green Heart</b><br>Namsan (남산, "South Mountain") rises 262m above central Seoul and has been a cultural landmark for over 1,700 years. During the Three Kingdoms period it served as a defensive fortification; today it hosts Seoul Tower (N Seoul Tower), hiking trails, and open-air stages. The mountain\'s forested slopes provide a cool retreat from Seoul\'s summer heat island effect.',
        "sights": '🌟 ICML Conference Venue | 🌟 Namsan Seoul Tower (evening)',
        "hotel": '✅ Hotel Skypark Myeongdong 2, Seoul (Booked)',
        "food": 'ICML catering | Namsan dakgalbi (spicy stir-fried chicken)',
        "hours": '🌟 ICML: Full day | 🌟 Namsan Cable Car: 10:00–23:00 | Seoul Tower: 10:00–23:00',
        "schedule": [
            ("08:30 – 09:00", "Breakfast at hotel. Head to ICML venue."),
            ("09:00 – 12:30", "ICML Day 2 — Morning sessions. Focus on papers in your research area."),
            ("12:30 – 14:00", "Lunch and networking at ICML. Exchange contacts with potential collaborators."),
            ("14:00 – 17:30", "ICML Day 2 — Afternoon sessions and poster presentations."),
            ("17:30 – 19:00", "ICML Day 2 — Evening sessions or workshop wrap-up."),
            ("19:00 – 20:30", "Take the Namsan Cable Car (남산 케이블카) from Myeongdong to Seoul Tower. Evening views of the city lights are spectacular. Allow 1–1.5 hours at the top."),
            ("20:30 – 22:00", "Dinner in the Myeongdong area. Try dakgalbi (dakgalbi, spicy stir-fried chicken) at a restaurant in the Myeongdong/Namsan area."),
        ],
    },
    {
        "id": 7,
        "title": "Day 7 (2025-07-09): ICML Day 3 — Conference & Hanok Village",
        "weather": "🌤️ 25-31°C (Warm/Humid)",
        "distance": "Local + Bukchon",
        "time": "Conference day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Bukchon Hanok Village — Living History</b><br>Bukchon (북촌) is a traditional Korean hanok village nestled between Gyeongbokgung and Changdeokgung palaces. Over 900 hanok (traditional Korean houses) line the narrow streets, many still inhabited. The village was a residential area for Joseon-era aristocrats (yangban) and represents one of the best-preserved hanok communities in Seoul. Unlike museum villages, Bukchon is a living neighbourhood — visitors are asked to be respectful of residents.',
        "sights": '🌟 ICML Conference Venue | 🌟 Bukchon Hanok Village (afternoon)',
        "hotel": '✅ Hotel Skypark Myeongdong 2, Seoul (Booked)',
        "food": 'ICML catering | Bukchon traditional Korean cuisine',
        "hours": '🌟 ICML: Full day | 🌟 Bukchon Hanok Village: 24 hours (respectful visiting 9:00–18:00)',
        "schedule": [
            ("08:30 – 09:00", "Breakfast at hotel. Head to ICML venue."),
            ("09:00 – 12:30", "ICML Day 3 — Morning sessions. Last full day of main conference."),
            ("12:30 – 14:00", "Lunch and final networking at ICML. Collect business cards, follow up on conversations."),
            ("14:00 – 17:30", "ICML Day 3 — Afternoon sessions, closing ceremonies."),
            ("17:30 – 19:00", "Walk to Bukchon Hanok Village (북촌한옥마을). Explore the traditional streets between Gyeongbokgung and Changdeokgung. Visit a hanok cafe for tea."),
            ("19:00 – 20:30", "Dinner near Insadong (인사동). Try traditional Korean set meal (hanjeongsik) at a hanok restaurant. Insadong is also great for souvenir shopping."),
            ("20:30 – 21:30", "Return to hotel. Pack for tomorrow — Sokcho leg begins."),
        ],
    },
]

for d in days_567:
    html += day_card(d)

# Days 8-12: Sokcho & Seoraksan
days_89 = [
    {
        "id": 8,
        "title": "Day 8 (2025-07-10): ICML Day 4 → Sokcho — East Coast Journey",
        "weather": "🌤️ 24-30°C (Warm/Humid)",
        "distance": "~250km (KTX)",
        "time": "~3h transit",
        "history": '<i class="fa-solid fa-scroll"></i> <b>The East Coast — Sokcho & Seoraksan</b><br>Sokcho (속초) sits on Korea\'s East Sea coast at the foot of Seoraksan National Park (설악산), one of Korea\'s most dramatic mountain ranges. The park is famous for its jagged granite peaks, ancient temples carved into cliffs, and the contrast between mountain wilderness and coastal beauty. The name "Seoraksan" is said to derive from the Silla-era poet Choi Chi-won, who described its peaks as "snow-capped rocks" (설악).',
        "sights": '🌟 ICML Closing | 🌟 Sokcho Beach (속초해수욕장) | 🌟 Seoraksan National Park entrance',
        "hotel": '✅ Sokcho Hotel (Booked)',
        "food": 'Sokcho fresh squid and mackerel | Seoraksan temple food',
        "hours": '🌟 ICML: Morning | 🌟 Sokcho Beach: 24 hours (open) | Seoraksan: 6:00–18:00',
        "schedule": [
            ("08:30 – 09:00", "Breakfast at hotel. Final ICML morning session."),
            ("09:00 – 12:00", "ICML Day 4 — Final morning sessions, closing remarks. Collect conference materials and souvenirs."),
            ("12:00 – 13:00", "Lunch near ICML venue. Pack up and head to Seoul Station."),
            ("13:00 – 14:00", "KTX Seoul Station → Sokcho. Journey time ~2h 15min. Book in advance via Korail."),
            ("14:00 – 16:15", "Arrive Sokcho Station. Taxi to hotel (approx. 10 min, ₩8,000–12,000). Drop bags."),
            ("16:15 – 18:00", "Walk along Sokcho Beach (속초해수욕장). The East Sea coast is different from the South Sea — clearer water, rockier shoreline. Walk to the Sokcho Gate (속초대교) for sunset views."),
            ("18:00 – 19:30", "Dinner at Sokcho Beach area. Fresh squid (ojingeo) and mackerel (godeunghoe) sashimi. Sokcho is famous for its East Sea seafood."),
            ("19:30 – 21:00", "Evening stroll. Visit the Sokcho Night Market for street food and souvenirs."),
        ],
    },
    {
        "id": 9,
        "title": "Day 9 (2025-07-11): Seoraksan National Park — Full Day Hike",
        "weather": "🌤️ 20-28°C (Mild at altitude)",
        "distance": "~15km hiking",
        "time": "Full day (mountain)",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Seoraksan — Korea\'s Most Dramatic Peak</b><br>Seoraksan National Park (설악산국립공원) covers 41,500 hectares of granite peaks, deep valleys, and ancient temples. The mountain rises to 1,708m (Ulsanbawi Peak) and is divided into four areas: Seonginbong (West), Gwongeumseong (East), Dongwon (North), and Geumgang (Central). The Geumgang area — "Golden Valley" — is the most famous, with its towering granite monoliths and waterfalls. The park has been a sacred site since the Silla period, with over 20 temples scattered through its valleys.',
        "sights": '🌟 Seoraksan Geumgang Valley (금강권) | 🌟 Ulsanbawi Peak (울산바위) | 🌟 Seongcheonsa Temple (성천사)',
        "hotel": '✅ Sokcho Hotel (Booked)',
        "food": 'Seoraksan temple food (bapsang) | Sokcho dakgalbi',
        "hours": '🌟 Seoraksan: 6:00–18:00 (summer) | 🌟 Ulsanbawi Cable Car: 9:00–18:00 | Park entry: Free',
        "schedule": [
            ("06:30 – 07:30", "Early breakfast at hotel. Pack hiking essentials: water (2L+), snacks, rain jacket, sun protection."),
            ("07:30 – 08:30", "Taxi to Seoraksan National Park — Geumgang entrance (금강권 입구). Allow time for the park shuttle bus."),
            ("08:30 – 12:30", "Hike the Geumgang Valley trail (금강산 탐방로). The main loop from Seongcheonsa Temple through the golden valley to Ulsanbawi is approximately 8km one way. Steep sections with stone steps — allow 3–4 hours at a moderate pace."),
            ("12:30 – 13:30", "Lunch at a mountain restaurant near Ulsanbawi. Temple-style bapsang (set meal) available at Seongcheonsa."),
            ("13:30 – 15:30", "Continue the loop trail back through Geumgang Valley. Stop at waterfalls and granite rock formations. The return hike is slightly easier (downhill)."),
            ("15:30 – 16:30", "Return to park entrance. Rest at a nearby cafe."),
            ("16:30 – 17:30", "Return to hotel. Shower and rest — hiking Seoraksan is physically demanding in July heat."),
            ("17:30 – 19:00", "Dinner at Sokcho. Try dakgalbi (spicy stir-fried chicken) — a Gangwon Province specialty."),
            ("19:00 – 20:30", "Evening rest. Prepare for tomorrow — Naksansa temple visit."),
        ],
    },
]

for d in days_89:
    html += day_card(d)

# Days 10-12
days_1011 = [
    {
        "id": 10,
        "title": "Day 10 (2025-07-12): Naksansa Temple & Myeongji Falls — Coastal Monastery",
        "weather": "🌤️ 23-29°C (Warm/Humid)",
        "distance": "~40km coastal drive",
        "time": "Full day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Naksansa — Temple on the Cliff</b><br>Naksansa (낙산사) is a Buddhist temple perched on a cliff overlooking the East Sea, one of Korea\'s most photogenic temples. Founded in 671 AD during the Silla period, it sits at the easternmost point of the Samjokgul (Three Rocks Cave) pilgrimage route. The temple\'s main hall faces the sea, and on clear days you can see the small island of Naksan-do. The temple is also famous for its morning bell (beomjong), one of Korea\'s most beautiful temple bells.',
        "sights": '🌟 Naksansa Temple (낙산사) | 🌟 Myeongji Falls (명지폭포) | 🌟 Samjokgul Cave',
        "hotel": '✅ Sokcho Hotel (Booked)',
        "food": 'Naksansa temple meal | Sokcho fresh seafood',
        "hours": '🌟 Naksansa: 6:00–18:00 | 🌟 Myeongji Falls: 9:00–17:00 | Temple entry: Free',
        "schedule": [
            ("07:00 – 08:00", "Early breakfast at hotel. Pack day bag with water and snacks."),
            ("08:00 – 09:00", "Taxi to Naksansa Temple (낙산사). The coastal road from Sokcho is scenic — allow time for photos."),
            ("09:00 – 12:00", "Explore Naksansa Temple (낙산사). Walk the cliffside paths, visit the main hall facing the sea, see the ancient bell tower. The temple grounds offer panoramic East Sea views. Allow 2–3 hours."),
            ("12:00 – 13:00", "Lunch at a temple restaurant or nearby cafe. Temple food (bapsang) is simple but delicious."),
            ("13:00 – 14:30", "Visit Myeongji Falls (명지폭포). A 20m waterfall in a lush forest valley near Sokcho. Short hike from the parking area."),
            ("14:30 – 16:00", "Walk to Samjokgul (삼족굴, Three Rocks Cave). A sacred cave at the easternmost point of Korea\'s pilgrimage route. The cave is a natural rock formation with Buddhist carvings."),
            ("16:00 – 17:30", "Return to hotel. Rest and recover from the day's walking."),
            ("17:30 – 19:00", "Dinner at Sokcho. Try fresh East Sea sashimi (hoe) — squid, mackerel, and sea bream."),
            ("19:00 – 20:30", "Evening walk along Sokcho Beach. The East Sea coast is particularly beautiful at sunset."),
        ],
    },
    {
        "id": 11,
        "title": "Day 11 (2025-07-13): Sokcho Coastal Leisure — Beach & Hot Springs",
        "weather": "🌤️ 24-30°C (Warm/Humid)",
        "distance": "Local Sokcho area",
        "time": "Leisure day",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Sokcho — Where Mountains Meet the Sea</b><br>Sokcho is unique among Korean coastal cities for its dramatic setting: Seoraksan National Park rises directly behind the city, while the East Sea stretches to the east. The area is famous for its hot springs (oncheon), particularly in the nearby Yanggu and Sokcho areas. Korean oncheon culture dates back to the Goryeo Dynasty, with mineral-rich hot springs believed to have therapeutic properties. Sokcho\'s combination of mountain and sea makes it one of Korea\'s most beloved weekend destinations.',
        "sights": '🌟 Sokcho Beach | 🌟 Dongheon Hot Spring (동헌온천) | 🌟 Sokcho Art Museum',
        "hotel": '✅ Sokcho Hotel (Booked)',
        "food": 'Sokcho squid BBQ | East Sea mackerel soup | Oncheon eggs',
        "hours": '🌟 Sokcho Beach: 24 hours | 🌟 Dongheon Hot Spring: 10:00–22:00 | Sokcho Art Museum: 10:00–18:00',
        "schedule": [
            ("09:00 – 10:00", "Late breakfast at hotel. Enjoy a relaxed morning — last full day in Sokcho."),
            ("10:00 – 12:00", "Visit Sokcho Art Museum (속초미술관) or explore the local art galleries along Beach Road. The museum features contemporary Korean and international artists."),
            ("12:00 – 13:30", "Lunch at Sokcho Beach area. Try squid BBQ (ojingeo-gui) — a local specialty where you grill fresh squid at your table."),
            ("13:30 – 15:30", "Relax at Sokcho Beach. Swim in the East Sea (water temperature ~22°C in July) or simply lounge on the sand. The beach is clean and well-maintained."),
            ("15:30 – 17:30", "Visit a local oncheon (hot spring). Dongheon Oncheon (동헌온천) is one of Sokcho's most popular. Soak in mineral-rich waters after days of hiking."),
            ("17:30 – 19:00", "Return to hotel. Freshen up and rest."),
            ("19:00 – 20:30", "Farewell dinner at Sokcho. Try a full Korean seafood feast — hoe (sashimi platter), grilled mackerel, and oncheon eggs (계란) cooked in the hot spring water."),
            ("20:30 – 21:30", "Final evening walk along Sokcho Beach. Pack for tomorrow's departure."),
        ],
    },
    {
        "id": 12,
        "title": "Day 12 (2025-07-14): Sokcho → Incheon — Departure",
        "weather": "🌤️ 23-29°C (Warm/Humid)",
        "distance": "~400km (KTX + AREX)",
        "time": "~5h transit",
        "history": '<i class="fa-solid fa-scroll"></i> <b>Farewell Korea</b><br>Your 12-day journey through Korea has taken you from the ancient Silla capital of Gyeongju, through Busan\'s coastal energy, four conference days in Seoul, and the dramatic mountain-sea landscape of Sokcho. Korea\'s blend of ancient heritage and modern innovation makes it one of Asia\'s most rewarding destinations. As you depart, remember the warmth of Korean hospitality (jeong, 정) — the deep sense of connection and care that defines Korean social life.',
        "sights": '🌟 Sokcho Morning Market | 🌟 Last-minute souvenir shopping',
        "hotel": 'N/A — Departure day',
        "food": 'Sokcho breakfast | Incheon Airport duty-free',
        "hours": '🌟 Sokcho Market: 6:00–14:00 | 🌟 Incheon Airport: 24 hours',
        "schedule": [
            ("06:30 – 07:30", "Early breakfast at hotel. Check out and store luggage."),
            ("07:30 – 08:30", "Visit Sokcho Morning Market (속초시장) for last-minute souvenirs and fresh fruit. Try oncheon eggs (계란) boiled in the local hot spring water."),
            ("08:30 – 09:30", "Taxi to Sokcho Station."),
            ("09:30 – 12:00", "KTX Sokcho → Seoul. Journey time ~2h 15min. Book in advance via Korail."),
            ("12:00 – 13:00", "Transfer at Seoul Station to AREX platform. Grab lunch at Seoul Station food court."),
            ("13:00 – 14:00", "AREX Seoul Station → Incheon Airport. Express train takes ~35 min; regular takes ~43 min."),
            ("14:00 – 15:00", "Arrive Incheon Airport. Check in for departure flight, clear security and immigration."),
            ("15:00 – 16:30", "Duty-free shopping at Incheon Airport. Korean cosmetics, ginseng, and traditional snacks make great souvenirs."),
            ("16:30 – 17:30", "Board departure flight. Safe travels home!"),
        ],
    },
]

for d in days_1011:
    html += day_card(d)

# Key Notes section
html += '''      <div id="notes" class="note-box">
        <h3><i class="fa-solid fa-circle-info"></i> Key Notes & Practical Tips</h3>
        <ul style="margin: 0; padding-left: 20px;">
<li><b>Transport:</b> Purchase a T-money card at Incheon Airport for all local transit (subway, bus, taxi). For KTX intercity travel, book via Korail (www.letskorail.com) or the Korail Talk app — July is peak season and trains sell out.</li>
<li><b>Weather:</b> July is the height of Korea's summer monsoon (jangma, 장마). Expect high humidity (80%+), temperatures 25–33°C, and frequent afternoon thunderstorms. Pack a lightweight rain jacket, umbrella, and quick-dry clothing.</li>
<li><b>Connectivity:</b> Purchase a Korean SIM card or eSIM at Incheon Airport (KT, SK Telecom, LG U+). Alternatively, rent a WiFi egg from the airport. Free WiFi is available at most cafes and subway stations.</li>
<li><b>Currency:</b> Korean Won (KRW). ATMs are widely available at subway stations and convenience stores. Credit cards are accepted almost everywhere, but carry cash (₩10,000–20,000 notes) for small restaurants and markets.</li>
<li><b>Tax Refund:</b> Non-Korean residents can claim VAT refunds (about 6%) on purchases over ₩30,000 at participating stores. Look for the "Tax Free" sign. Keep receipts and present them at the airport before departure.</li>
<li><b>Emergency Numbers:</b> Police: 112 | Ambulance/Fire: 119 | Tourist Hotline: 1330 (English, Chinese, Japanese). Your embassy's emergency number should be saved in your phone.</li>
<li><b>Packing:</b> Light, breathable clothing (cotton/linen), comfortable walking shoes for temple/mountain visits, sunscreen (SPF 50+), portable fan or cooling towel, power adapter (Korea uses Type C/F, 220V), portable power bank.</li>
<li><b>ICML Prep:</b> Download the ICML conference app in advance. Review the accepted paper list and create your personal schedule. Print or save a copy of your presentation materials as backup.</li>
<li><b>Hiking:</b> Seoraksan trails are well-maintained but steep. Start early (before 8am) to avoid midday heat and afternoon rain. Carry at least 2L of water per person. Trail conditions can be slippery after rain.</li>
<li><b>Dining:</b> Korean restaurants typically serve rice and soup with meals. Most menus have English translations in tourist areas. Tipping is not expected or customary.</li>
        </ul>
      </div>

    </div>
  </div>
</div>

<button class="fab" id="fabBtn"><i class="fa-solid fa-bars"></i></button>

<script>
  // Mobile menu toggle
  const fabBtn = document.getElementById('fabBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileOverlay = document.getElementById('mobileOverlay');
  const closeMenuBtn = document.getElementById('closeMenuBtn');

  function openMenu() { mobileMenu.classList.add('open'); mobileOverlay.style.display = 'block'; }
  function closeMenu() { mobileMenu.classList.remove('open'); mobileOverlay.style.display = 'none'; }

  fabBtn.addEventListener('click', openMenu);
  closeMenuBtn.addEventListener('click', closeMenu);
  mobileOverlay.addEventListener('click', closeMenu);

  // Close menu when a nav link is clicked
  document.querySelectorAll('#mobile-nav a').forEach(a => {
    a.addEventListener('click', closeMenu);
  });

  // Active nav highlighting on scroll
  const sections = document.querySelectorAll('.day-card, .note-box');
  const navLinks = document.querySelectorAll('#desktop-nav a, #mobile-nav a');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (pageYOffset >= sectionTop - 100) {
        current = section.getAttribute('id');
      }
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });

  // Print handler
  window.addEventListener('beforeprint', () => {
    document.body.style.fontSize = '12pt';
  });
</script>

</body>
</html>'''

with open('/Users/rdu/Documents/korea-trip/tour_package.html', 'w') as f:
    f.write(html)

print("tour_package.html written successfully")
print(f"File size: {len(html)} bytes")
