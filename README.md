# La Rosa — Odoo 19 Community website

A complete La Rosa arts, crafts and stationery storefront, packaged as one installable Odoo addon for CloudPepper. Developed by Spxcorp Limited.

**Module:** `larosa_website`
**Version:** `19.0.1.0.0`
**Target:** Odoo 19 Community
**Dependency:** Odoo's standard `website_sale` (installed automatically as needed). No Enterprise modules, external Python packages, API keys, or build steps are required.

## Install with CloudPepper

1. Add `https://github.com/sheveioncallender-boop/larosa-website.git` to the instance's custom addons repositories, using branch `main`.
2. Pull/sync the repository and restart/rebuild the Odoo instance as your CloudPepper deployment requires. The addon is the `larosa_website` folder directly inside the repository root.
3. In Odoo, enable developer mode, open **Apps → Update Apps List**, and search for **La Rosa**.
4. Install **La Rosa — Website & Shop**. It is marked as an application, so it also appears with the Apps filter enabled.
5. Open Website. Installation sets up the default website's name, supplied transparent logo, homepage, navigation, four editorial pages and six editable eCommerce categories.

If uploading files manually, copy the entire `larosa_website` folder into an addons directory. Do not upload individual source files through the website editor.

This repository prepares the addon; adding the repository and installing it in the live CloudPepper instance remain deployment steps.

## Storefront

- Home: a photographic welcome, art/craft/stationery departments, automatically selected published products, creative inspiration and store directions.
- Shop: native Odoo category navigation, product pages, variants, search, prices, account, cart and checkout.
- Creative Corner: three simple project ideas, linked to the corresponding shop categories.
- Our Story: the La Rosa introduction.
- Visit Us: phone, WhatsApp, editable opening hours, Google map and directions. Native `/contactus` links redirect here for this website.
- Sticky native header, mobile menu on the left, logo centred and cart on the right; phone in the mobile menu.
- Bundled real photographs and local fonts; no image-generation or third-party image/font requests at page load. The supplied La Rosa logo is used unchanged.
- Subtle entry effects that respect reduced-motion settings.
- Footer credit: **Developed by Spxcorp Limited.**

The map points to **North Hills Plaza, Santa Cruz, Trinidad and Tobago**, using the supplied address rather than an invented precise shop pin. Google Maps chooses the route from the visitor's location.

## Add products normally in Odoo

1. Create or edit a product in Odoo. Enable **Sales**, add its name, selling price and product photo.
2. Assign an eCommerce category (Art Supplies, Crafts & DIY, Stationery, School Essentials, Paper & Card, or Painting & Drawing). You can add, rename and reorder categories normally.
3. Assign it to this website, or leave the website empty to share it across websites where permitted.
4. Publish the product on the website.

Published, active, saleable products appear in the shop and automatically enter the homepage selection. The homepage displays up to eight, in website sequence order (newer products first when sequences match). The optional **Feature on La Rosa homepage** checkbox on the product's Sales tab puts a product first; it is not required for display.

Unpublishing or archiving removes a product from the homepage. Category links and product queries respect the native website/public access rules. Homepage prices use Odoo's visitor pricelist, taxes and fiscal position. Product links lead to native product pages so customers choose valid variants before adding to their cart.

No demonstration products, artificial stock, fictitious prices, payment providers or delivery promises are installed. The homepage remains fully designed when the catalogue is empty. Departments link to Shop until their corresponding categories become publicly available.

Payments, delivery rules, currency, taxes, stock visibility and customer accounts use your existing Odoo configuration. This module does not configure a payment gateway or change the company currency.

## Brand and contact settings

Open **Website → Configuration → Settings → La Rosa**:

- **La Rosa storefront:** enable/disable the public website styling for the selected website.
- **Store telephone:** defaults to `+1 868 463-4578`.
- **WhatsApp number:** defaults to `18684634578`; clear it to remove WhatsApp links.
- **Store address:** defaults to `North Hills Plaza, Santa Cruz / Trinidad and Tobago` and drives map/directions links.
- **Opening hours:** intentionally blank until confirmed. Enter the actual schedule to display it on the contact page and footer.

The burgundy palette also replaces Odoo Community purple for the backend navigation, primary actions and active selections. This compile-time backend colour choice applies throughout the database while the addon is installed. Semantic warning/error/success colours are retained. Public layouts are scoped to websites with La Rosa branding enabled.

Initial installation targets `website.default_website`, like the earlier Noel's and Value Seekers setups. On a database with multiple live brands, deploy to the intended database/default website; do not assume this addon is a per-user backend theme.

## Edit and upgrade

Use the normal Odoo Website editor for the editorial page copy and photographs. Dynamic product sections draw from the catalogue.

Pull the repository in CloudPepper, restart/rebuild as needed, and **Upgrade** the La Rosa app when new module versions are supplied. Pages, categories and navigation are created once with `noupdate`/installation hooks so upgrades preserve business edits, prices and publication settings. Asset checksums handle the normal browser cache refresh.

The homepage intentionally bypasses Odoo's full-page cache because publication and visitor-specific prices must be live. Other marketing pages keep normal Odoo caching.

Uninstalling restores the prior website name, logo and homepage if those are still the values installed by this addon. Pre-existing navigation entries changed by setup are restored when they still point to the installed URLs. Odoo removes module-owned pages, categories and menus during uninstall; products themselves are not created or deleted by this addon.

## Verification

See [VALIDATION.md](VALIDATION.md) for checks run against Odoo 19 Community. The addon includes HTTP tests covering catalogue publication, access boundaries, cart/checkout, page rendering, contact links and idempotent setup.

Run them against a disposable database with:

```bash
odoo -d larosa_test -i larosa_website --test-enable --test-tags /larosa_website --stop-after-init
```

Real photos and bundled font licence details are recorded in [PHOTO_CREDITS.md](PHOTO_CREDITS.md).
