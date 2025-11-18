# Svoy Krug Mobile App

Премиальная система лояльности для женщин 30-50 лет. Мобильное приложение на React Native.

## 📱 Tech Stack

- **React Native:** 0.81.0
- **TypeScript:** 5.7.2
- **Navigation:** React Navigation 6
- **State Management:** Redux Toolkit 2.10.1
- **UI:** Tiffany Blue (#0ABAB5) design system

## 🚀 Quick Start

### Prerequisites

- Node.js >= 18.0.0
- npm or yarn
- Xcode (for iOS)
- Android Studio (for Android)

### Installation

```bash
# Install dependencies
npm install

# Install iOS pods (macOS only)
cd ios && pod install && cd ..
```

### Running the App

```bash
# Start Metro bundler
npm start

# Run on iOS simulator
npm run ios

# Run on Android emulator
npm run android
```

## 📂 Project Structure

```
mobile/
├── src/
│   ├── screens/          # Screen components
│   │   ├── WelcomeScreen.tsx
│   │   ├── LoginScreen.tsx
│   │   └── HomeScreen.tsx
│   ├── navigation/       # React Navigation setup
│   │   ├── RootNavigator.tsx
│   │   ├── AuthNavigator.tsx
│   │   └── MainNavigator.tsx
│   ├── store/           # Redux store
│   │   ├── index.ts
│   │   └── slices/
│   │       ├── authSlice.ts
│   │       └── userSlice.ts
│   ├── theme/           # Design tokens
│   │   ├── colors.ts
│   │   ├── typography.ts
│   │   ├── spacing.ts
│   │   ├── borderRadius.ts
│   │   └── shadows.ts
│   ├── components/      # Reusable components (Sprint 2)
│   ├── services/        # API services (Sprint 2)
│   └── utils/           # Utility functions
├── App.tsx             # Root component
├── index.js            # Entry point
└── package.json
```

## 🎨 Design System

Design tokens imported from `docs/design/resources/design-tokens.json`:

### Colors
- **Primary:** Tiffany Blue (#0ABAB5)
- **Secondary:** Champagne Beige (#F5F1E8)
- **Accent:** Champagne Gold (#D4AF37)

### Typography
- **iOS:** SF Pro Display / SF Pro Text
- **Android:** Roboto

### Spacing
8px base grid system (xs: 4px, sm: 8px, md: 16px, lg: 24px, xl: 32px)

## 📋 Sprint 1 Features

### Implemented ✅
- React Native project structure
- TypeScript configuration
- Design system (colors, typography, spacing, shadows)
- Redux store (auth, user slices)
- React Navigation (stack + bottom tabs)
- Screens:
  - Welcome Screen (app introduction with Tiffany Blue branding)
  - Login Screen (phone input for SMS OTP)
  - Home Screen (dashboard placeholder)

### Not Implemented (Deferred to Sprint 2)
- Backend integration (API calls)
- SMS OTP verification flow
- QR code scanner
- Bonus system UI
- Events listing
- Partner businesses map

## 🧪 Testing

```bash
# Run tests
npm test

# Run linter
npm run lint

# Run formatter
npm run format
```

## 📝 Sprint 1 Notes

This is the **mobile app shell** for Sprint 1. The app demonstrates:

1. ✅ **Navigation:** Welcome → Login → Home (simulated auth)
2. ✅ **Design System:** Tiffany Blue theme applied
3. ✅ **State Management:** Redux store configured
4. ⏳ **Backend Integration:** Deferred to Sprint 2

### Known Limitations
- No actual backend API calls
- Login screen is UI-only (no SMS sending)
- Home screen shows placeholder data
- Only 1 tab active (Home), other tabs deferred to Sprint 2

## 🔧 Configuration

### Environment Variables

Create `.env` file (if needed for Sprint 2):

```env
API_URL=http://localhost:8000/api/v1
```

### Platform-Specific Notes

#### iOS
- Minimum iOS version: 13.0
- CocoaPods required
- Run `pod install` in `/ios` directory

#### Android
- Minimum Android SDK: 21 (Android 5.0)
- Gradle build system
- Enable Developer Mode on device/emulator

## 📚 Documentation References

- **Module Spec:** `docs/requirements/module-01-mobile-app.md`
- **Design System:** `docs/design/foundation/`
- **Sprint Progress:** `docs/progress/sprint_current.md`

## 🚀 Next Steps (Sprint 2)

1. Integrate with backend API (`/auth/send-otp`, `/auth/login`)
2. Implement SMS OTP verification flow
3. Add remaining screens (Events, Bonuses, Profile)
4. Implement QR code scanner
5. Add offline support (MMKV storage)
6. Performance optimization (React.memo, useCallback)

## 👥 Team

- **Mobile Team:** Sprint 1 (Shell implementation)
- **Backend Team:** Auth API ready for integration
- **Design:** Tiffany Blue system complete

---

**Version:** 1.0.0 (Sprint 1)
**Last Updated:** 2025-11-17
