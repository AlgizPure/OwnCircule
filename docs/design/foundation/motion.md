# Motion System

## Overview

The motion system defines how elements transition, animate, and respond to user interactions. Our approach emphasizes purposeful, elegant motion that feels premium without being distracting. Motion serves functional purposes: providing feedback, guiding attention, and enhancing the sense of interaction.

Built on timing values calibrated for both micro-interactions (200ms) and complex animations (500ms), our motion system creates a cohesive, responsive experience across iOS and Android platforms.

## Specifications

### Timing Values

We define three primary timing values for different interaction types:

| Timing | Duration | Use Case |
|--------|----------|----------|
| Micro | 200ms | Button taps, small state changes, opacity shifts |
| Standard | 300ms | Screen transitions, card reveals, form submissions |
| Complex | 500ms | Full-screen transitions, multi-step animations, onboarding |

### Easing Functions

Our easing functions are carefully chosen for a premium feel:

#### Ease In Out (Default)
```
cubic-bezier(0.4, 0, 0.2, 1)
```
- **Usage**: Most animations, transitions, general UI
- **Feel**: Smooth acceleration and deceleration
- **Premium characteristic**: Natural, unhurried motion

#### Ease Out (Responsive)
```
cubic-bezier(0.0, 0, 0.2, 1)
```
- **Usage**: Entrances, reveals, focus feedback
- **Feel**: Quick start, smooth deceleration
- **Premium characteristic**: Responsive, eager energy

#### Ease In (Exit)
```
cubic-bezier(0.4, 0, 1, 1)
```
- **Usage**: Dismissals, exits, content leaving
- **Feel**: Slow start, quick exit
- **Premium characteristic**: Polished departure

#### Linear (Transformation)
```
linear (0, 0, 1, 1)
```
- **Usage**: Rotations, color transitions, progress bars
- **Feel**: Constant velocity
- **Premium characteristic**: Mechanical precision where appropriate

### Easing Curve Specifications

```css
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-linear: linear;
```

## Usage Guidelines

### Micro Timing (200ms)

Use for quick, responsive interactions that provide immediate feedback.

**Components**:
- Button tap feedback
- Toggle switches
- Checkbox state change
- Simple opacity transitions
- Icon state changes
- Loading spinners (pulse)

**Example**:
```typescript
duration: 200,
easing: 'ease-in-out',
property: 'opacity, backgroundColor'
```

### Standard Timing (300ms)

Use for standard transitions between states and navigation.

**Components**:
- Screen transitions
- Modal open/close
- Card reveals
- Form field focus
- Drawer/sidebar open/close
- List item animations
- Expansion/collapse

**Example**:
```typescript
duration: 300,
easing: 'ease-in-out',
property: 'transform, opacity'
```

### Complex Timing (500ms)

Use for complex, multi-step animations and significant transitions.

**Components**:
- Full-screen transitions
- Multi-element choreography
- Onboarding sequences
- Loading states with progression
- Page transitions
- Animation sequences

**Example**:
```typescript
duration: 500,
easing: 'ease-in-out',
property: 'all'
```

## Design Tokens & Code Examples

### CSS Variables

```css
/* Timing */
--duration-micro: 200ms;
--duration-standard: 300ms;
--duration-complex: 500ms;

/* Easing */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-linear: linear;

/* Combined */
--transition-micro: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-standard: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-complex: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
```

### React Native Implementation

```typescript
// tokens/motion.ts
export const motion = {
  duration: {
    micro: 200,
    standard: 300,
    complex: 500,
  },
  
  easing: {
    inOut: [0.4, 0, 0.2, 1],
    out: [0, 0, 0.2, 1],
    in: [0.4, 0, 1, 1],
    linear: [0, 0, 1, 1],
  },
} as const;

export type MotionTiming = keyof typeof motion.duration;
export type MotionEasing = keyof typeof motion.easing;

// Helper to get easing string
export const getEasing = (easing: MotionEasing): Animated.EasingFunction => {
  const easingValues = motion.easing[easing];
  return Animated.bezier(easingValues[0], easingValues[1], easingValues[2], easingValues[3]);
};
```

### Button Tap Animation

