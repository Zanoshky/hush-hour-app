#!/usr/bin/env python3
"""Builds the guide pages in docs/ from the bodies below. Run after any edit and commit docs/. Fails on any dash."""
from pathlib import Path

D = Path(__file__).parent / "docs"
REPO = "https://github.com/Zanoshky/hush-hour-app"
PLAY = "https://play.google.com/store/apps/details?id=com.zanoshky.hushhour"
NAV = [("index.html", "Home"), ("guide.html", "Guide"), ("faq.html", "Questions"), ("report.html", "Report a bug")]


def page(name, title, desc, body):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == name else ""}>{t}</a>' for h, t in NAV)
    for bad in ("—", "–", " - "):
        if bad in body:
            raise SystemExit(f"{name}: dash {bad!r} in copy")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Hush Hour user guide</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060817">
<meta property="og:title" content="{title} · Hush Hour user guide">
<meta property="og:description" content="{desc}">
<link rel="icon" href="img/icon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/inter-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/icon.svg" alt="" width="36" height="36"><span>Hush Hour</span></a>
    <nav aria-label="Guide pages">{nav}</nav>
  </div>
</header>
<main id="main" class="page">
  <div class="wrap">
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <span>Guide text and images are shared under CC BY 4.0. The Hush Hour app itself is proprietary. Made by Marko Zanoski.</span>
    <nav aria-label="Footer"><a href="{PLAY}">Google Play</a><a href="https://hushhour.zanoski.com">hushhour.zanoski.com</a><a href="{REPO}/issues">Issues</a><a href="https://hushhour.zanoski.com/privacy">Privacy</a></nav>
  </div>
</footer>
</body>
</html>
"""
    (D / name).write_text(html)
    print(name)


page("index.html", "Home", "The user guide for Hush Hour, the white noise and sleep sound app for Android.", f"""
    <p class="kicker">User guide</p>
    <h1>Hush Hour</h1>
    <p class="lede" style="margin-left:0;text-align:left">Real rain, sea, stream, forest, crickets and fire recordings and white, pink and brown noise, mixed your way over a living night scene. Pay once, no ads, works offline.</p>
    <div class="shots">
      <figure><img src="img/home-playing.jpg" alt="Home while playing: the time, the mix, the timer chips and the pause button over a night scene with a campfire, water and rain." width="540" height="1200" fetchpriority="high"><figcaption>Home, playing a mix</figcaption></figure>
      <figure><img src="img/sounds.jpg" alt="The sound tiles: Rain, Window, Roof, Tent, Downpour, Storm, Ocean, Stream, Forest, Wind, Crickets, Campfire, Fireplace, Fan and White noise." width="540" height="1200" loading="lazy"><figcaption>The sounds</figcaption></figure>
      <figure><img src="img/mixes.jpg" alt="The Mixes page with a box to save the current mix and ready made mixes like Rainy cabin and Summer night." width="540" height="1200" loading="lazy"><figcaption>Mixes</figcaption></figure>
      <figure><img src="img/settings.jpg" alt="Settings: theme, still scene, sleep timer fade." width="540" height="1200" loading="lazy"><figcaption>Settings</figcaption></figure>
    </div>
    <div class="cta" style="justify-content:flex-start">
      <a class="btn main" href="guide.html">Read the guide</a>
      <a class="btn ghost" href="report.html">Report a bug or ask for a feature</a>
    </div>
