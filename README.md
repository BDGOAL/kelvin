# Japan Winter Trip 2026 — GitHub Pages

## How to publish (local photographs)

1. Upload the **whole project directory**, including `index.html`, `images/`, `download_images.py`, `photo_manifest.json`, and `.github/workflows/pages.yml`, to a public GitHub repository on the `main` branch.
2. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**.
3. The included GitHub Actions workflow downloads the photographs from Wikimedia Commons during deployment and packages them with the site. **The deployed HTML uses only local `/images/*.jpg` paths, not third-party image hotlinks.**
4. Open **Actions** to check whether all 11 images downloaded. A failed image request makes the build fail rather than quietly showing a blank picture; you can rerun the workflow.
5. Alternatively, run `python3 download_images.py` on your own computer and commit the generated `images/*.jpg` files before publishing; then use ordinary branch-based GitHub Pages if you prefer.

## Image fallback

The ZIP contains labeled SVG placeholders in `images/`, **not the original JPEG photo files**. The current creation environment cannot download the original image bytes directly. Until the download script has run successfully, the website shows transparent, clearly labeled scenic placeholders rather than blank gray rectangles. The script uses the Wikimedia Commons API, not broken `Special:FilePath` hotlinks.

## Credits

Read `PHOTO_CREDITS.md`. The downloaded files retain their respective Wikimedia Commons licenses. Please don't remove attribution. Some photos are not winter scenes; the Shiorie illustration refers to the surrounding hot spring area, not a photo of the hotel's room.

## Other functions

Day tabs, booking checklist and editable exchange rate remain. Checklist data stays in the user's browser; it does not sync with Google Sheets.