```typescript
import { Animated, TouchableOpacity } from 'react-native';
import { motion } from './tokens/motion';

const animatedScale = useRef(new Animated.Value(1)).current;

const onPressIn = () => {
  Animated.timing(animatedScale, {
    toValue: 0.98,
    duration: motion.duration.micro,
    easing: Animated.bezier(...motion.easing.inOut),
    useNativeDriver: true,
  }).start();
};

const onPressOut = () => {
  Animated.timing(animatedScale, {
    toValue: 1,
    duration: motion.duration.micro,
    easing: Animated.bezier(...motion.easing.out),
    useNativeDriver: true,
  }).start();
};

return (
  <Animated.View style={[{ transform: [{ scale: animatedScale }] }]}>
    <TouchableOpacity onPressIn={onPressIn} onPressOut={onPressOut}>
      {/* Button content */}
    </TouchableOpacity>
  </Animated.View>
);
```

### Modal Appearance Animation

```typescript
import { Animated, Modal } from 'react-native';
import { motion } from './tokens/motion';

const slideUpAnimation = useRef(new Animated.Value(0)).current;

useEffect(() => {
  if (visible) {
    Animated.timing(slideUpAnimation, {
      toValue: 1,
      duration: motion.duration.standard,
      easing: Animated.bezier(...motion.easing.out),
      useNativeDriver: true,
    }).start();
  }
}, [visible]);

const translateY = slideUpAnimation.interpolate({
  inputRange: [0, 1],
  outputRange: [500, 0],
});

return (
  <Animated.View style={{ transform: [{ translateY }] }}>
    {/* Modal content */}
  </Animated.View>
);
```

### Fade In/Out Transition

```typescript
import { Animated } from 'react-native';
import { motion } from './tokens/motion';

const fadeAnim = useRef(new Animated.Value(0)).current;

const fadeIn = () => {
  Animated.timing(fadeAnim, {
    toValue: 1,
    duration: motion.duration.micro,
    easing: Animated.bezier(...motion.easing.out),
    useNativeDriver: true,
  }).start();
};

const fadeOut = () => {
  Animated.timing(fadeAnim, {
    toValue: 0,
    duration: motion.duration.micro,
    easing: Animated.bezier(...motion.easing.in),
    useNativeDriver: true,
  }).start();
};

return (
  <Animated.View style={{ opacity: fadeAnim }}>
    {/* Content */}
  </Animated.View>
);
```

### Sequential Animation (Complex)

```typescript
import { Animated, View } from 'react-native';
import { motion } from './tokens/motion';

const animations = [
  new Animated.Value(0),
  new Animated.Value(0),
  new Animated.Value(0),
];

const startSequence = () => {
  Animated.sequence([
    Animated.timing(animations[0], {
      toValue: 1,
      duration: motion.duration.standard,
      easing: Animated.bezier(...motion.easing.out),
      useNativeDriver: true,
    }),
    Animated.timing(animations[1], {
      toValue: 1,
      duration: motion.duration.standard,
      easing: Animated.bezier(...motion.easing.out),
      useNativeDriver: true,
    }),
    Animated.timing(animations[2], {
      toValue: 1,
      duration: motion.duration.standard,
      easing: Animated.bezier(...motion.easing.out),
      useNativeDriver: true,
    }),
  ]).start();
};

return (
  <View>
    {animations.map((anim, idx) => (
      <Animated.View key={idx} style={{ opacity: anim }}>
        {/* Item */}
      </Animated.View>
    ))}
  </View>
);
```

## Animation Patterns

### Micro-Interaction: Button Press

```typescript
// 200ms, ease-in-out
// Scale: 1.0 → 0.98 → 1.0
// Opacity: (optional) 1.0 → 0.8 → 1.0
```

### Standard: Modal Entrance

```typescript
// 300ms, ease-out
// Transform: translateY(500px) → 0px
// Opacity: 0 → 1
// Scrim: Fade in simultaneously
```

### Standard: List Item Expansion

```typescript
// 300ms, ease-in-out
// Max Height: 0 → auto
// Opacity: 0.5 → 1
// Padding: 0 → 16px
```

### Complex: Screen Transition

```typescript
// 500ms, ease-in-out
// Outgoing: Scale 1.0 → 0.95, Opacity 1 → 0
// Incoming: Scale 1.05 → 1.0, Opacity 0 → 1
// Scrim: Fade in over 300ms
```

## Accessibility Considerations

### Prefers Reduced Motion

Users with `prefers-reduced-motion: reduce` should experience:
- Animations reduced to instant (0ms) or minimal (100ms)
- No easing - use linear transitions
- No sequential animations
- Maintain visual feedback without motion

