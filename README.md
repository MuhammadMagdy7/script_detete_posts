# script_delete_posts

A simple automation script to help remove Instagram posts using Selenium.  
This project is a quick utility for users who need to clean up or manage their Instagram posts in bulk from a scripted environment.

Why this project matters
- Saves time: delete many posts faster than manual clicks.
- Reproducible: you can run the same steps reliably across sessions.
- Helpful for small-scale account maintenance and testing.

Key value points
- Quick setup for users who already know how to run Python and use Google/Firefox WebDriver.
- A starting template that can be improved with safer credential handling, better selectors, and headless operation.
- Good learning example for Selenium automation and handling dynamic web pages.

Important warnings
- Instagram Terms of Service may restrict automation. Use this script at your own risk.
- Never hard-code real credentials in scripts you share. Use environment variables or a secure secrets store.
- Instagram frequently changes its HTML structure and class names; this script may need updates to selectors.

What’s included
- index.py — main Selenium script (removes posts by navigating to profile and using UI controls).
  - Note: the current script uses CSS/XPath selectors that may break with Instagram updates.
- README.md — this file (simple instructions and project value).
- LICENSE — MIT license (suggested).

Prerequisites
- Python 3.8+
- Selenium for Python: pip install selenium
- Firefox browser and geckodriver installed and available in PATH (or adapt to Chrome + chromedriver)
- A stable network connection and a test Instagram account for initial runs

Quick start (example)
1. Install dependencies:
   pip install selenium

2. Install geckodriver (for Firefox), or chromedriver if you adapt the script.

3. Edit index.py:
   - Replace the username and password placeholders with secure retrieval from environment variables, e.g.:
     ```python
     import os
     username = os.getenv("IG_USERNAME")
     password = os.getenv("IG_PASSWORD")
     ```
   - Update the profile URL to your profile, or make it a variable.

4. Run the script:
   python index.py

Security & best practices
- Use environment variables to store credentials (do not commit them).
- Test with a small number of posts first.
- Add delays and randomized waits to reduce automation detection.
- Consider running in a headless browser only after fully testing interactive flows.

Suggestions for immediate improvements
- Replace hard-coded selectors with robust strategies that fall back when elements change.
- Add CLI arguments (profile, max posts to delete, headless).
- Use explicit waits (WebDriverWait) instead of time.sleep for more reliable automation.
- Add logging to capture which posts were deleted and any errors.

Maintainer
- MuhammadMagdy7 — https://github.com/MuhammadMagdy7

License
- MIT (see LICENSE file)