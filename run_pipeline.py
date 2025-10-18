# ================================
# AUTO YOUTUBE SHORTS (BASIC TEST)
# ================================

# This is the robot's basic brain. It just finds a topic and writes a fake script.
# Later we will add video-making and uploading.

import requests
from datetime import datetime
import random

# Function to get trending topics from Google Trends (simple version)
def get_trending_topics():
    url = "https://trends.google.com/trends/hottrends/visualize/internal/data/en"
    try:
        topics = requests.get(url, timeout=10).json()
        return random.sample(topics, 5)
    except Exception as e:
        return ["Artificial Intelligence", "Health Tips", "Money Hacks", "Motivation", "Space Facts"]

# Function to make a simple short script text
def make_script(topic):
    hook = f"You won’t believe this about {topic}!"
    body = f"Did you know? {topic} is one of the most searched things right now!"
    end = "Follow for more amazing shorts like this!"
    return f"{hook}\n{body}\n{end}"

# MAIN PROGRAM
print("🤖 Auto YouTube Shorts Robot Starting...")
today = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"⏰ Current Time: {today}")

topics = get_trending_topics()
print("🔥 Trending Topics Found:", topics)

chosen = random.choice(topics)
print("🎯 Selected Topic:", chosen)

script = make_script(chosen)
print("\n📝 Generated Short Script:\n")
print(script)

print("\n✅ All done! (Next we’ll teach it to make and upload the video.)")
