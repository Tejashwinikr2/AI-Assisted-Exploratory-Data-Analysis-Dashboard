import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
from google import genai  # ✅ New official SDK import

# --------------------------------------------------------------------
# 🌐 Load environment variables and configure Gemini client
# --------------------------------------------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ Missing GEMINI_API_KEY in your .env file.")
else:
    # Create Gemini client (auto-picks up GEMINI_API_KEY)
    client = genai.Client(api_key=api_key)

# --------------------------------------------------------------------
# ⚙️ Streamlit Page Configuration
# --------------------------------------------------------------------
st.set_page_config(page_title="AI-EDA Dashboard", page_icon="🤖", layout="wide")
st.title("🤖 AI-Assisted Exploratory Data Analysis Dashboard")
st.markdown("Upload your dataset to explore it visually!")

# --------------------------------------------------------------------
# 📂 File Upload Section
# --------------------------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ----------------------------------------------------------------
    # 🧾 Dataset Preview and Summary
    # ----------------------------------------------------------------
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Summary")
    rows, cols = df.shape
    missing = df.isnull().sum().sum()
    st.write(f"**Rows:** {rows}, **Columns:** {cols}")
    st.write(f"**Total Missing Values:** {missing}")
    st.dataframe(df.describe())

    # ----------------------------------------------------------------
    # 🔥 Correlation Heatmap
    # ----------------------------------------------------------------
    numeric_df = df.select_dtypes(include=np.number)
    if not numeric_df.empty:
        corr = numeric_df.corr()
        st.subheader("🔥 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)

        # ------------------------------------------------------------
        # 🧩 Gemini Explanation Button
        # ------------------------------------------------------------
        if st.button("🧩 Explain Heatmap with Gemini"):
            st.subheader("📘 Gemini Explanation for the Heatmap")

            prompt = f"""
            You are a data visualization expert.
            Analyze this correlation heatmap summary:
            {corr.to_string(index=True)}
            Explain in simple, clear language what the chart indicates.
            Highlight strong or weak correlations, potential insights,
            and how these relationships could impact business or analysis decisions.
            """

            with st.spinner("🤖 Interpreting the heatmap using Gemini..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",  # ✅ latest model
                    contents=prompt
                )

            st.success("✅ Explanation Generated Successfully!")
            st.write(response.text)
    else:
        st.warning("⚠️ No numeric columns found for correlation heatmap.")
else:
    st.info("👈 Upload a CSV file to begin your analysis.")
