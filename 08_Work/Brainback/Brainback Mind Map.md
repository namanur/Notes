# Brainback System Mind Map

## 1. Core Engine (Accessibility Service)
- **Input:** UI AccessibilityEvents (YouTube, Instagram, Browsers)
- **Signal Logic:** View ID Match + Text Pattern Match + URL Fragment Check
- **Output:** System Global Action (BACK)
- **Persistence:** Increments Block Count (SharedPreferences)

## 2. Analytics Engine (Stats)
- **Source:** Android UsageStatsManager
- **Data:** Active Time (Daily), Total Phone Usage
- **Persistence:** Local Storage (SharedPreferences)

## 3. Policy & Enforcement Layer (New)
- **Mechanism:** "Anonymous Password Friction"
- **Trigger:** Manual Lock Activation (30 Min)
- **State:** Locked Until Timestamp
- **Constraint:** Settings access requires manually typing a 16-char random string generated 30 mins prior.

## 4. Presentation Layer (UI)
- **Style:** "Stitch" Digital Clarity Theme (Dark Mode)
- **Components:**
    - Real-time Dashboard (Compose)
    - Dynamic Bar Graphs (Compose)
    - Privacy & Trust Manifest (New)
    - Lock/Unlock Screen (New)

## 5. Security & Privacy
- **Privacy:** 100% Local (Offline by Design)
- **Trust:** Human-readable permission explanation for Parents/Users
- **Data:** No external server, No data sales, No user tracking.
