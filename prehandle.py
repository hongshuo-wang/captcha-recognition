import cv2

def prehandle(image_path):
    image = cv2.imread(image_path)
    image = cv2.medianBlur(image, 3)
    color = image[0][0]
    image = image - color
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return image

if __name__ == "__main__":
    # image = prehandle("captcha/datasets/test/zlmt_1640002382.png")
    image = prehandle("RBXW.png")
    cv2.imshow("image", image)
    cv2.waitKey(0)
