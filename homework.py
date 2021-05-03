import os
import cv2
import numpy as np

folder = '/home/utkupolat/Desktop/ImageProcessing/flowers'                      # Image directory path

files = list([os.path.join(folder, f) for f in os.listdir(folder)])             # We read all images from source folder and add to files list.

average = cv2.imread(files[0]).astype(np.float)
for file in files[1:]:                                                          # We compute the average of images.
    image = cv2.imread(file)                                                    # Start from an explicitly set as floating point, in order to force the
    average += image                                                            # conversion of the 8-bit values from the images, which would otherwise overflow
                                                                                # NumPy adds two images element wise, so pixel by pixel / channel by channel
average /= len(files)                                                           # Divide by count (again each pixel/channel is divided)

output = cv2.normalize(average, None, 0, 255, cv2.NORM_MINMAX)                  # Normalize the image, to spread the pixel intensities across 0..255
                                                                                # This will brighten the image without losing information
cv2.imwrite('output.png', output)                                               # Save image.

cv2.waitKey()                                                                   # For the see output images until we close them.
cv2.destroyAllWindows()
