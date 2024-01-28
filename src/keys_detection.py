import os

import cv2
import numpy as np

# Load the keyboard and template images
keyboard = cv2.imread(os.getcwd() + '/keys_det_temp/' + 'keyboard.jpeg', cv2.IMREAD_COLOR)
template_paths = [os.getcwd() + '/keys_det_temp/' + 'key_template.jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'key_template_cleanup.jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (1).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (2).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (3).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (4).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (5).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (6).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (7).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (8).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (9).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (10).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (11).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (12).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (13).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (14).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (15).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (16).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (17).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (18).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (19).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (20).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (21).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (22).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (23).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (24).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (25).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (26).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (27).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (28).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (29).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (30).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (31).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (32).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (33).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (34).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (35).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (36).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (37).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (38).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (38).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (39).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (40).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (41).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (42).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (43).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (44).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (45).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (46).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (47).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (48).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (49).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (50).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (51).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (52).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (53).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (54).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (55).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (56).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (57).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (58).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (59).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (60).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (61).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (62).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (63).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (64).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (65).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (66).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (67).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (68).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (69).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (70).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (71).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (72).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (73).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (74).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (75).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (76).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (77).jpeg',
                  os.getcwd() + '/keys_det_temp/' + 'keyboard (78).jpeg']

# Convert images to grayscale
keyboard_gray = cv2.cvtColor(keyboard, cv2.COLOR_BGR2GRAY)
# template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
threshold = 0.9
# Loop over each template
for template_path in template_paths:
    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(keyboard_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for matching score
    loc = np.where(result >= threshold)

    # Draw rectangles around the matches
    for pt in zip(*loc[::-1]):
        bottom_right = (pt[0] + template.shape[1], pt[1] + template.shape[0])
        cv2.rectangle(keyboard, pt, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Template Matching Result', keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
