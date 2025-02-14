import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects

# Create figure with a gradient background
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor('#FFF0F5')

# Gradient background
gradient = LinearSegmentedColormap.from_list("gradient", ['#FFF0F5', '#FFD1DC'])
x_bg, y_bg = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
ax.imshow(y_bg, extent=[-20, 20, -20, 30], origin='lower', cmap=gradient, alpha=0.8)

# Create the main heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Gradient fill for the heart
for i in range(5):
    plt.fill(x, y, facecolor='#FF69B4', alpha=0.6 - i * 0.1, zorder=-i)

# Glow effect around the heart
for width in [10, 8, 6]:
    plt.plot(x, y, color='pink', linewidth=width, alpha=0.2)

# Final heart outline
plt.plot(x, y, color='red', linewidth=2)

# Function to create small hearts
def small_heart(cx, cy, size=1):
    t = np.linspace(0, 2 * np.pi, 100)
    x = size * (16 * np.sin(t)**3) + cx
    y = size * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) + cy
    return x, y

# Add decorative small hearts
small_heart_positions = [
    (-15, -15), (15, -15), (0, 20), (-18, 5), (18, 5), (-12, 12), (12, 12)
]
for pos in small_heart_positions:
    x_small, y_small = small_heart(pos[0], pos[1], size=np.random.uniform(0.2, 0.4))
    plt.fill(x_small, y_small, color='#FF1493', alpha=np.random.uniform(0.3, 0.6))
    plt.plot(x_small, y_small, color='#FF1493', linewidth=1, alpha=0.5)

# Add initials inside the heart
ax.text(0, 0, "M.M", fontsize=36, fontweight='bold', color='#8B0000',
        ha='center', va='center', family='cursive')

# Add title with a romantic message and shadow effect
title = ax.text(0, 27, "Happy Valentine's Day ❤️", 
                fontsize=28, 
                fontweight='bold',
                color='#FF1493',
                ha='center',
                family='cursive')

title.set_path_effects([
    path_effects.withStroke(linewidth=4, foreground='white'),
    path_effects.Normal()
])

# Add a short poem or message
message = ax.text(0, -25, "You are the rhythm to my heart, the melody to my soul.\nForever yours, my Valentine 💕",
                  fontsize=16, 
                  color='#8B0000', 
                  ha='center', 
                  family='cursive')

# Set equal aspect ratio and remove axes
plt.axis('equal')
plt.axis('off')

# Subtle border
ax.set_frame_on(True)
ax.patch.set_edgecolor('#FFB6C1')
ax.patch.set_linewidth(2)

# Adjust layout
plt.tight_layout()

plt.show()
