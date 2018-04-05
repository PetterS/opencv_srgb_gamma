import numpy as np


def to_linear(srgb):
	linear = np.float32(srgb) / 255.0
	less = linear <= 0.04045
	linear[less] = linear[less] / 12.92
	linear[~less] = np.power((linear[~less] + 0.055) / 1.055, 2.4)
	return linear

    
def from_linear(linear):
	srgb = linear.copy()
	less = linear <= 0.0031308
	srgb[less] = linear[less] * 12.92
	srgb[~less] = 1.055 * np.power(linear[~less], 1.0 / 2.4) - 0.055
	return srgb * 255.0


if __name__ == "__main__":
	# Test
	for x in [0., 0.000123, 0.345, 0.9, 1.0]:
		assert abs(x - to_linear(from_linear(np.array([x])))) < 1e-6
	for x in range(256):
		assert round(x - from_linear(to_linear(np.array([x])))[0]) == 0
	print("Test OK.")
