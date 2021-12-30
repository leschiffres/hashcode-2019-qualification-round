import numpy as np
import time
from submit import interest_factor
def random_permutation_algorithm(slides): 
    np.random.shuffle(slides)
    return slides

def greedy_search(slides, K=100):
    start = time.time()
    # start with a random slide as start
    permutation = [slides.pop()]

    while slides:
        # find the slide that maximizes the interest factor to the last added slide
        # due to the fact that initially there are 60K possible slides we have to restrict the space
        # that's why we are going to consider just K=500 slides every time we decide for the next
        # slide that maximizes the interest factor to the previous one
        a = permutation[-1][0]
        max_rate, index = -1, -1
        search_space = min(len(slides), K)
        for i in range(search_space):
            b = slides[i][0]
            rate = interest_factor(a, b)
            if rate > max_rate:
                max_rate = rate
                index = i
        permutation.append(slides.pop(index))

        if len(slides) % 1000 == 0:
            current_time = round(time.time() - start, 2)
            print(f'Program Running: {current_time} seconds. Total Remaining Slides: {len(slides)}')
    return permutation
