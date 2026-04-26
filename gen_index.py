#!/usr/bin/env python3
"""Generate PixelForge Studio index.html"""

import sys

CSS = r"""
/* ===== PIXELFORGE STUDIO - FULL CSS ===== */
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');
:root {
  --bg: #0d0d1a; --panel: #151528; --panel2: #1e1e3a;
  --accent: #00ffcc; --accent2: #ff4d6d; --accent3: #ffe066; --accent4: #7c4fff;
  --text: #e8e8f0; --text-dim: #8888aa;
  --border: 2px solid var(--accent); --border2: 2px solid var(--accent2);
  --border3: 2px solid var(--accent3); --border4: 2px solid var(--accent4);
  --font-head: 'Press Start 2P', monospace; --font-body: 'VT323', monospace;
  --shadow: 0 0 16px rgba(0,255,204,0.18); --shadow2: 0 0 16px rgba(255,77,109,0.18);
  --radius: 4px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 18px; min-height: 100vh; overflow-x: hidden; }
body::before { content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.13) 2px, rgba(0,0,0,0.13) 4px); }
body::after { content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 9998;
  background: radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.55) 100%); }
#app-header { background: var(--panel); border-bottom: var(--border); padding: 16px 24px;
  display: flex; align-items: center; gap: 20px; box-shadow: var(--shadow); }
#logo-canvas { image-rendering: pixelated; border: 2px solid var(--accent4); }
.header-text { flex: 1; }
.app-title { font-family: var(--font-head); font-size: 1.1rem; color: var(--accent);
  text-shadow: 0 0 10px var(--accent), 2px 2px 0 var(--accent4); letter-spacing: 2px; margin-bottom: 6px; }
.app-subtitle { font-family: var(--font-body); font-size: 1.2rem; color: var(--accent3); letter-spacing: 3px; }
#tab-bar { display: flex; background: var(--panel); border-bottom: var(--border); overflow-x: auto; }
.tab-btn { font-family: var(--font-head); font-size: 0.65rem; color: var(--text-dim);
  background: transparent; border: none; border-right: 1px solid var(--panel2); padding: 14px 22px;
  cursor: pointer; transition: all 0.15s; white-space: nowrap; letter-spacing: 1px; }
.tab-btn:hover { color: var(--accent); background: var(--panel2); }
.tab-btn.active { color: var(--accent); background: var(--panel2); border-bottom: 3px solid var(--accent); box-shadow: inset 0 -3px 12px rgba(0,255,204,0.12); }
.tab-panel { display: none; padding: 20px; min-height: calc(100vh - 120px); }
.tab-panel.active { display: block; }
.panel-box { background: var(--panel); border: var(--border); border-radius: var(--radius); padding: 18px; margin-bottom: 18px; box-shadow: var(--shadow); }
.panel-box.accent2 { border: var(--border2); box-shadow: var(--shadow2); }
.panel-box.accent3 { border: var(--border3); }
.panel-box.accent4 { border: var(--border4); }
.panel-title { font-family: var(--font-head); font-size: 0.75rem; color: var(--accent); margin-bottom: 14px;
  text-shadow: 0 0 8px var(--accent); letter-spacing: 2px; }
.panel-title.accent2 { color: var(--accent2); text-shadow: 0 0 8px var(--accent2); }
.panel-title.accent3 { color: var(--accent3); text-shadow: 0 0 8px var(--accent3); }
.panel-title.accent4 { color: var(--accent4); text-shadow: 0 0 8px var(--accent4); }
.btn { font-family: var(--font-head); font-size: 0.6rem; color: var(--bg); background: var(--accent);
  border: none; border-radius: var(--radius); padding: 8px 14px; cursor: pointer; letter-spacing: 1px;
  transition: all 0.12s; box-shadow: 0 0 8px rgba(0,255,204,0.3); }
.btn:hover { background: #00ffe0; box-shadow: 0 0 16px rgba(0,255,204,0.6); transform: translateY(-1px); }
.btn:active { transform: translateY(1px); }
.btn.accent2 { background: var(--accent2); box-shadow: 0 0 8px rgba(255,77,109,0.3); color: #fff; }
.btn.accent2:hover { background: #ff6080; box-shadow: 0 0 16px rgba(255,77,109,0.6); }
.btn.accent3 { background: var(--accent3); box-shadow: 0 0 8px rgba(255,224,102,0.3); color: var(--bg); }
.btn.accent3:hover { background: #ffe980; }
.btn.accent4 { background: var(--accent4); box-shadow: 0 0 8px rgba(124,79,255,0.3); color: #fff; }
.btn.accent4:hover { background: #9060ff; }
.btn.sm { font-size: 0.5rem; padding: 5px 10px; }
.btn.lg { font-size: 0.7rem; padding: 12px 22px; }
.btn.active-tool { background: var(--accent4); color: #fff; box-shadow: 0 0 12px rgba(124,79,255,0.7); }
input[type=text], input[type=number], select { font-family: var(--font-body); font-size: 1.1rem;
  background: var(--panel2); color: var(--text); border: 1px solid var(--accent4); border-radius: var(--radius); padding: 5px 9px; }
input[type=range] { accent-color: var(--accent); cursor: pointer; width: 100%; }
input[type=color] { border: 1px solid var(--accent); border-radius: var(--radius); background: var(--panel2);
  cursor: pointer; padding: 1px; width: 36px; height: 28px; }
label { font-family: var(--font-body); color: var(--text-dim); font-size: 1rem; }
#learn-nav { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.learn-nav-btn { font-family: var(--font-head); font-size: 0.55rem; color: var(--text-dim);
  background: var(--panel2); border: 1px solid var(--accent4); border-radius: var(--radius);
  padding: 7px 12px; cursor: pointer; transition: all 0.12s; letter-spacing: 1px; }
.learn-nav-btn:hover { color: var(--accent4); border-color: var(--accent4); }
.learn-nav-btn.active { color: var(--accent4); border: 2px solid var(--accent4); background: #2a1e50; }
.learn-section { display: none; }
.learn-section.active { display: block; }
.learn-canvas-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 14px; align-items: flex-start; }
.learn-canvas-box { background: var(--panel2); border: 1px solid var(--accent4); border-radius: var(--radius); padding: 10px; text-align: center; }
.learn-canvas-label { font-family: var(--font-head); font-size: 0.45rem; color: var(--accent3); margin-top: 6px; letter-spacing: 1px; }
.palette-demo-grid { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px; }
.palette-demo-swatch { width: 28px; height: 28px; border-radius: 2px; border: 1px solid rgba(255,255,255,0.12); cursor: pointer; transition: transform 0.1s; }
.palette-demo-swatch:hover { transform: scale(1.18); }
.tips-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; }
.tip-card { background: var(--panel2); border: 1px solid var(--accent4); border-radius: var(--radius); padding: 14px; }
.tip-card-title { font-family: var(--font-head); font-size: 0.55rem; color: var(--accent3); margin-bottom: 8px; }
.tip-card-body { font-family: var(--font-body); font-size: 1.05rem; color: var(--text-dim); line-height: 1.5; }
.export-icons-row { display: flex; flex-wrap: wrap; gap: 18px; }
.export-icon-card { background: var(--panel2); border: 1px solid var(--accent); border-radius: var(--radius); padding: 16px 20px; min-width: 160px; text-align: center; }
.export-icon-symbol { font-size: 2.5rem; margin-bottom: 8px; }
.export-icon-name { font-family: var(--font-head); font-size: 0.55rem; color: var(--accent); margin-bottom: 5px; }
.export-icon-desc { font-size: 1rem; color: var(--text-dim); }
#create-layout { display: flex; gap: 12px; align-items: flex-start; flex-wrap: nowrap; }
#tool-sidebar { width: 56px; flex-shrink: 0; display: flex; flex-direction: column; gap: 4px;
  background: var(--panel); border: var(--border4); border-radius: var(--radius); padding: 8px 4px; }
.tool-btn { font-size: 1.3rem; background: var(--panel2); border: 1px solid var(--accent4);
  border-radius: var(--radius); padding: 6px; cursor: pointer; color: var(--text); text-align: center;
  transition: all 0.1s; line-height: 1; width: 100%; }
.tool-btn:hover { background: #2a1e50; border-color: var(--accent); }
.tool-btn.active { background: var(--accent4); border-color: var(--accent); color: #fff; }
.tool-separator { height: 1px; background: var(--accent4); margin: 4px 0; opacity: 0.4; }
#canvas-area { flex: 1; min-width: 0; display: flex; flex-direction: column; align-items: center; }
#canvas-controls { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; align-items: center; width: 100%; }
#editor-canvas { image-rendering: pixelated; cursor: crosshair; border: 2px solid var(--accent); box-shadow: var(--shadow); display: block; }
#canvas-outer { position: relative; overflow: auto; max-width: 100%; max-height: 560px; border: 1px solid var(--panel2); }
#right-panel { width: 200px; flex-shrink: 0; display: flex; flex-direction: column; gap: 10px; }
.color-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.color-swatch-main { width: 36px; height: 36px; border: 2px solid var(--accent); border-radius: 2px; cursor: pointer; display: inline-block; flex-shrink: 0; }
#fg-swatch { border-color: var(--accent); }
#bg-swatch { border-color: var(--text-dim); }
#swap-btn { font-size: 1.2rem; background: none; border: none; color: var(--accent3); cursor: pointer; padding: 2px 5px; transition: transform 0.2s; }
#swap-btn:hover { transform: rotate(180deg); }
.palette-grid { display: flex; flex-wrap: wrap; gap: 3px; margin-top: 6px; }
.palette-cell { width: 18px; height: 18px; border-radius: 2px; border: 1px solid rgba(255,255,255,0.12); cursor: pointer; transition: transform 0.1s; flex-shrink: 0; }
.palette-cell:hover { transform: scale(1.25); border-color: var(--accent); }
#layers-list { max-height: 260px; overflow-y: auto; margin-bottom: 6px; }
.layer-row { display: flex; align-items: center; gap: 5px; background: var(--panel2); border: 1px solid transparent;
  border-radius: var(--radius); padding: 5px 7px; margin-bottom: 4px; cursor: pointer; font-size: 0.95rem; transition: all 0.1s; }
.layer-row:hover { border-color: var(--accent4); }
.layer-row.active-layer { border-color: var(--accent); background: #1a1a38; }
.layer-eye { font-size: 1rem; cursor: pointer; flex-shrink: 0; opacity: 1; transition: opacity 0.1s; }
.layer-eye.hidden { opacity: 0.3; }
.layer-name { flex: 1; font-size: 0.9rem; color: var(--text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.layer-opacity { width: 50px; flex-shrink: 0; }
.layer-del { font-size: 0.85rem; color: var(--accent2); cursor: pointer; flex-shrink: 0; padding: 0 3px; }
.layer-del:hover { color: #ff8099; }
#frames-panel { background: var(--panel); border: var(--border4); border-radius: var(--radius); padding: 10px; margin-top: 10px; width: 100%; }
#frames-scroll { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 6px; margin-bottom: 8px; }
.frame-thumb { width: 52px; height: 52px; image-rendering: pixelated; border: 2px solid var(--accent4); border-radius: 2px; cursor: pointer; flex-shrink: 0; transition: border-color 0.1s; }
.frame-thumb.active-frame { border-color: var(--accent); box-shadow: 0 0 8px var(--accent); }
.frame-thumb:hover { border-color: var(--accent3); }
#anim-controls { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; padding: 8px 0; }
.anim-label { font-size: 0.9rem; color: var(--text-dim); }
#game-layout { display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-start; }
#game-left { flex: 1; min-width: 300px; }
#game-right { width: 340px; flex-shrink: 0; }
#game-canvas { display: block; image-rendering: pixelated; border: 2px solid var(--accent2); box-shadow: var(--shadow2); }
.sprite-slot { display: flex; align-items: center; gap: 10px; background: var(--panel2); border: 1px solid var(--accent4); border-radius: var(--radius); padding: 8px 12px; margin-bottom: 8px; }
.sprite-slot-label { font-family: var(--font-head); font-size: 0.5rem; color: var(--accent3); width: 90px; flex-shrink: 0; }
.sprite-slot-canvas { width: 32px; height: 32px; image-rendering: pixelated; border: 1px solid var(--accent4); background: #111; flex-shrink: 0; }
.sprite-slot-select { flex: 1; font-size: 0.9rem; background: var(--panel2); color: var(--text); border: 1px solid var(--accent4); border-radius: 2px; padding: 3px 6px; }
#map-editor-canvas { display: block; image-rendering: pixelated; border: 2px solid var(--accent3); cursor: crosshair; }
.tile-selector { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
.tile-select-btn { width: 36px; height: 36px; image-rendering: pixelated; border: 2px solid var(--accent4);
  border-radius: 2px; cursor: pointer; background: #111; transition: border-color 0.1s; padding: 0; }
.tile-select-btn.active-tile { border-color: var(--accent3); box-shadow: 0 0 8px var(--accent3); }
.tile-select-btn:hover { border-color: var(--accent); }
#virtual-dpad { display: flex; flex-direction: column; align-items: center; gap: 4px; margin-top: 10px; user-select: none; }
.dpad-row { display: flex; gap: 4px; align-items: center; }
.dpad-btn { width: 48px; height: 48px; font-size: 1.5rem; display: flex; align-items: center; justify-content: center;
  background: var(--panel2); border: 2px solid var(--accent4); border-radius: 6px; cursor: pointer; color: var(--text); transition: all 0.1s; -webkit-tap-highlight-color: transparent; }
.dpad-btn:active, .dpad-btn.pressed { background: var(--accent4); color: #fff; }
#jump-btn { width: 56px; height: 56px; font-family: var(--font-head); font-size: 0.55rem; background: var(--accent2);
  color: #fff; border: 2px solid #ff6080; border-radius: 50%; cursor: pointer; margin-left: 24px; transition: all 0.1s; }
#jump-btn:active { background: #ff6080; }
#export-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
.export-card { background: var(--panel); border: var(--border); border-radius: var(--radius); padding: 18px; box-shadow: var(--shadow); }
.export-card-title { font-family: var(--font-head); font-size: 0.65rem; color: var(--accent); margin-bottom: 12px; letter-spacing: 1px; }
.export-card.accent2 { border: var(--border2); }
.export-card.accent2 .export-card-title { color: var(--accent2); }
.export-card.accent3 { border: var(--border3); }
.export-card.accent3 .export-card-title { color: var(--accent3); }
.export-card.accent4 { border: var(--border4); }
.export-card.accent4 .export-card-title { color: var(--accent4); }
#gif-preview, #sheet-preview { image-rendering: pixelated; max-width: 100%; margin-top: 10px; border: 1px solid var(--accent4); display: none; }
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--panel); }
::-webkit-scrollbar-thumb { background: var(--accent4); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }
.row { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.col { display: flex; flex-direction: column; gap: 6px; }
.spacer { flex: 1; }
.divider { height: 1px; background: var(--panel2); margin: 10px 0; }
.text-accent { color: var(--accent); } .text-accent2 { color: var(--accent2); }
.text-accent3 { color: var(--accent3); } .text-accent4 { color: var(--accent4); }
.mt8 { margin-top: 8px; } .mb8 { margin-bottom: 8px; } .mb14 { margin-bottom: 14px; }
.shortcut-table { width: 100%; border-collapse: collapse; font-size: 1rem; }
.shortcut-table th, .shortcut-table td { padding: 5px 10px; border: 1px solid var(--panel2); text-align: left; }
.shortcut-table th { font-family: var(--font-head); font-size: 0.55rem; color: var(--accent3); background: var(--panel2); }
.shortcut-table td { color: var(--text); }
.kbd { background: var(--panel2); border: 1px solid var(--accent4); border-radius: 3px; padding: 1px 6px;
  font-family: var(--font-head); font-size: 0.5rem; color: var(--accent3); }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
@keyframes pulse { 0%, 100% { box-shadow: 0 0 8px var(--accent); } 50% { box-shadow: 0 0 22px var(--accent), 0 0 40px var(--accent); } }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.blink { animation: blink 1.2s infinite; }
.pulse-glow { animation: pulse 2s infinite; }
.fade-in { animation: fadeIn 0.3s ease; }
.playing-indicator { font-family: var(--font-head); font-size: 0.5rem; color: var(--accent2); animation: blink 0.7s infinite; margin-left: 8px; }
.playing-indicator.hidden { display: none; }
#status-bar { position: fixed; bottom: 0; left: 0; right: 0; background: var(--panel);
  border-top: 1px solid var(--accent4); padding: 4px 16px; font-size: 0.95rem; color: var(--text-dim);
  display: flex; gap: 20px; z-index: 100; }
.status-item { color: var(--text-dim); }
.status-item span { color: var(--accent3); }
.checker { background-image: linear-gradient(45deg, #333 25%, transparent 25%),
  linear-gradient(-45deg, #333 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #333 75%),
  linear-gradient(-45deg, transparent 75%, #333 75%);
  background-size: 12px 12px; background-position: 0 0, 0 6px, 6px -6px, -6px 0; background-color: #222; }
.layer-demo-wrap { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }
.layer-demo-label { font-size: 0.9rem; color: var(--text-dim); text-align: center; margin-top: 5px; }
.layer-demo-op { font-size: 1.6rem; color: var(--accent3); }
.progress-bar-wrap { background: var(--panel2); border-radius: 4px; height: 10px; overflow: hidden; margin: 8px 0; }
.progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--accent4), var(--accent)); transition: width 0.3s; }
.tut-highlight { outline: 3px solid var(--accent3); outline-offset: 2px; animation: pulse 1s infinite; }
@media (max-width: 900px) {
  #create-layout { flex-wrap: wrap; } #right-panel { width: 100%; flex-direction: row; flex-wrap: wrap; }
  #game-right { width: 100%; } #game-left { min-width: unset; }
}
@media (max-width: 600px) {
  .app-title { font-size: 0.7rem; } .tab-btn { font-size: 0.5rem; padding: 10px 12px; } #tool-sidebar { width: 44px; }
}
"""