**Implementation**:
```typescript
// tokens/motion.ts
export const getAnimationDuration = (preferredDuration: number): number => {
  // Check if user prefers reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return 0; // Instant transition
  }
  return preferredDuration;
};

// In component
const duration = getAnimationDuration(motion.duration.standard);
```

### Motion Sickness & Vestibular Disorders

- Avoid rapid, jerky motions
- Prevent parallax scrolling effects
- Use gentle easing curves
- Keep animation areas relatively small
- Avoid spinning or rotating elements excessively

### Focus & Keyboard Navigation

- Maintain motion consistency for keyboard-navigated items
- Ensure focus indicators animate similarly to mouse interactions
- Don't hide focus indicators during motion
- Keep animations brief enough not to delay user interaction

## Platform-Specific Considerations

### iOS

**UIView Animation**:
```swift
UIView.animate(
  withDuration: 0.3,
  delay: 0,
  options: .curveEaseInOut,
  animations: {
    // Animate properties
  }
)
```

**CABasicAnimation**:
- More control over complex animations
- Better for sequential, concurrent animations
- Use for property animations (bounds, position, etc.)

### Android

**ValueAnimator**:
```kotlin
ObjectAnimator.ofFloat(view, "translationY", 0f, 500f).apply {
  duration = 300
  interpolator = FastOutSlowInInterpolator()
}.start()
```

**Available Interpolators**:
- `AccelerateInterpolator` → ease-in
- `DecelerateInterpolator` → ease-out
- `AccelerateDecelerateInterpolator` → ease-in-out
- `LinearInterpolator` → linear

## Performance Optimization

### GPU-Accelerated Properties

Only animate these properties for best performance:

- `transform` (translate, scale, rotate)
- `opacity`
- `position` (as last resort)

Avoid animating:
- `width`, `height`
- `top`, `left`, `right`, `bottom`
- `padding`, `margin`

### Native Driver Usage

```typescript
Animated.timing(animRef, {
  toValue: 100,
  duration: 300,
  useNativeDriver: true, // Always use when possible
}).start();
```

## Motion in Responsive Design

### Small Screens (Mobile)

- Keep animations brief (200ms standard)
- Reduce complex animation count
- Test on actual devices for performance
- Prioritize critical feedback animations

### Larger Screens (Tablet, Desktop)

- Can extend slightly (300-400ms)
- More room for complex choreography
- Maintain consistency with mobile animations
- Scale animations proportionally

## Common Patterns & Examples

### Loading State

```typescript
// Continuous rotation, micro timing
const rotateAnim = useRef(new Animated.Value(0)).current;

useEffect(() => {
  const animation = Animated.loop(
    Animated.timing(rotateAnim, {
      toValue: 1,
      duration: motion.duration.complex,
      easing: Animated.bezier(...motion.easing.linear),
      useNativeDriver: true,
    })
  );
  animation.start();
}, []);
```

### Swipe Gesture Response

```typescript
// Immediate 200ms response to gesture
const animatedX = useRef(new Animated.Value(0)).current;

const onSwipe = (gestureX: number) => {
  Animated.timing(animatedX, {
    toValue: gestureX,
    duration: motion.duration.micro,
    easing: Animated.bezier(...motion.easing.inOut),
    useNativeDriver: true,
  }).start();
};
```

### Card Flip Animation

```typescript
// Complex animation with rotation
const flipAnim = useRef(new Animated.Value(0)).current;

const flip = () => {
  Animated.timing(flipAnim, {
    toValue: 1,
    duration: motion.duration.standard,
    easing: Animated.bezier(...motion.easing.inOut),
    useNativeDriver: true,
  }).start();
};

const rotateInterpolate = flipAnim.interpolate({
  inputRange: [0, 1],
  outputRange: ['0deg', '180deg'],
});
```

## Testing Motion

### Visual Verification

- Record animations at 60fps
- Compare with design specifications
- Test on various devices and OS versions
- Verify timing matches specifications

### Performance Testing

- Monitor frame rate during animations
- Check for jank or dropped frames
- Measure CPU/GPU usage
- Profile with DevTools

### Accessibility Testing

- Test with `prefers-reduced-motion: reduce`
- Verify keyboard navigation animations
- Screen reader compatibility
- Touch gesture animations

## Related Documentation

- [Spacing System](./spacing.md) - Distance in animations
- [Elevation System](./elevation.md) - Depth changes with motion
- [Design Tokens](../00_DESIGN_SYSTEM.md) - Complete token system
- [Accessibility Guidelines](../accessibility/wcag.md) - Motion accessibility
- [Components](../components/README.md) - Component animations
