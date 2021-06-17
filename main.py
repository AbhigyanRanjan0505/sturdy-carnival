from flask import Flask, jsonify
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations
import itertools

app = Flask(__name__)


@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })


@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    article = all_articles[0]
    liked_articles.append(article)

    return jsonify({
        "status": "success"
    }), 201


@app.route("/unliked-articles", methods=["POST"])
def unliked_articles():
    article = all_articles[0]
    not_liked_articles.append(article)

    return jsonify({
        "status": "success"
    }), 201


@app.route("/popular-articles")
def popular_articles():
    article_data = []

    for article in output:
        data = {
            "title": article[0],
            "eventType": article[1],
            "contentType": article[2],
            "url": article[3],
            "text": article[4],
            "lang": article[5]
        }

        article_data.append(data)

    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200


@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []

    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])

        for data in output:
            all_recommended.append(data)

    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,
                           _ in itertools.groupby(all_recommended))

    article_data = []
    for recommended in all_recommended:
        data = {
            "title": recommended[0],
            "eventType": recommended[1],
            "contentType": recommended[2],
            "url": recommended[3],
            "text": recommended[4],
            "lang": recommended[5]
        }

        article_data.append(data)

    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200


if __name__ == "__main__":
    app.run()
