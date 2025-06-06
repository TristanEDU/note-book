---
title: HIOUSA Project Summary
date: {{date}}
tags: []
---

# HIOUSA Project Summary

General overview of the project goals, features, and internal notes.

---
## From `project-description-for-nathen.md`

# HIOUSA Project Overview – Client Inputs & Research Summary <sub>GPT generated portion, may be inacurate</sub>

---

## 🧩 General Context About the Organization

- **Parent Company**: Prize Indemnity Holdings (PIH), Reno, Nevada
- **Owned Brands**:
  - [Hole-in-One USA](https://www.hiousa.com)
  - [Hole In One International](https://www.holeinoneinternational.com)
  - [Odds On Promotions](https://www.oddsonpromotions.com)
  - [Prize Indemnity Holdings](https://www.prizeindemnityholdings.com)
- **Key Contacts**:
  - Amy Fanter – Director of Marketing (primary contact)
  - David Bebout – IT Director (technical access & infrastructure)
- Historically relied on **offshore developers**, now transitioning to **U.S.-based partners** due to communication difficulties.

---

## 🛠️ Current Job Scope: HIOUSA.com

- **Primary Issue**: Three critical CSS files disappear periodically after cache clears or plugin updates, breaking homepage layout.
- **Site Configuration**:
  - **Theme**: Flat Bootstrap Child Theme (v1.5, outdated)
  - **Builder**: SiteOrigin Page Builder
  - **Hosting**: WP Engine (production, staging, and dev environments)
  - **WordPress Version**: 6.8
  - **PHP Version**: 8.2
- **Quick Quotes Module**:
  - Amazon-based insurance quoting API
  - Isolated from rest of WordPress site **do not modify**
- **Backups**:
  - WP Engine performs **nightly backups**
  - Last known good backup: **April 23, 2025**
- **Plugin Notes**:
  - 25+ plugins, most with auto-updates disabled
  - Includes: Contact Form 7, SiteOrigin Widgets, Wordfence, Smart Slider 3, Yoast SEO, etc.

---

## 💬 Client Statements (Amy Fanter)

- With the company **over 20 years**
- HIOUSA site acquired during pandemic and quickly **outperformed their flagship**
- Believes CSS issue tied to **bad PHP edits** by offshore devs
- Wants to **preserve current design during peak season**, open to redesign after
- Prefers **Elementor** over **Divi**, but new HIOI site is in Divi
- Interested in:
  - Short-term: Fixing the HIOUSA CSS bug
  - Mid-term: Potential theme update or rebuild
  - Long-term: Help launching HIOI site and cleaning up Odds On blog
- Seeks a **responsive, U.S.-based developer** for ongoing support
- Notes:
  - Odds On blog is “a mess”
  - Past developers used PHP hacks for speed, causing instability
  - Values transparency, communication, and WordPress fluency

---

## 🔍 Technical & Operational Insights

- **All sites hosted on WP Engine**
- **Unified infrastructure** across brands
- **Staging/Dev environments** are stable and safe to use
- Amy can manage:
  - HTML/CSS basics
  - Plugin installs and basic troubleshooting
- David can manage:
  - Server configuration
  - Firewall, access control, and backups
- **Key risk**: Prior developers implemented speed optimizations via raw PHP instead of standard WordPress plugins

---

## 💡 Opportunities Identified (Your Research & Observations)

- Recommend **clean rebuild** instead of chasing legacy bugs
- A **modernized theme update** may solve current issues
- **Odds On blog** is WordPress-based and under your control—easy modernization opportunity
- **HIOI Divi site** is close to launch but needs blog setup and polish
- **Odds On Promotions** suffers from:
  - Outdated design
  - Confusing blog navigation
  - Lack of CTAs and SEO elements
  - Visual inconsistencies on mobile

---

#My Aproach <sub>Sorry for not using GPT for this section but it was not giving the correct information</sub>
## My Discoveries
- the site is built with a theme that basicly allows you to drag a drop a text editor and then custom code the particular section of the page.
- there has been more then one change made to the wordpress php files. The one that I think is causing the issues is where they added fonts awsome which according to the client is when the site started having issues.
## My Approach
1. Throughly reviewed site before commiting to anything with client.
2. Determined that a simple patch is not a viable solution. There are just to many issues and it is not worth the clients time or my reputation to try and patch this together.
3. Determined on a strategy to deal with this
	- Propose a site rebuild with limeted support for existing site until the new one is launched (in the initial meeting the client acnowledged that this may be nessary so I think that this will not be a issue)
	- Propose a retainer imidiatly 
###Pricing
**Project Scope:**
- Rebuild the entire site from scratch on a clean WordPress install using **Elementor**
- Maintain existing layout/branding, with optional modernization if desired
- Migrate content and structure into a clean, responsive theme
- Integrate Quick Quotes as a placeholder (no changes to AWS backend)
- Deliver a fast, secure, and stable site on WP Engine’s infrastructure
- Apply performance and accessibility best practices

**Timeline:** ~2–3 weeks
**Ownership:** All assets and code transfer fully to you upon payment
**Flat Rate:** $2,400 – $3,000

### 🔄 Phase 2: Ongoing Retainer (Optional but Recommended)

| Tier       | Monthly Fee | Hours Included | Notes |
|------------|-------------|----------------|-------|
| **Basic**  | $375        | 10 hrs         | Light maintenance, plugin updates |
| **Standard** | $700      | 20 hrs         | Page updates, light design/dev, multi-site coverage |
| **Premium**  | $1,200    | 30 hrs         | Priority access, Divi build support, content overhauls |

**Benefits:**
- WP updates and plugin maintenance
- Staging site support (via WP Engine)
- Layout, copy, and content changes
- Priority response and availability
- Premium includes planning calls and 10% rollover of unused time

### 💡 Bundle Offer

- If you commit to any retainer tier for **3 months**, I’ll apply a **10% discount to the rebuild cost**.
- If you commit to either of the uper tier plans for **6 months** I will apply a **10% discount to the retainer**
The hoped for outcome is that she will sign up for the middel tier for 6 months. In light of that I will try and aim for the Premium tier.

---

## From `project-notes-hiousa.md`

#### WordPress Project Notes – HIOUSA.com

**Current Goal:**
Diagnose and resolve recurring CSS file loss after updates/caching events. Primary issue occurs unpredictably and results in homepage format loss.

**Key Dates:**
- Last known good backup: **April 23, 2025**
- Initial contact call and scope meeting: **May 7, 2025**

**People Involved:**
- Amy Fanter (Marketing Lead): ../assets/Amy-Fanter.md
- David Bebout (IT Director): Oversees server, staging, and access

**Platform Context:**
- Hosted on **WP Engine**
- Multiple environments: Production, Staging, Development
- Staging/Dev used for Quick Quotes integration testing
- Quick Quotes uses Amazon-based quoting API but is out-of-scope for current fix
- Theme in use is **SiteOrigin**, but a future site (in Divi) is under construction

**Challenges:**
- Previous devs made backend PHP edits (likely Google Fonts, custom cache layers)
- Frequent plugin updates triggering cascade failures
- Potential corrupted theme/customizer logic

**Short-Term Action Items:**
1. Access WP Engine and WordPress admin
2. Analyze root cause of CSS file loss
3. Provide quote and recommendation (by mid-next week)
4. Maintain formatting during active golf season

**Long-Term Opportunities:**
- Assist with new Hole In One International site (Divi-based)
- Clean up and modernize Odds On Promotions WordPress blog
- Ongoing maintenance and optimization

**Call Recording:**
- [Fathom Transcript](https://fathom.video/share/fyBCTRNmN-Qs8qXoNt1Vu933zWP2TxZt)

**Reference Emails:**
- [Project Scope Email](../assets/WordPress Work HIOUSA.eml)
- [Pre-Call Expectations](../assets/What to Expect in Today’s Call.eml)

See [organization-overview.md](organization-overview.md) for structural context.

---

