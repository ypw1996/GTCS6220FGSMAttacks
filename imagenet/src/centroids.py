import numpy as np


centroids = None
classes = [1, 105, 107, 109, 113, 114, 115, 122, 123, 128, 145, 146, 149, 151, 187, 207, 208, 235, 25, 267, 281, 283, 285, 286, 291, 294, 30, 301, 308, 309, 311, 313, 314, 315, 319, 32, 323, 325, 329, 338, 341, 345, 347, 349, 353, 354, 365, 367, 372, 386, 387, 398, 400, 406, 411, 414, 421, 424, 425, 427, 430, 435, 436, 437, 438, 440, 445, 447, 448, 457, 458, 462, 463, 466, 467, 470, 471, 474, 480, 485, 488, 492, 496, 50, 500, 508, 509, 511, 517, 525, 526, 532, 542, 543, 557, 562, 565, 567, 568, 570, 573, 576, 604, 605, 61, 612, 614, 619, 621, 625, 627, 635, 645, 652, 655, 675, 677, 678, 682, 683, 687, 69, 704, 707, 71, 716, 720, 731, 733, 734, 735, 737, 739, 744, 747, 75, 758, 76, 760, 761, 765, 768, 774, 779, 781, 786, 79, 801, 806, 808, 811, 815, 817, 821, 826, 837, 839, 842, 845, 849, 850, 853, 862, 866, 873, 874, 877, 879, 887, 888, 890, 899, 900, 909, 910, 917, 923, 924, 928, 929, 932, 935, 938, 945, 947, 950, 951, 954, 957, 962, 963, 964, 967, 970, 972, 973, 975, 978, 988, 99]


def test(input):
    if centroids is None:
        load()
    min_index = 0
    min_distance = np.linalg.norm(centroids[0] - input)
    for i in range(1, len(classes)):
        distance = np.linalg.norm(centroids[i] - input)
        if distance < min_distance:
            min_index = i
            min_distance = distance
    return classes[min_index]


def load():
    global centroids
    centroids = np.loadtxt('alexnet-centroids.np', dtype=float)


if __name__ == '__main__':
    x = np.zeros(10)
    print(test(x))
