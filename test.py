from main import Convolution2D, Pooling2D
from kernels import kernels


if __name__ == "__main__":
    
    # Convolution2D(
    #     image_path="images/test1.jpg",
    #     kernel=kernels["gaussian_blur"],
    #     stride=1,
    #     padding=1,
    #     fill=0,
    #     save=True,
    #     save_path="images/test1_output.jpg",
    #     show_images=False
    # )
    
    # Convolution2D(
    #     image_path="images/test2.jpg",
    #     kernel=kernels["emboss"],
    #     stride=1,
    #     padding=1,
    #     fill=0,
    #     save=True,
    #     save_path="images/test2_output.jpg",
    #     show_images=False
    # )
    
    Pooling2D(
        image_path="images/test2.jpg",
        kernel_size=(2, 2),
        method="max",
        stride=2,
        padding=0,
        fill=0,
        save=True,
        save_path="images/test2_maxpool.png",
        show_images=True,
        print_log=True
    )
    
    

    