""")

page("guide.html", "Guide", "How to use Hush Hour: sounds, mixes, the sleep timer, the dim screen, the widget and settings.", """
    <p class="kicker">Guide</p>
    <h1>How Hush Hour works</h1>

    <h2>Start in one tap</h2>
    <p>Press the big play button on home. The first time, soft rain on the roof plays. The line under the time says what plays and how long until it fades out.</p>

    <h2>Sounds</h2>
    <p>Scroll down to the sound tiles. Tap a tile to add its sound to the mix, tap it again to take it out. A tile that is on glows in its colour, gets a bright edge and a dot in the corner. You can play up to eight sounds at once.</p>
    <dl>
      <dt>Rain</dt><dd>Rain on a yard, rain on the glass (Window), on the roof, on a tent, a mountain downpour, and a storm with far thunder now and then.</dd>
      <dt>Water</dt><dd>Waves on the shore (Ocean) and a river murmur (Stream).</dd>
      <dt>Woods and night</dt><dd>Birds in the trees (Forest), wind in the leaves, and crickets on a summer night with an owl now and then.</dd>
      <dt>Fire</dt><dd>A campfire and a fireplace, with a log popping now and then.</dd>
      <dt>Noise</dt><dd>A bedroom fan, and white, pink and brown noise. White is bright like a hiss, pink is softer like steady rain, brown is deep and low.</dd>
    </dl>
    <p>Rare moments (thunder, the owl, a pop in the fire) can be turned off in Settings, Sound.</p>

    <h2>Your mix</h2>
    <p>Under the tiles, each sound in the mix has its own slider, and a cross to take it out. The Overall level slider sets the whole mix. Keep it low: soft enough that you could talk over it.</p>
    <p>Tap Save this mix, give it a name and tap Save. Your mixes are on the Mixes page (the stacked layers button at the top left of home), with nine ready made ones like Rainy cabin, Storm at sea and Deep focus. Tap a mix to play it. The cross on your own mixes deletes them.</p>

    <h2>The sleep timer</h2>
    <p>The chips on home set the timer: 15 or 30 minutes, 45 (the default), 1 hour, 1 hour 30, 2 hours, or All night. The timer starts when you press play. Near the end the sound fades out slowly, over 10 minutes by default; pick 5 or 20 in Settings, Sleep timer.</p>
    <p>Why a timer by default? Steady sound helps most while you fall asleep, and one study found noise left on all night took some dream sleep. All night is there if you want it.</p>

    <h2>The night scene</h2>
    <p>The scene behind home shows what you hear: rain falls for the rain sounds, drops gather on the glass for Window, the clouds light up softly when the storm's thunder rolls, the sea fills the valley, a campfire burns with embers rising, fireflies come out over the crickets and the forest, mist moves with the wind, and noise hangs an aurora in the sky.</p>
    <p>It only moves while you look at it. With the screen off or the app in the background nothing is drawn. If you like it calm, turn on Settings, Look, Still scene. With animations turned off in Android, it stands still too.</p>

    <h2>Dim the screen</h2>
    <p>Tap the moon button at the top of home. The screen goes black with only the time, in a dim grey, and the brightness drops to the lowest. Tap anywhere, or press Back, to wake it.</p>

    <h2>With the screen off</h2>
    <p>Sound keeps playing with the screen off. The notification and the lock screen show what plays, with pause and stop. A call or an alarm pauses it, and it comes back after. If headphones come out, it pauses so the sound never jumps to the speaker (you can turn that off in Settings, Sound). To play under a podcast or audiobook, turn on Play along with other apps.</p>

    <h2>The widget</h2>
    <p>Settings, Home screen, Add the widget. Or touch and hold your home screen, pick Widgets, then Hush Hour. The widget shows the mix and plays or pauses it with one tap. Tap its words to open the app.</p>

    <h2>Settings</h2>
    <dl>
      <dt>Look</dt><dd>Night, a deep midnight sky, or True black for OLED screens and dark rooms. Still scene stops all motion.</dd>
      <dt>Sleep timer</dt><dd>How long the fade at the end takes.</dd>
      <dt>Sound</dt><dd>Rare moments on or off; Keep it quiet, a soft ceiling on loudness (on by default); pause when headphones come out; play along with other apps.</dd>
      <dt>Help</dt><dd>This guide, the report page and the privacy policy.</dd>
    </dl>

    <h2>Accessibility</h2>
    <p>Every control has a TalkBack label, and each sound tile is read as a switch that is on or off. Touch targets are at least 48 dp, text grows with the phone's font size (the tiles get wider as it does), and text keeps a 7 to 1 contrast in both themes.</p>
