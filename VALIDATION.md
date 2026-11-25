# Validation — La Rosa 19.0.1.0.0

Checked on 25 November 2026 in a disposable Odoo 19 Community database. No live client database was used.

Platform source: Odoo `19.0`, commit `4104bb586a6a9a134fb9be4172e1e3c997c8312b`.

| Check | Result |
| --- | --- |
| Fresh install with native `website_sale` dependencies and no demo data | Passed |
| Python syntax, XML parsing, manifest/local asset references | Passed |
| Frontend, backend and brand SCSS compilation | Passed |
| Five Odoo integration tests | 0 failures, 0 errors |
| Home, Creative Corner, Our Story, Visit Us, contact redirect, shop and product routes | Passed |
| Publish/unpublish, archive and saleable-product filtering | Passed |
| Website isolation and logged-in-only shop access | Passed |
| Native add-to-cart, cart contents and checkout page | Passed |
| One-time setup can run again without duplicate menus or reset edits | Passed |
| Upgrade preserves page edits, contact details, category name, product price/publication and menu count | Passed |
| Chromium widths 1440, 768, 393 and 360 pixels | Passed; no horizontal overflow |
| Homepage photographs, logo and fonts | Loaded successfully at all tested widths |
| Mobile menu opening/closing, phone link and scroll restoration | Passed |
| Shop, Visit, Creative Corner, About and Cart mobile widths | Passed |
| Reduced-motion content visibility | Passed |
| Browser JavaScript page errors | None |
| Backend navigation colour after login | `rgb(101, 11, 24)` / `#650b18` |

Visual inspection confirmed the transparent La Rosa logo on burgundy, real photographs, readable type, desktop layout, compact mobile navigation and footer.

The empty-catalogue homepage was tested as well as publication of temporary test products. Test products were rolled back or removed; the deliverable contains no demo product records.

The homepage bypasses the public full-page cache so publication and visitor-dependent catalogue prices render live. Prices, variants and checkout remain native Odoo functionality.

Payment processing, shipping charges, email delivery and real-world Google Maps routing depend on the live instance and external services; those were not configured or transaction-tested here. CloudPepper installation remains the next deployment step.
