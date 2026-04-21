import cv2
import numpy as np

def compute_change_map(pre_path, post_path):
    pre = cv2.imread(pre_path)
    post = cv2.imread(post_path)

    pre = cv2.resize(pre, (800, 800))
    post = cv2.resize(post, (800, 800))

    gray_pre = cv2.cvtColor(pre, cv2.COLOR_BGR2GRAY)
    gray_post = cv2.cvtColor(post, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray_pre, gray_post)

    # 🔥 higher threshold → less noise
    _, thresh = cv2.threshold(diff, 40, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return thresh