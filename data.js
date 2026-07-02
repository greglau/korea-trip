const itineraryData = [
  {
    day: 1,
    date: "2025-07-03",
    title: "Gyeongju — Arrival & Tomb Complex",
    distance: "~380km (KTX from Incheon/Seoul)",
    time: "~2h15m transit",
    sights: "<b>Daereungwon Tomb Complex (대릉원).</b><br><br>The 23 massive grass tumuli of the Silla kingdom. These are not ruins but smooth, intact mounds, each 12–22m high, rising from the suburban streetscape. The interior of Cheonmachong (천마총) is open to visitors — a royal tomb filled with extraordinary gold artifacts discovered in 1973. Walk the full perimeter (approx. 1–1.5 hrs). Very flat, very relaxing.<br><br><b>Hwangridan-gil Street (황리단길).</b> The commercial alley just east of the tombs has good coffee shops and hanok-style boutiques. Great for late afternoon wandering at your own pace.<br><br><b>Donggung Palace & Wolji Pond (동궁과 월지).</b> The ancient royal retreat beautifully illuminated across the water. Spectacular at night — a 10–15 min walk from Hwangridan-gil. Free entry.",
    accommodation: "Gyeongju Hanok Guesthouse (e.g., Gyeongju Ran Hanok or similar). Traditional hanok compound with ondol rooms, steps from Daereungwon.<br><a href='https://www.trip.com/' target='_blank'>Trip.com Booking</a>",
    food: "<b>Lunch:</b> Bento box or snacks at Seoul Station for the train.<br><b>Dinner:</b> Hwangnam-ppang (황남빵) at Choi Yeonghwa Ppang — the original red bean bun shop. Buy warm ones to eat while walking.",
    practical: "Get a T-money card at Incheon Airport. Top up ₩50,000.<br>Flight lands ~10:00 AM. By the time you clear immigration, get bags, and take AREX to Seoul Station, it will be ~12:30 PM. Catch a 1:00–1:30 PM KTX, arriving Singyeongju Station around 3:30 PM.<br>Gyeongju has no subway. Use local city buses (Naver Maps handles Korean bus routing well) or taxis, which are inexpensive.<br>Daereungwon is only a 10–15-minute walk from most guesthouses in central Gyeongju.",
    spots: [
      { name: "Incheon Airport (인천공항)", type: "waypoint", lat: 37.4602, lng: 126.4407 },
      { name: "Daereungwon Tomb Complex (대릉원)", type: "sight", lat: 35.8297, lng: 129.2264 },
      { name: "Hwangridan-gil Street (황리단길)", type: "sight", lat: 35.8320, lng: 129.2310 },
      { name: "Donggung Palace & Wolji Pond (동궁과 월지)", type: "sight", lat: 35.8270, lng: 129.2240 },
      { name: "최영화빵 (Choi Yeonghwa Ppang)", type: "restaurant", lat: 35.8310, lng: 129.2280 },
      { name: "Gyeongju Hanok Guesthouse", type: "hotel", lat: 35.8280, lng: 129.2270 }
    ]
  },
  {
    day: 2,
    date: "2025-07-04",
    title: "Gyeongju → Busan — UNESCO Sites & Market Culture",
    distance: "~70km (KTX)",
    time: "2h transit",
    sights: "<b>Morning: Bulguksa Temple (불국사) & Seokguram Grotto (석굴암).</b><br><br>Start by 9:00am. Bus 10 or 11 out to Bulguksa Temple, then catch the shuttle up the mountain to Seokguram Grotto. Seokguram viewings are timed in slots of about 10 minutes each; peak July crowds mean waiting is likely. Go straight there.<br><br><b>Afternoon: Toyoko Inn Jungang Station check-in.</b><br><br><b>Jagalchi Market (자갈치시장).</b> Korea's largest seafood market. Walk the multi-level building, watch live fish and shellfish being sold, see the auction floor. You can have your selection cooked to order at restaurants on the upper floors.<br><br><b>BIFF Square (비프광장).</b> Historic square with street food, movie posters from the Busan International Film Festival. Try the ssiat hotteok (sweet seed-filled pancakes).",
    accommodation: "Toyoko Inn Busan Jungang Station (東京堂인釜山中央駅). Right on Line 1 subway station. Clean, reliable Japanese chain — no-frills but functional and well-located for transit.<br><a href='https://www.trip.com/' target='_blank'>Trip.com Booking</a>",
    food: "<b>Lunch:</b> Quick lunch in Gyeongju after Seokguram (~1:00 PM).<br><b>Dinner:</b> Ssiat hotteok (sweet seed-filled pancakes) at BIFF Square street stalls.",
    practical: "KTX from Singyeongju to Busan takes only 30 minutes — one of the shortest intercity train journeys in Korea. Book via Korail.<br>Busan subway is excellent and covers all the main sites in Nampo-dong (2 stops from Jungang Station).<br>Toyoko Inn Jungang Station is directly on Line 1 — perfect for hopping to Jagalchi Market (5 min) or Busan Station for KTX.",
    spots: [
      { name: "Singyeongju Station (KTX departure)", type: "waypoint", lat: 35.8200, lng: 129.2100 },
      { name: "Bulguksa Temple (불국사)", type: "sight", lat: 35.8082, lng: 129.3337 },
      { name: "Seokguram Grotto (석굴암)", type: "sight", lat: 35.8297, lng: 129.3460 },
      { name: "Jagalchi Market (자갈치시장)", type: "sight", lat: 35.1480, lng: 129.0600 },
      { name: "BIFF Square (비프광장)", type: "sight", lat: 35.1470, lng: 129.0580 },
      { name: "Toyoko Inn Busan Jungang", type: "hotel", lat: 35.1470, lng: 129.0560 }
    ]
  },
  {
    day: 3,
    date: "2025-07-05",
    title: "Busan → Seoul — Coastal Leisure & SRT to COEX",
    distance: "~450km (SRT)",
    time: "Late-night transit (~7pm–9:30pm)",
    sights: "<b>Morning: Haedong Yonggungsa Temple (해동용궁사).</b><br><br>One of the few temples in Korea built right on the coastline. The main hall sits on a rocky outcrop with waves crashing below — stunning views and peaceful atmosphere.<br><br><b>Afternoon: Haeundae Beach (해운대해수욕장).</b> Busan's most famous beach. Gentle coastal walk, refreshing dip if you dare (it's cold!). Crystal clear water in July.<br><br><b>Haeundae Sky Capsule.</b> Must be booked weeks in advance. A miniature capsule train that runs along the coast — unique photo opportunity.<br><br><b>Evening: SRT to Seoul.</b><br><br>Take a ~7:00 PM SRT from Busan to Suseo Station (arrive ~9:30 PM). Suseo is in Gangnam, just a 10-minute taxi ride to Grand Intercontinental COEX. Check in, drop bags, rest.",
    accommodation: "Grand Intercontinental Seoul COEX (그랜드 인터컨티넨탈 서울 코엑스). Right at the conference venue. Ultra-convenient for ICML days.<br><a href='https://www.trip.com/' target='_blank'>Trip.com Booking</a>",
    food: "<b>Lunch:</b> Haeundae Beach area — seafood restaurants along the coast.<br><b>Dinner:</b> Light meal at Busan Station or SRT onboard. COEX area for dinner after arrival.",
    practical: "Check out of Toyoko Inn by 10:00 AM. Take the subway to Busan Station and lock your luggage in the coin lockers.<br>Book SRT (not KTX) from Busan to Suseo — same travel time (~2h30m), but drops you in Gangnam, a 10-min taxi from COEX. Saves 45–60 min subway ride with luggage.<br>Express bus or subway from Jungang Station area to East Busan (~30 min).<br>Haeundae Sky Capsule: must be booked weeks in advance.",
    spots: [
      { name: "Haedong Yonggungsa Temple (해동용궁사)", type: "sight", lat: 35.1640, lng: 129.1820 },
      { name: "Haeundae Beach (해운대해수욕장)", type: "sight", lat: 35.1680, lng: 129.1640 },
      { name: "Busan Station (SRT departure)", type: "waypoint", lat: 35.1540, lng: 129.0570 },
      { name: "Suseo Station (SRT arrival)", type: "waypoint", lat: 37.5480, lng: 127.1460 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 4,
    date: "2025-07-06",
    title: "ICML Day 1 — Temple Lunch Escape",
    distance: "Subway to Gangnam",
    time: "Conference day",
    sights: "<b>COEX Convention Centre (코엑스 컨벤션센터).</b><br><br>Monday 7 – Thursday 10 July — ICML Conference at COEX, Gangnam. Technical sessions and networking.<br><br><b>Lunch Break Escape: Bongeunsa Temple (봉은사).</b> Across Yeongdong-daero from COEX, 5-min walk. The 23m standing Maitreya Buddha in stone, the cedar forest path behind the main halls. Free entry.<br><br><b>Evening: Ikseon-dong (익선동).</b> Narrow alleys behind Changdeokgung Palace, converted hanok buildings housing craft tea shops, makgeolli (rice wine) bars, and small restaurants. Very atmospheric at dusk.",
    accommodation: "Grand Intercontinental Seoul COEX (continued)",
    food: "<b>Lunch:</b> COEX underground mall — naengmyeon (cold noodles) or bibimbap options.<br><b>Dinner:</b> Makgeolli + pancakes (makgeolli + bindaetteok) at an Ikseon-dong hanok bar.",
    practical: "Subway Line 2 from COEX area to Ikseon-dong (Anguk Station) takes ~30 min. Book in advance via Korail — July is peak season.<br>Naver Maps is essential for Seoul navigation. Kakao Maps also excellent.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Bongeunsa Temple (봉은사)", type: "sight", lat: 37.5048, lng: 127.0396 },
      { name: "Ikseon-dong Makgeolli Bars", type: "restaurant", lat: 37.5740, lng: 126.9950 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 5,
    date: "2025-07-07",
    title: "ICML Day 2 — Temple Lunch Escape",
    distance: "Subway to Gangnam",
    time: "Conference day",
    sights: "<b>COEX Convention Centre (코엑스 컨벤션센터).</b><br><br>Monday 7 – Thursday 10 July — ICML Conference at COEX, Gangnam. Technical sessions and networking.<br><br><b>Lunch Break Escape: Bongeunsa Temple (봉은사).</b> Across Yeongdong-daero from COEX, 5-min walk. The 23m standing Maitreya Buddha in stone, the cedar forest path behind the main halls. Free entry.",
    accommodation: "Grand Intercontinental Seoul COEX (continued)",
    food: "<b>Lunch:</b> COEX underground mall — naengmyeon (cold noodles) or bibimbap options.<br><b>Dinner:</b> COEX area or Apgujeong-dong.",
    practical: "Subway Line 2 from COEX area. Naver Maps is essential for Seoul navigation.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Bongeunsa Temple (봉은사)", type: "sight", lat: 37.5048, lng: 127.0396 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 6,
    date: "2025-07-08",
    title: "ICML Day 3 — Temple Lunch Escape",
    distance: "Subway to Gangnam",
    time: "Conference day",
    sights: "<b>COEX Convention Centre (코엑스 컨벤션센터).</b><br><br>Monday 7 – Thursday 10 July — ICML Conference at COEX, Gangnam. Technical sessions and networking.<br><br><b>Lunch Break Escape: Bongeunsa Temple (봉은사).</b> Across Yeongdong-daero from COEX, 5-min walk. The 23m standing Maitreya Buddha in stone, the cedar forest path behind the main halls. Free entry.",
    accommodation: "Grand Intercontinental Seoul COEX (continued)",
    food: "<b>Lunch:</b> COEX underground mall — naengmyeon (cold noodles) or bibimbap options.<br><b>Dinner:</b> COEX area or Apgujeong-dong.",
    practical: "Subway Line 2 from COEX area. Naver Maps is essential for Seoul navigation.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Bongeunsa Temple (봉은사)", type: "sight", lat: 37.5048, lng: 127.0396 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 7,
    date: "2025-07-09",
    title: "ICML Day 4 — Temple Lunch Escape",
    distance: "Subway to Gangnam",
    time: "Conference day",
    sights: "<b>COEX Convention Centre (코엑스 컨벤션센터).</b><br><br>Monday 7 – Thursday 10 July — ICML Conference at COEX, Gangnam. Technical sessions and networking.<br><br><b>Lunch Break Escape: Bongeunsa Temple (봉은사).</b> Across Yeongdong-daero from COEX, 5-min walk. The 23m standing Maitreya Buddha in stone, the cedar forest path behind the main halls. Free entry.",
    accommodation: "Grand Intercontinental Seoul COEX (continued)",
    food: "<b>Lunch:</b> COEX underground mall — naengmyeon (cold noodles) or bibimbap options.<br><b>Dinner:</b> COEX area or Apgujeong-dong.",
    practical: "Subway Line 2 from COEX area. Naver Maps is essential for Seoul navigation.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Bongeunsa Temple (봉은사)", type: "sight", lat: 37.5048, lng: 127.0396 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 8,
    date: "2025-07-10",
    title: "ICML Final Day — Wrap-Up",
    distance: "Subway to Gangnam",
    time: "Conference day",
    sights: "<b>COEX Convention Centre (코엑스 컨벤션센터).</b><br><br>Final conference day. Wrap sessions, collect luggage — your COEX hotel can store bags while you finish.<br><br><b>Starfield Library (스타필드 코엑스 아카이브).</b> Inside COEX mall. The iconic multi-story bookshelf. Free, photogenic, 15 minutes.<br><br><b>COEX Underground Mall.</b> Final food shopping and last-minute souvenir browsing.",
    accommodation: "Grand Intercontinental Seoul COEX (final night at COEX)",
    food: "<b>Lunch:</b> COEX underground mall.<br><b>Dinner:</b> Upscale Korean in Apgujeong-dong or COEX area.",
    practical: "This is a lighter day — conference wraps early. Use the afternoon for final sightseeing or shopping.<br>COEX underground mall connects directly to the subway — useful for quick lunch runs.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Starfield Library (스타필드 코엑스)", type: "sight", lat: 37.5120, lng: 127.0580 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 9,
    date: "2025-07-11",
    title: "Seoul — Rest & Recovery Day",
    distance: "Walking / Subway",
    time: "Free day",
    sights: "<b>Rest & Recovery.</b><br><br>A lighter day after 4 conference days. Sleep in, enjoy the hotel amenities, or take a gentle walk around COEX/Starfield Mall.<br><br><b>Optional: Gangnam District Exploration.</b> Apgujeong-dong for high-end shopping, Cheongdam-dong for K-beauty stores and cafes. Or stay local — COEX has excellent dining and the Starfield Library is worth another visit.",
    accommodation: "Grand Intercontinental Seoul COEX (continued)",
    food: "<b>Breakfast:</b> Hotel buffet or COEX dining.<br><b>Lunch:</b> COEX underground mall or Apgujeong-dong.<br><b>Dinner:</b> Upscale Korean in Gangnam area.",
    practical: "This is a recovery day — no fixed schedule. Use it to rest, explore Gangnam at your own pace, or prepare for the move north of the river tomorrow.<br>Check out of COEX on Jul 12 morning.",
    spots: [
      { name: "COEX Convention Centre", type: "sight", lat: 37.5126, lng: 127.0590 },
      { name: "Apgujeong-dong (압구정동)", type: "sight", lat: 37.5270, lng: 127.0280 },
      { name: "Grand Intercontinental COEX", type: "hotel", lat: 37.5126, lng: 127.0590 }
    ]
  },
  {
    day: 10,
    date: "2025-07-12",
    title: "Seoul — Secret Garden & Gritty Alleys",
    distance: "Walking / Subway",
    time: "Full day",
    sights: "<b>Morning: Changdeokgung Palace (창덕궁) — Huwon (Secret Garden).</b><br><br>Guided tour of the Secret Garden. Requires ADVANCE BOOKING online at cdg.go.kr/english — strict daily cap of 100 visitors per time slot. The Secret Garden (Huwon) is a private royal retreat of pavilions and lotus ponds set in natural forest. Anguk Station, Line 3. Allow 2.5 hours total.<br><br><b>Afternoon: Ikseon-dong Hanok Village (익선동).</b> Narrow, zigzagging alleys filled with artisan shops. Stop at a teahouse and wander the converted hanok buildings.<br><br><b>Evening: Euljiro (을지로) — 'Hip-jiro.'</b> Chaotic alleyways outside the old printing shops. Cold draft beer, spicy pork, and fried garlic chicken. Gritty, authentic Seoul nightlife.",
    accommodation: "Boutique Hotel / Hanok Guesthouse in Jongno or Anguk neighborhood (e.g., near Anguk Station, Line 3). Traditional Seoul experience.<br><a href='https://www.trip.com/' target='_blank'>Trip.com Booking</a>",
    food: "<b>Lunch:</b> Light meal near Changdeokgung or Ikseon-dong.<br><b>Dinner:</b> Euljiro — cold draft beer, spicy pork (dwaeji bulgogi), and fried garlic chicken in the printing shop alleyways.",
    practical: "BOOK Changdeokgung Secret Garden slots now — they release exactly 6 days in advance online and sell out instantly.<br>Check out of Grand Intercontinental COEX by 10:00 AM. Take a taxi north of the Han River to your Jongno/Anguk hotel (~30 min). Drop bags.<br>Euljiro: Line 2 to Euljiro 1-ga Station. The alleyways are behind the old printing shops — look for the narrow lanes with outdoor tables.",
    spots: [
      { name: "Changdeokgung Palace (창덕궁)", type: "sight", lat: 37.5796, lng: 127.0080 },
      { name: "Changdeokgung Secret Garden (후원)", type: "sight", lat: 37.5820, lng: 127.0100 },
      { name: "Ikseon-dong Hanok Village (익선동)", type: "sight", lat: 37.5740, lng: 126.9950 },
      { name: "Euljiro 'Hip-jiro' (을지로)", type: "sight", lat: 37.5640, lng: 126.9800 },
      { name: "Jongno/Anguk Boutique Hotel", type: "hotel", lat: 37.5800, lng: 126.9900 }
    ]
  },
  {
    day: 11,
    date: "2025-07-13",
    title: "Seoul — Premium Wagyu & The City Wall",
    distance: "Walking / Subway",
    time: "Full day",
    sights: "<b>Morning: Majang Meat Market (마장도축시장).</b><br><br>Walk the ground-floor stalls, buy a beautiful cut of 1++ grade Hanwoo beef, and take it upstairs to a grill restaurant for a heavy, world-class lunch. This is where Seoul locals buy their premium beef.<br><br><b>Afternoon: Inwangsan City Wall (인왕산 성곽).</b> Begin the hike up from the base of Inwangsan as the sun begins to set. Reach the viewing points for perfect juxtaposition of the ancient stone fortress against the hyper-modern Seoul skyline.<br><br><b>Evening: Gwangjang Market (광장시장).</b> Sit at the center stalls for freshly fried mung bean pancakes (bindaetteok) and makgeolli. Netflix-featured stalls.",
    accommodation: "Boutique Hotel / Hanok Guesthouse in Jongno or Anguk neighborhood (final night)",
    food: "<b>Breakfast:</b> Coffee and pastry at a cafe around Anguk Station (e.g., Onion or Cafe Layered).<br><b>Lunch:</b> Majang Meat Market — 1++ grade Hanwoo beef, grilled at the restaurant upstairs.<br><b>Dinner:</b> Gwangjang Market — bindaetteok (mung bean pancakes) and makgeolli.",
    practical: "Majang Meat Market: Subway to Majang Station (Line 4). Allow 1.5–2 hours for the full experience.<br>Inwangsan City Wall: Start hiking around 3:30–4:00 PM for sunset views. N Seoul Tower is visible from the wall — great photo opportunity.<br>Gwangjang Market: 5-min walk from Jongno 5-ga Station (Lines 1, 3, 5). Arrive by 7:00 PM for the best atmosphere.",
    spots: [
      { name: "Majang Meat Market (마장도축시장)", type: "sight", lat: 37.6010, lng: 127.0350 },
      { name: "Inwangsan City Wall (인왕산 성곽)", type: "sight", lat: 37.5900, lng: 126.9780 },
      { name: "Gwangjang Market (광장시장)", type: "sight", lat: 37.5670, lng: 127.0090 },
      { name: "Jongno/Anguk Boutique Hotel", type: "hotel", lat: 37.5800, lng: 126.9900 }
    ]
  },
  {
    day: 12,
    date: "2025-07-14",
    title: "Seoul — Departure Day",
    distance: "~50km (AREX)",
    time: "~45 min transit",
    sights: "<b>Morning: Cheonggyecheon Stream (청계천).</b><br><br>A final morning walk along the sunken stream, right in the heart of the city. Peaceful, green, and a unique urban oasis.<br><br><b>Midday: AREX to Incheon Airport.</b><br><br>Check out of hotel and head to Seoul Station. Board the dedicated AREX Express Train at ~12:30 PM.<br><br><b>Afternoon: Incheon Airport.</b><br><br>Arrive at ICN by ~1:15 PM. Three and a half hours before your 4:45 PM flight to clear security, explore the massive terminals, and relax in the lounge.",
    accommodation: "— Departure day —",
    food: "<b>Breakfast:</b> Coffee and pastry near your hotel or at Seoul Station.<br><b>Lunch:</b> Incheon Airport T1 departures hall — excellent food options, Korean and international.",
    practical: "Cheonggyecheon Stream runs from Seoul Station area eastward — easy walk from most Jongno hotels.<br>AREX Seoul → Incheon takes ~43 min. Reserved seat recommended. ₩9,500.<br>Singapore Airlines check-in opens 3 hours before departure (13:45 for your 16:45 flight). Incheon is large but efficient — allow 90 minutes from arrival to airside.",
    spots: [
      { name: "Cheonggyecheon Stream (청계천)", type: "sight", lat: 37.5690, lng: 126.9800 },
      { name: "Seoul Station (AREX departure)", type: "waypoint", lat: 37.5545, lng: 126.9706 },
      { name: "Incheon Airport T1 (인천공항 T1)", type: "waypoint", lat: 37.4602, lng: 126.4407 }
    ]
  }
];

// REMOVED/ALTERNATIVE ITINERARY — what we left out from the original v1
const removedItinerary = [
  {
    day: "V1-Day 2",
    title: "Seoraksan Ridge Hike (REMOVED)",
    reason: "808 iron stairs + ridge trail = unsustainable in July heat for solo travel",
    original_sights: "<b>Ulsanbawi Rock (울산바위).</b><br>The iconic granite monolith with 808 iron stairs to the summit. Steep, exposed, no shade.<br><br><b>Gwongeumseong Fortress (관음성).</b> Cliff-top fortress ruins on the ridge trail. Requires full-day commitment.<br><br><b>Ridge Trail (능선길).</b> Connects Ulsanbawi to Seongiamsa Temple — 6+ hours of continuous uphill/downhill hiking.",
    alternative: "N/A — Seoraksan/Sokcho completely removed from itinerary in favor of Seoul cultural exploration.",
    transport: "Express bus from Dong Seoul Bus Terminal to Sokcho (3h). Local bus #7 to Seoraksan entrance.",
    hotel_original: "Seoraksan Guesthouse near Gwongeumseong entrance",
    hotel_current: "N/A — eliminated from route"
  },
  {
    day: "V1-Day 3",
    title: "Andong Hahoe Village (REMOVED)",
    reason: "Backtracking — Seoul → Andong → Seoul adds 6+ hours of transit for minimal unique value vs Gyeongju",
    original_sights: "<b>Hahoe Folk Village (하회마을).</b> UNESCO World Heritage. Traditional yangban village with stilt houses along the river. Mask dance performances.<br><br><b>Buyeo Palace (부용정).</b> Pavilion on the Nakdong River, iconic photo spot.<br><br><b>Pungyang Nongyo Mask Dance.</b> Traditional performance (seasonal).",
    alternative: "<b>Gyeongju instead:</b> Same UNESCO-level historical depth (Silla kingdom tombs, temples) with zero backtracking. Gyeongju is more walkable and has better food scene.",
    transport: "KTX Seoul → Andong (1h45m). Andong → Seoul (1h45m) — round trip = 3.5h transit for one day.",
    hotel_original: "Andong Hanok Stay near Hahoe Village",
    hotel_current: "N/A — eliminated from route"
  },
  {
    day: "V1-Day 4",
    title: "Naksansa Temple & Towangseong Falls (REMOVED)",
    reason: "Redundant with Seoraksan day — same mountain area, adds transit complexity",
    original_sights: "<b>Naksansa Temple (낙산사).</b> Cliffside temple overlooking the East Sea. Historic temple with mountain backdrop.<br><br><b>Towangseong Falls (토왕성폭포).</b> Waterfall valley trail — moderate hike through forest.",
    alternative: "N/A — Naksansa Temple also removed. Seoul cultural exploration provides richer historical depth.",
    transport: "Local bus #7 from Sokcho to Naksansa (30 min). Falls require 1h round-trip hike.",
    hotel_original: "Sokcho guesthouse near Naksansa",
    hotel_current: "N/A — eliminated from route"
  },
  {
    day: "V1-Day 5-8",
    title: "Conference Days (UNCHANGED)",
    reason: "",
    original_sights: "<b>ICML at COEX, Gangnam.</b><br>Monday 7 – Thursday 10 July — same as current itinerary.",
    alternative: "Identical to current plan. No changes needed.",
    transport: "Subway Line 2 to COEX Station (Yeoksam). Walking from hotel.",
    hotel_original: "Grand Intercontinental Seoul COEX",
    hotel_current: "Grand Intercontinental Seoul COEX (unchanged)"
  }
];

// TRANSPORT & HOTEL SUMMARY
const routeSummary = {
  transport: [
    { segment: "Incheon → Seoul", method: "AREX (Airport Railroad)", duration: "~43 min", cost: "₩9,500" },
    { segment: "Seoul → Gyeongju", method: "KTX (high-speed rail)", duration: "~2h15m", cost: "₩60,000–75,000" },
    { segment: "Gyeongju → Busan", method: "KTX (high-speed rail)", duration: "~30 min", cost: "₩18,000–25,000" },
    { segment: "Busan → Seoul", method: "SRT (Super Rapid Train)", duration: "~2h30m", cost: "₩65,000–80,000" },
    { segment: "Seoul → Incheon", method: "AREX (Airport Railroad)", duration: "~43 min", cost: "₩9,500" }
  ],
  hotels: [
    { nights: "Night 1", location: "Gyeongju (central)", hotel: "Gyeongju Hanok Guesthouse", reason: "Traditional hanok experience, walking distance to Daereungwon." },
    { nights: "Night 2", location: "Busan (Jungang Station)", hotel: "Toyoko Inn Busan Jungang Station", reason: "Right on Line 1 subway. Walking distance to Jagalchi Market & BIFF Square." },
    { nights: "Nights 3–8", location: "Seoul (Gangnam/COEX)", hotel: "Grand Intercontinental Seoul COEX", reason: "Right at the conference venue. Ultra-convenient for ICML days (Jul 5–12)." },
    { nights: "Nights 9–10", location: "Seoul (Jongno/Anguk)", hotel: "Boutique Hotel / Hanok Guesthouse", reason: "Traditional Seoul experience. Walking distance to Changdeokgung, Bukchon, Gwangjang Market." },
    { nights: "Night 11", location: "Incheon Airport area", hotel: "N/A — AREX from Seoul Station, depart 16:45", reason: "No overnight needed. AREX at ~12:30 PM, arrive ICN by 1:15 PM." }
  ],
  removed_items: [
    { item: "Seoraksan Ridge Hike (Ulsanbawi + 808 stairs)", reason: "Unsustainable in July heat for solo travel", saved_time: "~6 hours hiking" },
    { item: "Andong Hahoe Village", reason: "Backtracking adds 3.5h transit for minimal unique value vs Gyeongju", saved_time: "~7 hours total (transit + visit)" },
    { item: "Naksansa Temple & Towangseong Falls", reason: "Redundant with Seoraksan area; adds transit complexity", saved_time: "~4 hours (transit + hike)" },
    { item: "Sokcho", reason: "Long transit (4h each way) for minimal unique value vs Seoul cultural exploration. Better departure logistics staying in Seoul.", saved_time: "~8 hours transit + 2 nights hotel" }
  ]
};
