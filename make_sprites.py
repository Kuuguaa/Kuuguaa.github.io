# 生成像素蔬菜 sprite（SVG，硬边渲染）
# 用法：python make_sprites.py  → 输出到 ../images/
# 字符图例见各 sprite 的 PALETTE，每行一个字符串，一个字符=一个像素

import os

OUT = os.path.join(os.path.dirname(__file__), "..", "images")

GREEN_DARK = "#2d5016"   # 最深绿（描边）
GREEN = "#4e7a3a"        # 主体绿
GREEN_MID = "#5d8a4a"    # 苦瓜主体
GREEN_LIGHT = "#8bac0f"  # 亮绿
PALE = "#eef3c2"         # 果肉
SEED = "#e0cd7e"         # 籽
SEED_DARK = "#b39b4e"    # 籽阴影

SPRITES = {
    # 苦瓜切片（呼应头像照片）
    "sprite-bitter": {
        "palette": {"D": GREEN_DARK, "G": GREEN_MID, "g": GREEN_LIGHT, "P": PALE, "S": SEED, "s": SEED_DARK},
        "map": [
            "................",
            "......DDDD......",
            "....DDGGGGDD....",
            "...DGGgGGgGGD...",
            "..DGgGGGGGGGgD..",
            "..DGGPPPPPPPGGD.",
            ".DGgPPPPPPPPPgD.",
            ".DGPPsSSsPPPPGD.",
            "DGGPSPPPsPPPPGGD",
            "DGPPsPPPsPPsPGGD",
            "DGPPSPPsSPPPPGGD",
            ".DGPPPPSSPPPPGD.",
            ".DGgPPPPPPPPgGD.",
            "..DGGPPPPPPGGD..",
            "..DGgGGGGGGgD...",
            "...DGGgGGgGD....",
            "....DDGGGGDD....",
            "......DDDD......",
        ],
    },
    # 黄瓜（竖）
    "sprite-cucumber": {
        "palette": {"D": GREEN_DARK, "G": GREEN, "g": GREEN_LIGHT, "b": "#cfe08a"},
        "map": [
            "...DD...",
            "..DgGD..",
            "..DGGD..",
            ".DGbGGD.",
            ".DGGGgD.",
            ".DGgGGD.",
            ".DGGGbD.",
            ".DGgGGD.",
            ".DGGGgD.",
            ".DGbGGD.",
            ".DGGGgD.",
            ".DGgGGD.",
            ".DGGbGD.",
            ".DGgGGD.",
            "..DGGD..",
            "...DD...",
        ],
    },
    # 嫩芽
    "sprite-sprout": {
        "palette": {"D": GREEN_DARK, "G": GREEN, "g": GREEN_LIGHT},
        "map": [
            ".D....D.",
            "DgD..DgD",
            "DGgDDgGD",
            ".DGGGGD.",
            "..DGgD..",
            "...DD...",
            "...DD...",
            "..DDDD..",
        ],
    },
    # 小叶子（单）
    "sprite-leaf": {
        "palette": {"D": GREEN_DARK, "G": GREEN, "g": GREEN_LIGHT},
        "map": [
            "....DD..",
            "..DDgGD.",
            ".DGggGGD",
            "DGgGGGgD",
            "DGGGGGD.",
            ".DGGDD..",
            "..DD....",
        ],
    },
}


def to_svg(name, palette, rows):
    h = len(rows)
    w = max(len(r) for r in rows)
    rects = []
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in palette:
                rects.append(f'<rect x="{x}" y="{y}" width="1" height="1" fill="{palette[ch]}"/>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'shape-rendering="crispEdges">{"".join(rects)}</svg>'
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, spec in SPRITES.items():
        svg = to_svg(name, spec["palette"], spec["map"])
        path = os.path.join(OUT, name + ".svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("written:", path)


if __name__ == "__main__":
    main()
