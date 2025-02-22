# colorgram library
import colorgram

colors= colorgram.extract("image.png")

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r,g,b,)
    rgb_colors.append(new_colors)

print(rgb_colors)