HTML_BODY = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PixelForge Studio - Pixel Art &amp; Game Creation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&amp;family=VT323&amp;display=swap" rel="stylesheet">
<style>
CSSPLACEHOLDER
</style>
</head>
<body>
<header id="app-header">
  <canvas id="logo-canvas" width="56" height="56"></canvas>
  <div class="header-text">
    <div class="app-title">&#x2728; PIXELFORGE STUDIO</div>
    <div class="app-subtitle">PIXEL ART &amp; GAME CREATION PLATFORM</div>
  </div>
  <div style="text-align:right;font-size:0.85rem;color:var(--text-dim);">
    <div id="hdr-size" style="color:var(--accent3);">16x16</div>
    <div id="hdr-tool" style="color:var(--accent);">PENCIL</div>
  </div>
</header>
<div id="tab-bar">
  <button class="tab-btn active" onclick="switchTab('learn')" id="tab-learn-btn">&#x1F393; LEARN</button>
  <button class="tab-btn" onclick="switchTab('create')" id="tab-create-btn">&#x1F3A8; CREATE</button>
  <button class="tab-btn" onclick="switchTab('game')" id="tab-game-btn">&#x1F3AE; GAME</button>
  <button class="tab-btn" onclick="switchTab('export')" id="tab-export-btn">&#x1F4E4; EXPORT</button>
