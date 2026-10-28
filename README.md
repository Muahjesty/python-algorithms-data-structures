# AI-Assisted Movie Recommendation System

A Python 3.12 command-line interface (CLI) movie recommendation engine developed through collaborative prompt engineering with LLMs (ChatGPT, Claude, Gemini). The system processes user ratings and movie metadata to deliver top-N recommendation pipelines, user preference scoring, and automated test coverage.

---

## Key Features

* **Top-$N$ Global Recommendations**: Ranks top-rated movies across all dataset categories by average user rating.
* **Genre-Specific Top-$N$ Filtering**: Computes average ratings within individual genres to return top-performing titles per category.
* **Genre Popularity Analysis**: Evaluates overall genre rankings by computing aggregate scores across nested movie rating averages.
* **User Affinity & Personalized Recommendations**: Identifies a user's top-preferred genre and generates $3$ unrated movie recommendations from that genre.
* **Automated Test Suite (`test_movie_recommender.py`)**: Executes end-to-end testing across data loading, filtering pipelines, edge cases, and rating accuracy.

---

## Technical Specifications

| Aspect | Specification |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Architecture** | Functional modular CLI with docstring specifications |
| **AI Workflows** | Prompt-engineered using OpenAI ChatGPT / Anthropic Claude / Google Gemini |
| **Data Format** | Pipe-delimited plain text (`movie_genre\|movie_id\|movie_name`, `movie_name\|rating\|user_id`) |
| **Testing** | Automated unit & regression tester suite (`test_movie_recommender.py`) |

---

## System Architecture & Data Schema

### Input Data Format

1. **Movies File (`movies.txt`)**:
   ```text
   Comedy|101|Toy Story (1995)
   Action|102|The Dark Knight (2008)
   ```
2. **Ratings File (`ratings.txt`)**:
   ```text
   Toy Story (1995)|4.5|user_01
   The Dark Knight (2008)|5.0|user_01
   ```

---

## Usage & Execution

### Running the Recommendation CLI
Launch the interactive command-line application to load data files and run custom queries:
```bash
python movie_recommender.py
```

### Running Automated Test Suite
Execute automated test coverage across ranking algorithms, edge cases, and rating precision:
```bash
python test_movie_recommender.py
```

---

## Project Structure

```text
.
├── movie_recommender.py       # Main executable CLI application
├── test_movie_recommender.py  # Automated testing framework
├── coding_doc.pdf             # LLM prompt engineering logs & design rationale
├── testing_doc.pdf            # Test coverage strategy & input distribution analysis
├── .gitignore                 # Excludes cache files and local datasets
└── README.md                  # Project documentation
```

---

## Documentation Summary

* **`coding_doc.pdf`**: Complete transcript of prompts used with AI chatbots, case-sensitivity rules, data formatting edge cases handled, and language features implemented.
* **`testing_doc.pdf`**: Design breakdown of custom test datasets, boundary conditions, user rating distributions, and execution paths verified.
