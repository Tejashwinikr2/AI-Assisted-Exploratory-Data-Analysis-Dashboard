import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
from google import genai  
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Missing GEMINI_API_KEY in your .env file.")
else:
    client = genai.Client(api_key=api_key)

st.set_page_config(page_title="AI-EDA Dashboard", page_icon="🤖", layout="wide")
st.title("AI-Assisted Exploratory Data Analysis Dashboard")
st.markdown("Upload your dataset to explore it visually!")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary")
    rows, cols = df.shape
    missing = df.isnull().sum().sum()
    st.write(f"**Rows:** {rows}, **Columns:** {cols}")
    st.write(f"**Total Missing Values:** {missing}")
    st.dataframe(df.describe())

    numeric_df = df.select_dtypes(include=np.number)
    if not numeric_df.empty:
        corr = numeric_df.corr()
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)
        if st.button("Explain Heatmap with Gemini"):
            st.subheader("Gemini Explanation for the Heatmap")

            prompt = f"""
            You are a data visualization expert.
            Analyze this correlation heatmap summary:
            {corr.to_string(index=True)}
            Explain in simple, clear language what the chart indicates.
            Highlight strong or weak correlations, potential insights,
            and how these relationships could impact business or analysis decisions.
            """

            with st.spinner("Interpreting the heatmap using Gemini..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=prompt
                )

            st.success("Explanation Generated Successfully!")
            st.write(response.text)
    else:
        st.warning("No numeric columns found for correlation heatmap.")
else:
    st.info("Upload a CSV file to begin your analysis.")
if uploaded_file is not None:
    language = st.selectbox("Choose explanation language", ["English", "Hindi", "Kannada", "Telugu"])
    lang_map = {"English": "English", "Hindi": "Hindi", "Kannada": "Kannada", "Telugu": "Telugu"}
    if 'df' in locals():
        numeric_df = df.select_dtypes(include=np.number)
        if not numeric_df.empty:
            if st.button("Explain Heatmap with Gemini (Multilingual)"):
                with st.spinner("Generating explanation..."):
                    prompt = f"You are a data visualization expert. Analyze this correlation matrix and explain in {lang_map[language]} in simple, clear language what the main relationships are, highlighting strong positive or negative correlations, weak or near-zero relationships, and practical implications for analysis or business decisions. Provide actionable suggestions where appropriate.\n\nCorrelation matrix:\n{corr.to_string(index=True)}\n\nRespond only in {lang_map[language]}."
                    try:
                        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                        text = getattr(response, "text", None) or response
                        st.subheader(f"Gemini explanation ({language})")
                        st.write(text)
                    except Exception as e:
                        st.error(f"Failed to generate explanation: {e}")
            if st.button("Explain Dataset Summary with Gemini (Multilingual)"):
                with st.spinner("Generating dataset summary..."):
                    top_corr_pairs = []
                    num = numeric_df
                    if num.shape[1] >= 2:
                        abs_corr = num.corr().abs()
                        abs_corr.values[np.triu_indices_from(abs_corr.values)] = np.nan
                        flat = abs_corr.unstack().dropna().sort_values(ascending=False)
                        for idx, val in flat.head(5).items():
                            a, b = idx
                            top_corr_pairs.append((a, b, float(val)))
                    summary_text = f"Rows: {rows}, Columns: {cols}, Total missing values: {missing}\n\nTop numeric columns summary:\n{numeric_df.describe().transpose().head(10).to_string()}\n\nTop correlation pairs:\n"
                    for a, b, v in top_corr_pairs:
                        summary_text += f"{a} <> {b}: {round(v,2)}\n"
                    prompt = f"You are a data analyst. In {lang_map[language]}, provide a concise, user-friendly summary of the dataset below, call out any data quality issues, key numeric summaries, important correlations, and recommended next steps for preprocessing or modeling. Keep bullets short and actionable.\n\nDataset summary:\n{summary_text}\n\nRespond only in {lang_map[language]}."
                    try:
                        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                        text = getattr(response, "text", None) or response
                        st.subheader(f"Gemini dataset summary ({language})")
                        st.write(text)
                    except Exception as e:
                        st.error(f"Failed to generate summary: {e}")
        else:
            st.warning("No numeric columns found for multilingual explanations.")
if uploaded_file is not None:
    if 'df' in locals():
        numeric_df = df.select_dtypes(include=np.number)
        if not numeric_df.empty:
            if st.checkbox("Auto-generate charts (histograms & box plots)"):
                st.subheader("Auto-generated Histograms")
                for col in numeric_df.columns:
                    data = numeric_df[col].dropna()
                    if data.empty:
                        continue
                    fig, ax = plt.subplots()
                    try:
                        sns.histplot(data, kde=True, ax=ax)
                    except Exception:
                        ax.hist(data)
                    ax.set_title(f"Histogram: {col}")
                    st.pyplot(fig)
                st.subheader("Auto-generated Box Plots")
                for col in numeric_df.columns:
                    data = numeric_df[col].dropna()
                    if data.empty:
                        continue
                    fig, ax = plt.subplots()
                    try:
                        sns.boxplot(x=data, ax=ax)
                    except Exception:
                        ax.boxplot(data)
                    ax.set_title(f"Box plot: {col}")
                    st.pyplot(fig)
        else:
            st.info("No numeric columns available for auto-generated charts.")
