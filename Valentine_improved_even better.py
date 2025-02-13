import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import matplotlib.patheffects as path_effects
from matplotlib.colors import LinearSegmentedColormap

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor('#FFF0F5')

# Gradient background
gradient = LinearSegmentedColormap.from_list("gradient", ['#FFF0F5', '#FFD1DC'])
x_bg, y_bg = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
ax.imshow(y_bg, extent=[-20, 20, -20, 30], origin='lower', cmap=gradient, alpha=0.8)

# Main heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Sparkles: Create random points for sparkle effects
num_sparkles = 50
sparkle_x = np.random.uniform(-18, 18, num_sparkles)
sparkle_y = np.random.uniform(-18, 25, num_sparkles)
sparkle_sizes = np.random.uniform(10, 40, num_sparkles)
sparkle_alphas = np.random.uniform(0.3, 0.8, num_sparkles)

# Rose petals: Randomly generate positions and rotations
num_petals = 30
petal_x = np.random.uniform(-20, 20, num_petals)
petal_y = np.random.uniform(-10, 30, num_petals)
petal_rotations = np.random.uniform(0, 360, num_petals)

# Function to draw rose petals
def draw_rose_petals():
    for i in range(num_petals):
        petal = Ellipse((petal_x[i], petal_y[i]), width=2, height=1, angle=petal_rotations[i],
                        color='#FF69B4', alpha=0.8)
        ax.add_patch(petal)

# Function to create small hearts
def small_heart(cx, cy, size=1):
    t = np.linspace(0, 2 * np.pi, 100)
    x = size * (16 * np.sin(t)**3) + cx
    y = size * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) + cy
    return x, y

# Decorative small hearts
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

# Add title
title = ax.text(0, 27, "Happy Valentine's Day",
                fontsize=28,
                fontweight='bold',
                color='#FF1493',
                ha='center',
                family='cursive')
title.set_path_effects([
    path_effects.withStroke(linewidth=4, foreground='white'),
    path_effects.Normal()
])

# Add a romantic message
message = ax.text(0, -25, "You are the rhythm to my heart, the melody to my soul.\nForever yours, my Valentine",
                  fontsize=16,
                  color='#8B0000',
                  ha='center',
                  family='serif')

# Animation function
def update(frame):
    ax.clear()

    # Redraw gradient background
    ax.imshow(y_bg, extent=[-20, 20, -20, 30], origin='lower', cmap=gradient, alpha=0.8)

    # Heart pulsating effect
    scale = 1 + 0.02 * np.sin(frame * 0.2)
    x_scaled, y_scaled = x * scale, y * scale
    ax.fill(x_scaled, y_scaled, facecolor='#FF69B4', alpha=0.6, zorder=1)
    ax.plot(x_scaled, y_scaled, color='red', linewidth=2)

    # Sparkles twinkling effect
    for i in range(num_sparkles):
        ax.scatter(sparkle_x[i], sparkle_y[i], s=sparkle_sizes[i],
                   color='white', alpha=np.abs(np.sin(frame * 0.2 + i)), zorder=2)

    # Draw rose petals falling
    global petal_y
    petal_y -= 0.2  # Simulate falling
    petal_y = np.where(petal_y < -20, 30, petal_y)  # Reset petals if they fall out of view
    draw_rose_petals()

    # Redraw small hearts
    for pos in small_heart_positions:
        x_small, y_small = small_heart(pos[0], pos[1], size=np.random.uniform(0.2, 0.4))
        ax.fill(x_small, y_small, color='#FF1493', alpha=np.random.uniform(0.3, 0.6))
        ax.plot(x_small, y_small, color='#FF1493', linewidth=1, alpha=0.5)

    # Redraw initials
    ax.text(0, 0, "M.M", fontsize=36, fontweight='bold', color='#8B0000',
            ha='center', va='center', family='cursive')

    # Redraw title and message
    ax.text(0, 27, "Happy Valentine's Day",
            fontsize=28, fontweight='bold', color='#FF1493', ha='center', family='cursive')
    ax.text(0, -25, "You are the rhythm to my heart, the melody to my soul.\nForever yours, my Valentine",
            fontsize=16, color='#8B0000', ha='center', family='serif')

    # Remove axes for a clean look
    ax.axis('equal')
    ax.axis('off')

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Show plot
plt.show()
