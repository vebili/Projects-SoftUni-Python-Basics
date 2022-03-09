import math

paint_boxes = float(input())
wallpaper_rolls = float(input())
pair_of_gloves = float(input())
brushes = float(input())
paint = 21.50 * paint_boxes
wallpaper_rolls_price = 5.20 * wallpaper_rolls
gloves = math.ceil(wallpaper_rolls * 35 / 100)
gloves_price = gloves * pair_of_gloves
brush = math.floor(paint_boxes * 48 / 100)
brush_price = brush * brushes

last_price = (paint + wallpaper_rolls_price + gloves_price + brush_price) * 1 / 15

print(f"This delivery will cost {last_price:.2f} lv.")
