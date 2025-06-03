import random

def fetch_seo_data(keyword):
    # Just mocking it with random values for now
    return {
        "search_volume": random.randint(100, 10000),
        "keyword_difficulty": round(random.uniform(0.1, 1.0), 2),  # scale 0-1
        "avg_cpc": round(random.uniform(0.5, 10.0), 2)  # in dollars
    }
