# 🎮 Temple Dash 3D

Endless runner game — *bhaago, sikke toplao, gundo se laddo!*

## Architecture

```
🎮 Temple Dash (Three.js, single index.html)
        ↓
📦 GitHub Pages  →  Game / Frontend (hosting)
        ↓
☁️ Supabase     →  Backend
   ├─ Login / Signup (email + password)
   ├─ Coins
   ├─ Score
   └─ Leaderboard
```

## Features

- 🔐 Login / Signup (Supabase Auth) — guest mode bhi hai
- ☁️ Cloud save — best score, kills, achievements, coins sab online
- 🏆 Top 10 leaderboard
- 📱 Mobile (touch) + desktop (mouse/keyboard) dono chalta hai

## Play

Khelne ke liye GitHub Pages link kholo — bas wahi run game hai jo APK me hai.

## Tech

- Three.js 3D endless runner
- Supabase JS SDK (inline, koi CDN dependency nahi)
- Har game ka record `game_events` me, player stats `players` table me
