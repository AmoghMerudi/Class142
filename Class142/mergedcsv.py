import csv

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

    allMovies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open("movielinks.csv", "a+") as f:
    reader = csv.reader
    data = list(reader)
    allMoviesLink =data[1:]

for movieitem in allMovies:
    posterfound = any(movieitem[8] in movieitems for movieitems in allMoviesLink)

    if posterfound:
        for movieitems in allMoviesLink:
            if movieitem[8] == movieitems[0]:
                movieitem.append(movieitems[1])

                if len(movieitem) == 28:
                    with open("final.csv", "a+") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movieitem)
                