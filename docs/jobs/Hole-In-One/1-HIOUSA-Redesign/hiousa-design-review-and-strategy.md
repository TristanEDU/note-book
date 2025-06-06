---
title: HIOUSA Design Review & Strategy
date: {{date}}
tags: []
---

# HIOUSA Design Review & Strategy

Summary of the current site audit, UI/UX requirements, and visual design plans for the rebuild.

---
## From `hiousa-site-review.md`

#Site review of HIOUSA.com
##Build
###Theme
####Flat Bootstrap Child <sub>Version: 1.5 by XtremelySocial</sub> 
|Child theme for Flat Bootstrap. Includes a stylesheet (style.css) for you to restyle any of the CSS and a functions.php file to change theme parameters or components. Both files include samples of a few common things you might want to do.

This is a older non WP blog theme... Can't say I am impressed with how it looks.
###Plugins
- Accordions - By PickPlugins *(Fully responsive and mobile ready accordion grid for wordpress.)*
- Classic Editor *(Enables the WordPress classic editor and the old-style Edit Post screen with TinyMCE, Meta Boxes etc. Supports the older plugins that extend this screen.)*
- Contact Form 7 *(Just another contact form plugin. Simple but flexible.)*
- Contact Form 7 Modules: Hidden Fields *(Add hidden fields to the popular Contact Form 7 plugin.)*
- Contact Form 7 Modules: Send All Fields *(Send all submitted fields in the message body using one simple tag: `[all-fields]`.)*
- Contact Form CFDB7 *(Save and manage Contact Form 7 messages. Never lose important data.)*
- Contact Form DB *(Save form submissions to your database.)*
- Enable Media Replace *(Easily replace any media file by uploading a new file in the "Edit Media" section.)*
- Gutenberg *(Adds functionality and features for the WordPress block editor.)*
- Health Check & Troubleshooting *(Checks the health of your WordPress install.)*
- Mailgun *(Mailgun integration for WordPress.)*
- Max Mega Menu *(Enable a mega menu, written the WordPress way.)*
- Page Builder by SiteOrigin *(A drag and drop, responsive page builder that simplifies building your website.)*
- Quick Page/Post Redirect Plugin *(Redirect Pages, Posts or Custom Post Types to another location quickly.)*
- Really Simple SSL *(Easily migrate your website to SSL.)*
- Regenerate Thumbnails *(Regenerate the thumbnails for one or more image uploads.)*
- Simple CSS for widgets *(Easily apply your own CSS class(es) to any specific widget.)*
- SiteOrigin Widgets Bundle *(A collection of widgets ready to use, extendable and neatly bundled.)*
- Smart Slider 3 *(Responsive slider plugin for WordPress.)*
- Wordfence Security *(Firewall & Malware Scan for WordPress.)*
- WP Rollback *(Rollback any WordPress.org theme or plugin to a previous version.)*
- WPCode *(Easily add code snippets to WordPress.)*
- Yoast Duplicate Post *(Clone posts and pages, including powerful Rewrite & Re-publish.)*
- Yoast SEO *(SEO solution for WordPress including content analysis, XML sitemaps and more.)*
###Site Health Dashboard Info

<details>

	<pre><code>
