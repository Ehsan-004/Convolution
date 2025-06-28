import numpy as np
from Conv2D import Conv2D
from multiprocessing import Pool
import cv2
from kernels import kernels


def Convolution2D(image_path, kernel, stride=1, padding=0, fill=0,
                  save=False, save_path="processed_image.png", show_images=True, resize_fx=0.5, resize_fy=0.5, print_log=True):
    
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"there is no image with path: {image_path}")

    img = cv2.resize(img, (0, 0), fx=resize_fx,  fy=resize_fy, interpolation=cv2.INTER_AREA)


    b_channel, g_channel, r_channel = cv2.split(img)

    if print_log:
        print(f"blue channel: {b_channel.shape}") # (480, 640)
        print(f"green channel: {g_channel.shape}") # (480, 640)
        print(f"red channel: {r_channel.shape}") # (480, 640)

    lists = [a.tolist() for a in [b_channel, g_channel, r_channel]]

    if not len(kernel):
        raise ValueError("kernel is empty!")

    args = [(l, kernel, stride, padding, fill) for l in lists]
    # Conv2D(data, kernel, stride, padding, fill)

    if print_log:
        print("starting to process")
    
    with Pool(4) as p:
        a = p.starmap(Conv2D, args)
    
    if print_log:
        for idx, channel_name in enumerate(["Blue", "Green", "Red"]):
            print(f"\n--- {channel_name} channel raw conv2d output ---")
            arr = np.array(a[idx])
            print(f"  min: {np.min(arr)}, max: {np.max(arr)}, mean: {np.mean(arr)}")
            
            print(f"  Sample 5x5: \n{arr[:5,:5]}")
            
        print("processing finished")
    
    # _b_channel, _g_channel, _r_channel = [np.clip(np.array(x[1]), 0, 255).astype(np.uint8) for x in a]
    result = []
    
    # A little help from chat GPT
    epsilon = 1e-5
    for x in a:
        arr = np.array(x, dtype=np.float32)
        min_val, max_val = arr.min(), arr.max()
        
        if abs(max_val - min_val) < epsilon:
            norm = np.zeros_like(arr, dtype=np.uint8) 
        else:
            norm = ((arr - min_val) / (max_val - min_val) * 255).astype(np.uint8)

        result.append(norm)

    # for i in range(3):
    #     result[i] = cv2.resize(result[i], (img.shape[1], img.shape[0]), interpolation=cv2.INTER_LINEAR)

    _b_channel, _g_channel, _r_channel = result


    merged_image = cv2.merge([_b_channel, _g_channel, _r_channel])

    if show_images:
        cv2.imshow('Original Image', img)
        cv2.imshow('Processed Image', merged_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows() 
    
    if save:
        cv2.imwrite(save_path, merged_image)

    
if __name__ == "__main__":

    Convolution2D(
        image_path="images/Frame 1.png",
        kernel=kernels["sharpen"],
        stride=1,
        padding=1,
        fill=0,
        save=False,
        save_path="images/output.png",
        show_images=True
    )
