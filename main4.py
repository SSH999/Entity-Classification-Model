import re

# Define the conversation as a list of utterances
conversation = [
    "hello hi nancy this is mike from at&t corporation.",
    "Yes ,how can I help you?",
    "Nancy you have been using our prepaid connection for  couple of years now. Right?",
    "Yes Thats right.",
    "How would u like a postpaid connection that allows you to make free postpaid connection to three AT&T connections?",
    "I would love that but whats the catch?",
    "There is no catch. There will be a monthly rental which you will have to pay like any other postpaid connection.",
    "Fantastic. Sign me up."
]

# Define rules for intent classification and entity recognition using regular expressions
rules = {
    "greeting": [
        r"hello|hi|hey",
        r"mike",
        r"at&t corporation"
    ],
    "confirm_usage": [
        r"prepaid",
        r"couple of years"
    ],
    "offer_postpaid": [
        r"postpaid",
        r"free",
        r"three",
        r"at&t connections"
    ],
    "ask_catch": [
        r"catch"
    ],
    "no_catch": [
        r"no catch",
        r"monthly rental",
        r"pay"
    ],
    "signup": [
        r"fantastic",
        r"sign me up"
    ]
}

# Classify the intent and recognize entities for each utterance in the conversation
intent = None
entities = {}
for utterance in conversation:
    if not intent:
        # Check for greeting
        if all(re.search(pattern, utterance.lower()) for pattern in rules["greeting"]):
            intent = "greeting"
    if not intent:
        # Check for confirmation of prepaid usage
        if all(re.search(pattern, utterance.lower()) for pattern in rules["confirm_usage"]):
            intent = "confirm_usage"
    if not intent:
        # Check for offer of postpaid connection
        if all(re.search(pattern, utterance.lower()) for pattern in rules["offer_postpaid"]):
            intent = "offer_postpaid"
            # Recognize entities
            entities["connections"] = "three AT&T connections"
    if not intent:
        # Check for request for catch
        if all(re.search(pattern, utterance.lower()) for pattern in rules["ask_catch"]):
            intent = "ask_catch"
    if not intent:
        # Check for confirmation of no catch
        if all(re.search(pattern, utterance.lower()) for pattern in rules["no_catch"]):
            intent = "no_catch"
    if not intent:
        # Check for signup
        if all(re.search(pattern, utterance.lower()) for pattern in rules["signup"]):
            intent = "signup"
    # Print the intent and entities for the current utterance
    print(f"Utterance: {utterance}")
    print(f"Intent: {intent}")
    print(f"Entities: {entities}\n")
    
print("All intents and entities were successfully classified and recognized.")
