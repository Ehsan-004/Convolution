import numpy as np
from Conv2D import Conv2D
from multiprocessing import Pool
import cv2

def main():
    img = cv2.imread("images/Frame 1.png")

    img = cv2.resize(img, (0, 0), fx=0.17,  fy=0.17, interpolation=cv2.INTER_AREA)


    b_channel, g_channel, r_channel = cv2.split(img)


    print(f"blue channel: {b_channel.shape}") # (480, 640)
    print(f"green channel: {g_channel.shape}") # (480, 640)
    print(f"red channel: {r_channel.shape}") # (480, 640)

    lists = [a.tolist() for a in [b_channel, g_channel, r_channel]]

    BlurKernel = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]


    args = [(l, BlurKernel, 2, 1) for l in lists]  # padding=1

    # Conv2D(data, kernel, stride, padding, fill)

    print("starting to process")
    
    with Pool(4) as p:
        a = p.starmap(Conv2D, args)
        
    for idx, channel_name in enumerate(["Blue", "Green", "Red"]):
        print(f"\n--- {channel_name} channel raw conv2d output ---")
        arr = np.array(a[idx][1])
        print("min:", np.min(arr))
        print("max:", np.max(arr))
        print("mean:", np.mean(arr))
        print("Sample top-left corner (5x5):")
        print(arr[:5, :5])
            

    print("processing finished")
    
    # _b_channel, _g_channel, _r_channel = [np.clip(np.array(x[1]), 0, 255).astype(np.uint8) for x in a]
    result = []
    epsilon = 1e-5  # عدد کوچیک برای جلوگیری از تقسیم بر صفر
    for x in a:
        arr = np.array(x[1], dtype=np.float32)
        min_val, max_val = arr.min(), arr.max()
        
        if abs(max_val - min_val) < epsilon:
            norm = np.zeros_like(arr, dtype=np.uint8)  # تصویر خاکستری کامل (مثلاً بدون تغییر)
        else:
            norm = ((arr - min_val) / (max_val - min_val) * 255).astype(np.uint8)

        result.append(norm)

    # Resize to match original image size
    for i in range(3):
        result[i] = cv2.resize(result[i], (img.shape[1], img.shape[0]), interpolation=cv2.INTER_LINEAR)


    _b_channel, _g_channel, _r_channel = result


    merged_image = cv2.merge([_b_channel, _g_channel, _r_channel])

    
    cv2.imshow('Original Image', img)
    cv2.imshow('Processed Image', merged_image)

    cv2.waitKey(0) # منتظر می‌ماند تا کلیدی فشرده شود
    cv2.destroyAllWindows() 
    
if __name__ == "__main__":
    # img = np.zeros((50, 50), dtype=np.uint8)
    # img[20:30, 20:30] = 255  # یه مربع سفید وسط تصویر

    # cv2.imwrite("test.jpg", img)

    main()
