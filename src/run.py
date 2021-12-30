from parse import parse_file
from submit import compute_score, output_results
from implementation import random_permutation_algorithm, greedy_search
import random

def split_photos(photo_type):
    vertical, horizontal = ([] for _ in range(2))
    for i in range(len(photo_type)):
        if photo_type[i] == 'V':
            vertical.append(i)
        else:
            horizontal.append(i)
    return vertical, horizontal

# receives as input the indexes of the vertical photos and returns pairs of them
def build_vertical_slides(vertical_photos):
    # first way: pick random pairs
    
    # while there are at least two photos to form a pair 
    vertical_pairs = []
    while len(vertical_photos) > 1:
        pair = [vertical_photos.pop(random.randint(0, len(vertical_photos)-1)), vertical_photos.pop(random.randint(0, len(vertical_photos)-1))]
        vertical_pairs.append(pair)

    return vertical_pairs

input_filenames = ["a_example", "b_lovely_landscapes", "c_memorable_moments", "d_pet_pictures", "e_shiny_selfies"]
input_filenames = ["d_pet_pictures"]
for f in input_filenames:
    print("-"*100)
    print("Filename:",f+'.txt')
    # read file
    filename = './input/' + f + '.txt'
    total_photos, photo_type, total_tags, tags_list = parse_file(filename)
    vertical, horizontal = split_photos(photo_type)
    print('Vertical: {0} , Horizontal: {1}' .format(len(vertical), len(horizontal)))
    
    # Single vertical photos are not alowed in a file. They have to be organised pairwise in a slide.
    # The following function places vertical photos into pairs completely at random.
    vertical_slides = build_vertical_slides(vertical)
    
    slides  = []
    for pair in vertical_slides:
        tags =  tags_list[pair[0]].union(tags_list[pair[1]])
        slides.append([tags, pair[0], pair[1]])

    for h in horizontal:
        tags = tags_list[h]
        slides.append([tags, h])
    
    # print(slides)
    # at this point the variable slides is a list where for each slides two things are stored:
    # - the tags (as a set)
    # - the id(s) of the photo(s) included in this slide
    # e.g. [[{'smile', 'garden', 'selfie'}, 1, 2], [{'cat', 'sun', 'beach'}, 0], [{'cat', 'garden'}, 3]]
    # so given a slide index i, we can acess the tags simply by slides[i][0] and its photos by slides[i][1:]
    
    total_slides = len(slides)
    print("Total number of slides : %d" %(total_slides))
    
    # slides = random_permutation_algorithm(slides)
    # slides = simulating_annealing(slides)

    slides = greedy_search(slides, K=1000)

    print("Total Score : %d" %(compute_score(slides)))

    output_file = './output/' + f + '.txt'
    output_results(output_file, slides)

    