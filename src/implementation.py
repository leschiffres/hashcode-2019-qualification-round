import numpy as np
import time
from submit import interest_factor, compute_score
import random
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

def simulated_annealing(slides):
    def decision(probability):
        return random.random() < probability

    # pick an initial permutation
    t = 1000
    tmin = 1
    coolingRate = 0.0003
    
    best_permutation = [i for i in range(len(slides))]
    best_score = compute_score(slides)

    print('-'*100)
    print('Starting Simulated Annealing Process')
    print('-'*100)
    print(f'Initial Best Score: {best_score}')
    
    permutation = [i for i in range(len(slides))]
    score = best_score
    while t > tmin:        
        # find two random positions to change
        pos1 = random.randint(0, len(permutation)-1)
        pos2 = random.randint(0, len(permutation)-1)
        
        new_solution = permutation.copy()
        # exchange elements
        new_solution[pos1], new_solution[pos2] = new_solution[pos2], new_solution[pos1]
        new_score = compute_score([slides[i] for i in new_solution])
        
        # update max_score
        if best_score < new_score :
            best_score = new_score
            best_permutation = new_solution.copy()
            print(f'Found New Best Score: {best_score}')
            
        if new_score > score:
            score = new_score
            permutation = new_solution.copy()
        else:
            # accept worse solution with probability np.exp(-(score - new_score)/t)
            if decision(np.exp(-(score - new_score)/t)):
                score = new_score
                permutation = new_solution.copy()
        t = t*(1-coolingRate)
    
    return [slides[i] for i in best_permutation]
