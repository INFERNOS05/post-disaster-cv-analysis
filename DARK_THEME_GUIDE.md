# 🌙 Dark Theme Visual Guide

## Premium Dark Dashboard Design

### Color Scheme

```
┌─────────────────────────────────────────────────────────────┐
│                    DARK THEME PALETTE                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Background (Main)          Surface (Cards)                  │
│  #0F172A ████████           #1E293B ████████                 │
│  Dark Slate                 Lighter Slate                    │
│                                                               │
│  Primary (Accent)           Secondary (Success)              │
│  #3B82F6 ████████           #10B981 ████████                 │
│  Bright Blue                Emerald Green                    │
│                                                               │
│  Accent (Highlight)         Warning (Medium)                 │
│  #8B5CF6 ████████           #F59E0B ████████                 │
│  Purple                     Amber                            │
│                                                               │
│  Danger (Severe)            Text (Primary)                   │
│  #EF4444 ████████           #F1F5F9 ████████                 │
│  Red                        Light Gray                       │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🛰️ CV-Based Post-Disaster Damage Assessment                │
│  Advanced Computer Vision Pipeline for Satellite Imagery    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐             │
│  │Upload│ │Pipeline│ │Damage│ │Heatmap│ │Reports│            │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘             │
│                                                               │
│  [Active tab content displayed here]                         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab 1: Upload & Process

```
┌─────────────────────────────────────────────────────────────┐
│  📤 Upload Satellite Image                                   │
│  Upload a pre-disaster satellite image to begin analysis    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────┐  ┌──────────────────┐         │
│  │                         │  │ 📋 Image Metadata │         │
│  │   [Image Preview]       │  │                   │         │
│  │                         │  │ Filename: sat.jpg │         │
│  │   Drag & Drop Zone      │  │ Size: 245 KB      │         │
│  │                         │  │ Dimensions: 800×600│        │
│  │                         │  │ Format: JPEG      │         │
│  └─────────────────────────┘  │                   │         │
│                                │ ┌──────────────┐ │         │
│                                │ │🚀 Run Full CV│ │         │
│                                │ │   Analysis   │ │         │
│                                │ └──────────────┘ │         │
│                                └──────────────────┘         │
│                                                               │
│  Progress: ████████████░░░░░░░░ 60%                         │
│  Status: Performing segmentation...                          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab 2: CV Processing Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│  🔬 Computer Vision Processing Pipeline                      │
│  Visualize each stage of the CV processing workflow         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Stage 1: Image Preprocessing                                │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  📸 Original Input   │  │  📐 Resized (512×512)│        │
│  │  [Image]             │  │  [Image]             │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
│  Stage 2: Image Enhancement                                  │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  🔲 Original         │  │  ✨ Enhanced         │        │
│  │  [Image]             │  │  [Image]             │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
│  Stage 3: Edge Detection                                     │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  ✨ Enhanced Input   │  │  🔍 Canny Edges      │        │
│  │  [Image]             │  │  [Image]             │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
│  Stage 4: Image Segmentation                                 │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  ✨ Enhanced Input   │  │  🎨 Segmented Regions│        │
│  │  [Image]             │  │  [Image]             │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
│  Stage 5: Feature Extraction                                 │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  ✨ Enhanced Input   │  │  🎯 Harris Corners   │        │
│  │  [Image]             │  │  [Image]             │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab 3: Damage Assessment

```
┌─────────────────────────────────────────────────────────────┐
│  ⚠️ Damage Assessment Results                                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ Overall  │ │ Severity │ │  Total   │ │Confidence│      │
│  │  Medium  │ │  6.8/10  │ │  45.2%   │ │  89.5%   │      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │
│                                                               │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  📸 Input Image      │  │  🎯 Damage Regions   │        │
│  │                      │  │                      │        │
│  │  [Original Image]    │  │  [Predicted Damage]  │        │
│  │                      │  │                      │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                               │
│  📊 Damage Distribution                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  100│                                                │   │
│  │   80│ ███                                            │   │
│  │   60│ ███ ███                                        │   │
│  │   40│ ███ ███ ███                                    │   │
│  │   20│ ███ ███ ███                                    │   │
│  │    0└─────────────────                               │   │
│  │      Low  Med  Severe                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab 4: Heatmap Analysis

```
┌─────────────────────────────────────────────────────────────┐
│  🗺️ Heatmap Analysis                                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────┐  ┌──────────────────┐         │
│  │                         │  │ 🎨 Severity      │         │
│  │  🔥 Damage Intensity    │  │    Legend        │         │
│  │     Heatmap             │  │                   │         │
│  │                         │  │ ████ Low Risk    │         │
│  │  [Colormap Overlay]     │  │ 🟢 0-30%         │         │
│  │                         │  │                   │         │
│  │                         │  │ ████ Medium Risk │         │
│  │                         │  │ 🟡 30-60%        │         │
│  │                         │  │                   │         │
│  │                         │  │ ████ High Risk   │         │
│  │                         │  │ 🔴 60-100%       │         │
│  │                         │  │                   │         │
│  └─────────────────────────┘  │ 📈 Risk Zones    │         │
│                                │                   │         │
│                                │ Low:    25.3%    │         │
│                                │ Medium: 48.2%    │         │
│                                │ High:   26.5%    │         │
│                                └──────────────────┘         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Tab 5: Reports & Export

