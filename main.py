import random


# TODO: Fix recency bias

options = [
]


ratings = dict.fromkeys(options, 1)
for _ in range(len(options) // 3):
    random.shuffle(options)
    fav = options[0]
    fav_rating = ratings[fav]

    for i in range(1, len(options)):
        opt = options[i]
        choice = input(f'Keep {fav} vs {opt}?\n')
        print()
        if choice.lower() in ['y', 'yes', '1']:
            fav_rating += ratings[opt]
        else:
            ratings[fav] = fav_rating
            fav = opt
            fav_rating += ratings[opt]
    else:
        ratings[fav] = fav_rating


for opt in sorted(ratings, key=lambda k: ratings[k], reverse=True):
    print(opt, ratings[opt])

