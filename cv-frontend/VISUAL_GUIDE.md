# 🎨 Visual Guide - CV Disaster Dashboard

## 📱 Page Previews

### 🏠 Dashboard Home
```
┌─────────────────────────────────────────────────────────────┐
│  🛰️ CV Disaster Dashboard                    [Sidebar] ☰   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│     CV-Based Post-Disaster Damage Assessment &               │
│     Urban Density Mapping using Satellite Imagery            │
│                                                               │
│     AI-powered satellite imagery analysis for disaster       │
│     recovery and urban planning.                             │
│                                                               │
│                   [🚀 Start Analysis]                         │
│                                                               │
│  📊 Key Performance Indicators                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 🛰️       │ │ ⚠️       │ │ 🏙️       │ │ 🎯       │       │
│  │ Images   │ │ Damage   │ │ Dense    │ │ Analysis │       │
│  │ Processed│ │ Severity │ │ Urban    │ │ Accuracy │       │
│  │   142    │ │   7.4    │ │ Zones 38 │ │  94.2%   │       │
│  │   +12    │ │   -0.3   │ │   +5     │ │  +1.1    │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│                                                               │
│  🔄 How It Works                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │    📤    │ │    🤖    │ │    📊    │                    │
│  │  Upload  │ │  Analyze │ │   View   │                    │
│  │          │ │          │ │  Results │                    │
│  └──────────┘ └──────────┘ └──────────┘                    │
│                                                               │
│  ─────────────────────────────────────────────────────────  │
│  Project Team | OST Project 2026 | Powered by Streamlit    │
└─────────────────────────────────────────────────────────────┘
```