```
### wp-core ###

version: 6.8
site_language: en_US
user_language: en_US
timezone: +00:00
permalink: /%postname%/
https_status: true
multisite: false
user_registration: 0
blog_public: 1
default_comment_status: open
environment_type: production
user_count: 11
dotorg_communication: true
wpengine_api: true
wpengine_api_direct: false

### wp-paths-sizes ###

wordpress_path: /nas/content/live/hiousa
wordpress_size: 138.89 MB (145635299 bytes)
uploads_path: /nas/content/live/hiousa/wp-content/uploads
uploads_size: 108.66 MB (113936503 bytes)
themes_path: /nas/content/live/hiousa/wp-content/themes
themes_size: 8.85 MB (9281616 bytes)
plugins_path: /nas/content/live/hiousa/wp-content/plugins
plugins_size: 147.58 MB (154751907 bytes)
fonts_path: /nas/content/live/hiousa/wp-content/uploads/fonts
fonts_size: directory not found
database_size: 107.03 MB (112230400 bytes)
total_size: 511.01 MB (535835725 bytes)

### wp-dropins (1) ###

advanced-cache.php: true

### wp-active-theme ###

name: Flat Bootstrap Child (flat-bootstrap-child)
version: 1.5
author: XtremelySocial
author_website: (undefined)
parent_theme: Flat Bootstrap (flat-bootstrap)
theme_features: core-block-patterns, widgets-block-editor, title-tag, automatic-feed-links, post-thumbnails, menus, html5, editor-styles, editor-style, custom-background, custom-header, widgets
theme_path: /nas/content/live/hiousa/wp-content/themes/flat-bootstrap-child
auto_update: Disabled

### wp-parent-theme ###

name: Flat Bootstrap (flat-bootstrap)
version: 1.10.1
author: XtremelySocial
author_website: https://xtremelysocial.com
theme_path: /nas/content/live/hiousa/wp-content/themes/flat-bootstrap
auto_update: Disabled

### wp-themes-inactive (1) ###

Twenty Twenty-Four: version: 1.3, author: the WordPress team, Auto-updates disabled

### wp-mu-plugins (6) ###

Force Strong Passwords - WPE Edition: version: 1.8.0, author: Jason Cosper
Health Check Troubleshooting Mode: author: (undefined), version: 1.9.2
WP Engine Cache Plugin: version: 1.3.3, author: WP Engine
WP Engine Seamless Login Plugin: version: 1.6.1, author: WP Engine
WP Engine Security Auditor: version: 1.1.1, author: wpengine
WP Engine System: version: 6.4.4, author: WP Engine

### wp-plugins-active (25) ###

Accordions - By PickPlugins: version: 2.3.11, author: PickPlugins (latest version: 2.3.12), Auto-updates disabled
Classic Editor: version: 1.6.7, author: WordPress Contributors, Auto-updates disabled
Contact Form 7: version: 6.0.6, author: Takayuki Miyoshi, Auto-updates disabled
Contact Form 7 Modules: Hidden Fields: version: 2.0.2, author: Katz Web Services, Inc., Auto-updates disabled
Contact Form 7 Modules: Send All Fields: version: 2.0.2, author: Katz Web Services, Inc., Auto-updates disabled
Contact Form CFDB7: version: 1.3.0, author: Arshid, Auto-updates disabled
Contact Form DB: version: 2.10.26, author: Michael Simpson, Auto-updates disabled
Enable Media Replace: version: 4.1.6, author: ShortPixel, Auto-updates disabled
Gutenberg: version: 20.7.0, author: Gutenberg Team, Auto-updates disabled
Health Check & Troubleshooting: version: 1.7.1, author: The WordPress.org community, Auto-updates disabled
Mailgun: version: 2.1.7, author: Mailgun (latest version: 2.1.8), Auto-updates disabled
Max Mega Menu: version: 3.5, author: megamenu.com, Auto-updates disabled
Page Builder by SiteOrigin: version: 2.31.7, author: SiteOrigin (latest version: 2.31.8), Auto-updates disabled
Quick Page/Post Redirect Plugin: version: 5.2.4, author: anadnet, Auto-updates disabled
Really Simple Security: version: 9.3.5, author: Really Simple Security, Auto-updates disabled
Regenerate Thumbnails: version: 3.1.6, author: Alex Mills (Viper007Bond), Auto-updates disabled
Simple CSS for widgets: version: 1.0, author: Gagan S Goraya, Auto-updates disabled
SiteOrigin Widgets Bundle: version: 1.68.2, author: SiteOrigin (latest version: 1.68.3), Auto-updates disabled
Smart Slider 3: version: 3.5.1.27, author: Nextend, Auto-updates disabled
The Tooltip: version: 1.0.2, author: Alobaidi, Auto-updates disabled
Wordfence Security: version: 8.0.5, author: Wordfence, Auto-updates disabled
WPCode Lite: version: 2.2.7, author: WPCode, Auto-updates disabled
WP Rollback: version: 2.0.7, author: WP Rollback, Auto-updates disabled
Yoast Duplicate Post: version: 4.5, author: Enrico Battocchi & Team Yoast, Auto-updates disabled
Yoast SEO: version: 25.0, author: Team Yoast (latest version: 25.1), Auto-updates disabled

### wp-media ###

image_editor: WP_Image_Editor_Imagick
imagick_module_version: 1691
imagemagick_version: ImageMagick 6.9.11-60 Q16 x86_64 2021-01-25 https://imagemagick.org
imagick_version: 3.7.0
file_uploads: 1
post_max_size: 100M
upload_max_filesize: 50M
max_effective_size: 50 MB
max_file_uploads: 20
imagick_limits: 
	imagick::RESOURCETYPE_AREA: 137 MB
	imagick::RESOURCETYPE_DISK: 1073741824
	imagick::RESOURCETYPE_FILE: 6144
	imagick::RESOURCETYPE_MAP: 512 MB
	imagick::RESOURCETYPE_MEMORY: 256 MB
	imagick::RESOURCETYPE_THREAD: 1
	imagick::RESOURCETYPE_TIME: 9.22337203685E+18
imagemagick_file_formats: 3FR, 3G2, 3GP, AAI, AI, APNG, ART, ARW, AVI, AVIF, AVS, BGR, BGRA, BGRO, BIE, BMP, BMP2, BMP3, BRF, CAL, CALS, CANVAS, CAPTION, CIN, CIP, CLIP, CMYK, CMYKA, CR2, CR3, CRW, CUR, CUT, DATA, DCM, DCR, DCX, DDS, DFONT, DJVU, DNG, DOT, DPX, DXT1, DXT5, EPDF, EPI, EPS, EPS2, EPS3, EPSF, EPSI, EPT, EPT2, EPT3, ERF, EXR, FAX, FILE, FITS, FRACTAL, FTP, FTS, G3, G4, GIF, GIF87, GRADIENT, GRAY, GRAYA, GROUP4, GV, H, HALD, HDR, HEIC, HISTOGRAM, HRZ, HTM, HTML, HTTP, HTTPS, ICB, ICO, ICON, IIQ, INFO, INLINE, IPL, ISOBRL, ISOBRL6, J2C, J2K, JBG, JBIG, JNG, JNX, JP2, JPC, JPE, JPEG, JPG, JPM, JPS, JPT, JSON, K25, KDC, LABEL, M2V, M4V, MAC, MAGICK, MAP, MASK, MAT, MATTE, MEF, MIFF, MKV, MNG, MONO, MOV, MP4, MPC, MPG, MRW, MSL, MSVG, MTV, MVG, NEF, NRW, NULL, ORF, OTB, OTF, PAL, PALM, PAM, PANGO, PATTERN, PBM, PCD, PCDS, PCL, PCT, PCX, PDB, PDF, PDFA, PEF, PES, PFA, PFB, PFM, PGM, PGX, PICON, PICT, PIX, PJPEG, PLASMA, PNG, PNG00, PNG24, PNG32, PNG48, PNG64, PNG8, PNM, POCKETMOD, PPM, PREVIEW, PS, PS2, PS3, PSB, PSD, PTIF, PWP, RADIAL-GRADIENT, RAF, RAS, RAW, RGB, RGBA, RGBO, RGF, RLA, RLE, RMF, RW2, SCR, SCT, SFW, SGI, SHTML, SIX, SIXEL, SPARSE-COLOR, SR2, SRF, STEGANO, SUN, SVG, SVGZ, TEXT, TGA, THUMBNAIL, TIFF, TIFF64, TILE, TIM, TTC, TTF, TXT, UBRL, UBRL6, UIL, UYVY, VDA, VICAR, VID, VIDEO, VIFF, VIPS, VST, WBMP, WEBM, WEBP, WMF, WMV, WMZ, WPG, X, X3F, XBM, XC, XCF, XPM, XPS, XV, XWD, YCbCr, YCbCrA, YUV
gd_version: 2.3.0
gd_formats: GIF, JPEG, PNG, WebP, BMP, XPM
ghostscript_version: not available

### wp-server ###

server_architecture: Linux 5.4.0-1145-gcp x86_64
httpd_software: Apache
php_version: 8.2.28 64bit
php_sapi: apache2handler
max_input_variables: 10000
time_limit: 3600
memory_limit: 512M
max_input_time: 3600
upload_max_filesize: 50M
php_post_max_size: 100M
curl_version: 7.81.0 OpenSSL/3.0.2
suhosin: false
imagick_availability: true
pretty_permalinks: true
htaccess_extra_rules: false
static_robotstxt_file: true
current: 2025-05-14T01:31:20+00:00
utc-time: Wednesday, 14-May-25 01:31:20 UTC
server-time: 2025-05-14T01:31:19+00:00

### wp-database ###

extension: mysqli
server_version: 8.0.41-32
client_version: mysqlnd 8.2.28
max_allowed_packet: 16777216
max_connections: 500

### wp-constants ###

WP_HOME: undefined
WP_SITEURL: undefined
WP_CONTENT_DIR: /nas/content/live/hiousa/wp-content
WP_PLUGIN_DIR: /nas/content/live/hiousa/wp-content/plugins
WP_MEMORY_LIMIT: 40M
WP_MAX_MEMORY_LIMIT: 512M
WP_DEBUG: false
WP_DEBUG_DISPLAY: false
WP_DEBUG_LOG: false
SCRIPT_DEBUG: false
WP_CACHE: true
CONCATENATE_SCRIPTS: undefined
COMPRESS_SCRIPTS: undefined
COMPRESS_CSS: undefined
WP_ENVIRONMENT_TYPE: undefined
WP_DEVELOPMENT_MODE: undefined
DB_CHARSET: utf8
DB_COLLATE: undefined

### wp-filesystem ###

wordpress: writable
wp-content: writable
uploads: writable
plugins: writable
themes: writable
fonts: does not exist
mu-plugins: writable

```
	</code></pre>

