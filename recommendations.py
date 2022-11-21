import random

movie_list = ["Dune",
              "Star Wars",
              "Lost",
              "Shawshank Redemption",
              "24",
              "Inception",
              "Shutter Island",
              "All Dogs Go to Heaven",
              "12 Angry Men"]

def random_recommender():
    random.shuffle(movie_list)
    return movie_list[:4]

def nmf_recommender():
    return NotImplemented

def cosine_recommender():
    return NotImplemented

if __name__ == '__main__':
    print(random_recommender())