
## 📋 Task Overview

You are given a large natural language text (e.g., a product description or news article). Your goal is to:

1. **Normalize the text**:
   - Convert to lowercase
   - Remove non-alphabetic characters (punctuation, numbers, etc.)

2. **Extract subwords**:
   - A subword is any contiguous sequence of characters within a word
   - Count all subwords from the normalized text

3. **Build a vocabulary**:
   - Include only subwords that appear **at least `min_freq` times**

4. **Tokenize new input**:
   - Normalize the input sentence
   - Use **greedy, longest-match-first** strategy to tokenize using the vocabulary
   - If no subword matches, treat the current character as a token

---

## 🚀 Example

**Training text**:
```
"International, interaction! Interstellar: Internal? Intentional."
```

**Minimum frequency**: `2`

**Input sentence**:
```
"Intentional"
```

**Expected output**:
```python
['inte', 'nt', 'ional']
```

---

## 🧩 Functions

### `build_subword_vocab`

```python
def build_subword_vocab(text: str, min_freq: int) -> set:
    """
    Build a set of subwords from the training text.

    Steps:
    - Normalize: lowercase + remove non-alphabetic characters
    - Split into words
    - Generate all subwords (contiguous sequences)
    - Count frequency
    - Return only subwords with frequency >= min_freq
    """
```

### `tokenize_with_vocab`

```python
def tokenize_with_vocab(text: str, vocab: set) -> list:
    """
    Tokenize a normalized input string using the subword vocabulary.

    Strategy:
    - Greedy, longest-match-first from left to right
    - If no subword matches at a position, use the single character
    """
```

---

## 🛠 Example Code

```python
text = "International, interaction! Interstellar: Internal? Intentional."
vocab = build_subword_vocab(text, min_freq=2)

print(vocab)

tokens = tokenize_with_vocab("Intentional", vocab)
print(tokens)  
```
