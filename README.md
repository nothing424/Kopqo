# Kopqo AI

A free AI platform with 5 powerful modules — no login, no limits, premium futuristic UI.

## Features

| Module | Description |
|--------|-------------|
| **Chat AI** | ChatGPT-style assistant powered by DeepSeek. Persistent history via localStorage. |
| **App Generator** | Generate full website or app code from a text prompt. Copy or download. |
| **Prompt Generator** | Transform rough ideas into structured, optimized AI prompts. |
| **Image AI** | Generate logos, banners, wallpapers, and UI concepts with style presets. |
| **File Upload AI** | Upload images or text files and get instant AI analysis. |

## Running Locally

### Option A — Python (recommended, no install needed)

```bash
python server.py
```

Opens at **http://localhost:8080** automatically.

To use a different port:
```bash
python server.py 3000
```

### Option B — VS Code Live Server

Install the **Live Server** extension, right-click `index.html`, select **Open with Live Server**.

### Option C — Node.js (npx)

```bash
npx serve .
```

## File Structure

```
kopqo-ai/
├── index.html          # Home page
├── server.py           # Python local server
├── css/
│   └── style.css       # Full design system
├── js/
│   └── main.js         # Shared utilities (toast, copy, nav)
└── pages/
    ├── chat.html        # Chat AI
    ├── generator.html   # App / Web Generator
    ├── prompt.html      # Prompt Generator
    ├── image.html       # Image AI Generator
    └── upload.html      # File Upload AI
```

## Tech Stack

- Pure HTML5 / CSS3 / Vanilla JavaScript
- Google Fonts (Inter + Space Grotesk)
- Fetch API for all AI calls
- LocalStorage for chat history
- Pollinations.ai for image generation
- No frameworks, no build step, no dependencies

## APIs Used

- **Chat AI**: `api-nanzz.my.id` — DeepSeek model
- **App Generator**: `api-nanzz.my.id` — Blackbox AI
- **Prompt Generator**: `api-nanzz.my.id` — Prompt enhancer
- **Image AI**: `image.pollinations.ai` — Free image generation
- **File AI**: `api-nanzz.my.id` — DeepSeek analysis

## Design System

- **Colors**: Space Grey `#1C1C1E`, Accent Purple `#7B5EA7`, Accent Blue `#4A6CF7`
- **Typography**: Space Grotesk (display) + Inter (body)
- **Style**: Glassmorphism, frosted glass, floating cards, 2026 spatial UI
- **Responsive**: Mobile-first, CSS Grid, 1280px max-width

---

&copy; 2026 Kopqo AI — Free AI Platform
