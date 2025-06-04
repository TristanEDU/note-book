# 🧠 Using Adobe Fonts with Elementor Free via the Project ID Workaround

If you want to use **Adobe Fonts (Typekit)** like **Myriad Pro** in Elementor Free and don't have access to the original Adobe account, there is a reliable **workaround** using the **Custom Adobe Fonts (Typekit)** plugin.

---

## ✅ Objective

Enable fonts like **Myriad Pro** to:
- Be available in the **Elementor font dropdown**
- Work with **Elementor Free**
- Avoid requiring direct access to Adobe Fonts dashboard
- Avoid a Creative Cloud subscription (as long as the existing kit still works)

---

## 🔧 Plugin Used

**Plugin:** `Custom Adobe Fonts (Typekit)`  
**Author:** Brainstorm Force  
**Purpose:** Allows you to register Adobe Fonts into WordPress and Elementor by just providing the **Project ID**.

---

## 🔍 What is the Project ID?

When Adobe Fonts gives you an embed URL like:

```html
<link rel="stylesheet" href="https://use.typekit.net/fqf3yti.css">
````

The `fqf3yti` portion is your **Project ID**.

This ID uniquely references the published **web font kit** created under an Adobe Fonts account. You **do not need to own the account** — if the kit is public and published, the fonts will load fine.

---

## ✅ How to Use This in Elementor Free

### 🔹 Step-by-Step Instructions

1. **Install the Plugin**

   * Go to `Plugins > Add New`
   * Search for: `Custom Adobe Fonts (Typekit)`
   * Author: Brainstorm Force
   * Click **Install** and then **Activate**

2. **Find the Project ID**

   * Locate the `<link rel="stylesheet" href="https://use.typekit.net/abc123.css">` in the site `<head>` (you can find it via View Source or browser DevTools)
   * Copy only the part between the last `/` and `.css`, e.g.:

     ```
     abc123
     ```

3. **Add the Project ID to the Plugin**

   * Go to: `Appearance > Adobe Fonts`
   * Paste the ID (e.g., `abc123`) into the **Project ID** field
   * Click **Save**

4. **Use in Elementor**

   * Now open Elementor and go to **Site Settings > Typography** or edit any widget and go to **Style > Typography**
   * The Adobe fonts (e.g., `Myriad Pro`, `Myriad Pro Condensed`) should now appear in the **Font Family** dropdown

---

## ⚠️ Limitations

* You can only use **weights/styles** that are included in the published kit
* If the kit only includes `font-weight: 700`, you won’t be able to use light, italic, or thin variants
* You cannot **edit** the kit unless you have access to the original Adobe Fonts account

---

## ✅ Benefits of This Workaround

* No need for Elementor Pro
* Fonts show up in the Elementor UI (not just via custom CSS)
* Retains full Elementor Free design flow
* Doesn’t require re-hosting fonts or editing functions.php

---

## 🧪 Test Before You Rely On It

Once you enter the Project ID:

* Go to any Elementor text widget
* Set the font to `Myriad Pro`
* Set the weight to `700`
* Preview the site and inspect the element to confirm the correct font is applied

---

## 🗂 Example: Known Working Kit

```html
<link rel="stylesheet" href="https://use.typekit.net/pwm1bwo.css">
```

Valid Project ID:

```
pwm1bwo
```

Includes:

* Myriad Pro (700)
* Myriad Pro Condensed (700)
---

## ✅ Summary

This is a clean workaround to **use premium Adobe Fonts in Elementor Free** when:

* You don’t control the Adobe account
* You just need access to fonts from a known working embed
* You want to avoid Elementor Pro and still use fonts from the dropdown

**Tip:** Always back up the ID and embed code — if the Adobe account deletes the kit, the font will stop working.