### 📤 Upload Page
```
┌─────────────────────────────────────────────────────────────┐
│  📤 Upload Satellite Image                                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Upload a satellite image to begin AI-powered damage         │
│  assessment and urban density analysis.                      │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  📁 Choose a satellite image                         │    │
│  │  Drag and drop file here                             │    │
│  │  Limit 200MB per file • JPG, PNG, TIFF              │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  🖼️ Image Preview                                            │
│  ┌─────────────────────┐  ┌──────────────────┐             │
│  │                     │  │ 📋 Image Metadata │             │
│  │   [Satellite Image] │  │                   │             │
│  │                     │  │ Filename: sat.jpg │             │
│  │                     │  │ File Size: 245 KB │             │
│  │                     │  │ Dimensions: 800×600│            │
│  │                     │  │ Format: JPEG      │             │
│  └─────────────────────┘  └──────────────────┘             │
│                                                               │
│              [🤖 Analyze Image]                              │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### ⚠️ Damage Assessment Page
```
┌─────────────────────────────────────────────────────────────┐
│  ⚠️ Damage Assessment Results                                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  🖼️ Original Image          📊 Overall Assessment           │
│  ┌─────────────────────┐    ┌──────────────────┐           │
│  │                     │    │ [Medium Damage]   │           │
│  │   [Satellite Image] │    │                   │           │
│  │                     │    │ Confidence Score  │           │
│  │                     │    │      87.0%        │           │
│  │                     │    │ ████████░░ 87%    │           │
│  └─────────────────────┘    └──────────────────┘           │
│                                                               │
│  📋 Region-wise Damage Statistics                            │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ Region │ Damage Class │ Affected Area │ Confidence │    │
│  ├─────────────────────────────────────────────────────┤    │
│  │ Zone A │ Severe       │ 45.2%         │ 0.92       │    │
│  │ Zone B │ Medium       │ 32.8%         │ 0.85       │    │
│  │ Zone C │ Low          │ 15.3%         │ 0.78       │    │
│  │ Zone D │ Medium       │ 28.7%         │ 0.88       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│              [📥 Download Report (CSV)]                      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### 🏙️ Urban Density Page
```
┌─────────────────────────────────────────────────────────────┐
│  🏙️ Urban Density Mapping                                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  🗺️ Satellite Image with Density Overlay                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                                                       │    │
│  │         [Satellite Image with Overlay]               │    │
│  │                                                       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  📊 Summary Metrics                                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │ Built-Up Area│ │ Population   │ │ Dominant     │        │
│  │    62.5%     │ │ Proxy: 7.8   │ │ Class:       │        │
│  │              │ │              │ │ Moderate     │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                               │
│  🏘️ Density Zone Breakdown                                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │ 🌾       │ │ 🏘️       │ │ 🏙️       │                    │
│  │ Sparse   │ │ Moderate │ │ Dense    │                    │
│  │  25.3%   │ │  48.2%   │ │  26.5%   │                    │
│  └──────────┘ └──────────┘ └──────────┘                    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### 📊 Analytics Page
```
┌─────────────────────────────────────────────────────────────┐
│  📊 Analytics Reports                                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  📈 Damage Trend by Region                                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  100│                                                │    │
│  │   80│ ███ ███ ███ ███ ███ ███                       │    │
│  │   60│ ███ ███ ███ ███ ███ ███                       │    │
│  │   40│ ███ ███ ███ ███ ███ ███                       │    │
│  │   20│ ███ ███ ███ ███ ███ ███                       │    │
│  │    0└─────────────────────────────                  │    │
│  │      A   B   C   D   E   F                          │    │
│  │      ■ Low  ■ Medium  ■ Severe                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌──────────────────────────┐ ┌──────────────────────────┐  │
│  │ 📅 Monthly Processed     │ │ 🎯 Model Confidence      │  │
│  │    Images                │ │    History               │  │
│  │  ┌────────────────────┐  │ │  ┌────────────────────┐ │  │
│  │  │ 35│                │  │ │  │1.0│          ╱─╲    │ │  │
│  │  │ 30│ ███            │  │ │  │0.9│      ╱─╲╱   ╲  │ │  │
│  │  │ 25│ ███ ███        │  │ │  │0.8│  ╱─╲╱         │ │  │
│  │  │ 20│ ███ ███ ███    │  │ │  │0.7│╱─              │ │  │
│  │  │  0└────────────────│  │ │  │  0└────────────────│ │  │
│  │  │    Jan Feb ... Dec │  │ │  │    1  5  10  15  20│ │  │
│  │  └────────────────────┘  │ │  └────────────────────┘ │  │
│  └──────────────────────────┘ └──────────────────────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### ⚙️ Settings Page
```
┌─────────────────────────────────────────────────────────────┐
│  ⚙️ Settings                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  🤖 Model Configuration                                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Confidence Threshold                                  │   │
│  │ ├────────●──────────┤ 0.50                           │   │
│  │                                                        │   │
│  │ Damage Sensitivity Level                              │   │
│  │ [Medium ▼]                                            │   │
│  │                                                        │   │
│  │ ☑ Enable Heatmap Overlay                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  🎨 Display Preferences                                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Chart Color Scheme                                    │   │
│  │ [Default ▼]                                           │   │
│  │                                                        │   │
│  │ ☑ Show Dummy Data Banner                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│              [🔄 Reset to Defaults]                          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 🎨 Color Palette

```
Primary (Blue)      Secondary (Green)   Background         Text
#2563EB            #10B981             #F8FAFC            #111827
████████           ████████            ████████           ████████

Danger (Red)       Amber (Orange)      Muted              
#EF4444            #F59E0B             rgba(17,24,39,0.5)
████████           ████████            ████████           
```

## 📐 Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Header (Logo + Title)                                       │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                   │
│ Sidebar  │  Main Content Area                               │
│          │                                                   │
│ • Home   │  ┌─────────────────────────────────────────┐    │
│ • Upload │  │                                          │    │
│ • Damage │  │  Page Content                           │    │
│ • Density│  │                                          │    │
│ • Analytics│  │                                          │    │
│ • Settings│  │                                          │    │
│ • About  │  │                                          │    │
│          │  └─────────────────────────────────────────┘    │
│          │                                                   │
├──────────┴──────────────────────────────────────────────────┤
│  Footer (Project Team | OST 2026 | Powered by...)          │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Component Hierarchy

```
App (app.py)
├── Sidebar Navigation
│   ├── Logo
│   ├── Title
│   └── Page Links (7)
│
├── Main Content
│   ├── Hero Section
│   │   ├── Title
│   │   ├── Description
│   │   └── CTA Button
│   │
│   ├── KPI Cards (4)
│   │   ├── Icon
│   │   ├── Value
│   │   ├── Label
│   │   └── Delta
│   │
│   └── How It Works (3 steps)
│       ├── Upload
│       ├── Analyze
│       └── View Results
│
└── Footer
    ├── Project Team
    ├── OST Project 2026
    └── Tech Stack
