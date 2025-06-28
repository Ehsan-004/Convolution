identity = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

edge_detection = [
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0],
]

sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
]

box_blur = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
]

gaussian_blur = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16],
]

emboss = [
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2],
]

sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
]

sobel_y = [
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1],
]

outline = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
]

motion_blur = [
    [1/9, 0, 0],
    [0, 1/9, 0],
    [0, 0, 1/9],
]

kernels = {
    "identity": identity,
    "edge": edge_detection,
    "sharpen": sharpen,
    "box_blur": box_blur,
    "gaussian_blur": gaussian_blur,
    "emboss": emboss,
    "sobel_x": sobel_x,
    "sobel_y": sobel_y,
    "outline": outline,
    "motion_blur": motion_blur,
}
