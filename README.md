# Sign-Friendly Text Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Convert English sentences into sign-language-friendly text by removing stopwords and simplifying grammar. Built with Python, Streamlit, and NLTK.

## How It Works

Sign languages use simplified grammar that focuses on **content words** (nouns, verbs, adjectives) rather than function words (articles, prepositions, auxiliary verbs). This tool:

1. **Tokenizes** input text using NLTK's word tokenizer
2. **Removes** punctuation and non-alphabetic tokens
3. **Filters out** English stopwords (is, the, and, etc.)
4. **Returns** the simplified, sign-friendly output

### Example

| Input | Output |
|-------|--------|
| "I will be going to the market tomorrow." | "going market tomorrow" |
| "The quick brown fox jumps over the lazy dog." | "quick brown fox jumps lazy dog" |
| "She is reading a very interesting book about science." | "reading interesting book science" |

## Features

- Single sentence conversion with side-by-side comparison
- Batch conversion for multiple sentences
- Word count statistics and reduction percentage
- Toggle to show removed words
- Example sentences in the sidebar

## Installation

```bash
git clone https://github.com/Anlinnazateth/Sign-friendly-Text-generator.git
cd Sign-friendly-Text-generator
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

NLTK data downloads automatically on first run.

## Usage

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Project Structure

```
Sign-friendly-Text-generator/
├── app.py              # Streamlit UI
├── utils.py            # Core conversion logic
├── sign.py             # Legacy version (reference)
├── requirements.txt    # Python dependencies
├── LICENSE
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI
└── tests/
    └── test_converter.py
```

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## License

MIT License. See [LICENSE](LICENSE) for details.