```

## 📱 Responsive Breakpoints

```
Desktop (> 768px)          Tablet (768px)           Mobile (< 768px)
┌──────────────────┐      ┌──────────────┐         ┌──────────┐
│ [4 columns]      │      │ [2 columns]  │         │ [1 column]│
│ ┌──┐┌──┐┌──┐┌──┐│      │ ┌──┐┌──┐     │         │ ┌────────┐│
│ │  ││  ││  ││  ││      │ │  ││  │     │         │ │        ││
│ └──┘└──┘└──┘└──┘│      │ └──┘└──┘     │         │ └────────┘│
└──────────────────┘      │ ┌──┐┌──┐     │         │ ┌────────┐│
                          │ │  ││  │     │         │ │        ││
                          │ └──┘└──┘     │         │ └────────┘│
                          └──────────────┘         └──────────┘
```

## 🎭 Interactive Elements

### Buttons
```
Primary Button          Secondary Button       Danger Button
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ 🚀 Action    │       │ ⚙️ Settings  │       │ 🗑️ Delete    │
└──────────────┘       └──────────────┘       └──────────────┘
#2563EB (Blue)         #6B7280 (Gray)         #EF4444 (Red)

Hover Effect:          Hover Effect:          Hover Effect:
Darker + Shadow        Darker                 Darker + Shadow
```

### Cards
```
KPI Card               Chart Card             Result Card
┌──────────────┐      ┌──────────────┐       ┌──────────────┐
│ 🎯 Icon      │      │ 📊 Title     │       │ ⚠️ Status    │
│              │      │              │       │              │
│ 142          │      │ [Chart]      │       │ [Content]    │
│ Label        │      │              │       │              │
│ +12 ↑        │      │ Description  │       │ [Actions]    │
└──────────────┘      └──────────────┘       └──────────────┘
```

### Badges
```
Low Damage            Medium Damage          Severe Damage
┌──────────┐         ┌──────────┐           ┌──────────┐
│   Low    │         │  Medium  │           │  Severe  │
└──────────┘         └──────────┘           └──────────┘
#10B981 (Green)      #F59E0B (Amber)        #EF4444 (Red)
```

## 🔄 User Flow

```
Start
  │
  ├─→ Dashboard Home
  │     │
  │     ├─→ View KPIs
  │     ├─→ Read "How It Works"
  │     └─→ Click "Start Analysis"
  │           │
  ├─→ Upload Page
  │     │
  │     ├─→ Select Image
  │     ├─→ View Preview
  │     ├─→ Check Metadata
  │     └─→ Click "Analyze"
  │           │
  │           ├─→ Processing (2s)
  │           └─→ Success ✅
  │                 │
  ├─→ Damage Assessment
  │     │
  │     ├─→ View Image
  │     ├─→ Check Classification
  │     ├─→ Review Statistics
  │     └─→ Download Report
  │
  ├─→ Urban Density
  │     │
  │     ├─→ View Overlay
  │     ├─→ Check Metrics
  │     └─→ Review Zones
  │
  ├─→ Analytics
  │     │
  │     ├─→ View Trends
  │     ├─→ Check History
  │     └─→ Analyze Patterns
  │
  ├─→ Settings
  │     │
  │     ├─→ Adjust Parameters
  │     ├─→ Change Preferences
  │     └─→ Reset if Needed
  │
  └─→ About
        │
        ├─→ Read Objectives
        ├─→ View Tech Stack
        └─→ Meet Team
```

---

**Visual Guide Complete** ✅

This guide provides a visual representation of the dashboard's layout, components, and user flow. Use it as a reference for understanding the UI structure and navigation patterns.
