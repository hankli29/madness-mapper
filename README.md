# MadnessMapper

Machine learning-powered NCAA basketball tournament matchup predictor with live odds integration and AI-generated matchup analysis.

**[Live Demo](https://madnessmapper.streamlit.app/)**

## About

MadnessMapper predicts likely winners of NCAA basketball tournament matchups using an XGBoost model trained on team-level efficiency metrics and historical betting market data. Users select two teams and get a winner prediction with confidence, plus a plain-language explanation generated from the model's underlying reasoning.

## Tech Stack

- **ML & Training:** Python, XGBoost, scikit-learn, MLflow
- **Web App:** Streamlit
- **External APIs:** The Odds API, Gemini API
- **Data Processing:** pandas

## How It Works

MadnessMapper builds training data from 14 years of historical NCAA tournament games, combining KenPom/Barttorvik team-level efficiency metrics with historical betting odds (moneyline, spread, totals). Training data is augmented with mirrored team orderings to prevent positional bias, then joined to odds via a hand-curated team name mapping.
The XGBoost classifier is trained with MLflow experiment tracking, achieving 73% accuracy across multiple random seeds. At inference, the app fetches live betting odds from The Odds API when available, combines them with current team statistics, and produces a winner prediction with confidence. A Gemini-generated explanation contextualizes the prediction using the statistical features that most influenced it.

## Run Locally

1. Clone the repository
```bash
git clone https://github.com/hankli29/madness-mapper.git
cd madness-mapper
```
2. Set up venv and install required dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Set up environment variables
```bash
# Requires a `.env` file with:
GEMINI_API_KEY=your_gemini_api_key
ODDS_API_KEY=your_odds_api_key
```
4. Run web app
```bash
streamlit run scripts/app.py
```

## Limitations

- Live odds are only available when The Odds API has the matchup listed, generally during the CBB season (November-April).
- Adding historical betting odds as features did not measurably improve accuracy over a stats-only baseline, likely because efficiency metrics already encode much of the same signal that drives betting lines.
- The model depends on historical tournament patterns, so unusual matchups, roster changes, injuries, or late-season context may not be fully captured.