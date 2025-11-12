# TransformerVisualization — Streamlit demo

Simple Streamlit app to visualize 2D text embeddings from `posts_embedded_mapped.csv` using Plotly.

## What this project contains
- `app.py` — Streamlit application. Loads `posts_embedded_mapped.csv`, lets you choose number of observations (capped at 2000), and displays an interactive Plotly scatter of the `x`/`y` coordinates.
- `posts_embedded_mapped.csv` — data file with text, embedding coordinates, labels, and other metadata used by the app.

## Expected CSV layout
The app expects `posts_embedded_mapped.csv` in the project root. Typical columns used by the app include:
- `x` — x-coordinate (float)
- `y` — y-coordinate (float)
- `lab` — label/category (e.g., `Trump`, `Biden`)
- `wrapped_text` — shorter/HTML-wrapped version of the text for hover
- `text` — original full text (optional)
- `date` — date string (optional)
- `embs` — raw embedding list as a string (optional)

The CSV in this repository includes an index column in column 0 which the app reads as the DataFrame index.

## Requirements
- Python 3.8+
- Packages: streamlit, pandas, plotly