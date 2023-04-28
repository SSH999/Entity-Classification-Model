import re
import json

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
with open("output.json", "w") as f:
    for utterance in conversation:
        intent = None
        entities = {}
        output = {}
        # Check for greeting
        if all(re.search(pattern, utterance.lower()) for pattern in rules["greeting"]):
            intent = "greeting"
        # Check for confirmation of prepaid usage
        elif all(re.search(pattern, utterance.lower()) for pattern in rules["confirm_usage"]):
            intent = "confirm_usage"
        # Check for offer of postpaid connection
        elif all(re.search(pattern, utterance.lower()) for pattern in rules["offer_postpaid"]):
            intent = "offer_postpaid"
            # Recognize entities
            entities["connections"] = "three AT&T connections"
        # Check for request for catch
        elif all(re.search(pattern, utterance.lower()) for pattern in rules["ask_catch"]):
            intent = "ask_catch"
        # Check for confirmation of no catch
        elif all(re.search(pattern, utterance.lower()) for pattern in rules["no_catch"]):
            intent = "no_catch"
        # Check for signup
        elif all(re.search(pattern, utterance.lower()) for pattern in rules["signup"]):
            intent = "signup"
        # Store the intent and entities in the output dictionary
        output["Utterance"] = utterance
        output["Intent"] = intent
        output["Entities"] = entities
        # Write output to file
        json.dump(output, f)
        f.write("\n")
