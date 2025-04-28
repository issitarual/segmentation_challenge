import cv2
import numpy as np
import matplotlib.pyplot as plt

def segmentation_pipeline(imagem):
    """
    This function aims to segment walls and windows from a given architectural plan.
    Input: Image (architectural plan)
    Output: (Binary mask of walls, Binary mask of walls)
    """
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    pixel_values = blur.reshape((-1, 1))
    pixel_values = np.float32(pixel_values)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 3
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers.flatten())
    labels = labels.flatten()

    segmented_img = centers[labels]
    segmented_img = segmented_img.reshape(blur.shape)

    sorted_centers = np.sort(centers)

    wall_mask = np.zeros_like(gray)
    window_mask = np.zeros_like(gray)

    for i, center in enumerate(centers):
        mask = np.where(labels == i, 255, 0).astype(np.uint8).reshape(gray.shape)

        if center == sorted_centers[-1]:
            wall_mask = cv2.bitwise_or(wall_mask, mask)
        elif center == sorted_centers[-2]:
            window_mask = cv2.bitwise_or(window_mask, mask)

    kernel = np.ones((3,3), np.uint8)
    wall_mask = cv2.morphologyEx(wall_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    window_mask = cv2.morphologyEx(window_mask, cv2.MORPH_OPEN, kernel, iterations=2)

    return wall_mask, window_mask, segmented_img