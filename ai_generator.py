import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