</details>
##Observations
- there are several securitiy tasks in the site health enviroment.
##Questions
1. I was supposed to get accese to the dev and staging sites as well as hiousa.com but I only have accese to hiousa.com and the dev site.

##Rebuild
My current recomendation is that we completly rebuild the site from the ground up. The page editor is junk and then there are so many overlaping plugins I don't even want to start messing with them and to top it off the site is not well built to begin with.
###My Offer
-

---

## From `hiousa-ui-design-checklist.md`

---
title: HIOUSA UI Design Checklist
---
##Design blueprint
[Basic web design example tailored to Hole in One](../../../web-design/Example-Design-Project.md)

## ✅ HIOUSA Rebuild – UI/UX Design Checklist

---

### 🔁 Quote Conversion

- [ ] CTA “Get an Instant Quote” in hero section
- [ ] Sticky header with visible CTA
- [ ] Multi-step quote form (modal or inline)
- [ ] Call-to-action repeated at bottom of page

---

### 📱 Mobile Optimization

- [ ] Mobile-first design principles followed
- [ ] Responsive across all breakpoints
- [ ] Navigation is touch-friendly and collapsible
- [ ] Form elements are thumb-reachable
- [ ] Font sizes ≥ 16px for readability

---

### 🛡 Trust & Credibility

