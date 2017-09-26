import imageio
from PIL import Image, ImageDraw, ImageFont

from cube_constants import (SIDES, ORIGINAL_IMAGE, GRAFFITIED_IMAGE,
							SIDES_ON_A_CUBE, SQUARES_IN_A_ROW,
							SQUARES_IN_A_COLUMN)

def draw(mycube):
	"""Paints over the original cube image with a cube configuration."""
	with open(ORIGINAL_IMAGE, 'rb') as base_handle:
		base = Image.open(base_handle).convert('RGBA')
		overlay = Image.new('RGBA', base.size, (255,255,255,0))
		d = ImageDraw.Draw(overlay)
		for i in range (0, SIDES_ON_A_CUBE):
			if (len(polygons[i]) == 0):
				continue
			for j in range (0, SQUARES_IN_A_ROW):
				for k in range (0, SQUARES_IN_A_COLUMN):
					colour = mycube.get_face(SIDES[i])[j][k].colour
					d.polygon(polygons[i][j][k], colour, None)
		out = Image.alpha_composite(base, overlay)
		out.save(GRAFFITIED_IMAGE)

polygons = [
			[ # Left
				[
					[(14, 40), (13, 101), (38, 113), (40, 49)],
					[(44, 51), (43, 118), (70, 130), (74, 61)],
					[(76, 66), (75, 134), (105, 147), (106, 76)]
				],
				[
					[(11, 120), (10, 186), (35, 199), (38, 129)],
					[(43, 134), (41, 200), (70, 214), (72, 144)],
					[(78, 147), (77, 220), (106, 232), (108, 161)]
				],
				[
					[(10, 203), (10, 264), (34, 279), (38, 213)],
					[(41, 218), (40, 280), (70, 297), (72, 231)],
					[(76, 237), (76, 302), (106, 317), (107, 250)]
				]
			],

			[ # Upper
				[
					[(27, 27), (48, 36), (111, 32), (84, 20)],
					[(100, 22), (124, 32), (187, 26), (164, 18)],
					[(175, 17), (202, 27), (262, 25), (234, 14)]
				],
				[
					[(55, 38), (83, 48), (144, 45), (120, 33)],
					[(135, 33), (161, 43), (224, 40), (199, 28)],
					[(210, 28), (240, 41), (298, 37), (266, 25)]
				],
				[
					[(86, 51), (114, 62), (182, 59), (153, 47)],
					[(166, 46), (194, 59), (260, 53), (232, 42)],
					[(247, 42), (275, 53), (337, 49), (306, 37)]
				]
			],

			[ # Front
				[
					[(119, 77), (118, 145), (183, 144), (188, 72)],
					[(199, 71), (199, 139), (264, 138), (268, 67)],
					[(279, 65), (280, 130), (341, 128), (342, 60)]
				],
				[
					[(119, 162), (118, 235), (184, 233), (186, 159)],
					[(198, 156), (199, 226), (264, 225), (266, 152)],
					[(277, 146), (278, 217), (339, 214), (341, 145)]
				],
				[
					[(120, 252), (121, 318), (184, 314), (184, 246)],
					[(198, 244), (198, 311), (262, 305), (263, 240)],
					[(276, 234), (277, 298), (337, 294), (339, 228)]
				]
			],
			[], # Down
			[], # Right
			[], # Back
		 ]
