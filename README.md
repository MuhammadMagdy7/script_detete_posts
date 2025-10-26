# script_delete_posts — Instagram cleanup automation with Selenium

A focused automation script to bulk-delete Instagram posts via Selenium WebDriver. Ideal for quick cleanups and learning browser automation patterns.

---

## Overview
- Logs in to Instagram, navigates to your profile, opens posts, and deletes them via the UI.
- Demonstrates Selenium element location, waits, and action sequencing.
- Serves as a template you can harden with better selectors and safer credential handling.

## Why this project matters
- Saves time vs. manual deletion for many posts.
- Teaches practical Selenium flows on a dynamic website.
- Provides a reproducible, scriptable approach for account maintenance.

## Tech stack
- Python 3.8+
- Selenium WebDriver
- Firefox + geckodriver (or Chrome + chromedriver with small edits)

## Project structure
- index.py — main Selenium flow
- README.md — this guide
- LICENSE — MIT

## Quick start
1) Install dependencies:
   pip install selenium
2) Install and add WebDriver (geckodriver or chromedriver) to PATH.
3) Configure credentials via environment variables:
   - IG_USERNAME
   - IG_PASSWORD
4) Run the script:
   python index.py

## Configuration
- Credentials: load from environment variables (recommended). Avoid hard-coding secrets.
- Profile URL: set to your Instagram handle’s profile.
- Headless mode: can be enabled if you adapt WebDriver options.

## Usage
- Ensure you can log in normally via browser (2FA/verification may interfere).
- Use small delays plus explicit waits to reduce flakiness.
- Start with a small subset of posts.

## Troubleshooting
- Elements not found: update CSS/XPath selectors and add WebDriverWait instead of fixed sleeps.
- Login interruptions (2FA/verification): handle manually or in code where appropriate.
- StaleElementReferenceException: re-find elements after DOM updates.

## Roadmap
- [ ] Replace time.sleep with WebDriverWait
- [ ] CLI args: --max-posts, --headless, --profile
- [ ] More robust selectors and fallback strategies
- [ ] Logging + dry-run mode

## License
MIT — see LICENSE.

## Maintainer
- MuhammadMagdy7 — https://github.com/MuhammadMagdy7