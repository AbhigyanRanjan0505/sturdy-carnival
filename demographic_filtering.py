import pandas

df = pandas.read_csv("articles.csv")

df = df.sort_values(["total_events"], ascending=True)

output = df[["title", "eventType", "contentType",
             "url", "text", "lang"]].head(20).values.tolist()
