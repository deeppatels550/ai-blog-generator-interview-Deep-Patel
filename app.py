from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import atexit


app = Flask(__name__)
load_dotenv()


@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    seo_data = fetch_seo_data(keyword)
    blog_post = generate_blog_post(keyword, seo_data)
    print("Endpoint hit")

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post": blog_post
    })

def scheduled_blog_job():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blog_output_{timestamp}.md"
    with open(filename, "w") as f:
        f.write(blog_post)

    print(f"[{timestamp}] ✅ Blog post generated and saved as {filename}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_blog_job, trigger="interval", days=1)
scheduler.start()

# Ensure scheduler stops on app exit
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run(debug=True, port=5001)
