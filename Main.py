from skimage import color, io
from skimage.filters import roberts, sobel, scharr, prewitt
import matplotlib.pyplot as plt
from detection import get_blood_vessels

if __name__ == '__main__':

    # Do odkomentowania aby wykorzystywał wszystkie pliki z folderu
    # imagesDirectory =
    # onlyfiles = [f for f in listdir("images") if isfile(join(mypath, f))]

    img = io.imread('images/01_dr.JPG')
    mask = io.imread('mask/01_dr_mask.tif')

    img = get_blood_vessels(img, mask)

    fig, ax = plt.subplots()
    ax.imshow(img, cmap="gray")
    plt.show()


    # image = color.rgb2gray(img)
    #
    #
    # edge_roberts = roberts(image)
    # edge_sobel = sobel(image)
    #
    # fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
    #                        figsize=(8, 4))
    #
    # ax[0].imshow(edge_roberts, cmap=plt.cm.gray)
    # ax[0].set_title('Roberts Edge Detection')
    #
    # ax[1].imshow(edge_sobel, cmap=plt.cm.gray)
    # ax[1].set_title('Sobel Edge Detection')
    #
    # for a in ax:
    #     a.axis('off')
    #
    # plt.tight_layout()
    # plt.show()