</div>
<main>
TABLEARN
TABCREATE
TABGAME
TABEXPORT
</main>
STATUSBAR
JSSCRIPT
</body>
</html>
"""

TAB_LEARN = """
<div id="tab-learn" class="tab-panel active">
  <div id="learn-nav">
    <button class="learn-nav-btn active" onclick="showLearnSection(0)">1. INTRO</button>
    <button class="learn-nav-btn" onclick="showLearnSection(1)">2. FIRST SPRITE</button>
    <button class="learn-nav-btn" onclick="showLearnSection(2)">3. ANIMATION</button>
    <button class="learn-nav-btn" onclick="showLearnSection(3)">4. COLOR &amp; PALETTES</button>
    <button class="learn-nav-btn" onclick="showLearnSection(4)">5. LAYERS</button>
    <button class="learn-nav-btn" onclick="showLearnSection(5)">6. EXPORTING</button>
    <button class="learn-nav-btn" onclick="showLearnSection(6)">7. TIPS</button>
  </div>
  <div id="learn-sec-0" class="learn-section active">
    <div class="panel-box">
      <div class="panel-title">&#x1F3AE; WHAT IS PIXEL ART?</div>
      <p style="font-size:1.15rem;color:var(--text);line-height:1.7;margin-bottom:12px;">
        Pixel art is a form of digital art where images are created at the pixel level using a limited palette and small canvas sizes.
        It became popular in the 8-bit and 16-bit gaming eras (1980s-1990s) when hardware constraints forced artists to be creative with very few pixels.
        Today pixel art is a beloved aesthetic used in indie games, web graphics, and digital art.
      </p>
      <p style="font-size:1.1rem;color:var(--text-dim);line-height:1.6;margin-bottom:12px;">
        Key characteristics: limited palette (2-64 colors), small resolution (8x8 to 64x64 typical),
        intentional pixel placement, clean outlines, dithering for gradients, animation via sprite sheets.
      </p>
      <div class="learn-canvas-row">
        <div class="learn-canvas-box">
          <canvas id="learn-walk-canvas" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;"></canvas>
          <div class="learn-canvas-label">WALK CYCLE</div>
        </div>
        <div class="learn-canvas-box">
          <canvas id="learn-idle-canvas" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;"></canvas>
          <div class="learn-canvas-label">IDLE ANIM</div>
        </div>
        <div class="learn-canvas-box">
          <canvas id="learn-explosion-canvas" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;"></canvas>
          <div class="learn-canvas-label">EXPLOSION</div>
        </div>
        <div class="learn-canvas-box">
          <canvas id="learn-coin-canvas" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;"></canvas>
          <div class="learn-canvas-label">COIN SPIN</div>
        </div>
        <div class="learn-canvas-box">
          <canvas id="learn-fire-canvas" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;"></canvas>
          <div class="learn-canvas-label">FIRE ANIM</div>
        </div>
      </div>
      <div style="margin-top:14px;">
        <div style="font-family:var(--font-head);font-size:0.6rem;color:var(--accent3);margin-bottom:8px;">&#x1F4D6; PIXEL ART HISTORY</div>
        <div style="font-size:1.05rem;color:var(--text-dim);line-height:1.8;">
          <span style="color:var(--accent);">1972</span> &#x2014; Pong: one of the first commercial video games with pixel graphics<br>
          <span style="color:var(--accent);">1978</span> &#x2014; Space Invaders introduces iconic pixel aliens<br>
          <span style="color:var(--accent);">1981</span> &#x2014; Donkey Kong &amp; Mario first appear as pixel sprites<br>
          <span style="color:var(--accent);">1985</span> &#x2014; Super Mario Bros sets the standard for NES pixel art<br>
          <span style="color:var(--accent);">1990s</span> &#x2014; SNES/Genesis: 16-bit color, larger sprites, Mode 7<br>
          <span style="color:var(--accent);">2000s</span> &#x2014; 3D takes over but pixel art survives on handhelds<br>
          <span style="color:var(--accent);">2010s</span> &#x2014; Indie renaissance: Minecraft, Terraria, Shovel Knight<br>
          <span style="color:var(--accent);">2020s</span> &#x2014; Pixel art as deliberate aesthetic in modern games
        </div>
      </div>
    </div>
  </div>
  <div id="learn-sec-1" class="learn-section">
    <div class="panel-box">
      <div class="panel-title accent2">&#x1F3AF; DRAWING YOUR FIRST SPRITE</div>
      <p style="font-size:1.1rem;color:var(--text);line-height:1.6;margin-bottom:12px;">
        Draw a simple 8x8 heart pixel by pixel. Click the highlighted yellow pixels to paint them red!
      </p>
      <div id="tut-progress-wrap" class="progress-bar-wrap" style="max-width:300px;">
        <div id="tut-progress-bar" class="progress-bar-fill" style="width:0%"></div>
      </div>
      <div id="tut-step-text" style="font-size:1.05rem;color:var(--accent3);margin-bottom:12px;">Click the highlighted pixels to draw the heart!</div>
      <div class="row">
        <div class="learn-canvas-box">
          <canvas id="learn-tut-canvas" width="128" height="128" style="image-rendering:pixelated;width:256px;height:256px;cursor:crosshair;border:2px solid var(--accent2);"></canvas>
          <div class="learn-canvas-label">8x8 HEART TUTORIAL</div>
        </div>
        <div style="max-width:260px;">
          <div style="font-family:var(--font-head);font-size:0.55rem;color:var(--accent);margin-bottom:8px;">THE HEART PATTERN</div>
          <div style="font-size:1rem;color:var(--text-dim);line-height:1.9;font-family:monospace;">
            . X X . . X X .<br>
            X X X X X X X X<br>
            X X X X X X X X<br>
            . X X X X X X .<br>
            . . X X X X . .<br>
            . . . X X . . .<br>
            . . . . . . . .<br>
            . . . . . . . .
          </div>
          <div class="row mt8">
            <button class="btn sm" onclick="resetTutorial()">&#x21BA; RESET</button>
            <button class="btn sm accent3" onclick="autoCompleteTutorial()">AUTO-FILL</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div id="learn-sec-2" class="learn-section">
    <div class="panel-box">
      <div class="panel-title accent3">&#x25B6; ANIMATION BASICS</div>
      <p style="font-size:1.1rem;color:var(--text);line-height:1.6;margin-bottom:14px;">
        Animation works by showing multiple frames rapidly. Draw in each frame then press Play!
      </p>
      <div class="row mb14">
        <div style="display:flex;gap:10px;">
          <div class="learn-canvas-box">
            <canvas id="mini-frame-0" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;cursor:crosshair;border:2px solid var(--accent);"></canvas>
            <div class="learn-canvas-label" style="color:var(--accent);">FRAME 1</div>
          </div>
          <div class="learn-canvas-box">
            <canvas id="mini-frame-1" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;cursor:crosshair;border:2px solid var(--accent4);"></canvas>
            <div class="learn-canvas-label">FRAME 2</div>
          </div>
          <div class="learn-canvas-box">
            <canvas id="mini-frame-2" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;cursor:crosshair;border:2px solid var(--accent4);"></canvas>
            <div class="learn-canvas-label">FRAME 3</div>
          </div>
        </div>
        <div>
          <canvas id="mini-preview" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;border:2px solid var(--accent2);"></canvas>
          <div class="learn-canvas-label" style="color:var(--accent2);">PREVIEW</div>
        </div>
      </div>
      <div class="row">
        <button class="btn accent2" onclick="miniAnimPlay()">&#x25B6; PLAY</button>
        <button class="btn" onclick="miniAnimStop()">&#x23F9; STOP</button>
        <label>Frame:</label>
        <select id="mini-active-frame" onchange="setMiniActiveFrame(this.value)">
          <option value="0">Frame 1</option><option value="1">Frame 2</option><option value="2">Frame 3</option>
        </select>
        <label>Color:</label>
        <input type="color" id="mini-color" value="#ff4d6d">
        <button class="btn sm" onclick="clearMiniFrame()">CLEAR</button>
      </div>
      <div style="margin-top:16px;font-size:1.05rem;color:var(--text-dim);line-height:1.7;">
        <strong style="color:var(--accent3);">Animation tips:</strong><br>
        &#x2022; Keep changes small and consistent between frames<br>
        &#x2022; Use onion skinning to see the previous frame as a ghost<br>
        &#x2022; Walk cycles typically use 4-8 frames at 8-12 FPS<br>
        &#x2022; Loop: last frame should transition smoothly back to frame 1
      </div>
    </div>
  </div>
  <div id="learn-sec-3" class="learn-section">
    <div class="panel-box">
      <div class="panel-title accent4">&#x1F3A8; COLOR &amp; PALETTES</div>
      <p style="font-size:1.1rem;color:var(--text);line-height:1.6;margin-bottom:14px;">
        Limiting your palette forces creative decisions and gives art a cohesive look. Click any swatch to use that color!
      </p>
      <div style="margin-bottom:14px;">
        <div style="font-family:var(--font-head);font-size:0.6rem;color:var(--accent);margin-bottom:8px;">DB16 (16 colors) &#x2014; DawnBringer</div>
        <div class="palette-demo-grid" id="pal-demo-db16"></div>
      </div>
      <div style="margin-bottom:14px;">
        <div style="font-family:var(--font-head);font-size:0.6rem;color:var(--accent2);margin-bottom:8px;">NES PALETTE &#x2014; Nintendo Entertainment System</div>
        <div class="palette-demo-grid" id="pal-demo-nes"></div>
      </div>
      <div style="margin-bottom:14px;">
        <div style="font-family:var(--font-head);font-size:0.6rem;color:var(--accent3);margin-bottom:8px;">GAMEBOY (4 colors) &#x2014; Original green screen</div>
        <div class="palette-demo-grid" id="pal-demo-gb"></div>
      </div>
      <div style="margin-bottom:14px;">
        <div style="font-family:var(--font-head);font-size:0.6rem;color:var(--accent4);margin-bottom:8px;">CGA PALETTE (16 colors) &#x2014; IBM PC classic</div>
        <div class="palette-demo-grid" id="pal-demo-cga"></div>
      </div>
      <div style="font-size:1.05rem;color:var(--text-dim);line-height:1.7;margin-top:10px;">
        <strong style="color:var(--accent3);">Color theory for pixel art:</strong><br>
        &#x2022; Limit to 4-16 colors for a cohesive retro look<br>
        &#x2022; One highlight, one base, one shadow per object<br>
        &#x2022; Dithering: alternate two colors for gradients<br>
        &#x2022; Avoid pure black outlines &#x2014; use dark hue variants<br>
        &#x2022; Keep your palette consistent across all sprites
      </div>
    </div>
  </div>
  <div id="learn-sec-4" class="learn-section">
    <div class="panel-box">
      <div class="panel-title">&#x1F5C2; LAYERS</div>
      <p style="font-size:1.1rem;color:var(--text);line-height:1.6;margin-bottom:14px;">
        Layers let you separate parts of your artwork. Hide, reorder, and adjust opacity independently.
      </p>
      <div class="layer-demo-wrap">
        <div>
          <canvas id="layer-demo-1" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;border:1px solid var(--accent4);"></canvas>
          <div class="layer-demo-label">Layer 1: Background</div>
        </div>
        <div class="layer-demo-op">+</div>
        <div>
          <canvas id="layer-demo-2" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;border:1px solid var(--accent4);"></canvas>
          <div class="layer-demo-label">Layer 2: Character</div>
        </div>
        <div class="layer-demo-op">=</div>
        <div>
          <canvas id="layer-demo-combined" width="64" height="64" style="image-rendering:pixelated;width:128px;height:128px;border:2px solid var(--accent);"></canvas>
          <div class="layer-demo-label" style="color:var(--accent);">Combined</div>
        </div>
      </div>
      <div style="margin-top:16px;font-size:1.05rem;color:var(--text-dim);line-height:1.7;">
        <strong style="color:var(--accent3);">Layer tips:</strong><br>
        &#x2022; Background on bottom layer, details on top<br>
        &#x2022; Use opacity for shadow and transparency effects<br>
        &#x2022; PixelForge supports up to 8 layers per sprite
      </div>
    </div>
  </div>
  <div id="learn-sec-5" class="learn-section">
    <div class="panel-box">
      <div class="panel-title accent2">&#x1F4E4; EXPORTING</div>
      <p style="font-size:1.1rem;color:var(--text);line-height:1.6;margin-bottom:14px;">
        Multiple export formats for different use cases. Choose the right format!
      </p>
      <div class="export-icons-row">
        <div class="export-icon-card">
          <div class="export-icon-symbol">&#x1F5BC;</div>
          <div class="export-icon-name">PNG</div>
          <div class="export-icon-desc">Lossless single frame. Best for still art and game assets.</div>
        </div>
        <div class="export-icon-card" style="border-color:var(--accent2);">
          <div class="export-icon-symbol">&#x1F3AC;</div>
          <div class="export-icon-name" style="color:var(--accent2);">GIF</div>
          <div class="export-icon-desc">Animated. Limited to 256 colors. Good for sharing online.</div>
        </div>
        <div class="export-icon-card" style="border-color:var(--accent3);">
          <div class="export-icon-symbol">&#x1F4CB;</div>
          <div class="export-icon-name" style="color:var(--accent3);">SPRITE SHEET</div>
          <div class="export-icon-desc">All frames in one PNG grid. Standard for game engines.</div>
        </div>
        <div class="export-icon-card" style="border-color:var(--accent4);">
          <div class="export-icon-symbol">&#x1F3A5;</div>
          <div class="export-icon-name" style="color:var(--accent4);">WEBM VIDEO</div>
          <div class="export-icon-desc">High quality via MediaRecorder. For showcasing work.</div>
        </div>
        <div class="export-icon-card">
          <div class="export-icon-symbol">&#x1F3AE;</div>
          <div class="export-icon-name">HTML5 GAME</div>
          <div class="export-icon-desc">Standalone game.html with sprites and map baked in.</div>
        </div>
      </div>
    </div>
  </div>
  <div id="learn-sec-6" class="learn-section">
    <div class="panel-box">
      <div class="panel-title accent3">&#x1F4A1; PIXEL ART TIPS</div>
      <div class="tips-grid">
        <div class="tip-card"><div class="tip-card-title">&#x1F4CF; START SMALL</div>
          <div class="tip-card-body">Begin with 8x8 or 16x16. Constraints breed creativity.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F3AF; READABLE SILHOUETTE</div>
          <div class="tip-card-body">Your sprite should be recognizable from silhouette alone.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F504; AVOID JAGGIES</div>
          <div class="tip-card-body">Diagonal lines should use 1-pixel steps consistently.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F4A1; USE DITHERING</div>
          <div class="tip-card-body">Alternate two colors in a checkerboard for gradient effects.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F308; LIMIT YOUR PALETTE</div>
          <div class="tip-card-body">4-16 colors forces cohesion. One highlight, one shadow per element.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F4A1; ZOOM IN/OUT OFTEN</div>
          <div class="tip-card-body">Work at 8x-16x but check at 1x regularly.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F31F; LIGHT SOURCE</div>
          <div class="tip-card-body">Pick one consistent light direction. Top-left is traditional.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F50D; STUDY REFERENCES</div>
          <div class="tip-card-body">Study classic NES/SNES sprites. Deconstruct their techniques.</div></div>
        <div class="tip-card"><div class="tip-card-title">&#x1F504; SAVE OFTEN</div>
          <div class="tip-card-body">Export frequently. Use layers to preserve working copies.</div></div>
      </div>
    </div>
  </div>
