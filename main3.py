# Import necessary libraries
import spacy

# Load the pre-trained NLU model
nlp = spacy.load("en_core_web_sm")

# Define rules for intent classification and entity recognition
rules = {
    "order_pizza": {"keywords": ["order", "pizza"], "entities": {"topping": ["pepperoni", "mushroom", "sausage"]}},
    "schedule_appointment": {"keywords": ["schedule", "appointment", "dentist"], "entities": {"specialty": ["dentist", "orthodontist", "periodontist"]}},
    "find_hotel": {"keywords": ["hotel", "downtown", "Chicago"], "entities": {"location": ["downtown Chicago", "loop", "river north"]}},
    "get_weather": {"keywords": ["weather", "New York City"], "entities": {"location": ["New York City", "Manhattan", "Queens"]}},
    "buy_car": {"keywords": ["buy", "car"], "entities": {"feature": ["leather seats", "sunroof", "navigation system"]}}
}

# Define a sample dataset of sentences to classify
dataset = [
    "I want to order a pizza with pepperoni.",
    "Can I schedule an appointment with the dentist for next week?",
    "I'm looking for a hotel in downtown Chicago.",
    "What's the weather like in Manhattan today?",
    "I want to buy a new car with leather seats and a sunroof."
]

# Classify the intent and recognize entities for each example sentence in the dataset
for sentence in dataset:
    intent = None
    for key in rules.keys():
        if all(word in sentence.lower() for word in rules[key]["keywords"]):
            intent = key
            break
    entities = {}
    if intent is not None and "entities" in rules[intent]:
        doc = nlp(sentence)
        for entity_type in rules[intent]["entities"].keys():
            for entity_value in rules[intent]["entities"][entity_type]:
                if entity_value.lower() in sentence.lower():
                    for ent in doc.ents:
                        if ent.label_ == entity_type and entity_value in ent.text.lower():
                            entities[entity_type] = entity_value
                            break
                    break
    print(f"Sentence: {sentence}")
    print(f"Intent: {intent}")
    print(f"Entities: {entities}")
    print()
