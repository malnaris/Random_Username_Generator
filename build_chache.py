# build_cache.py
import json
import nltk
from nltk.corpus import wordnet as wn

print("Downloading WordNet data (one-time build)...")
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

THEME_SEEDS = {
    "Cyberpunk / Tech": ["technology", "computer", "digital", "robot", "network", "electricity", "code"],
    "Sci-Fi / Space": ["space", "star", "planet", "galaxy", "astronomy", "alien", "rocket"],
    "Fantasy / Mythic": ["magic", "dragon", "monster", "legend", "myth", "ghost", "sword"],
    "Gaming / Esports": ["game", "battle", "fight", "speed", "warrior", "victory", "stealth"],
    "Nature / Wild": ["forest", "animal", "mountain", "ice", "storm", "ocean", "plant"]
}

compiled_themes = {}

print("Building fast pre-compiled theme caches...")
for theme, seeds in THEME_SEEDS.items():
    adjectives = set()
    nouns = set()

    for seed in seeds:
        synsets = wn.synsets(seed)
        for syn in synsets:
            related_synsets = syn.hyponyms() + syn.part_meronyms() + syn.attributes() + [syn]
            for rel_syn in related_synsets:
                for lemma in rel_syn.lemmas():
                    word = lemma.name().lower().replace("_", "")
                    if 3 <= len(word) <= 10 and word.isalpha():
                        pos = rel_syn.pos()
                        if pos in ('a', 's'):
                            adjectives.add(word)
                        elif pos == 'n':
                            nouns.add(word)

    compiled_themes[theme] = {
        "adj": list(adjectives),
        "nouns": list(nouns)
    }

# Save locally to JSON for instant sub-millisecond loading
with open("themed_words.json", "w", encoding="utf-8") as f:
    json.dump(compiled_themes, f, indent=2)

print(" Done! 'themed_words.json' generated successfully.")
