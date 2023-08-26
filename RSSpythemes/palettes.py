from colour import Color
from matplotlib.colors import LinearSegmentedColormap, to_hex

# Significance red hex colour
signif_red = '#e41b12'

# Significance yellow hex colour
signif_yellow = '#f4c100'

# Significance blue hex colour
signif_blue = '#009cc4'

# Significance orange hex colour
signif_orange = '#f07d00'

# Significance green hex colour
signif_green = '#3fa535'

# Palette colours
RSS_PALETTES = dict(
    signif_seq=dict(colors=('#163B13', '#20551B', '#2A7024', '#348A2C', '#3FA535', '#5DB355', '#7CC175', '#9BD095', '#B9DEB6'), order=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
    signif_div=dict(colors=('#E41B12', '#EB5751', '#F29490', '#F9D1CF', '#FFFFFF', '#CCEBF3', '#88D0E3', '#43B6D3', '#009CC4'), order=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
    signif_qual=dict(colors=('#3fa535', '#f4c100', '#009cc4', '#f07d00'), order=(1, 2, 3, 4))
  )

# Palette function
def RSScols(name, n=None, palette_type="discrete"):

    palette = RSS_PALETTES.get(name)

    if not palette_type or type(name) in (int, float):
        raise Exception(f"Palette {name} does not exist.")

    if not n:
        n = len(palette["colors"])
        print(f"Palette '{name}' has '{n}' discrete colors")


    if palette_type not in {"discrete", "continuous"}:
        palette_type = "discrete"

    if palette_type == "discrete" and n > len(palette["colors"]):
        print(f"Number of requested colors ('{n}') greater than number of colors '{name}' can offer. \n Setting brew_type to 'continuous' instead.")
        palette_type = "continuous"

    out = list()
    if palette_type == "continuous":

        colors = [Color(c).rgb for c in palette["colors"]]
        color_map = LinearSegmentedColormap.from_list(name, colors, N=n)
        for i in range(n):
            out.append(to_hex(color_map(i)))

    elif palette_type == "discrete":

        rounds = n // len(palette["colors"])
        delta = n % len(palette["colors"])
        for _ in range(rounds):
            for i in range(len(palette["colors"])):
                idx = palette["order"][i] - 1
                color = palette["colors"][idx]
                out.append(color)

        for i in range(delta):
            idx = palette["order"][i] - 1
            color = palette["colors"][idx]
            out.append(color)

    return out