```
┌─────────────────────────────────────────────────────────────┐
│  📊 Reports & Export                                         │
│  Download Analysis Results                                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │ 🖼️ PNG Images│ │ 📊 CSV Report│ │ 📄 PDF Report│        │
│  │              │ │              │ │              │        │
│  │ Download     │ │ Download     │ │ Generate     │        │
│  │ processed    │ │ metrics as   │ │ comprehensive│        │
│  │ images       │ │ CSV          │ │ report       │        │
│  │              │ │              │ │              │        │
│  │ ┌──────────┐ │ │ ┌──────────┐ │ │ ┌──────────┐ │        │
│  │ │📥 Heatmap│ │ │ │📥 Download│ │ │ │📥 Generate│ │        │
│  │ └──────────┘ │ │ └──────────┘ │ │ └──────────┘ │        │
│  │ ┌──────────┐ │ │              │ │              │        │
│  │ │📥 Damage │ │ │              │ │              │        │
│  │ └──────────┘ │ │              │ │              │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                               │
│  📋 Analysis Summary                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Category          │ Result      │ Status            │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ Classification    │ Medium      │ ⚠️                │   │
│  │ Severity Score    │ 6.8/10      │ 📊                │   │
│  │ Total Affected    │ 45.2%       │ 🗺️                │   │
│  │ Confidence Level  │ 89.5%       │ ✅                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## UI Components

### Metric Cards
```
┌──────────────────┐
│  Metric Label    │
│  ──────────────  │
│                  │
│     8.5/10       │  ← Large value (gradient color)
│                  │
│  ──────────────  │
│  Severity Score  │  ← Small label (muted)
└──────────────────┘
```

### Progress Bar
```
Processing: ████████████░░░░░░░░ 60%
Status: Performing segmentation...
```

### Severity Badges
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│   Low   │  │ Medium  │  │ Severe  │
└─────────┘  └─────────┘  └─────────┘
 #10B981      #F59E0B      #EF4444
  Green        Amber         Red
```

### Image Containers
```
┌─────────────────────────┐
│                         │
│    [Image Display]      │
│                         │
├─────────────────────────┤
│  📸 Image Label         │
└─────────────────────────┘
```

---

## Responsive Behavior

### Desktop (> 768px)
```
┌──────────────┬──────────────┐
│   Column 1   │   Column 2   │
│   [Image]    │   [Image]    │
└──────────────┴──────────────┘
```

### Mobile (< 768px)
```
┌──────────────┐
│   Column 1   │
│   [Image]    │
├──────────────┤
│   Column 2   │
│   [Image]    │
└──────────────┘
```

---

## Gradient Effects

### Hero Title
```
Background: Linear gradient (135deg)
  #3B82F6 (Blue) → #8B5CF6 (Purple)
Text: Transparent with gradient clip
Effect: Shimmering gradient text
```

### Buttons
```
Background: Linear gradient (135deg)
  #3B82F6 (Blue) → #8B5CF6 (Purple)
Hover: Transform translateY(-2px)
Shadow: 0 6px 20px rgba(59, 130, 246, 0.4)
```

### Cards
```
Background: Linear gradient (135deg)
  #1E293B (Surface) → #334155 (Surface Light)
Border: 1px solid rgba(148, 163, 184, 0.1)
Shadow: 0 4px 20px rgba(0,0,0,0.4)
```

---

## Typography Hierarchy

```
Hero Title (H1)
  Font Size: 2.5rem (40px)
  Weight: 900 (Black)
  Color: Gradient (Blue → Purple)

Section Header (H2)
  Font Size: 2rem (32px)
  Weight: 700 (Bold)
  Color: #F1F5F9 (Light Gray)

Card Header (H3)
  Font Size: 1.5rem (24px)
  Weight: 700 (Bold)
  Color: #3B82F6 (Primary Blue)

Subsection (H4)
  Font Size: 1.25rem (20px)
  Weight: 600 (Semi-Bold)
  Color: #F1F5F9 (Light Gray)

Body Text
  Font Size: 1rem (16px)
  Weight: 400 (Regular)
  Color: #94A3B8 (Muted Gray)

Labels
  Font Size: 0.875rem (14px)
  Weight: 600 (Semi-Bold)
  Color: #94A3B8 (Muted Gray)
  Transform: Uppercase
  Letter Spacing: 1px
```

---

## Animation & Transitions

### Hover Effects
```css
Button Hover:
  transform: translateY(-2px)
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4)
  transition: all 0.3s ease

Card Hover:
  border-color: #3B82F6
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.2)
  transition: all 0.3s ease
```

### Progress Animation
```
Smooth gradient animation
Linear progress from 0% to 100%
Color: Blue → Purple gradient
Duration: Based on processing stage
```

---

**🌙 Dark Theme Complete - Professional & Modern**

The premium dark theme creates a sophisticated, professional appearance that makes the CV workflow look substantial and production-ready.
