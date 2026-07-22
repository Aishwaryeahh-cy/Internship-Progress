# Product Rating System

ratings = []

n = int(input("Enter Number of Ratings: "))


for i in range(n):

    rating = int(input("Enter Rating (1-5): "))

    ratings.append(rating)


print("\nRatings")

print(ratings)


# Average

total = 0

for rating in ratings:

    total += rating


average = total / len(ratings)


print("Average Rating:", average)


# Count 5-Star Ratings

five_star = 0

for rating in ratings:

    if rating == 5:

        five_star += 1


print("5-Star Ratings:", five_star)


# Ascending Order

ratings.sort()

print("Ratings in Ascending Order:", ratings)