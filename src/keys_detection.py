from pathlib import Path

import cv2
import numpy as np

path = str(Path(__file__).parents[0])

# Load the keyboard and template images
keyboard = cv2.imread(path + '/keys_det_temp/' + 'keyboard.jpeg', cv2.IMREAD_COLOR)
template_paths = [path + '/keys_det_temp/' + 'key_template.jpeg',
                  path + '/keys_det_temp/' + 'key_template_cleanup.jpeg',
                  path + '/keys_det_temp/' + 'keyboard (1).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (2).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (3).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (4).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (5).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (6).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (7).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (8).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (9).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (10).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (11).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (12).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (13).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (14).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (15).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (16).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (17).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (18).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (19).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (20).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (21).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (22).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (23).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (24).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (25).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (26).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (27).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (28).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (29).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (30).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (31).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (32).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (33).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (34).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (35).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (36).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (37).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (38).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (38).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (39).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (40).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (41).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (42).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (43).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (44).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (45).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (46).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (47).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (48).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (49).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (50).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (51).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (52).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (53).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (54).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (55).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (56).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (57).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (58).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (59).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (60).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (61).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (62).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (63).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (64).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (65).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (66).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (67).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (68).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (69).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (70).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (71).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (72).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (73).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (74).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (75).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (76).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (77).jpeg',
                  path + '/keys_det_temp/' + 'keyboard (78).jpeg']

# Convert images to grayscale
keyboard_gray = cv2.cvtColor(keyboard, cv2.COLOR_BGR2GRAY)
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