- [ ] Include testimonial carousel with photos/names
- [ ] Add “Over $50M in prizes paid” banner
- [ ] Display licensing and underwriter badges
- [ ] Feature client logos or affiliations

---

### 🧱 Design System & Structure

- [ ] Use 12-column layout grid
- [ ] Max 2 typefaces used across site
- [ ] Pre-designed reusable content blocks
- [ ] Elementor or similar no-code builder selected
- [ ] Design files exportable as templates

---

### 🚀 Performance & Accessibility

- [ ] Theme selected for speed (e.g., Astra, GeneratePress)
- [ ] Images optimized and lazy-loaded
- [ ] Alt tags on all media elements
- [ ] High contrast ratios for accessibility
- [ ] Lighthouse score ≥ 90 for mobile & desktop

---

### 🧪 Measurement Readiness

- [ ] Google Analytics installed
- [ ] Tag Manager added
- [ ] Form submissions tracked as goals
- [ ] Heatmap tool enabled (e.g., Hotjar, Clarity)

---

## From `hiousa-ui-design-strategy.md`

---
title: HIOUSA UI Design Strategy
---

## 🎯 Core UI Design Focus Areas for HIOUSA.com

---

### 1. Conversion-First Layouts
**Goal:** Drive leads via quotes and inquiries.

