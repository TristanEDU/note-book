# CSS Relative Units

Notes on how to use common CSS relative units.

## `rem`
- Stands for **root em**.
- Equals the font size of the root element (`<html>`).
- Great for establishing consistent spacing and type scale.

## `em`
- Relative to the font size of the current element.
- Inherits size from its parent, so values compound when nested.
- Useful when elements should scale with the local font size.

## `vh`
- Represents a percentage of the viewport height.
- `100vh` is the full height of the viewport.
- Common for creating full screen sections or hero banners.

## `vw`
- Represents a percentage of the viewport width.
- `100vw` is the full width of the viewport.
- Be mindful of scrollbars which may cause horizontal overflow.
