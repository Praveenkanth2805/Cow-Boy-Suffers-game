# 🐎 Cowboy Suffer – Technical Specification
3D Endless Runner Game (Subway Style)

---

## 1. Project Overview

**Game Name:** Cowboy Suffer  
**Engine:** Panda3D  
**Language:** Python 3.11+  
**Initial Platform:** Windows PC  
**Future Platform:** Android  

### Game Type
3D Endless Runner (Lane-Based System)

### Theme
Stylized Wild West World:
- Desert
- Cowboy Town
- Canyon

---

## 2. Core Gameplay Systems

### 2.1 Movement System

- 3 Lane System (-1, 0, +1)
- Smooth lane transition interpolation
- Gravity-based jump system
- Slide mechanic

### Controls (Keyboard Only)

- Left Arrow → Move Left
- Right Arrow → Move Right
- Up Arrow → Jump
- Down Arrow → Slide

---

## 3. Camera System

Advanced Dynamic Camera:

- Fixed follow distance
- Lane change tilt
- Speed boost zoom
- Collision shake
- Adaptive FOV based on speed

---

## 4. Game Modes

### 4.1 Endless Mode

- Infinite procedural generation
- Score based on:
  - Distance
  - Coins collected

### 4.2 Level Mode

- Predefined difficulty stages
- Increasing obstacle density
- Environment variation per level

---

## 5. Player System

### Character

- Stylized cartoon cowboy
- Modular skin system
- Unlockable outfits

### Lives & Collision

- 2 Lives
- Shield ignores one hit
- No shield + 0 lives = Game Over

---

## 6. Obstacles

Types:

- Cow Vehicles
- Horse Carts
- Rolling Hay Bundles
- Cactus

Spawn System:

- Lane-based spawning
- Procedural timing
- Difficulty-scaled spawn rate

---

## 7. Power-Up System

| Power-Up     | Effect                         | Duration |
|--------------|--------------------------------|----------|
| Speed Boost  | Increase running speed         | 5 sec    |
| Shield       | Ignore one collision           | Until hit|
| Coin Magnet  | Auto collect nearby coins      | 7 sec    |
| Horse Mode   | Temporary faster ride mode     | 6 sec    |

---

## 8. Environment System

Dynamic Environment Switching:

- Desert
- Town
- Canyon

### Weather Effects

- Clear
- Sandstorm (Reduced visibility)
- Rain (Town only)
- Dynamic weather transitions

---

## 9. Economy System

### Coins

- Collected during run
- Stored locally

### Shop

- Character skins
- Horse skins
- Cosmetic upgrades

---

## 10. UI System

### Main Menu

- Play
- Endless Mode
- Level Select
- Shop
- Character Select
- Settings
- High Scores
- Credits
- Exit

### In-Game UI

- Score
- Coins
- Lives
- Active Power-ups indicator

---

## 11. Save System

### Type
Local lightweight storage

### Format
JSON File

### Path
save/game_data.json

### Stored Data

- High Score
- Total Coins
- Unlocked Skins
- Settings
- Level Progress

Target Save Size: < 50KB

---

## 12. Folder Structure

cowboy_suffer/

- main.py
- config.py
- models/
- textures/
- sounds/
- ui/
- systems/
    - player.py
    - lane_system.py
    - obstacle_manager.py
    - powerups.py
    - camera_controller.py
    - weather_system.py
    - save_system.py
- save/
    - game_data.json

---

## 13. Performance Optimization

- Object pooling for obstacles
- Level of Detail (LOD)
- Compressed textures
- Limited particle systems
- Efficient collision detection
- Target 60 FPS (Mid-range PC)

---

## 14. Future Expansion

- Online leaderboard
- Multiplayer race mode
- Daily challenges
- Boss levels
- Android monetization support

---

# Final Status

✔ Complete Game Design  
✔ Modular Architecture  
✔ Scalable for Android  
✔ Performance Optimized  
✔ Expansion Ready