import re

def build_subword_vocab(text: str, min_freq: int) -> set:
    text = re.sub(r"[^a-z ]", " ", text.lower())
    words = text.split()
    freq = {}
    
    for word in words:
        for i in range(len(word)):
            for j in range(i, len(word) + 1):
                sub = word[i:j]
                if sub in freq:
                    freq[sub] += 1
                else:
                    freq[sub] = 1
    vocab = set()
    for sub in freq:
        if freq[sub] >= min_freq:
            vocab.add(sub)
    return vocab

def tokenize_with_vocab(text: str, vocab: set) -> list:
    text = re.sub(r"[^a-z]", "", text.lower())
    tokens = []
    n = 0
    while n <(len(text)):
        long_part = ""
        for j in range(n+1, len(text) + 1):
            part = text[n:j]
            if part in vocab and len(part) > len(long_part):
                long_part = part
        if long_part:
            tokens.append(long_part)
            n += len(long_part)
        else:
            n += 1
    return tokens
    
    
text = "International, interaction! Interstellar: Internal? Intentional."
vocab = build_subword_vocab(text, 2)
print(vocab)

tokens = tokenize_with_vocab("Intentional", vocab)
print(tokens) 