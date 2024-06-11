import random

# This is temporary script which generate 'random' prompt
adjectives = ["beautiful", "sunny", "gloomy", "colorful", "serene", "vibrant", "dark", "mysterious", "tranquil", "lively"]
nouns = ["forest", "ocean", "mountain", "cityscape", "desert", "skyline", "sunset", "waterfall", "garden", "village"]
verbs = ["glowing", "shining", "resting", "flowing", "standing", "whispering", "blooming", "rising", "reflecting", "falling"]
prepositions = ["in", "with", "under", "over", "beside", "around", "near", "on", "between", "through"]

# Function to generate a random description
def generate_description():
    phrase_length = random.randint(2, 5)
    description = []

    while len(description) < phrase_length:
        if len(description) % 2 == 0:
            description.append(random.choice(adjectives + nouns + verbs))
        else:
            description.append(random.choice(prepositions))

    return " ".join(description)

if __name__ == "__main__":
    print(generate_description())