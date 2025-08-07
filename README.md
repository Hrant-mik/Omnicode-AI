📘 Subword Vocabulary Tokenizer
🧠 Task Description
This project implements a subword-based tokenizer using a greedy longest-match-first strategy.

You are given a large natural language text (e.g., a paragraph from a news article or product description).
The tokenizer is built in two phases:

📌 Step 1 — Build Subword Vocabulary
Normalize the text
Convert all characters to lowercase and remove non-alphabetic characters (i.e., keep only a-z and spaces).

Extract all subwords
From each word in the normalized text, extract all contiguous substrings (subwords).

Filter by frequency
Only include those subwords that occur at least min_freq times.

📌 Step 2 — Tokenize New Text
Given a new input string:

Normalize it the same way.

Tokenize it by matching subwords from the vocabulary using a greedy, longest-match-first strategy.

If no subword matches at a given position, treat the current character as a separate token.

🧩 Functions to Implement
def build_subword_vocab(text: str, min_freq: int) -> set:
    """
    Build a vocabulary of subwords based on the training text.
    A subword is any contiguous sequence of characters within a word.
    Only include subwords that appear at least `min_freq` times.
    """
    pass
def tokenize_with_vocab(text: str, vocab: set) -> list:
    """
    Tokenize the input text using the provided subword vocabulary.
    Use greedy longest-match-first strategy.
    If no subword matches at a position, treat the current character as a token.
    """
    pass
✅ Example
training_text = "International, interaction! Interstellar: Internal? Intentional."
min_freq = 2
vocab = build_subword_vocab(training_text, min_freq)

sentence = "Intentional"
tokens = tokenize_with_vocab(sentence, vocab)

print(tokens)  # Output: ['inte', 'nt', 'ional']
