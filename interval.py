#ratings are from 1 to 100
raterange = 100

def conf(ratings):
    interval = (ratings[-1]-ratings[0])/raterange
    c = float (len(ratings))
    perc = 1.0
    mean = float (raterange/2)
    inside = ratings
    while (perc>interval):
        if ((mean-inside[0])>(inside[-1]-mean)):
            interval = float (2.0*(mean-inside[0])/raterange)
            inside = inside[1:]
        else:
            interval = float (2.0*(inside[-1]-mean)/raterange)
            inside = inside[:-1]
        perc = float (len(inside)/c)
        if (interval == 0.0):
            return 1.0
    return 1-interval

#a few examples
ratings = [29.0, 29.0, 29.0, 30.0, 31.0, 40.0, 45.0, 50.0, 51.0, 76.0, 90.0]
assert (int (100*conf(ratings)) == 62)

ratings = [1.0, 2.0, 50.0, 50.0, 90.0]
assert (int (100*conf(ratings)) == 2)

ratings = [45, 50, 50, 50, 50, 51, 52, 53]
assert (int (100*conf(ratings)) == 100)

ratings = [50, 50, 50, 50]
assert (int (100*conf(ratings)) == 100)
