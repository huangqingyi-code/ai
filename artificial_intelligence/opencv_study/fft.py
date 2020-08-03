#numpy fourier transform
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("image/1.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.figure(figsize=(10,10))
plt.subplot(221),plt.imshow(img,cmap="gray")
plt.title("input image"),plt.yticks([]),plt.xticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum)
plt.title("magnitude spectrum"),plt.xticks([]),plt.yticks([])

h,w = img.shape
row = h // 2
col = w //2
mask = np.zeros((h,w),dtype=np.uint8)
# mask[...,] = 255
mask[h//2-30:h//2+30,w//2-30:w//2+30] = 1
fshift = fshift*mask
# print(type(fshift),fshift.shape)
# print(fshift.dtype)    #complex128
# fshift = cv2.bitwise_and(fshift,mask)
# fshift[(h//2-30):(h//2+30),(w//2-30):(w//2+30)] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(223),plt.imshow(img_back,cmap="gray")
plt.title("image after hpf"),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(img_back)
plt.title("result in jet"),plt.xticks([]),plt.yticks([])

plt.show()

#opencv fourier transform
#
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('9.jpg', 0)
#
# dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
#
# magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
#
# plt.figure(figsize=(10, 10))
# plt.subplot(221), plt.imshow(img, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#
# rows, cols = img.shape
# crow, ccol = rows // 2, cols // 2
# # create a mask first, center square is 1, remaining all zeros
# mask = np.zeros((rows, cols, 2), np.uint8)
# mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
# fshift = dft_shift * mask
# # apply mask and inverse DFT
#
# f_ishift = np.fft.ifftshift(fshift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
#
# plt.subplot(223), plt.imshow(img_back, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(img_back)
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#
# plt.show()