</div>
"""

TAB_CREATE = """
<div id="tab-create" class="tab-panel">
  <div id="canvas-controls" class="row mb8">
    <label>Size:</label>
    <select id="size-select" onchange="resizeCanvas(this.value)">
      <option value="8">8x8</option><option value="16" selected>16x16</option>
      <option value="32">32x32</option><option value="64">64x64</option>
    </select>
    <label>Zoom:</label>
    <select id="zoom-select" onchange="setZoom(parseInt(this.value))">
      <option value="2">2x</option><option value="4">4x</option>
      <option value="8" selected>8x</option><option value="16">16x</option>
    </select>
    <button class="btn sm" onclick="toggleGrid()" id="grid-btn">&#x22EF; GRID: ON</button>
    <button class="btn sm accent3" onclick="clearActiveLayer()">&#x1F5D1; CLEAR</button>
    <button class="btn sm accent2" onclick="newProject()">&#x2B; NEW</button>
    <span class="spacer"></span>
    <span id="cursor-pos" style="font-size:0.9rem;color:var(--text-dim);">X:-- Y:--</span>
  </div>
  <div id="create-layout">
    <div id="tool-sidebar">
      <button class="tool-btn active" id="tool-pencil" onclick="setTool('pencil')" title="Pencil (B)">&#x270F;</button>
      <button class="tool-btn" id="tool-eraser" onclick="setTool('eraser')" title="Eraser (E)">&#x25A1;</button>
      <button class="tool-btn" id="tool-fill" onclick="setTool('fill')" title="Fill (F)">&#x1FA63;</button>
      <button class="tool-btn" id="tool-eyedropper" onclick="setTool('eyedropper')" title="Pick (I)">&#x1F489;</button>
      <div class="tool-separator"></div>
      <button class="tool-btn" id="tool-line" onclick="setTool('line')" title="Line (L)">&#x2571;</button>
      <button class="tool-btn" id="tool-rect" onclick="setTool('rect')" title="Rect (R)">&#x25A1;</button>
      <button class="tool-btn" id="tool-fillrect" onclick="setTool('fillrect')" title="Filled Rect">&#x25A0;</button>
      <button class="tool-btn" id="tool-circle" onclick="setTool('circle')" title="Circle (C)">&#x25CB;</button>
      <button class="tool-btn" id="tool-fillcircle" onclick="setTool('fillcircle')" title="Filled Circle">&#x25CF;</button>
      <div class="tool-separator"></div>
      <button class="tool-btn" onclick="undo()" title="Undo Ctrl+Z">&#x21A9;</button>
      <button class="tool-btn" onclick="redo()" title="Redo Ctrl+Y">&#x21AA;</button>
    </div>
    <div id="canvas-area">
      <div id="canvas-outer" class="checker">
        <canvas id="editor-canvas" width="128" height="128"></canvas>
      </div>
      <div id="frames-panel">
        <div class="row mb8">
          <span style="font-family:var(--font-head);font-size:0.55rem;color:var(--accent4);">FRAMES</span>
          <button class="btn sm accent4" onclick="addFrame()">+ ADD</button>
          <button class="btn sm accent2" onclick="deleteFrame()">&#x2212; DEL</button>
          <button class="btn sm" onclick="duplicateFrame()">&#x2398; DUP</button>
          <span class="spacer"></span>
          <span id="frame-count-display" style="font-size:0.9rem;color:var(--text-dim);">1/1</span>
        </div>
        <div id="frames-scroll"></div>
        <div id="anim-controls" class="row">
          <button class="btn sm accent2" id="play-btn" onclick="toggleAnim()">&#x25B6; PLAY</button>
          <span class="playing-indicator hidden" id="playing-dot">&#x25CF; PLAYING</span>
          <label>FPS:</label>
          <input type="range" id="fps-slider" min="1" max="30" value="8" oninput="setFPS(this.value)" style="width:80px;">
          <span id="fps-display" style="color:var(--accent3);">8</span>
          <button class="btn sm" id="onion-btn" onclick="toggleOnionSkin()">ONION: OFF</button>
          <button class="btn sm" id="loop-btn" onclick="toggleLoop()">LOOP: ON</button>
        </div>
      </div>
    </div>
    <div id="right-panel">
      <div class="panel-box" style="padding:12px;">
        <div class="panel-title" style="font-size:0.6rem;margin-bottom:8px;">&#x1F3A8; COLORS</div>
        <div class="color-row">
          <div id="fg-swatch" class="color-swatch-main" title="Foreground" onclick="openColorPicker('fg')"></div>
          <div id="bg-swatch" class="color-swatch-main" title="Background" onclick="openColorPicker('bg')"></div>
          <button id="swap-btn" onclick="swapColors()" title="Swap">&#x21C4;</button>
        </div>
        <div class="row mb8">
          <label style="font-size:0.85rem;">HEX:</label>
          <input type="text" id="hex-input" value="#ff4d6d" style="width:80px;font-size:0.9rem;" oninput="onHexInput(this.value)">
          <input type="color" id="color-picker" value="#ff4d6d" oninput="onColorPickerChange(this.value)">
        </div>
        <div class="row mb8">
          <label style="font-size:0.85rem;">PALETTE:</label>
          <select id="palette-select" onchange="loadPalette(this.value)" style="font-size:0.85rem;">
            <option value="db16">DB16</option><option value="nes">NES</option>
            <option value="gameboy">GameBoy</option><option value="cga">CGA</option>
          </select>
        </div>
        <div id="palette-grid" class="palette-grid"></div>
      </div>
      <div class="panel-box" style="padding:12px;">
        <div class="panel-title" style="font-size:0.6rem;margin-bottom:8px;">&#x1F5C2; LAYERS</div>
        <div class="row mb8">
          <button class="btn sm" onclick="addLayer()">+ ADD</button>
          <button class="btn sm accent2" onclick="deleteLayer()">&#x2212; DEL</button>
          <button class="btn sm" onclick="moveLayerUp()">&#x2191;</button>
          <button class="btn sm" onclick="moveLayerDown()">&#x2193;</button>
        </div>
        <div id="layers-list"></div>
      </div>
      <div class="panel-box" style="padding:12px;">
        <div class="panel-title" style="font-size:0.6rem;margin-bottom:8px;">&#x2328; SHORTCUTS</div>
        <table class="shortcut-table">
          <tr><td><span class="kbd">B</span></td><td>Pencil</td></tr>
          <tr><td><span class="kbd">E</span></td><td>Eraser</td></tr>
          <tr><td><span class="kbd">F</span></td><td>Fill</td></tr>
          <tr><td><span class="kbd">I</span></td><td>Eyedropper</td></tr>
          <tr><td><span class="kbd">L</span></td><td>Line</td></tr>
          <tr><td><span class="kbd">R</span></td><td>Rect</td></tr>
          <tr><td><span class="kbd">C</span></td><td>Circle</td></tr>
          <tr><td><span class="kbd">Ctrl+Z</span></td><td>Undo</td></tr>
          <tr><td><span class="kbd">Ctrl+Y</span></td><td>Redo</td></tr>
          <tr><td><span class="kbd">[ ]</span></td><td>Zoom</td></tr>
        </table>
      </div>
    </div>
  </div>
</div>
"""

TAB_GAME = """
<div id="tab-game" class="tab-panel">
  <div id="game-layout">
    <div id="game-left">
      <div class="panel-box accent4" style="margin-bottom:12px;">
        <div class="panel-title accent4">&#x1F464; SPRITE ASSIGNMENT</div>
        <div class="sprite-slot">
          <div class="sprite-slot-label">PLAYER</div>
          <canvas class="sprite-slot-canvas" id="game-player-canvas" width="32" height="32"></canvas>
          <select class="sprite-slot-select" id="game-player-select" onchange="assignSprite('player',parseInt(this.value))">
            <option value="-1">-- None --</option>
          </select>
        </div>
        <div class="sprite-slot">
          <div class="sprite-slot-label">GROUND TILE</div>
          <canvas class="sprite-slot-canvas" id="game-tile0-canvas" width="32" height="32"></canvas>
          <select class="sprite-slot-select" id="game-tile0-select" onchange="assignSprite('tile0',parseInt(this.value))">
            <option value="-1">-- None --</option>
          </select>
        </div>
        <div class="sprite-slot">
          <div class="sprite-slot-label">WALL TILE</div>
          <canvas class="sprite-slot-canvas" id="game-tile1-canvas" width="32" height="32"></canvas>
          <select class="sprite-slot-select" id="game-tile1-select" onchange="assignSprite('tile1',parseInt(this.value))">
            <option value="-1">-- None --</option>
          </select>
        </div>
        <div class="sprite-slot">
          <div class="sprite-slot-label">HAZARD TILE</div>
          <canvas class="sprite-slot-canvas" id="game-tile2-canvas" width="32" height="32"></canvas>
          <select class="sprite-slot-select" id="game-tile2-select" onchange="assignSprite('tile2',parseInt(this.value))">
            <option value="-1">-- None --</option>
          </select>
        </div>
        <div class="sprite-slot">
          <div class="sprite-slot-label">COIN TILE</div>
          <canvas class="sprite-slot-canvas" id="game-tile3-canvas" width="32" height="32"></canvas>
          <select class="sprite-slot-select" id="game-tile3-select" onchange="assignSprite('tile3',parseInt(this.value))">
            <option value="-1">-- None --</option>
          </select>
        </div>
      </div>
      <div class="panel-box accent3" style="margin-bottom:12px;">
        <div class="panel-title accent3">&#x1F5FA; MAP EDITOR (20x15)</div>
        <div class="row mb8">
          <span style="font-size:0.95rem;color:var(--text-dim);">Active Tile:</span>
          <div class="tile-selector">
            <button class="tile-select-btn active-tile" id="ts-erase" onclick="selectTileType(-1)" title="Erase">&#x2715;</button>
            <canvas class="tile-select-btn" id="ts-0" onclick="selectTileType(0)" title="Ground" width="36" height="36"></canvas>
            <canvas class="tile-select-btn" id="ts-1" onclick="selectTileType(1)" title="Wall" width="36" height="36"></canvas>
            <canvas class="tile-select-btn" id="ts-2" onclick="selectTileType(2)" title="Hazard" width="36" height="36"></canvas>
            <canvas class="tile-select-btn" id="ts-3" onclick="selectTileType(3)" title="Coin" width="36" height="36"></canvas>
          </div>
          <button class="btn sm accent2" onclick="clearGameMap()">CLEAR MAP</button>
          <button class="btn sm" onclick="fillGroundRow()">FILL GROUND</button>
        </div>
        <canvas id="map-editor-canvas" width="320" height="240" style="image-rendering:pixelated;width:640px;max-width:100%;cursor:crosshair;border:2px solid var(--accent3);display:block;"></canvas>
      </div>
    </div>
    <div id="game-right">
      <div class="panel-box" style="margin-bottom:12px;">
        <div class="panel-title" style="font-size:0.6rem;">&#x1F3AE; GAME MODE</div>
        <div class="row">
          <button class="btn active-tool" id="mode-platformer-btn" onclick="setGameMode('platformer')">PLATFORMER</button>
          <button class="btn" id="mode-topdown-btn" onclick="setGameMode('topdown')">TOP-DOWN</button>
        </div>
      </div>
      <div class="panel-box accent2" style="margin-bottom:12px;">
        <div class="panel-title accent2">&#x25B6; GAME PREVIEW</div>
        <canvas id="game-canvas" width="320" height="240" style="image-rendering:pixelated;width:100%;max-width:320px;display:block;border:2px solid var(--accent2);"></canvas>
        <div class="row mt8">
          <button class="btn lg accent2" id="game-play-btn" onclick="toggleGame()">&#x25B6; PLAY GAME</button>
          <span id="game-score-display" style="font-size:1.2rem;color:var(--accent3);">Score: 0</span>
        </div>
        <div id="virtual-dpad">
          <div class="dpad-row">
            <div style="width:48px;"></div>
            <div class="dpad-btn" id="dpad-up" ontouchstart="dpadPress('up')" ontouchend="dpadRelease('up')" onmousedown="dpadPress('up')" onmouseup="dpadRelease('up')">&#x2191;</div>
            <div style="width:48px;"></div>
            <button id="jump-btn" ontouchstart="dpadPress('jump')" ontouchend="dpadRelease('jump')" onmousedown="dpadPress('jump')" onmouseup="dpadRelease('jump')">JUMP</button>
          </div>
          <div class="dpad-row">
            <div class="dpad-btn" id="dpad-left" ontouchstart="dpadPress('left')" ontouchend="dpadRelease('left')" onmousedown="dpadPress('left')" onmouseup="dpadRelease('left')">&#x2190;</div>
            <div class="dpad-btn" id="dpad-down" ontouchstart="dpadPress('down')" ontouchend="dpadRelease('down')" onmousedown="dpadPress('down')" onmouseup="dpadRelease('down')">&#x2193;</div>
            <div class="dpad-btn" id="dpad-right" ontouchstart="dpadPress('right')" ontouchend="dpadRelease('right')" onmousedown="dpadPress('right')" onmouseup="dpadRelease('right')">&#x2192;</div>
          </div>
        </div>
        <div style="font-size:0.95rem;color:var(--text-dim);margin-top:8px;">
          &#x2328; WASD / Arrow keys &#x2014; Space/W/Up to jump
        </div>
      </div>
      <div class="panel-box">
        <div class="panel-title" style="font-size:0.6rem;">&#x1F4E6; EXPORT GAME</div>
        <button class="btn lg accent4" onclick="exportGame()">&#x1F4E6; DOWNLOAD game.html</button>
        <p style="font-size:1rem;color:var(--text-dim);margin-top:8px;line-height:1.5;">
          Exports a standalone HTML5 game with your sprites, map, and game mode baked in.
        </p>
      </div>
    </div>
  </div>
