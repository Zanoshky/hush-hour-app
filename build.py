#!/usr/bin/env python3
"""Builds the guide pages in docs/ from the bodies below. Run after any edit and commit docs/. Fails on any dash.

The look is the Zanoshky Standard, the same as hushhour.zanoski.com: docs/tokens.css is a copy of the house
tokens (never edit it here), docs/style.css the guide's own parts. Both are inlined into every page so no
stylesheet holds up the first paint. Every screenshot in docs/img is a real capture of the app."""
import re
from pathlib import Path

D = Path(__file__).parent / "docs"
REPO = "https://github.com/Zanoshky/hush-hour-app"
PLAY = "https://play.google.com/store/apps/details?id=com.zanoshky.hushhour"
SITE = "https://hushhour.zanoski.com"
NAV = [("index.html", "Home"), ("guide.html", "Guide"), ("faq.html", "Questions"), ("report.html", "Report a bug")]

CSS = "\n".join((D / f).read_text() for f in ("tokens.css", "style.css"))
CSS = re.sub(r"/\*.*?\*/", "", CSS, flags=re.S)
CSS = re.sub(r"\s*\n\s*", "\n", CSS).strip()


def shot(img, alt, name, line, lazy=True):
    load = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"'
    stem = img.rsplit(".", 1)[0]
    # The jpg stays for the README on GitHub; pages pick a small webp, about half the bytes.
    src = f'srcset="img/{stem}-300.webp 300w, img/{stem}-540.webp 540w" sizes="(min-width: 840px) 260px, 45vw"'
    return (f'<figure><img src="img/{img}" {src} alt="{alt}" width="540" height="1200" {load}>'
            f'<figcaption>{name}<span>{line}</span></figcaption></figure>')


def page(name, title, desc, body):
    for bad in ("\u2014", "\u2013", " - "):
        if bad in body:
            raise SystemExit(f"{name}: dash {bad!r} in copy")
    nav = "".join(f'<a class="hide-s" href="{h}"{" aria-current=\"page\"" if h == name else ""}>{t}</a>' for h, t in NAV)
    foot = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == name else ""}>{t}</a>' for h, t in
                   [(SITE, "Home"), ("index.html", "User guide"), ("faq.html", "Questions"), ("report.html", "Report a bug"),
                    (f"{SITE}/privacy", "Privacy"), (f"{SITE}/terms", "Terms")])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Hush Hour user guide</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f6f7f9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="{title} · Hush Hour user guide">
<meta property="og:description" content="{desc}">
<link rel="icon" href="img/icon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/jetbrains-mono-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/inter-regular.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/icon.svg" alt="" width="34" height="34"><span>Hush Hour</span></a>
    <nav aria-label="Guide pages">{nav}<a class="key" href="{PLAY}">Get the app</a></nav>
  </div>
</header>
<main id="main" class="page">
  <div class="wrap">
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <span>Hush Hour by <a href="https://zanoski.com">Marko Zanoski</a></span>
    <nav aria-label="Footer">{foot}</nav>
    <p class="lic">Guide text and images are shared under CC BY 4.0. The Hush Hour app itself is proprietary.</p>
  </div>
</footer>
</body>
</html>
"""
    (D / name).write_text(html)
    print(name)


page("index.html", "Home", "The user guide for Hush Hour, the white noise and sleep sound app for Android.", f"""
    <p class="lbl">User guide</p>
    <h1>Hush Hour</h1>
    <p class="lede">Real rain, sea, stream, forest, wind, crickets and fire recordings, and white, pink and brown noise, mixed your way, with a sleep timer that fades out. Pay once, no ads, works offline.</p>
    <div class="keys">
      <a class="key filled" href="guide.html">Read the guide</a>
      <a class="key tonal" href="report.html">Report a bug or ask for a feature</a>
    </div>
    <ul class="shots">
      <li>{shot("home-playing.jpg", "Sounds while playing: the time, the sleep timer dial with 45 minutes left and Silent by 11:15 PM, the pause key, the mix name and the timer chips, with Sounds, Mixes and Settings in the bar at the foot.", "Sounds", "The dial, play and the timer.", lazy=False)}</li>
      <li>{shot("sounds.jpg", "The sound tiles on Sounds: Rain, Window, Roof, Tent, Downpour, Storm, Ocean, Stream, Forest, Wind, Crickets, Campfire, Fireplace, Fan, White noise and Pink noise. The five in the mix are lit.", "The sounds", "Tap a tile to add it.")}</li>
      <li>{shot("mixes.jpg", "Mixes: a box to name and save what plays now, your own mixes, then ready made ones like Rainy cabin, Summer night and Campfire.", "Mixes", "Yours, and nine ready made.")}</li>
      <li>{shot("settings.jpg", "Settings: cards of rows, Look, Sleep and sound with Sleep timer, Sound and Add the widget, then App with Privacy and Help and feedback, each saying what is set now.", "Settings", "The last item in the bar.")}</li>
    </ul>
