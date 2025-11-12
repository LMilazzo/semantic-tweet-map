import ast
import streamlit as st
import pandas as pd
import plotly.express as px

# Simple Streamlit + Plotly app to view 2D embeddings from
# `posts_embedded_mapped.csv`
CSV_PATH = "posts_embedded_mapped.csv"

# === DataFrame Sampling ===
def sample_posts(df, val_col="lab", n=50):
    trump_sample = df[df[val_col] == "Trump"].sample(n=n)
    biden_sample = df[df[val_col] == "Biden"].sample(n=n)
    return pd.concat([trump_sample, biden_sample]).reset_index(drop=True)

# === PLOT FUNCTION ===
def default_plot(data):
    fig = px.scatter(data, x="x", y="y", color="lab", 
                 title="", template="plotly_dark",
                 custom_data=["lab", "wrapped_text"],
                 color_discrete_map={"Trump" : "#E74C3C", "Biden" : "#3498DB"})

    fig.update_layout(legend_title_text="Political Figure", xaxis_title="", yaxis_title="")
    fig.update_traces(hovertemplate="%{customdata[0]}<br><br>%{customdata[1]}<extra></extra>")
    return fig

# =============================================================================================================

def main():
    st.set_page_config(page_title="Semantic Text Embedding Visualization Demo", layout="wide")
    st.title("Exploring Semantic Text Mapping Through Political Tweets")

    left, center, right = st.columns([1, 6, 1])

    with center:
        # Controls above the plot
        col_reload, col_num, empty = st.columns([1, 2, 4])
        with col_reload:
            if st.button("New Data"):
                pass

        with col_num:
            n_obs = st.number_input(
                "Observations per person",
                min_value=1,
                max_value=2000,
                value=1000,
                step=10
            )

        # Load data and sample
        df = pd.read_csv(CSV_PATH)

        # Plot
        fig = default_plot(sample_posts(df, n=n_obs))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            f"<small>Showing {n_obs * 2:,} observations (of {len(df):,}) — data from "
            "<a href='https://www.kaggle.com/datasets/muhammetakkurt/trump-2024-campaign-truthsocial-truths-tweets'>Donald Trump Truth Social Dataset</a> "
            "and <a href='https://www.kaggle.com/datasets/thedevastator/uncovering-joe-biden-s-message-through-social-me'>Joe Biden Tweets Dataset</a></small>",
            unsafe_allow_html=True
        )
        st.markdown(f"<small>Transformer Model: <a href='https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2'>all-MiniLM-L6-v2</a>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