</div>
"""

TAB_EXPORT = """
<div id="tab-export" class="tab-panel">
  <div id="export-grid">
    <div class="export-card">
      <div class="export-card-title">&#x1F5BC; PNG - CURRENT FRAME</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Export the currently active frame as a PNG with transparency (all visible layers composited).
      </p>
      <button class="btn" onclick="exportPNGCurrentFrame()">&#x2B07; DOWNLOAD frame.png</button>
    </div>
    <div class="export-card accent2">
      <div class="export-card-title">&#x1F5C3; PNG - ALL FRAMES</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Export each frame as a separate PNG file (frame_0.png, frame_1.png, etc).
      </p>
      <button class="btn accent2" onclick="exportPNGAllFrames()">&#x2B07; DOWNLOAD ALL FRAMES</button>
    </div>
    <div class="export-card accent3">
      <div class="export-card-title">&#x1F4CB; SPRITE SHEET</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Combine all frames into a single sprite sheet image. Configure columns below.
      </p>
      <div class="row mb8">
        <label>Columns:</label>
        <input type="number" id="sheet-cols" value="4" min="1" max="32" style="width:60px;">
      </div>
      <button class="btn accent3" onclick="exportSpriteSheet()">&#x2B07; DOWNLOAD spritesheet.png</button>
      <img id="sheet-preview" alt="Sprite Sheet Preview">
    </div>
    <div class="export-card accent4">
      <div class="export-card-title">&#x1F3AC; ANIMATED GIF</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Encode all frames as an animated GIF using the inline LZW encoder.
      </p>
      <div class="row mb8">
        <label>FPS:</label>
        <input type="number" id="gif-fps" value="8" min="1" max="30" style="width:60px;">
      </div>
      <button class="btn accent4" onclick="exportGIF()">&#x2B07; DOWNLOAD animation.gif</button>
      <img id="gif-preview" alt="GIF Preview">
      <div id="gif-status" style="font-size:0.95rem;color:var(--text-dim);margin-top:6px;"></div>
    </div>
    <div class="export-card">
      <div class="export-card-title" style="color:var(--accent3);">&#x1F3A5; WEBM VIDEO</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Record animation frames using MediaRecorder and download as WebM video.
      </p>
      <div class="row mb8">
        <label>FPS:</label>
        <input type="number" id="webm-fps" value="8" min="1" max="30" style="width:60px;">
      </div>
      <button class="btn accent3" onclick="exportWebM()">&#x25CF; RECORD &amp; DOWNLOAD</button>
      <div id="webm-status" style="font-size:0.95rem;color:var(--text-dim);margin-top:6px;"></div>
    </div>
    <div class="export-card accent2">
      <div class="export-card-title">&#x1F3AE; HTML5 GAME EXPORT</div>
      <p style="font-size:1rem;color:var(--text-dim);margin-bottom:12px;line-height:1.5;">
        Download a complete standalone HTML5 game with your sprites, map, and engine baked in.
      </p>
      <button class="btn accent2" onclick="exportGame()">&#x1F4E6; DOWNLOAD game.html</button>
    </div>
  </div>
</div>
"""

STATUS_BAR = """
<div id="status-bar">
  <div class="status-item">Tool: <span id="sb-tool">PENCIL</span></div>
  <div class="status-item">Canvas: <span id="sb-canvas">16x16</span></div>
  <div class="status-item">Zoom: <span id="sb-zoom">8x</span></div>
  <div class="status-item">Layer: <span id="sb-layer">Layer 1</span></div>
  <div class="status-item">Frame: <span id="sb-frame">1/1</span></div>
  <div class="status-item">Pos: <span id="sb-pos">--,--</span></div>