""")

page("guide.html", "Guide", "How to use Hush Hour: Sounds, Mixes and Settings, the sleep timer, More, the dim screen and the widget.", f"""
    <p class="lbl">Guide</p>
    <h1>How Hush Hour works</h1>

    <div class="with-shot">
      <div class="doc">
        <h2>Start in one tap</h2>
        <p>Hush Hour opens on Sounds. Press the round play key under the dial. The first time, soft rain on the roof plays. The dial says what is going on (Ready, Time left, Fading out or All night), how long is left, and the clock time it goes silent. The line under it names what plays.</p>

        <h2>Three sections in the bar</h2>
        <p>The bar at the foot of the screen has three sections: Sounds, Mixes and Settings. The one you are on sits on a blue pill. Tap another to switch; it opens at its top. Tap the one you are on to scroll back to its top. Back on Mixes or Settings takes you to Sounds.</p>
        <p>At the top right are two keys on every section: the moon dims the screen, and the three dots open More.</p>
      </div>
      {shot("home-playing.jpg", "Sounds while playing: the time, the sleep timer dial with 45 minutes left and Silent by 11:15 PM, the pause key, the mix name and the timer chips, with Sounds, Mixes and Settings in the bar at the foot.", "Sounds", "The dial, play and the timer chips.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>Sounds</h2>
        <p>Scroll down on Sounds to the sound tiles. Tap a tile to add its sound to the mix, tap it again to take it out. A tile that plays is lit in moonlight, with a bar along its foot that shows its level. You can play up to eight sounds at once.</p>
        <dl class="rows plate">
          <div><dt>Rain</dt><dd>Rain on a yard, rain on the glass (Window), on the roof, on a tent, a mountain downpour, and a storm with far thunder now and then.</dd></div>
          <div><dt>Water</dt><dd>Waves on the shore (Ocean) and a river murmur (Stream).</dd></div>
          <div><dt>Woods and night</dt><dd>Birds in the trees (Forest), wind in the leaves, and crickets on a summer night with an owl now and then.</dd></div>
          <div><dt>Fire</dt><dd>A campfire and a fireplace, with a log popping now and then.</dd></div>
          <div><dt>Noise</dt><dd>A bedroom fan, and white, pink and brown noise. White is bright like a hiss, pink is softer like steady rain, brown is deep and low.</dd></div>
        </dl>
        <p style="margin-top:16px">Rare moments (thunder, the owl, a pop in the fire) can be turned off in Settings, Sound.</p>
      </div>
      {shot("sounds.jpg", "The sound tiles: Rain, Window, Roof, Tent, Downpour, Storm, Ocean, Stream, Forest, Wind, Crickets, Campfire, Fireplace, Fan, White noise and Pink noise. The five in the mix are lit.", "The tiles", "A lit tile is in the mix.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>Your mix</h2>
        <p>Under the tiles, Your mix lists each sound that plays with its own slider, its level, and a cross to take it out. Overall level sets the whole mix. Keep it low: soft enough that you could talk over it.</p>
        <p>Save this mix, at the foot of the card, takes you to Mixes with the name box ready.</p>
      </div>
      {shot("levels.jpg", "Your mix: Roof, Campfire, Ocean, Crickets and Brown noise, each with its level and a cross to take it out, then Overall level and Save this mix.", "Your mix", "A slider for each sound.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>Mixes</h2>
        <p>At the top of Mixes, Save what plays now: type a name, like Sunday rain, and tap Save. Your mixes show under Yours, with a cross to delete each one. Under Ready made are nine to start from: Rainy cabin, Summer night, Campfire, Storm at sea, Tent in the rain, Window seat, Shore at dawn, Deep focus and Soft hush.</p>
        <p>Tap a mix to play it. Hush Hour plays it and takes you back to Sounds. The mix that plays says Playing now, in moonlight.</p>
      </div>
      {shot("mixes.jpg", "Mixes: a box to name and save what plays now, Yours with the line Mixes you save show here, then Ready made: Rainy cabin, Summer night and Campfire.", "Mixes", "Save yours, or start from nine.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>The sleep timer</h2>
        <p>The chips under the dial set the timer: 15 or 30 minutes, 45 (the default), 1 hour, 1 hour 30, 2 hours, 2 hours 30, or All night. The chosen chip is blue with a small tick. The timer starts when you press play. Near the end the sound fades out slowly, over 10 minutes by default; pick 5 or 20 in Settings, Sleep timer.</p>
        <p>Why a timer by default? Steady sound helps most while you fall asleep, and one study found noise left on all night took some dream sleep. All night is there if you want it.</p>

        <h2>More</h2>
        <p>The three dots at the top open More, a sheet from the foot of the screen. It names what plays, then holds Save this mix and Add the widget.</p>
      </div>
      {shot("more.jpg", "The More sheet: Hush Hour, what plays now, then Save this mix and Add the widget.", "More", "Save, and the widget.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>Dim the screen</h2>
        <p>Tap the moon at the top. The screen goes black with only the time, in a dim grey, and the brightness drops to the lowest. Tap anywhere, or press Back, to wake it.</p>

        <h2>With the screen off</h2>
        <p>Sound keeps playing with the screen off. The notification and the lock screen show what plays, with pause and stop. A call or an alarm pauses it, and it comes back after. If headphones come out, it pauses so the sound never jumps to the speaker (you can turn that off in Settings, Sound). To play under a podcast or audiobook, turn on Play along with other apps.</p>

        <h2>The widget</h2>
        <p>Pick Add the widget in More or in Settings, Sleep and sound. Or touch and hold your home screen, pick Widgets, then Hush Hour. The widget shows the mix and plays or pauses it with one tap. Tap its words to open the app.</p>
      </div>
      {shot("dim.jpg", "The dimmed screen: black, with only the time in a dim grey.", "Dimmed", "Only the time, in dim grey.")}
    </div>

    <div class="with-shot">
      <div class="doc">
        <h2>Settings</h2>
        <p>Settings is the last item in the bar. It is a page of cards, each row saying what is set now; a row with an arrow opens its own small page, and the arrow at the top left of that page takes you back.</p>
        <dl class="rows plate">
          <div><dt>Look</dt><dd>Follow the phone (Light by day, Dark at night), Light, Dark, or Black, true black for OLED screens and dark rooms. Dark is where Hush Hour starts.</dd></div>
          <div><dt>Sleep timer</dt><dd>How long the fade at the end takes: 5 minutes, 10 minutes (gentle) or 20 minutes (very slow), and why it fades.</dd></div>
          <div><dt>Sound</dt><dd>Rare moments on or off; Keep it quiet, a soft ceiling on loudness; pause when headphones come out; play along with other apps.</dd></div>
          <div><dt>Add the widget</dt><dd>Play and pause from your home screen.</dd></div>
          <div><dt>Privacy</dt><dd>The promises as red ban chips, every permission the app holds and why, and the privacy policy in full.</dd></div>
          <div><dt>Help and feedback</dt><dd>This guide, the report page, a note that Hush Hour is for rest and not medical care, and the credits: where the recordings come from and the fonts.</dd></div>
          <div><dt>Support the developer</dt><dd>A short line, If Hush Hour helps you, you can support it, over the Buy me a coffee row, which opens buymeacoffee.com/zanoshky in your browser.</dd></div>
          <div><dt>About</dt><dd>The version, and where your mixes and settings are kept.</dd></div>
        </dl>
      </div>
      {shot("privacy.jpg", "Privacy in Settings: red ban chips No ads, No tracking, No analytics, No crash reports, No error reports, No account, No AI and No internet, then Play in the background, Keep the phone awake and Internet denied by design, each with why.", "Privacy", "Every promise and permission, once.")}
    </div>

    <div class="doc">
      <h2>Accessibility</h2>
      <p>Every control has a TalkBack label, and each sound tile is read as a switch that is on or off. Touch targets are at least 48 dp, text grows with the phone's font size (the tiles get wider as it does, one across at the biggest sizes), and words keep a 7 to 1 contrast in every look.</p>
    </div>
""")

page("faq.html", "Questions", "Answers to common questions about Hush Hour, and what to try when something does not work.", """
    <div class="doc">
    <p class="lbl">Questions</p>
    <h1>Questions and fixes</h1>

    <h2>The sound stops after a while</h2>
    <p>First check the timer chips on Sounds: the default is 45 minutes. Pick All night to keep it going. If it stops before the timer ends, your phone may be closing apps to save battery. Open Android settings, Apps, Hush Hour, Battery, and choose Unrestricted. Some phones (Xiaomi, Huawei, Samsung) have their own extra battery lists; <a href="https://dontkillmyapp.com">dontkillmyapp.com</a> shows the steps for each.</p>

    <h2>It paused on its own</h2>
    <p>A call, an alarm or another app playing sound pauses Hush Hour; it comes back after a call. Headphones coming out also pause it. Both can be changed in Settings, Sound.</p>

    <h2>It is too loud or too quiet</h2>
    <p>Use the Overall level slider in Your mix on Sounds and your phone's volume buttons. Keep it quiet sets a soft ceiling; turn it off in Settings, Sound if the phone is far away and you need more.</p>

    <h2>Where did my mixes go?</h2>
    <p>Saved mixes are on Mixes, in the bar at the foot of the screen, under Yours. Settings is the last item in that bar.</p>

    <h2>Can I hear the loop?</h2>
    <p>Each sound is a loop of two to four minutes that joins without a seam, starts at a new point every time, and drifts a little in level, so it should never sound the same twice. If you can hear a click or a jump in one sound, please report it with the sound's name.</p>

    <h2>Does it use the internet or my data?</h2>
    <p>No. The app does not even ask for internet access. Your settings and mixes stay on your phone. See the <a href="https://hushhour.zanoski.com/privacy">privacy policy</a>.</p>

    <h2>Is it safe in a baby's room?</h2>
    <p>Keep the phone across the room, not in or by the cot, keep the level low, and use the timer.</p>

    <h2>Is it a medical app?</h2>
    <p>No. Hush Hour is for rest and relaxation. It is not a medical device and does not diagnose, treat, cure, or prevent any medical condition. For sleep problems, talk to a doctor or other healthcare professional.</p>

    <h2>Where do the sounds come from?</h2>
    <p>From field recordings shared free of rights (CC0) on Freesound, picked and cut for Hush Hour. White, pink and brown noise are made for the app.</p>
    </div>
""")

page("report.html", "Report a bug", "How to report a Hush Hour bug or ask for a feature on GitHub.", f"""
    <div class="doc" style="max-width:none">
    <p class="lbl">Report</p>
    <h1>Report a bug or ask for a feature</h1>
    <p style="margin-top:16px">Found something broken, or have an idea? Tell us on GitHub. A free GitHub account is all you need.</p>
    <div class="cards">
      <div class="card plate"><h2 class="h3">Bug report</h2><p>Something does not work, sounds wrong, or crashes.</p><a class="key filled" href="{REPO}/issues/new?template=bug_report.yml">Report a bug</a></div>
      <div class="card plate"><h2 class="h3">Feature request</h2><p>A sound, a mix or something you would like Hush Hour to do.</p><a class="key tonal" href="{REPO}/issues/new?template=feature_request.yml">Ask for a feature</a></div>
    </div>
    </div>
    <div class="doc">
    <h2>Before you write</h2>
    <ul>
      <li>Search the <a href="{REPO}/issues">open issues</a> first. If yours is there, add a thumbs up or a comment.</li>
      <li>Check the <a href="faq.html">questions and fixes</a> page.</li>
      <li>One problem per report makes it faster to fix.</li>
    </ul>

    <h2>What helps</h2>
    <dl class="rows plate">
      <div><dt>App version</dt><dd>Settings, About, or Android settings, Apps, Hush Hour.</dd></div>
      <div><dt>Phone model and Android version</dt><dd>Android settings, About phone.</dd></div>
      <div><dt>Which screen or sound</dt><dd>Sounds, a sound by name, the timer, Your mix, Mixes, More, Settings, the notification or the widget.</dd></div>
      <div><dt>Steps</dt><dd>What you did, one step per line, so we can do the same.</dd></div>
      <div><dt>Expected and actual</dt><dd>What you thought would happen, and what happened.</dd></div>
      <div><dt>A picture or a recording</dt><dd>A screenshot or a short screen recording. Drag it into the form.</dd></div>
    </dl>
    <p style="margin-top:16px">Issues on GitHub are public. Before you attach a screenshot, crop or cover anything private.</p>

    <h2>Other ways</h2>
    <p>Prefer not to use GitHub? Write to <span class="mail">marko@zanoski.com</span> (<a href="mailto:marko@zanoski.com">write an email</a>).</p>
    </div>
""")