- 🟢 Primary CTA in hero: “Get an Instant Quote” button
- 🎯 Sticky header with a contrasting CTA button
- 🧩 Reusable blocks: service highlights, trust badges, testimonials, quote form
- 📋 Multi-step quote modal or inline form (don’t send users to a new page)

**Why it matters:** You're selling prize insurance — not blog posts. The UI should funnel users to the quote action fast, with minimal friction.

---

### 2. Clean, Mobile-Optimized Structure
**Goal:** Mobile-first design with responsive behaviors across breakpoints.

- 🧱 Use a 12-column grid system and clear spacing rules
- 📱 Prioritize thumb-reachable CTAs and simplified navigation
- 📉 Collapse secondary content into accordions or tabs on mobile
- 📐 Use larger fonts and buttons for all form inputs

---

### 3. Trust & Authority Signals
**Goal:** Reassure users that HIOUSA is safe, experienced, and legitimate.

- 🏆 Showcases: “$50M+ in prizes paid”, “17,000+ events covered”
- 🧾 A+ insurance rating badge or underwriter partner info
- ✅ Client logos or “As seen in…” banners
- 🗣 Testimonials with names and organizations

---

### 4. Visual Hierarchy & Simplicity
**Goal:** Guide the user visually — no cognitive overload.

- 🧠 One idea per section; scannable copy
- ✍️ Limit to ~2 typefaces (heading + body)
- 🎨 Strong color contrast for CTAs, subtle neutrals for body sections
- 📏 Consistent margins, padding, and spacing across components

---

### 5. Modular, Scalable Design System
**Goal:** Allow the team (Amy, David, future vendors) to reuse and maintain sections.

- ✅ Pre-designed blocks for:
  - Service highlights
  - Case studies/testimonials
  - Industry-specific landing pages
  - Embedded lead capture forms
- 🧱 Built with Elementor or similar (not hardcoded)

---

### 6. Performance & Accessibility
**Goal:** Ensure fast load times and compliance.

- 🚀 Use lightweight themes (GeneratePress, Astra)
- 🧼 Optimize images and only load essentials
- ♿️ Ensure color contrast, alt text, and keyboard nav
- 🌐 Test using Lighthouse, GTMetrix, and WebPageTest

---

## 👇 Recap: Your Top 5 UI Priorities

| Priority                        | Outcome                        |
|-------------------------------|--------------------------------|
| 🔁 Clear quote funnel          | More lead submissions          |
| 📱 Mobile-first layout         | Wider accessibility            |
| 🛡 Trust-building elements     | Higher conversion confidence   |
| 🧱 Modular content blocks      | Faster iterations & scalability|
| 🚀 Speed & accessibility       | Better SEO + usability         |

---

