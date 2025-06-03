from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post

app = Flask(__name__)
load_dotenv()

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    seo_data = fetch_seo_data(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post": blog_post
    })

if __name__ == '__main__':
    app.run(debug=True)
