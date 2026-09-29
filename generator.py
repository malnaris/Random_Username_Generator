# generator.py
import json
import os
import random

CACHE_FILE = "themed_words.json"

# Fallback minimal words if json hasn't been built yet
DEFAULT_THEMES = {
    "Cyberpunk / Tech": {
        "adj": ["cyber", "quantum", "binary", "atomic", "glitch", "neural", "matrix", "holographic"],
        "nouns": ["cipher", "circuit", "node", "nexus", "daemon", "terminal", "proxy", "pulse"]
    }
}

def load_themes():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    print("Warning: themed_words.json not found. Run 'python build_cache.py' first for full word pools.")
    return DEFAULT_THEMES

THEME_DATA = load_themes()

def generate_themed_username(theme_name, separator="-", mode="3-word"):
    pool = THEME_DATA.get(theme_name, list(THEME_DATA.values())[0])
    adjectives = pool["adj"]
    nouns = pool["nouns"]

    if mode == "2-word":
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        return f"{adj}{separator}{noun}"

    elif mode == "3-word":
        # Ensure distinct words if pool allows
        if len(adjectives) >= 2:
            adj1, adj2 = random.sample(adjectives, 2)
        else:
            adj1 = adj2 = random.choice(adjectives)
        noun = random.choice(nouns)
        return f"{adj1}{separator}{adj2}{separator}{noun}"

    else:  # Hybrid Mode
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        num = random.randint(10, 999)
        return f"{adj}{separator}{noun}{separator}{num}"