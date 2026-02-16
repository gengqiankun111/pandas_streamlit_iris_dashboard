
# iris_visualization.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import custom data processing module
from data_processing import load_and_preprocess_iris_data

# Set English font configuration (remove Chinese font settings)
# plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
# plt.rcParams["axes.unicode_minus"] = False  # Fix negative sign display issue

# ---------------------- 1. Page Basic Configuration ----------------------
st.set_page_config(
    page_title="Iris Dataset Analysis and Visualization",
    page_icon="🌸",
    layout="wide",  # Wide screen layout
    initial_sidebar_state="expanded"  # Sidebar expanded by default
)

# Page title
st.title("🌸 Iris Dataset Analysis and Visualization")
st.divider()  # Divider line

# ---------------------- 2. Call Data Processing Module to Load Data ----------------------
@st.cache_data  # Cache data to avoid repeated processing
def get_iris_data():
    """Call data processing function, encapsulate caching logic"""
    try:
        df, missing_values, duplicate_rows = load_and_preprocess_iris_data()
        return df, missing_values, duplicate_rows
    except Exception as e:
        st.error(e)
        return None, None, None

# Load data
df, missing_values, duplicate_rows = get_iris_data()

# Stop execution if data loading fails
if df is None:
    st.stop()

# ---------------------- 3. Display Basic Data Information ----------------------
st.subheader("📊 Basic Data Information")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Data Dimensions", f"{df.shape[0]} rows × {df.shape[1]} columns")

with col2:
    st.metric("Total Missing Values", missing_values.sum())

with col3:
    st.metric("Duplicate Count (Cleaned)", duplicate_rows)

# Display first 5 rows and descriptive statistics
tab1, tab2 = st.tabs(["Data Preview", "Descriptive Statistics"])
with tab1:
    st.dataframe(df.head(10), use_container_width=True)

with tab2:
    # Group statistics by flower species
    desc_stats = df.groupby("species").describe()
    st.dataframe(desc_stats, use_container_width=True)

st.divider()

# ---------------------- 4. Interactive Visualization ----------------------
st.subheader("🎨 Data Visualization Analysis")

# Sidebar filtering conditions
st.sidebar.header("🔍 Visualization Filters")
# Select features to analyze
features = df.columns.drop("species").tolist()
selected_x = st.sidebar.selectbox("X-axis Feature", features, index=0)
selected_y = st.sidebar.selectbox("Y-axis Feature", features, index=1)
# Choose whether to display legend
show_legend = st.sidebar.checkbox("Show Legend", value=True)

# Display visualization charts in columns
col1, col2 = st.columns(2)

# Chart 1: Scatter plot (classified by species)
with col1:
    st.subheader(f"{selected_x} vs {selected_y} Scatter Plot")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x=selected_x,
        y=selected_y,
        hue="species",
        palette="Set2",
        s=80,
        ax=ax,
        legend="auto" if show_legend else False
    )
    ax.set_xlabel(selected_x, fontsize=12)
    ax.set_ylabel(selected_y, fontsize=12)
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# Chart 2: Box plot (feature distribution by species)
with col2:
    st.subheader(f"{selected_x} Box Plot (by Species)")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
        data=df,
        x="species",
        y=selected_x,
        palette="Set2",
        ax=ax
    )
    ax.set_xlabel("Iris Species", fontsize=12)
    ax.set_ylabel(selected_x, fontsize=12)
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# Chart 3: Histogram (feature distribution)
st.subheader(f"{selected_x} Histogram (by Species)")
fig, ax = plt.subplots(figsize=(10, 5))
for species in df["species"].unique():
    sns.histplot(
        df[df["species"] == species][selected_x],
        label=species,
        alpha=0.6,
        bins=15,
        ax=ax
    )
ax.set_xlabel(selected_x, fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
if show_legend:
    ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

# Chart 4: Correlation heatmap
st.subheader("Feature Correlation Heatmap")
# Select only numeric features to calculate correlation
numeric_df = df.select_dtypes(include=["float64", "int64"])
corr = numeric_df.corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,  # Display correlation coefficient values
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    ax=ax,
    fmt=".2f"
)
ax.set_title("Feature Correlation Matrix", fontsize=12)
st.pyplot(fig)

# ---------------------- 5. Data Download ----------------------
st.divider()
st.subheader("💾 Data Download")
# Convert processed dataset to CSV format for download
csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Processed Iris Dataset",
    data=csv_data,
    file_name="iris_processed.csv",
    mime="text/csv"
)

# Footer
st.divider()
st.caption("Iris Dataset Analysis and Visualization Project | Built with Pandas + Streamlit")