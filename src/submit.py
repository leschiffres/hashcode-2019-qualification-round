def interest_factor(a, b):
    return min(len(a-b), len(b-a), len(a.intersection(b)))

def compute_score(slides):
    total_score = 0
    for i in range(len(slides)-1):
        # print(f'Computing interest factor for slides: {i}, {i+1}, {slides[i]}, {slides[i+1]}')
        total_score += interest_factor(slides[i][0], slides[i+1][0])
    return total_score

def output_results(filename, slides): 
    output_submission = [len(slides)] 
    with open(filename, 'w') as f:
        f.write(str(len(slides))+ '\n')
        for s in slides:
            photo_ids = [str(id) for id in s[1:]]
            f.write(' '.join(photo_ids) + '\n')
    f.close()
