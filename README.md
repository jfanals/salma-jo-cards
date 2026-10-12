# Salma Jô — business card design gallery

A static website with business-card proposals for Salma Jô.

- `index.html`: original six concepts and printing research.
- `live-wire.html`: six Live wire layouts, a fixed settings toolbar, photo picker, framing controls and local photo upload.
- `ugly-comic-sans.html`: deliberately ridiculous Comic Sans version.

Open any HTML file locally or visit the GitHub Pages site. Uploaded photos are processed in the browser and are not sent to a server; they disappear on reload. The supplied web photo previews are stored with this public site.

## Before printing

These are RGB design drafts, not certified print-ready PDFs. Confirm the contact details, QR destination, bleed, font embedding, colour profile and image quality with the printer.

Photographs are web-sourced design previews. No license or print permission is asserted or granted for them. Source links and available credit information appear in the Live wire gallery. Obtain permission or replace them with approved press photos before printing. No open-source license is granted for third-party assets.

Printing prices and cutoff research were checked on 12 October 2026 and are not live quotations or delivery guarantees.

## Rebuild embedded photo assets

With Python and Pillow installed:

```sh
python build-photo-assets.py
```

The website itself needs no build step or dependencies.
