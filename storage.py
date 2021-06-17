import csv

all_articles = []

with open("articles.csv") as file:
    reader = csv.reader(file)
    data = list(reader)

    all_articles = data[1:]

liked_article = []
not_liked_article = []
