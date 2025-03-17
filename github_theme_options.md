# <div align="center">GitHub Color Scheme Customization Guide</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=150&section=header&text=GitHub%20Theme%20Options&fontSize=40&fontAlignY=35&animation=fadeIn&fontColor=white" width="100%" alt="GitHub Theme Options Header"/>
</div>

<div align="center">
  <p>A collection of beautiful color schemes to customize your GitHub experience.</p>
</div>

## Why Customize GitHub's Appearance?

GitHub's default color scheme might not appeal to everyone. Customizing the interface can:

- Reduce eye strain during long coding sessions
- Match your personal aesthetic preferences
- Improve readability and focus
- Make your development environment more enjoyable

## How to Apply Custom Themes

1. **Install a browser extension**:
   - For Chrome: [Stylus](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne)
   - For Firefox: [Stylus](https://addons.mozilla.org/en-US/firefox/addon/styl-us/)
   - For Safari: [Cascadea](https://cascadea.app/)

2. **Create a new style**:
   - Click on the extension icon
   - Select "Create new style"
   - Paste the CSS code from `custom_github_theme.css`
   - Set it to apply to "URLs on the domain" `github.com`
   - Name your style and save

3. **Refresh GitHub** to see the changes

## Color Scheme Options

Below are several color schemes you can use. To apply a different scheme, simply replace the `:root` section in the CSS file with one of these options.

### 1. Moonlight (Default in the CSS file)

A soothing dark blue theme with purple and gold accents.

```css
:root {
  --color-bg-canvas: #1e2030;
  --color-bg-primary: #222436;
  --color-bg-secondary: #2f334d;
  --color-bg-tertiary: #292e42;
  --color-border-primary: #444a73;
  --color-text-primary: #c8d3f5;
  --color-text-secondary: #a9b8e8;
  --color-text-tertiary: #7a88cf;
  --color-link: #65bcff;
  --color-link-hover: #82d8ff;
  --color-accent: #c099ff;
  --color-accent-emphasis: #ffc777;
  --color-success: #c3e88d;
  --color-danger: #ff757f;
  --color-warning: #ffc777;
  --color-info: #65bcff;
}
```

### 2. Forest Night

A nature-inspired dark theme with green and earthy tones.

```css
:root {
  --color-bg-canvas: #1c2119;
  --color-bg-primary: #232b1f;
  --color-bg-secondary: #2d3729;
  --color-bg-tertiary: #2a3324;
  --color-border-primary: #4a5d41;
  --color-text-primary: #d3c6aa;
  --color-text-secondary: #b9b08f;
  --color-text-tertiary: #9a9176;
  --color-link: #7fbbb3;
  --color-link-hover: #a7c080;
  --color-accent: #d699b6;
  --color-accent-emphasis: #e67e80;
  --color-success: #a7c080;
  --color-danger: #e67e80;
  --color-warning: #dbbc7f;
  --color-info: #7fbbb3;
}
```

### 3. Nord

A clean, arctic-inspired theme with cool blue tones.

```css
:root {
  --color-bg-canvas: #2e3440;
  --color-bg-primary: #3b4252;
  --color-bg-secondary: #434c5e;
  --color-bg-tertiary: #4c566a;
  --color-border-primary: #5e81ac;
  --color-text-primary: #eceff4;
  --color-text-secondary: #e5e9f0;
  --color-text-tertiary: #d8dee9;
  --color-link: #88c0d0;
  --color-link-hover: #8fbcbb;
  --color-accent: #b48ead;
  --color-accent-emphasis: #ebcb8b;
  --color-success: #a3be8c;
  --color-danger: #bf616a;
  --color-warning: #ebcb8b;
  --color-info: #81a1c1;
}
```

### 4. Dracula

A popular dark theme with vibrant colors.

```css
:root {
  --color-bg-canvas: #282a36;
  --color-bg-primary: #2d303e;
  --color-bg-secondary: #343746;
  --color-bg-tertiary: #3c3f58;
  --color-border-primary: #6272a4;
  --color-text-primary: #f8f8f2;
  --color-text-secondary: #e2e2dc;
  --color-text-tertiary: #bfbfb8;
  --color-link: #8be9fd;
  --color-link-hover: #9aeffd;
  --color-accent: #bd93f9;
  --color-accent-emphasis: #ffb86c;
  --color-success: #50fa7b;
  --color-danger: #ff5555;
  --color-warning: #ffb86c;
  --color-info: #8be9fd;
}
```

### 5. Solarized Dark

A scientific precision color scheme with selective contrast.

```css
:root {
  --color-bg-canvas: #002b36;
  --color-bg-primary: #073642;
  --color-bg-secondary: #0d4a59;
  --color-bg-tertiary: #115c6d;
  --color-border-primary: #2aa198;
  --color-text-primary: #fdf6e3;
  --color-text-secondary: #eee8d5;
  --color-text-tertiary: #93a1a1;
  --color-link: #268bd2;
  --color-link-hover: #2aa198;
  --color-accent: #6c71c4;
  --color-accent-emphasis: #cb4b16;
  --color-success: #859900;
  --color-danger: #dc322f;
  --color-warning: #b58900;
  --color-info: #268bd2;
}
```

### 6. GitHub Dark Dimmed (Similar to GitHub's own dark theme but customized)

A softer dark theme that's easier on the eyes.

```css
:root {
  --color-bg-canvas: #22272e;
  --color-bg-primary: #2d333b;
  --color-bg-secondary: #343b44;
  --color-bg-tertiary: #3a434f;
  --color-border-primary: #545d68;
  --color-text-primary: #adbac7;
  --color-text-secondary: #909dab;
  --color-text-tertiary: #768390;
  --color-link: #539bf5;
  --color-link-hover: #6cb6ff;
  --color-accent: #986ee2;
  --color-accent-emphasis: #daaa3f;
  --color-success: #57ab5a;
  --color-danger: #e5534b;
  --color-warning: #daaa3f;
  --color-info: #539bf5;
}
```

### 7. Synthwave '84

A retro, neon-inspired theme reminiscent of 80s aesthetics.

```css
:root {
  --color-bg-canvas: #241b2f;
  --color-bg-primary: #2a1f37;
  --color-bg-secondary: #34294a;
  --color-bg-tertiary: #3e325a;
  --color-border-primary: #ff7edb;
  --color-text-primary: #f9f9f9;
  --color-text-secondary: #d8d8d8;
  --color-text-tertiary: #a8a8a8;
  --color-link: #36f9f6;
  --color-link-hover: #72f1fd;
  --color-accent: #ff7edb;
  --color-accent-emphasis: #ffcc00;
  --color-success: #72f1b8;
  --color-danger: #fe4450;
  --color-warning: #ffcc00;
  --color-info: #36f9f6;
}
```

### 8. Light Theme - Soft Pastel

If you prefer a light theme, this soft pastel option is easy on the eyes.

```css
:root {
  --color-bg-canvas: #f8f5f2;
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f3f0ed;
  --color-bg-tertiary: #eae6e1;
  --color-border-primary: #d1cdc7;
  --color-text-primary: #383a42;
  --color-text-secondary: #5c6370;
  --color-text-tertiary: #8a8a8a;
  --color-link: #4078f2;
  --color-link-hover: #0184bc;
  --color-accent: #a626a4;
  --color-accent-emphasis: #c18401;
  --color-success: #50a14f;
  --color-danger: #e45649;
  --color-warning: #c18401;
  --color-info: #0184bc;
}
```

## Customizing the Contribution Graph

The contribution graph colors can be customized separately. Find this section in the CSS:

```css
/* Contribution graph */
.js-calendar-graph-svg rect {
  stroke: var(--color-bg-canvas) !important;
}

.js-calendar-graph-svg rect[data-level="1"] {
  fill: #4a5482 !important;
}

.js-calendar-graph-svg rect[data-level="2"] {
  fill: #6273b3 !important;
}

.js-calendar-graph-svg rect[data-level="3"] {
  fill: #82a8ff !important;
}

.js-calendar-graph-svg rect[data-level="4"] {
  fill: #c099ff !important;
}
```

### Alternative Contribution Graph Color Schemes:

#### Gradient Green (Classic GitHub style but enhanced)

```css
.js-calendar-graph-svg rect[data-level="1"] {
  fill: #4a9c59 !important;
}

.js-calendar-graph-svg rect[data-level="2"] {
  fill: #37c871 !important;
}

.js-calendar-graph-svg rect[data-level="3"] {
  fill: #26e485 !important;
}

.js-calendar-graph-svg rect[data-level="4"] {
  fill: #00ff9d !important;
}
```

#### Sunset Gradient

```css
.js-calendar-graph-svg rect[data-level="1"] {
  fill: #e67e80 !important;
}

.js-calendar-graph-svg rect[data-level="2"] {
  fill: #e69875 !important;
}

.js-calendar-graph-svg rect[data-level="3"] {
  fill: #dbbc7f !important;
}

.js-calendar-graph-svg rect[data-level="4"] {
  fill: #ffdf87 !important;
}
```

#### Ocean Blue

```css
.js-calendar-graph-svg rect[data-level="1"] {
  fill: #3b5bdb !important;
}

.js-calendar-graph-svg rect[data-level="2"] {
  fill: #4c6ef5 !important;
}

.js-calendar-graph-svg rect[data-level="3"] {
  fill: #5c7cfa !important;
}

.js-calendar-graph-svg rect[data-level="4"] {
  fill: #748ffc !important;
}
```

## Further Customization

You can modify any part of the CSS to suit your preferences. Here are some elements you might want to customize:

- Button colors and hover states
- Code syntax highlighting
- Issue and PR labels
- Navigation elements
- Profile sidebar

## Sharing Your Theme

If you create a theme you love, consider sharing it with others:

1. Upload your CSS to a GitHub Gist
2. Share it on social media with #GitHubTheme
3. Submit it to userstyles.org or similar theme repositories

## Need Help?

If you need assistance with customizing your GitHub theme or have questions about CSS, feel free to reach out to me on [GitHub](https://github.com/rahulgaur608) or [Twitter](https://twitter.com/rahulgaur608).

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer" width="100%" alt="Footer Banner"/>
</div>

<div align="center">
  <p>Enjoy your personalized GitHub experience!</p>
</div> 