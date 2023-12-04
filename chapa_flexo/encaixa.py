from rectpack import newPacker
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def optimal_rectangle_packing(rectangles):
    packer = newPacker()

    for i, rect in enumerate(rectangles):
        packer.add_rect(*rect, rid=i)

    packer.add_bin(1000, 1000)  # Replace with the dimensions of your bounding rectangle

    packer.pack()

    rectangles_placement = packer[0]
    print(rectangles_placement)

    return rectangles_placement

def visualize_rectangles(rectangles, placement):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)  # Adjust according to your bounding rectangle dimensions
    ax.set_ylim(0, 1000)

    for rect in placement:
        current_rect = rectangles[rect.rid]
        rect_patch = patches.Rectangle((rect.x, rect.y), rect.width, rect.height, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect_patch)
        ax.annotate(rect.rid, (rect.x + rect.width / 2, rect.y + rect.height / 2), color='b', weight='bold', fontsize=8, ha='center', va='center')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example rectangles (width, height)
rectangles = [
    (200, 100),
    (150, 150),
    (100, 200),
    (300, 100),
]

result = optimal_rectangle_packing(rectangles)

# Print the result
for rect in result:
    print(f"Rectangle {rect.rid} placed at ({rect.x}, {rect.y}) with dimensions ({rect.width}, {rect.height})")

# Visualize the rectangles
visualize_rectangles(rectangles, result)
