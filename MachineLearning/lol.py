import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 6))

# Define positions (Manually set for clarity)
# Processes on the Left, Resources on the Right
pos = {
    'P3': (0.2, 0.8),
    'P2': (0.2, 0.5),
    'P1': (0.2, 0.2),
    'R3': (0.8, 0.8),
    'R2': (0.8, 0.35), # Placed between P1 and P2
    'R1': (0.8, 0.6),  
    'R4': (0.8, 0.1)
}

# Drawing Functions
def draw_process(ax, xy, label):
    circle = patches.Circle(xy, 0.08, edgecolor='black', facecolor='#AEC6CF', zorder=2)
    ax.add_patch(circle)
    ax.text(xy[0], xy[1], label, ha='center', va='center', weight='bold', fontsize=12)

def draw_resource(ax, xy, label, instances=1):
    rect = patches.Rectangle((xy[0]-0.08, xy[1]-0.08), 0.16, 0.16, edgecolor='black', facecolor='#FFB347', zorder=2)
    ax.add_patch(rect)
    # Label outside
    ax.text(xy[0]+0.12, xy[1], label, ha='left', va='center', weight='bold', fontsize=12)
    
    # Draw instance dots
    if instances == 1:
        ax.add_patch(patches.Circle(xy, 0.015, color='black', zorder=3))
    elif instances == 2:
        ax.add_patch(patches.Circle((xy[0]-0.03, xy[1]), 0.015, color='black', zorder=3))
        ax.add_patch(patches.Circle((xy[0]+0.03, xy[1]), 0.015, color='black', zorder=3))

# Draw Edges
def draw_arrow(ax, start, end, style='->'):
    # Calculate offsets to touch boundaries not centers
    # Simple direct line for now
    ax.annotate("",
                xy=end, xycoords='data',
                xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black', shrinkA=15, shrinkB=15),
                zorder=1)

# --- Draw Nodes ---
# Processes
for p in ['P1', 'P2', 'P3']:
    draw_process(ax, pos[p], p)

# Resources (R2 has 2 instances based on edges, R4 is free)
draw_resource(ax, pos['R3'], 'R3', instances=1)
draw_resource(ax, pos['R1'], 'R1', instances=1)
draw_resource(ax, pos['R2'], 'R2', instances=2)
draw_resource(ax, pos['R4'], 'R4', instances=1)

# --- Draw Edges from Set E ---
# Request Edges (P -> R)
draw_arrow(ax, pos['P1'], pos['R1'])
draw_arrow(ax, pos['P2'], pos['R3'])

# Allocation Edges (R -> P)
draw_arrow(ax, pos['R1'], pos['P2'])
draw_arrow(ax, pos['R3'], pos['P3'])
# R2 has two allocations
draw_arrow(ax, pos['R2'], pos['P2'])
draw_arrow(ax, pos['R2'], pos['P1'])

# Settings
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("Resource Allocation Graph", fontsize=16)

plt.show()