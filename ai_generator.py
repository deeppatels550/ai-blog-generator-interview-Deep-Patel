import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword, seo_data):
    prompt = f"""
You are a professional blog writer.

Write a blog post about: **{keyword}**

Incorporate the following SEO metrics:
- Search Volume: {seo_data['search_volume']}
- Keyword Difficulty: {seo_data['keyword_difficulty']}
- Average CPC: ${seo_data['avg_cpc']}

Structure:
- Title
- Intro paragraph
- 3 sections with headers
- Conclusion
- Insert placeholders like {{AFF_LINK_1}} where affiliate links might go

Format it in Markdown.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    blog_content = response['choices'][0]['message']['content']
    return blog_content