</div>
"""

JS_SCRIPT = r"""
<script>
(() => {
  const $ = id => document.getElementById(id), clamp = (v,a,b)=>Math.max(a,Math.min(b,v));
  const palettes = {
    db16:['#140c1c','#442434','#30346d','#4e4a4e','#854c30','#346524','#d04648','#757161','#597dce','#d27d2c','#8595a1','#6daa2c','#d2aa99','#6dc2ca','#dad45e','#deeed6'],
    nes:['#7c7c7c','#0000fc','#0000bc','#4428bc','#940084','#a80020','#a81000','#881400','#503000','#007800','#006800','#005800','#004058','#000000','#bcbcbc','#0078f8'],
    gameboy:['#0f380f','#306230','#8bac0f','#9bbc0f'],
    cga:['#000000','#0000aa','#00aa00','#00aaaa','#aa0000','#aa00aa','#aa5500','#aaaaaa','#555555','#5555ff','#55ff55','#55ffff','#ff5555','#ff55ff','#ffff55','#ffffff']
  };

  let size = 16, zoom = 8, tool = 'pencil', fg = '#ff4d6d', bg = '#000000', colorTarget='fg', showGrid = true;
  let onion=false, loop=true, fps=8, playing=false, playTimer=null, drawing=false, dragStart=null, activeFrame=0, activeLayer=0;
  let undoStack=[], redoStack=[];
  const maxHistory=30, mapW=20, mapH=15, tileSize=16;
  let gameMode='platformer', gameOn=false, score=0, selectedTile=-1;
  let gameMap = Array.from({length:mapH},()=>Array.from({length:mapW},()=>-1));
  const gameSprites={player:-1,tile0:-1,tile1:-1,tile2:-1,tile3:-1}, keys={left:false,right:false,up:false,down:false,jump:false};
  const player={x:32,y:32,w:14,h:14,vx:0,vy:0,ground:false}; let gTs=0;

  const makeLayer = n => ({name:n,visible:true,opacity:1,pixels:new Array(size*size).fill(null)});
  const makeFrame = () => ({layers:[makeLayer('Layer 1')]});
  let frames = [makeFrame()];
  const frameLayers = ()=>frames[activeFrame].layers, layer = ()=>frameLayers()[activeLayer];
  const idx=(x,y)=>y*size+x, inb=(x,y)=>x>=0&&y>=0&&x<size&&y<size;
  const snapshot = ()=>JSON.stringify({frames,size,activeFrame,activeLayer});
  const restore = s => { const o=JSON.parse(s); frames=o.frames; size=o.size; activeFrame=Math.min(o.activeFrame,frames.length-1); activeLayer=Math.min(o.activeLayer,frameLayers().length-1); syncProject(); renderAll(); };
  const pushHistory = ()=>{ undoStack.push(snapshot()); if(undoStack.length>maxHistory) undoStack.shift(); redoStack=[]; };

  function switchTab(t){ document.querySelectorAll('.tab-panel').forEach(e=>e.classList.remove('active')); document.querySelectorAll('.tab-btn').forEach(e=>e.classList.remove('active')); $('tab-'+t)?.classList.add('active'); $('tab-'+t+'-btn')?.classList.add('active'); if(t==='game') drawGame(); }
  window.switchTab = switchTab;
  function showLearnSection(i){ document.querySelectorAll('.learn-section').forEach(e=>e.classList.remove('active')); document.querySelectorAll('.learn-nav-btn').forEach((e,n)=>e.classList.toggle('active',n===i)); $('learn-sec-'+i)?.classList.add('active'); }
  window.showLearnSection = showLearnSection;

  const tutPattern = new Set(['1,0','2,0','5,0','6,0','0,1','1,1','2,1','3,1','4,1','5,1','6,1','7,1','0,2','1,2','2,2','3,2','4,2','5,2','6,2','7,2','1,3','2,3','3,3','4,3','5,3','6,3','2,4','3,4','4,4','5,4','3,5','4,5']);
  let tutDone = new Set();
  function drawTutorial(){ const c=$('learn-tut-canvas'); if(!c) return; const x=c.getContext('2d'), s=c.width/8; x.clearRect(0,0,c.width,c.height); for(let py=0;py<8;py++)for(let px=0;px<8;px++){ const k=`${px},${py}`; x.fillStyle=((px+py)%2)?'#21213a':'#19192b'; x.fillRect(px*s,py*s,s,s); if(tutPattern.has(k)){x.fillStyle=tutDone.has(k)?'#ff4d6d':'rgba(255,224,102,.35)'; x.fillRect(px*s+1,py*s+1,s-2,s-2);} x.strokeStyle='rgba(255,255,255,.08)'; x.strokeRect(px*s,py*s,s,s);} const p=Math.round(tutDone.size/tutPattern.size*100); $('tut-progress-bar').style.width=p+'%'; $('tut-step-text').textContent=p<100?`Progress: ${p}%`: 'Great! Heart complete!'; }
  function resetTutorial(){ tutDone = new Set(); drawTutorial(); }
  function autoCompleteTutorial(){ tutDone = new Set(tutPattern); drawTutorial(); }
  window.resetTutorial = resetTutorial; window.autoCompleteTutorial = autoCompleteTutorial;

  const miniFrames = Array.from({length:3},()=>new Array(64).fill(null)); let miniActive=0, miniTimer=null;
  const drawMini = i => { const c=$('mini-frame-'+i), x=c.getContext('2d'), s=c.width/8; x.clearRect(0,0,c.width,c.height); for(let y=0;y<8;y++)for(let xx=0;xx<8;xx++){ const v=miniFrames[i][y*8+xx]; x.fillStyle=v||(((xx+y)%2)?'#20203a':'#19192c'); x.fillRect(xx*s,y*s,s,s); x.strokeStyle='rgba(255,255,255,.07)'; x.strokeRect(xx*s,y*s,s,s);} };
  const drawMiniPreview = i => { const c=$('mini-preview'),x=c.getContext('2d'),s=c.width/8; x.clearRect(0,0,c.width,c.height); miniFrames[i].forEach((v,n)=>{ if(!v) return; x.fillStyle=v; x.fillRect((n%8)*s,((n/8)|0)*s,s,s); }); };
  function setMiniActiveFrame(v){ miniActive=parseInt(v,10)||0; drawMiniPreview(miniActive); }
  function clearMiniFrame(){ miniFrames[miniActive].fill(null); drawMini(miniActive); drawMiniPreview(miniActive); }
  function miniAnimPlay(){ miniAnimStop(); let i=0; miniTimer=setInterval(()=>drawMiniPreview((i++)%3),120); }
  function miniAnimStop(){ if(miniTimer) clearInterval(miniTimer); miniTimer=null; drawMiniPreview(miniActive); }
  window.setMiniActiveFrame=setMiniActiveFrame; window.clearMiniFrame=clearMiniFrame; window.miniAnimPlay=miniAnimPlay; window.miniAnimStop=miniAnimStop;

  function syncProject(){ const c=$('editor-canvas'); c.width=size*zoom; c.height=size*zoom; $('size-select').value=String(size); $('zoom-select').value=String(zoom); $('hdr-size').textContent=`${size}x${size}`; $('sb-canvas').textContent=`${size}x${size}`; $('sb-zoom').textContent=`${zoom}x`; renderFrames(); renderLayers(); refreshSpriteSelectors(); }
  function renderEditor(){ const c=$('editor-canvas'),x=c.getContext('2d'); x.clearRect(0,0,c.width,c.height); for(let y=0;y<size;y++)for(let xx=0;xx<size;xx++){ x.fillStyle=((xx+y)%2)?'#24243a':'#1a1a2d'; x.fillRect(xx*zoom,y*zoom,zoom,zoom); } if(onion&&frames.length>1) composite((activeFrame-1+frames.length)%frames.length,x,zoom,.25); composite(activeFrame,x,zoom,1); if(showGrid&&zoom>=4){ x.strokeStyle='rgba(255,255,255,.11)'; for(let g=0;g<=size;g++){ x.beginPath();x.moveTo(g*zoom+.5,0);x.lineTo(g*zoom+.5,size*zoom);x.stroke(); x.beginPath();x.moveTo(0,g*zoom+.5);x.lineTo(size*zoom,g*zoom+.5);x.stroke(); } } }
  function composite(fi,ctx,px,alpha){ const fr=frames[fi]; ctx.save(); fr.layers.forEach(l=>{ if(!l.visible) return; ctx.save(); ctx.globalAlpha=alpha*l.opacity; l.pixels.forEach((v,i)=>{ if(!v) return; ctx.fillStyle=v; ctx.fillRect((i%size)*px,((i/size)|0)*px,px,px); }); ctx.restore(); }); ctx.restore(); }
  function renderFrames(){ const s=$('frames-scroll'); s.innerHTML=''; frames.forEach((_,i)=>{ const c=document.createElement('canvas'); c.width=52;c.height=52;c.className='frame-thumb'+(i===activeFrame?' active-frame':''); c.onclick=()=>{activeFrame=i;activeLayer=Math.min(activeLayer,frameLayers().length-1);renderAll();}; s.appendChild(c); composite(i,c.getContext('2d'),52/size,1); }); $('frame-count-display').textContent=`${activeFrame+1}/${frames.length}`; $('sb-frame').textContent=`${activeFrame+1}/${frames.length}`; }
  function renderLayers(){ const list=$('layers-list'); list.innerHTML=''; frameLayers().forEach((l,i)=>{ const row=document.createElement('div'); row.className='layer-row'+(i===activeLayer?' active-layer':''); row.onclick=()=>{activeLayer=i;renderAll();}; const eye=document.createElement('span'); eye.className='layer-eye'+(l.visible?'':' hidden'); eye.textContent='👁'; eye.onclick=e=>{e.stopPropagation();l.visible=!l.visible;renderAll();}; const nm=document.createElement('span'); nm.className='layer-name'; nm.textContent=l.name; const op=document.createElement('input'); op.type='range'; op.min='0'; op.max='100'; op.value=String(Math.round(l.opacity*100)); op.className='layer-opacity'; op.oninput=e=>{l.opacity=(parseInt(e.target.value,10)||0)/100;renderEditor();}; const del=document.createElement('span'); del.className='layer-del'; del.textContent='✕'; del.onclick=e=>{e.stopPropagation();deleteLayer(i);}; row.append(eye,nm,op,del); list.appendChild(row); }); $('sb-layer').textContent=layer()?.name||'N/A'; }
  function renderPalette(){ const g=$('palette-grid'), pal=palettes[$('palette-select').value]||palettes.db16; g.innerHTML=''; pal.forEach(c=>{ const d=document.createElement('div'); d.className='palette-cell'; d.style.background=c; d.onclick=()=>{ if(colorTarget==='fg') fg=c; else bg=c; syncColorUI(); }; g.appendChild(d); }); }
  function syncColorUI(){ $('fg-swatch').style.background=fg; $('bg-swatch').style.background=bg; const c=colorTarget==='fg'?fg:bg; $('hex-input').value=c; $('color-picker').value=c; }
  function setTool(t){ tool=t; document.querySelectorAll('#tool-sidebar .tool-btn').forEach(b=>b.classList.remove('active')); $('tool-'+t)?.classList.add('active'); $('sb-tool').textContent=t.toUpperCase(); $('hdr-tool').textContent=t.toUpperCase(); }
  window.setTool=setTool;

  function pt(ev,c=$('editor-canvas'),px=zoom,sz=size){ const r=c.getBoundingClientRect(), cx=(ev.clientX-r.left)*(c.width/r.width), cy=(ev.clientY-r.top)*(c.height/r.height); return {x:clamp(Math.floor(cx/px),0,sz-1),y:clamp(Math.floor(cy/px),0,sz-1)}; }
  function flood(x,y,color){ const l=layer(), t=l.pixels[idx(x,y)]||null; if((color||null)===t) return; const st=[[x,y]], seen=new Set(); while(st.length){ const [cx,cy]=st.pop(),k=cx+','+cy; if(seen.has(k)||!inb(cx,cy)) continue; seen.add(k); const i=idx(cx,cy),v=l.pixels[i]||null; if(v!==t) continue; l.pixels[i]=color; st.push([cx+1,cy],[cx-1,cy],[cx,cy+1],[cx,cy-1]); } }
  function line(x0,y0,x1,y1,c){ let dx=Math.abs(x1-x0),sx=x0<x1?1:-1,dy=-Math.abs(y1-y0),sy=y0<y1?1:-1,e=dx+dy; while(true){ if(inb(x0,y0)) layer().pixels[idx(x0,y0)]=c; if(x0===x1&&y0===y1) break; const e2=2*e; if(e2>=dy){e+=dy;x0+=sx;} if(e2<=dx){e+=dx;y0+=sy;} } }
  function rect(x0,y0,x1,y1,c,f){ const mnx=Math.min(x0,x1),mxx=Math.max(x0,x1),mny=Math.min(y0,y1),mxy=Math.max(y0,y1); for(let y=mny;y<=mxy;y++)for(let x=mnx;x<=mxx;x++){ if(f||x===mnx||x===mxx||y===mny||y===mxy) if(inb(x,y)) layer().pixels[idx(x,y)]=c; } }
  function circ(x0,y0,x1,y1,c,f){ const cx=((x0+x1)/2)|0, cy=((y0+y1)/2)|0, rx=Math.max(1,Math.abs((x1-x0)/2)), ry=Math.max(1,Math.abs((y1-y0)/2)); for(let y=cy-ry;y<=cy+ry;y++)for(let x=cx-rx;x<=cx+rx;x++){ const d=((x-cx)/rx)**2+((y-cy)/ry)**2; if(f?d<=1:d>=.78&&d<=1.22) if(inb(x,y)) layer().pixels[idx(x,y)]=c; } }

  function paintAt(x,y,start,end){ const c=tool==='eraser'?null:fg; if(tool==='pencil'||tool==='eraser'){ layer().pixels[idx(x,y)]=c; return; } if(tool==='fill'&&start){ flood(x,y,c); return; } if(tool==='eyedropper'&&start){ for(let i=frameLayers().length-1;i>=0;i--){ const v=frameLayers()[i].pixels[idx(x,y)]; if(v){ if(colorTarget==='fg') fg=v; else bg=v; syncColorUI(); break; } } return; } if(['line','rect','fillrect','circle','fillcircle'].includes(tool)){ if(start) dragStart={x,y}; if(end&&dragStart){ if(tool==='line') line(dragStart.x,dragStart.y,x,y,c); if(tool==='rect') rect(dragStart.x,dragStart.y,x,y,c,false); if(tool==='fillrect') rect(dragStart.x,dragStart.y,x,y,c,true); if(tool==='circle') circ(dragStart.x,dragStart.y,x,y,c,false); if(tool==='fillcircle') circ(dragStart.x,dragStart.y,x,y,c,true); dragStart=null; } } }

  function resizeCanvas(v){ pushHistory(); const n=clamp(parseInt(v,10)||16,8,64); frames=frames.map(fr=>({layers:fr.layers.map(l=>{ const old=Math.sqrt(l.pixels.length)|0,nl={...l,pixels:new Array(n*n).fill(null)}; for(let y=0;y<Math.min(old,n);y++)for(let x=0;x<Math.min(old,n);x++) nl.pixels[y*n+x]=l.pixels[y*old+x]; return nl; })})); size=n; syncProject(); renderAll(); }
  function setZoom(v){ zoom=clamp(parseInt(v,10)||8,2,16); syncProject(); renderEditor(); }
  function toggleGrid(){ showGrid=!showGrid; $('grid-btn').textContent=`⋯ GRID: ${showGrid?'ON':'OFF'}`; renderEditor(); }
  function clearActiveLayer(){ pushHistory(); layer().pixels.fill(null); renderAll(); }
  function newProject(){ if(!confirm('Start new project?')) return; frames=[makeFrame()]; activeFrame=0; activeLayer=0; undoStack=[]; redoStack=[]; syncProject(); renderAll(); }
  function undo(){ if(!undoStack.length) return; redoStack.push(snapshot()); restore(undoStack.pop()); }
  function redo(){ if(!redoStack.length) return; undoStack.push(snapshot()); restore(redoStack.pop()); }
  function addFrame(){ pushHistory(); frames.push(JSON.parse(JSON.stringify(frames[activeFrame]))); activeFrame=frames.length-1; renderAll(); }
  function deleteFrame(){ if(frames.length<=1) return; pushHistory(); frames.splice(activeFrame,1); activeFrame=Math.min(activeFrame,frames.length-1); renderAll(); }
  function duplicateFrame(){ pushHistory(); frames.splice(activeFrame+1,0,JSON.parse(JSON.stringify(frames[activeFrame]))); activeFrame++; renderAll(); }
  function setFPS(v){ fps=clamp(parseInt(v,10)||8,1,30); $('fps-display').textContent=String(fps); if(playing){ toggleAnim(); toggleAnim(); } }
  function toggleOnionSkin(){ onion=!onion; $('onion-btn').textContent=`ONION: ${onion?'ON':'OFF'}`; renderEditor(); }
  function toggleLoop(){ loop=!loop; $('loop-btn').textContent=`LOOP: ${loop?'ON':'OFF'}`; }
  function toggleAnim(){ if(playing){ clearInterval(playTimer); playTimer=null; playing=false; $('play-btn').innerHTML='▶ PLAY'; $('playing-dot').classList.add('hidden'); return; } playing=true; $('play-btn').innerHTML='⏸ STOP'; $('playing-dot').classList.remove('hidden'); playTimer=setInterval(()=>{ if(activeFrame===frames.length-1&&!loop){ toggleAnim(); return; } activeFrame=(activeFrame+1)%frames.length; renderAll(); },1000/fps); }
  function openColorPicker(t){ colorTarget=t; syncColorUI(); $('color-picker').click(); }
  function swapColors(){ const t=fg; fg=bg; bg=t; syncColorUI(); }
  function onHexInput(v){ if(!/^#?[0-9a-fA-F]{6}$/.test(v)) return; const h=(v[0]==='#'?v:'#'+v).toLowerCase(); if(colorTarget==='fg') fg=h; else bg=h; syncColorUI(); }
  function onColorPickerChange(v){ const h=v.toLowerCase(); if(colorTarget==='fg') fg=h; else bg=h; syncColorUI(); }
  function loadPalette(){ renderPalette(); }
  function addLayer(){ if(frameLayers().length>=8) return; pushHistory(); frames.forEach(fr=>fr.layers.push(makeLayer('Layer '+(fr.layers.length+1)))); activeLayer=frameLayers().length-1; renderAll(); }
  function deleteLayer(i=activeLayer){ if(frameLayers().length<=1) return; pushHistory(); frames.forEach(fr=>fr.layers.splice(i,1)); activeLayer=Math.min(activeLayer,frameLayers().length-1); renderAll(); }
  function moveLayerUp(){ if(activeLayer<=0) return; pushHistory(); frames.forEach(fr=>{ const t=fr.layers[activeLayer-1]; fr.layers[activeLayer-1]=fr.layers[activeLayer]; fr.layers[activeLayer]=t; }); activeLayer--; renderAll(); }
  function moveLayerDown(){ if(activeLayer>=frameLayers().length-1) return; pushHistory(); frames.forEach(fr=>{ const t=fr.layers[activeLayer+1]; fr.layers[activeLayer+1]=fr.layers[activeLayer]; fr.layers[activeLayer]=t; }); activeLayer++; renderAll(); }
  Object.assign(window,{resizeCanvas,setZoom,toggleGrid,clearActiveLayer,newProject,undo,redo,addFrame,deleteFrame,duplicateFrame,setFPS,toggleOnionSkin,toggleLoop,toggleAnim,openColorPicker,swapColors,onHexInput,onColorPickerChange,loadPalette,addLayer,deleteLayer,moveLayerUp,moveLayerDown});

  const frameCanvas = (fi,s=1)=>{ const c=document.createElement('canvas'); c.width=size*s; c.height=size*s; composite(fi,c.getContext('2d'),s,1); return c; };
  const dl = (blob,name)=>{ const u=URL.createObjectURL(blob),a=document.createElement('a'); a.href=u;a.download=name; document.body.appendChild(a);a.click();a.remove(); setTimeout(()=>URL.revokeObjectURL(u),1200); };
  function exportPNGCurrentFrame(){ frameCanvas(activeFrame).toBlob(b=>b&&dl(b,'frame.png'),'image/png'); }
  function exportPNGAllFrames(){ frames.forEach((_,i)=>frameCanvas(i).toBlob(b=>b&&dl(b,`frame_${i}.png`),'image/png')); }
  function exportSpriteSheet(){ const cols=clamp(parseInt($('sheet-cols').value,10)||4,1,32),rows=Math.ceil(frames.length/cols),c=document.createElement('canvas'); c.width=cols*size;c.height=rows*size; const x=c.getContext('2d'); frames.forEach((_,i)=>x.drawImage(frameCanvas(i), (i%cols)*size, ((i/cols)|0)*size)); c.toBlob(b=>b&&dl(b,'spritesheet.png'),'image/png'); $('sheet-preview').src=c.toDataURL('image/png'); $('sheet-preview').style.display='block'; }
  function lzw(min,idxs){ const clear=1<<min,end=clear+1; let dict=new Map(), reset=()=>{dict=new Map();for(let i=0;i<clear;i++)dict.set(String(i),i)}; reset(); let sz=min+1,next=end+1,codes=[clear],w=String(idxs[0]||0); for(let i=1;i<idxs.length;i++){ const k=String(idxs[i]),wk=w+','+k; if(dict.has(wk)) w=wk; else { codes.push(dict.get(w)); if(next<4096){ dict.set(wk,next++); if(next===(1<<sz)&&sz<12) sz++; } else { codes.push(clear); reset(); sz=min+1; next=end+1; } w=k; } } codes.push(dict.get(w)); codes.push(end); const out=[]; let b=0,bl=0,cSz=min+1,dSz=end+1; const wr=(c,s)=>{ b|=c<<bl; bl+=s; while(bl>=8){ out.push(b&255); b>>=8; bl-=8; } }; for(const c of codes){ wr(c,cSz); if(c===clear){ cSz=min+1; dSz=end+1; } else if(c!==end){ dSz++; if(dSz===(1<<cSz)&&cSz<12) cSz++; } } if(bl>0) out.push(b&255); return out; }
  function exportGIF(){ $('gif-status').textContent='Encoding GIF...'; try{ const fcs=frames.map((_,i)=>frameCanvas(i)), w=fcs[0].width,h=fcs[0].height, pal=new Map([['0,0,0,0',0]]); for(const c of fcs){ const d=c.getContext('2d').getImageData(0,0,w,h).data; for(let i=0;i<d.length&&pal.size<256;i+=4){ if(d[i+3]<8) continue; const k=`${d[i]},${d[i+1]},${d[i+2]},255`; if(!pal.has(k)) pal.set(k,pal.size); } } const entries=[...pal.keys()].map(k=>k.split(',').map(Number)), p2=Math.max(2,Math.ceil(Math.log2(Math.max(2,entries.length)))); while(entries.length<(1<<p2)) entries.push([0,0,0,0]); const min=Math.max(2,p2), bytes=[], push=(...a)=>a.forEach(v=>bytes.push(v&255)), u16=n=>push(n&255,(n>>8)&255); push(71,73,70,56,57,97); u16(w);u16(h); push(128|112|(p2-1),0,0); entries.forEach(([r,g,b])=>push(r,g,b)); push(33,255,11,78,69,84,83,67,65,80,69,50,46,48,3,1,0,0,0); const delay=Math.max(1,Math.round(100/(clamp(parseInt($('gif-fps').value,10)||fps,1,30)))); for(const c of fcs){ const d=c.getContext('2d').getImageData(0,0,w,h).data, idxs=new Uint8Array(w*h); for(let i=0,p=0;i<d.length;i+=4,p++){ if(d[i+3]<8){ idxs[p]=0; continue; } const k=`${d[i]},${d[i+1]},${d[i+2]},255`; idxs[p]=pal.get(k)||0; } push(33,249,4,1);u16(delay);push(0,0); push(44);u16(0);u16(0);u16(w);u16(h);push(0); push(min); const data=lzw(min,idxs); for(let i=0;i<data.length;i+=255){ const b=data.slice(i,i+255); push(b.length); b.forEach(v=>push(v)); } push(0); } push(59); const blob=new Blob([new Uint8Array(bytes)],{type:'image/gif'}); dl(blob,'animation.gif'); $('gif-preview').src=URL.createObjectURL(blob); $('gif-preview').style.display='block'; $('gif-status').textContent='GIF ready.'; }catch(e){ $('gif-status').textContent='GIF failed: '+e.message; } }
  async function exportWebM(){ if(!window.MediaRecorder){ $('webm-status').textContent='MediaRecorder unsupported.'; return; } const ff=clamp(parseInt($('webm-fps').value,10)||fps,1,30), c=document.createElement('canvas'); c.width=size*8;c.height=size*8; const x=c.getContext('2d'),stream=c.captureStream(ff),chunks=[],rec=new MediaRecorder(stream,{mimeType:'video/webm'}); rec.ondataavailable=e=>e.data?.size&&chunks.push(e.data); rec.onstop=()=>dl(new Blob(chunks,{type:'video/webm'}),'animation.webm'); $('webm-status').textContent='Recording...'; rec.start(); for(let i=0;i<frames.length;i++){ x.clearRect(0,0,c.width,c.height); x.drawImage(frameCanvas(i,8),0,0); await new Promise(r=>setTimeout(r,1000/ff)); } rec.stop(); $('webm-status').textContent='WebM complete.'; }
  function exportGame(){ const data={mode:gameMode,map:gameMap}; const html=`<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><style>body{margin:0;background:#111;color:#eee;font-family:monospace}canvas{display:block;margin:12px auto;border:2px solid #5cf}</style></head><body><canvas id=g width=320 height=240></canvas><script>const D=${JSON.stringify(data)},c=document.getElementById('g'),x=c.getContext('2d'),t=16,p={x:32,y:32,w:14,h:14,vx:0,vy:0,g:0},k={l:0,r:0,u:0,d:0,j:0}; addEventListener('keydown',e=>{if(['a','ArrowLeft'].includes(e.key))k.l=1;if(['d','ArrowRight'].includes(e.key))k.r=1;if(['w','ArrowUp'].includes(e.key))k.u=1;if(['s','ArrowDown'].includes(e.key))k.d=1;if(e.key===' ')k.j=1}); addEventListener('keyup',e=>{if(['a','ArrowLeft'].includes(e.key))k.l=0;if(['d','ArrowRight'].includes(e.key))k.r=0;if(['w','ArrowUp'].includes(e.key))k.u=0;if(['s','ArrowDown'].includes(e.key))k.d=0;if(e.key===' ')k.j=0}); const mt=(x0,y0)=>x0<0||y0<0||y0>=D.map.length||x0>=D.map[0].length?1:D.map[y0][x0],solid=v=>D.mode==='platformer'?(v===0||v===1):(v===1); function lp(){ if(D.mode==='platformer'){ p.vx=(k.l?-1.5:0)+(k.r?1.5:0); if((k.j||k.u)&&p.g){p.vy=-4.6;p.g=0} p.vy=Math.min(5,p.vy+.22); let nx=p.x+p.vx,ny=p.y,l=Math.floor(nx/t),r=Math.floor((nx+p.w-1)/t),tt=Math.floor(ny/t),b=Math.floor((ny+p.h-1)/t); if((p.vx<0&&(solid(mt(l,tt))||solid(mt(l,b))))||(p.vx>0&&(solid(mt(r,tt))||solid(mt(r,b)))))nx=p.x; p.x=nx; ny=p.y+p.vy; tt=Math.floor(ny/t);b=Math.floor((ny+p.h-1)/t); l=Math.floor(p.x/t);r=Math.floor((p.x+p.w-1)/t); if(p.vy>0&&(solid(mt(l,b))||solid(mt(r,b)))){ny=b*t-p.h;p.vy=0;p.g=1}else if(p.vy<0&&(solid(mt(l,tt))||solid(mt(r,tt)))){ny=(tt+1)*t;p.vy=0} p.y=ny; } else { let nx=p.x+(k.l?-1.5:0)+(k.r?1.5:0), ny=p.y+(k.u?-1.5:0)+(k.d?1.5:0), l=Math.floor(nx/t),r=Math.floor((nx+p.w-1)/t),tt=Math.floor(ny/t),b=Math.floor((ny+p.h-1)/t); if(!(solid(mt(l,tt))||solid(mt(r,tt))||solid(mt(l,b))||solid(mt(r,b)))){p.x=nx;p.y=ny} } x.fillStyle='#000';x.fillRect(0,0,c.width,c.height); for(let y=0;y<D.map.length;y++)for(let xx=0;xx<D.map[y].length;xx++){ const v=D.map[y][xx]; if(v<0) continue; x.fillStyle=v===0?'#346524':v===1?'#666':v===2?'#d04648':'#ffe066'; x.fillRect(xx*t,y*t,t,t)} x.fillStyle='#00ffcc';x.fillRect(p.x,p.y,p.w,p.h); requestAnimationFrame(lp)} lp();<\\/script></body></html>`; dl(new Blob([html],{type:'text/html'}),'game.html'); }
  Object.assign(window,{exportPNGCurrentFrame,exportPNGAllFrames,exportSpriteSheet,exportGIF,exportWebM,exportGame});

  function refreshSpriteSelectors(){ ['game-player-select','game-tile0-select','game-tile1-select','game-tile2-select','game-tile3-select'].forEach(id=>{ const s=$(id),old=s.value; s.innerHTML='<option value=\"-1\">-- None --</option>'; frames.forEach((_,i)=>{ const o=document.createElement('option'); o.value=String(i); o.textContent='Frame '+(i+1); s.appendChild(o); }); if([...s.options].some(o=>o.value===old)) s.value=old; }); drawSpriteSlots(); }
  function assignSprite(slot,i){ gameSprites[slot]=Number.isFinite(i)?i:-1; drawSpriteSlots(); drawMapEditor(); drawGame(); }
  function drawPrev(c,fi){ if(!c) return; const x=c.getContext('2d'); x.clearRect(0,0,c.width,c.height); if(fi<0||fi>=frames.length){ x.fillStyle='#111';x.fillRect(0,0,c.width,c.height); return; } x.drawImage(frameCanvas(fi,1),0,0,c.width,c.height); }
  function drawSpriteSlots(){ drawPrev($('game-player-canvas'),gameSprites.player); drawPrev($('game-tile0-canvas'),gameSprites.tile0); drawPrev($('game-tile1-canvas'),gameSprites.tile1); drawPrev($('game-tile2-canvas'),gameSprites.tile2); drawPrev($('game-tile3-canvas'),gameSprites.tile3); drawPrev($('ts-0'),gameSprites.tile0); drawPrev($('ts-1'),gameSprites.tile1); drawPrev($('ts-2'),gameSprites.tile2); drawPrev($('ts-3'),gameSprites.tile3); }
  function selectTileType(t){ selectedTile=t; document.querySelectorAll('.tile-select-btn').forEach(e=>e.classList.remove('active-tile')); (t===-1?$('ts-erase'):$('ts-'+t))?.classList.add('active-tile'); }
  function clearGameMap(){ gameMap=Array.from({length:mapH},()=>Array.from({length:mapW},()=>-1)); drawMapEditor(); drawGame(); }
  function fillGroundRow(){ for(let x=0;x<mapW;x++) gameMap[mapH-1][x]=0; drawMapEditor(); drawGame(); }
  function setGameMode(m){ gameMode=m; $('mode-platformer-btn').classList.toggle('active-tool',m==='platformer'); $('mode-topdown-btn').classList.toggle('active-tool',m==='topdown'); }
  function dpadPress(k){ keys[k]=true; $('dpad-'+k)?.classList.add('pressed'); } function dpadRelease(k){ keys[k]=false; $('dpad-'+k)?.classList.remove('pressed'); }
  Object.assign(window,{assignSprite,selectTileType,clearGameMap,fillGroundRow,setGameMode,dpadPress,dpadRelease});
  function drawMapEditor(){ const c=$('map-editor-canvas'),x=c.getContext('2d'),s=c.width/mapW; x.clearRect(0,0,c.width,c.height); for(let y=0;y<mapH;y++)for(let xx=0;xx<mapW;xx++){ x.fillStyle='#121222'; x.fillRect(xx*s,y*s,s,s); const t=gameMap[y][xx],k=t===0?'tile0':t===1?'tile1':t===2?'tile2':t===3?'tile3':null; if(k&&gameSprites[k]>=0) x.drawImage(frameCanvas(gameSprites[k],1),xx*s,y*s,s,s); else if(t>=0){ x.fillStyle=t===0?'#346524':t===1?'#6a6a7f':t===2?'#d04648':'#ffe066'; x.fillRect(xx*s+1,y*s+1,s-2,s-2); } x.strokeStyle='rgba(255,255,255,.09)'; x.strokeRect(xx*s,y*s,s,s); } }
  const mapTile=(tx,ty)=>tx<0||ty<0||tx>=mapW||ty>=mapH?1:gameMap[ty][tx], solid=t=>gameMode==='platformer'?(t===0||t===1):(t===1);
  function drawGame(){ const c=$('game-canvas'),x=c.getContext('2d'); x.fillStyle='#0b0b15'; x.fillRect(0,0,c.width,c.height); for(let y=0;y<mapH;y++)for(let xx=0;xx<mapW;xx++){ const t=gameMap[y][xx],k=t===0?'tile0':t===1?'tile1':t===2?'tile2':t===3?'tile3':null; if(k&&gameSprites[k]>=0) x.drawImage(frameCanvas(gameSprites[k],1),xx*tileSize,y*tileSize,tileSize,tileSize); else if(t>=0){ x.fillStyle=t===0?'#346524':t===1?'#666688':t===2?'#d04648':'#ffe066'; x.fillRect(xx*tileSize,y*tileSize,tileSize,tileSize);} } if(gameSprites.player>=0) x.drawImage(frameCanvas(gameSprites.player,1),player.x,player.y,player.w,player.h); else { x.fillStyle='#00ffcc';x.fillRect(player.x,player.y,player.w,player.h); } $('game-score-display').textContent='Score: '+score; }
  function stepGame(dt){ if(gameMode==='platformer'){ player.vx=(keys.left?-82:0)+(keys.right?82:0); if((keys.jump||keys.up)&&player.ground){player.vy=-150;player.ground=false;} player.vy=Math.min(260,player.vy+380*dt); let nx=player.x+player.vx*dt, ny=player.y, l=Math.floor(nx/tileSize),r=Math.floor((nx+player.w-1)/tileSize),t=Math.floor(ny/tileSize),b=Math.floor((ny+player.h-1)/tileSize); if((player.vx<0&&(solid(mapTile(l,t))||solid(mapTile(l,b))))||(player.vx>0&&(solid(mapTile(r,t))||solid(mapTile(r,b))))) nx=player.x; player.x=nx; ny=player.y+player.vy*dt; t=Math.floor(ny/tileSize);b=Math.floor((ny+player.h-1)/tileSize); l=Math.floor(player.x/tileSize);r=Math.floor((player.x+player.w-1)/tileSize); if(player.vy>0&&(solid(mapTile(l,b))||solid(mapTile(r,b)))){ny=b*tileSize-player.h;player.vy=0;player.ground=true}else if(player.vy<0&&(solid(mapTile(l,t))||solid(mapTile(r,t)))){ny=(t+1)*tileSize;player.vy=0} player.y=ny; } else { const sp=88*dt; let nx=player.x+(keys.left?-sp:0)+(keys.right?sp:0), ny=player.y+(keys.up?-sp:0)+(keys.down?sp:0), l=Math.floor(nx/tileSize),r=Math.floor((nx+player.w-1)/tileSize),t=Math.floor(ny/tileSize),b=Math.floor((ny+player.h-1)/tileSize); if(!(solid(mapTile(l,t))||solid(mapTile(r,t))||solid(mapTile(l,b))||solid(mapTile(r,b)))){player.x=nx;player.y=ny;} } player.x=clamp(player.x,0,mapW*tileSize-player.w); player.y=clamp(player.y,0,mapH*tileSize-player.h); const tx=Math.floor((player.x+player.w/2)/tileSize),ty=Math.floor((player.y+player.h/2)/tileSize),tv=mapTile(tx,ty); if(tv===3){gameMap[ty][tx]=-1;score+=10;} if(tv===2){player.x=32;player.y=32;player.vx=0;player.vy=0;score=Math.max(0,score-5);} }
  function gameLoop(ts){ if(!gameOn) return; const dt=Math.min(.033,(ts-gTs)/1000||.016); gTs=ts; stepGame(dt); drawGame(); requestAnimationFrame(gameLoop); }
  function toggleGame(){ gameOn=!gameOn; $('game-play-btn').innerHTML=gameOn?'⏸ STOP GAME':'▶ PLAY GAME'; if(gameOn){ gTs=performance.now(); requestAnimationFrame(gameLoop); } }
  window.toggleGame=toggleGame;

  function renderAll(){ renderEditor(); renderFrames(); renderLayers(); drawMapEditor(); drawSpriteSlots(); }

  function bindEvents(){
    $('editor-canvas').addEventListener('mousedown',e=>{ pushHistory(); drawing=true; const p=pt(e); paintAt(p.x,p.y,true,false); renderEditor(); });
    $('editor-canvas').addEventListener('mousemove',e=>{ const p=pt(e); $('cursor-pos').textContent=`X:${p.x} Y:${p.y}`; $('sb-pos').textContent=`${p.x},${p.y}`; if(drawing&&(tool==='pencil'||tool==='eraser')){ paintAt(p.x,p.y,false,false); renderEditor(); } });
    $('editor-canvas').addEventListener('mouseup',e=>{ if(!drawing) return; drawing=false; const p=pt(e); paintAt(p.x,p.y,false,true); renderAll(); });
    $('editor-canvas').addEventListener('mouseleave',()=>{ drawing=false; $('cursor-pos').textContent='X:-- Y:--'; $('sb-pos').textContent='--,--'; });
    $('editor-canvas').addEventListener('touchstart',e=>{ e.preventDefault(); pushHistory(); drawing=true; const p=pt(e.touches[0]); paintAt(p.x,p.y,true,false); renderEditor(); },{passive:false});
    $('editor-canvas').addEventListener('touchmove',e=>{ e.preventDefault(); if(!drawing) return; const p=pt(e.touches[0]); if(tool==='pencil'||tool==='eraser'){ paintAt(p.x,p.y,false,false); renderEditor(); } },{passive:false});
    $('editor-canvas').addEventListener('touchend',e=>{ e.preventDefault(); drawing=false; if(dragStart){ paintAt(dragStart.x,dragStart.y,false,true); renderAll(); } },{passive:false});
    $('map-editor-canvas').addEventListener('mousedown',e=>{ const r=e.target.getBoundingClientRect(),tx=clamp(Math.floor((e.clientX-r.left)/r.width*mapW),0,mapW-1),ty=clamp(Math.floor((e.clientY-r.top)/r.height*mapH),0,mapH-1); gameMap[ty][tx]=selectedTile; drawMapEditor(); drawGame(); });
    $('learn-tut-canvas').addEventListener('click',e=>{ const p=pt(e,$('learn-tut-canvas'),$('learn-tut-canvas').width/8,8),k=`${p.x},${p.y}`; if(tutPattern.has(k)) tutDone.add(k); drawTutorial(); });
    for(let i=0;i<3;i++) $('mini-frame-'+i).addEventListener('mousedown',e=>{ const p=pt(e,$('mini-frame-'+i),$('mini-frame-'+i).width/8,8); miniFrames[i][p.y*8+p.x]=$('mini-color').value; drawMini(i); if(i===miniActive) drawMiniPreview(i); });
    addEventListener('keydown',e=>{ const k=e.key.toLowerCase(); if(e.ctrlKey&&k==='z'){e.preventDefault();undo();} else if(e.ctrlKey&&k==='y'){e.preventDefault();redo();} if(k==='b')setTool('pencil'); if(k==='e')setTool('eraser'); if(k==='f')setTool('fill'); if(k==='i')setTool('eyedropper'); if(k==='l')setTool('line'); if(k==='r')setTool('rect'); if(k==='c')setTool('circle'); if(e.key==='[')setZoom(Math.max(2,zoom/2)); if(e.key===']')setZoom(Math.min(16,zoom*2)); if(k==='a'||e.key==='ArrowLeft')keys.left=true; if(k==='d'||e.key==='ArrowRight')keys.right=true; if(k==='w'||e.key==='ArrowUp')keys.up=true; if(k==='s'||e.key==='ArrowDown')keys.down=true; if(e.key===' ')keys.jump=true; });
    addEventListener('keyup',e=>{ const k=e.key.toLowerCase(); if(k==='a'||e.key==='ArrowLeft')keys.left=false; if(k==='d'||e.key==='ArrowRight')keys.right=false; if(k==='w'||e.key==='ArrowUp')keys.up=false; if(k==='s'||e.key==='ArrowDown')keys.down=false; if(e.key===' ')keys.jump=false; });
  }

  function seed(){ const c=(size/2)|0; for(let y=c-3;y<=c+3;y++)for(let x=c-3;x<=c+3;x++){ if(Math.abs(x-c)+Math.abs(y-c)<=4&&inb(x,y)) layer().pixels[idx(x,y)]='#ff4d6d'; } }
  function initLearnVisuals(){
    const ids=['learn-walk-canvas','learn-idle-canvas','learn-explosion-canvas','learn-coin-canvas','learn-fire-canvas'];
    ids.forEach((id,n)=>{ const c=$(id),x=c.getContext('2d'); let t=0; setInterval(()=>{ x.clearRect(0,0,c.width,c.height); for(let i=0;i<7;i++){ x.fillStyle=(i+n)%3===0?'#00ffcc':(i+n)%3===1?'#ff4d6d':'#ffe066'; x.fillRect(8+i*7,28+Math.sin((t+i)/3)*8,5,5);} t++; },120); });
    [['pal-demo-db16',palettes.db16],['pal-demo-nes',palettes.nes],['pal-demo-gb',palettes.gameboy],['pal-demo-cga',palettes.cga]].forEach(([id,p])=>{ const e=$(id); p.forEach(c=>{ const d=document.createElement('div'); d.className='palette-demo-swatch'; d.style.background=c; d.onclick=()=>{fg=c;colorTarget='fg';syncColorUI();switchTab('create');}; e.appendChild(d); }); });
  }

  function init(){
    seed(); for(let x=0;x<mapW;x++) gameMap[mapH-1][x]=0;
    syncProject(); setTool('pencil'); renderPalette(); syncColorUI(); renderAll();
    for(let i=0;i<3;i++) drawMini(i); drawMiniPreview(0); drawTutorial(); initLearnVisuals(); bindEvents(); drawGame();
  }
  addEventListener('load',init);
})();
</script>
"""


def build_html() -> str:
    return (
        HTML_BODY
        .replace('CSSPLACEHOLDER', CSS)
        .replace('TABLEARN', TAB_LEARN)
        .replace('TABCREATE', TAB_CREATE)
        .replace('TABGAME', TAB_GAME)
        .replace('TABEXPORT', TAB_EXPORT)
        .replace('STATUSBAR', STATUS_BAR)
        .replace('JSSCRIPT', JS_SCRIPT)
    )


def main() -> None:
    html = build_html()
    sys.stdout.write(html)
    from pathlib import Path
    Path(__file__).with_name('index.html').write_text(html, encoding='utf-8')


if __name__ == '__main__':
    main()
