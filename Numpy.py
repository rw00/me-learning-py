weight_kg = [65.2, 80.5, 55.3, 87.7, 52.8]
height_m = [1.77, 1.91, 1.74, 1.85, 1.65]

import numpy as np
# alternative to Lists; fast and easy

np_weight_kg = np.array(weight_kg)
np_height_m = np.array(height_m)

bmi = np_weight_kg / (np_height_m ** 2)

np_weight_lbs = np_weight_kg * 2.2
