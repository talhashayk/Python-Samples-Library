names = ["Big T", "Lil T", "Juju", "Cous"]
governments = ["Talha Sheikh", "Daniel Oluwashegun", "Adam El-Tunsi"]
movie_and_rating = {"Forest Gump": 8, "Dark Knight": 10,
                    "Interstellar": 9, "Spoderman": 2}

# Basic Comprehension
l = []
for person in names:
    l.append(person)
print("Street:\t\t", l)
l.clear()
###################################################################################
l2 = [person for person in governments]
###################################################################################
print("Government:\t", l2)

print()

# Concatenate Comprehension
for person in names:
    l.append(person + " is a big man")
print("Street:\t\t", l)
l.clear()
###################################################################################
l2 = [person + " is a bigman" for person in governments]
###################################################################################
print("Government:\t", l2)

print()

# Conditional Comprehension
for movie in movie_and_rating:
    if movie_and_rating.get(movie) > 6:
        l.append(movie)
print("Good Movies:\t", l)
###################################################################################
l2 = [movie for movie in movie_and_rating if movie_and_rating.get(movie) > 9]
###################################################################################
print("Better Movies:\t", l2)
