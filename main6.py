import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Read the transcript from the file
with open("audio_transcript.txt", "r") as f:
    transcript = f.read()

# Tokenize the transcript into sentences and remove stopwords
sentences = sent_tokenize(transcript)
stop_words = set(stopwords.words("english"))
filtered_sentences = []
for sentence in sentences:
    words = word_tokenize(sentence)
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    filtered_sentences.append(" ".join(filtered_words))

# Generate the summary by taking the first 5 sentences
summary = " ".join(filtered_sentences[:5])

# Print the summary
print(summary)

# Save the summary to a file
with open("summary.txt", "w") as f:
    f.write(summary.replace(". ", ".\n"))
