movie = "My    beautiful\n laundrette!"

# Create a list of the above string
# without extra spaces nor new lines
movie_list = movie.split()
# Use slices, concatenation and list index all in one line
# to join the elements of the list excluding the exclamation mark
movie_joined = movie_list[:-1] + [movie_list[-1][:-1]]

# Change the word laundrette to garden
movie_joined[-1] = "garden"

# Capitalize only the first character of each word and print the new string
movie_final = ' '.join(word.capitalize() for word in movie_joined)
print(movie_final)