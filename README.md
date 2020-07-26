# DS PRODUCT VISION #

### Features: ###
- genre
- album
- artist
- song name
- song length
- relevance (plays/day maybe?)
- regional popularity/origin
- era of release
- social connections (maybe)

### Stretch Features: ###
- tone
- lyrics/sentiment analysis
- danceability


### Project Goals: ###
**Q: Describe the established data source with at least rough data able to be provided on day one.**\
A: List of songs, basic info about songs, song name, artist, album, length of song, genre, general classification/categorization, number of plays, indicator of how much you might like song\
**Q: Write a description for what the data science problem is. What uncertainty or prediction are you trying to discover? How could this data be used to find a solution to this problem?**\
A: The Data Science team aims to solve the problem of inadequate or inaccurate predictions of songs that the user might enjoy. Current models do not seem to be super effective -- a large portion of our team does not enjoy ~30% of their Discovery Weekly playlist, and we aim to minimize that number (aiming for ~20%)\
**Q: What's in a good song suggestion? How do we know the suggestion was good? Did the user like it or add it to playlist of any kind?**\
A: From our team's personal experience, listening to a song all the way through without skipping is generally the best indication of whether a song was a good prediction or not. Adding a song to a playlist or liking a song can give an indication about a particularly good suggestion, but we've discovered that most users are not likely to do this on "good suggestions" only "really good suggestions".\
**Q: What kind of target output can you deliver to the Web/UX/iOS teams to work with? Is it in JSON format or something else?**\
A: The Spotify API already outputs search requests as JSON, which our Data Engineer plans to flatten for ease of data analysis. We plan to change this back to Python via a Flask app when we return it to the backend team.\