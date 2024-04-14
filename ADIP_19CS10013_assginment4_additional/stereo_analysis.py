# stereo_analysis.py
import cv2
import numpy as np
from points import points1, points2  # Importing the points from points.py

def get_calibration_matrix(H, W):
    return np.array([
        [-H/2, 0, H/2],
        [0, W/2, W/2],
        [0, 0, 1]
    ])

def estimate_homography(pts1, pts2, H, W):
    K = get_calibration_matrix(H, W)
    H_matrix, status = cv2.findHomography(pts1, pts2, method=cv2.RANSAC)
    return H_matrix

def estimate_rotation_matrix(H, K):
    K_inv = np.linalg.inv(K)
    R = K_inv.dot(H).dot(K)
    return R

def estimate_fundamental_matrix(pts1, pts2):
    F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_8POINT)
    return F


H = 576  # Height of the image
W = 1024  # Width of the image

H_matrix = estimate_homography(points1, points2, H, W)
K = get_calibration_matrix(H, W)
R = estimate_rotation_matrix(H_matrix, K)
F = estimate_fundamental_matrix(points1, points2)

print("Calibration Matrix K:")
print(K)
print("Homography Matrix H:")
print(H_matrix)
print("Rotation Matrix R:")
print(R)
print("Fundamental Matrix F:")
print(F)
