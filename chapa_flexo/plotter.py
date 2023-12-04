import matplotlib.pyplot as plt
from matplotlib import patches
from rectpack import newPacker
from icecream import ic


WIDTH, HEIGHT = 914, 500


def impose_printouts(printouts: dict):
    packer = newPacker()

    for p in printouts.keys():
        packer.add_rect(*printouts[p], rid=p)

    packer.add_bin(WIDTH, HEIGHT)
    packer.pack() # type: ignore

    return packer[0]


def visualize_imposition(printouts, imposicao):
    fig, ax = plt.subplots()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    for rect in imposicao:
        current_rect = printouts[rect.rid]
        rect_patch = patches.Rectangle(
            (rect.x, rect.y),
            rect.width,
            rect.height,
            linewidth=1,
            edgecolor="r",
            facecolor="none",
        )
        ax.add_patch(rect_patch)
        ax.annotate(
            rect.rid,
            (rect.x + rect.width / 2, rect.y + rect.height / 2),
            color="b",
            weight="bold",
            fontsize=8,
            ha="center",
            va="center",
        )

    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


printes = [
    (210, 297),
    (210, 297),
    (297, 420),
    (297, 420),
    (210, 297),
    (210, 297),
    (400, 200),
    (350, 300),
    (500, 300),
    (210, 297),
]

printes = dict(enumerate(printes))


while printes:
    resultado = impose_printouts(printes)

    visualize_imposition(printes, resultado)

    for rect in resultado:
        print(
            f"Rectangle {rect.rid} placed at "\
            f"({rect.x}, {rect.y}) "\
            f"with dimensions ({rect.width}, {rect.height})"
        )
        printes.pop(rect.rid)