""")

page("faq.html", "Questions", "Answers to common questions about Hush Hour, and what to try when something does not work.", """
    <p class="kicker">Questions</p>
    <h1>Questions and fixes</h1>

    <h2>The sound stops after a while</h2>
    <p>First check the timer chips on home: the default is 45 minutes. Pick All night to keep it going. If it stops before the timer ends, your phone may be closing apps to save battery. Open Android settings, Apps, Hush Hour, Battery, and choose Unrestricted. Some phones (Xiaomi, Huawei, Samsung) have their own extra battery lists; <a href="https://dontkillmyapp.com">dontkillmyapp.com</a> shows the steps for each.</p>

    <h2>It paused on its own</h2>
    <p>A call, an alarm or another app playing sound pauses Hush Hour; it comes back after a call. Headphones coming out also pause it. Both can be changed in Settings, Sound.</p>

    <h2>It is too loud or too quiet</h2>
    <p>Use the Overall level slider on home and your phone's volume buttons. Keep it quiet sets a soft ceiling; turn it off in Settings, Sound if the phone is far away and you need more.</p>

    <h2>Can I hear the loop?</h2>
    <p>Each sound is a loop of two to four minutes that joins without a seam, starts at a new point every time, and drifts a little in level, so it should never sound the same twice. If you can hear a click or a jump in one sound, please report it with the sound's name.</p>

    <h2>Does it use the internet or my data?</h2>
    <p>No. The app does not even ask for internet access. Your settings and mixes stay on your phone. See the <a href="https://hushhour.zanoski.com/privacy">privacy policy</a>.</p>

    <h2>Is it safe in a baby's room?</h2>
    <p>Keep the phone across the room, not in or by the cot, keep the level low, and use the timer.</p>

    <h2>Is it a medical app?</h2>
    <p>No. Hush Hour is for rest and relaxation, and does not diagnose or treat anything. If you sleep badly most nights, talk to a doctor.</p>

    <h2>Where do the sounds come from?</h2>
    <p>From field recordings shared free of rights (CC0) on Freesound, picked and cut for Hush Hour. White, pink and brown noise are made for the app.</p>
""")

page("report.html", "Report a bug", "How to report a Hush Hour bug or ask for a feature on GitHub.", f"""
    <p class="kicker">Report</p>
    <h1>Report a bug or ask for a feature</h1>
    <p>Found something broken, or have an idea? Tell us on GitHub. A free GitHub account is all you need.</p>
    <div class="grid" style="margin-top:24px">
      <div class="card"><h2 class="h3">Bug report</h2><p>Something does not work, sounds wrong, or crashes.</p><p style="margin-top:16px"><a class="btn main" href="{REPO}/issues/new?template=bug_report.yml">Report a bug</a></p></div>
      <div class="card"><h2 class="h3">Feature request</h2><p>A sound, a mix or something you would like Hush Hour to do.</p><p style="margin-top:16px"><a class="btn ghost" href="{REPO}/issues/new?template=feature_request.yml">Ask for a feature</a></p></div>
    </div>

    <h2>Before you write</h2>
    <ul>
      <li>Search the <a href="{REPO}/issues">open issues</a> first. If yours is there, add a thumbs up or a comment.</li>
      <li>Check the <a href="faq.html">questions and fixes</a> page.</li>
      <li>One problem per report makes it faster to fix.</li>
    </ul>

    <h2>What helps</h2>
    <dl>
      <dt>App version</dt><dd>Android settings, Apps, Hush Hour. The version is near the bottom of that page.</dd>
      <dt>Phone model and Android version</dt><dd>Android settings, About phone.</dd>
      <dt>Which screen or sound</dt><dd>Home, a sound by name, the timer, Mixes, Settings, the notification or the widget.</dd>
      <dt>Steps</dt><dd>What you did, one step per line, so we can do the same.</dd>
      <dt>Expected and actual</dt><dd>What you thought would happen, and what happened.</dd>
      <dt>A picture or a recording</dt><dd>A screenshot or a short screen recording. Drag it into the form.</dd>
    </dl>
    <p>Issues on GitHub are public. Before you attach a screenshot, crop or cover anything private.</p>

    <h2>Other ways</h2>
    <p>Prefer not to use GitHub? Write to <span class="mail">marko@zanoski.com</span> (<a href="mailto:marko@zanoski.com">write an email</a>).</p>
""")
