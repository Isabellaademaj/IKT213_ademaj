
#1.

import cv2
import numpy as np

def harriscornerdetection(reference_image):
    img = cv2.imread(reference_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    dst = cv2.dilate(dst, None)

    img[dst>0.01*dst.max()] = [0, 0, 255]

    cv2.imwrite("solutions/harris.png", img)

harriscornerdetection("reference_img.png")


#2 SIFT

def align_images(image_to_align, reference_image, max_features, good_match_precent):
    img1 = cv2.imread(image_to_align)
    img2 = cv2.imread(reference_image)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    flann_index_kdtree = 1
    index_params = dict(algorithm = flann_index_kdtree, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k = 2)

    good_matches = []

    for m, n in matches:
        if m.distance < good_match_precent * n.distance:
            good_matches.append(m)

    print("Number of good matches", len(good_matches))

    if len(good_matches) < max_features:
        print("Not enough good matches")
        return

    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)

    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

    homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    matches_mask = mask.ravel().tolist()

    height, width = img2.shape[:2]

    aligned = cv2.warpPerspective(img1, homography, (width, height))

    draw_params = dict(matchColor = (255, 0, 0), singlePointColor = None, matchesMask = matches_mask, flags = 2)

    matches_image = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, **draw_params)


    cv2.imwrite("solutions/aligned.png", aligned)
    cv2.imwrite("solutions/matches_image.png", matches_image)

align_images(
    "align_this.jpg",
    "reference_img.png",
    10,
    0.7
    )