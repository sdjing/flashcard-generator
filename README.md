# AI Flashcard Generator

Generates Q&A flashcards from any PDF or text document using the Anthropic API. Upload your notes or a textbook chapter and get a set of study cards instantly.

## Features
- PDF and TXT file support
- Adjustable number of flashcards (5–20)
- Interactive card viewer with flip functionality
- Export flashcards as CSV

## Tech Stack
- Python
- Anthropic API (Claude)
- Streamlit
- pdfminer.six

## Setup

1. Clone the repo
```
git clone https://github.com/sdjing/flashcard-generator.git
cd flashcard-generator
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Add your Anthropic API key
```
echo ANTHROPIC_API_KEY=your-key-here > .env
```

4. Run the app
```
python -m streamlit run flashcard_app.py
```

## Usage
1. Upload a PDF or TXT file
2. Set how many flashcards to generate
3. Click **Generate Flashcards**
4. Flip through cards or download as CSV
