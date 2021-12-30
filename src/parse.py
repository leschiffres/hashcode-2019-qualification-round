# receives as input a filename and returns the parameters of the input file
# n: total number of photos
# photo_type: a list containing V|H for every photo, depending on whether the photo is vertical or horizontal
# total_tags: a list for every photo containing its total number of tags (contains numbers)
# tags_list: a list containing the tags of every photo (contains strings)
def parse_file(filename):
    lines = open(filename).readlines()
    n = int(lines[0])
    
    photo_type = []
    total_tags = []
    tags_list = []
    for i in range(1, len(lines)):
        words = lines[i].split()
        photo_type.append(words[0])
        total_tags.append(int(words[1]))
        tags_list.append(set(words[2:len(words)]))
    return n, photo_type, total_tags, tags_list
