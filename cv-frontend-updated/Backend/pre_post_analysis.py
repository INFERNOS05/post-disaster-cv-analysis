import cv2
import matplotlib.pyplot as plt

def show_pre_post(pre_path, post_path):
    pre = cv2.imread(pre_path)
    post = cv2.imread(post_path)

    pre = cv2.cvtColor(pre, cv2.COLOR_BGR2RGB)
    post = cv2.cvtColor(post, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(pre)
    plt.title("Pre-Disaster")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(post)
    plt.title("Post-Disaster")
    plt.axis("off")

    plt.show()