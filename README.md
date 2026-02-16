Pandas & Streamlit CSV Data Analysis Dashboard
A production-ready, end-to-end Python project for professional CSV data processing and interactive visualization. Built with the Iris dataset as a demo, this project follows industry-standard modular architecture and is optimized for rapid customization to client-specific CSV analytics needs (sales, user behavior, finance, survey data, etc.).

✨ Core Features
Modular Code Architecture: Clean separation of data processing and visualization layers – scalable for enterprise-grade projects.

Robust Data Handling: Automated online CSV loading, missing value detection, and duplicate record removal.

Interactive Visualizations: Dynamic scatter plots, boxplots, histograms, and correlation heatmaps.

Customizable Dashboard: Streamlit interface with sidebar filters for real-time data exploration.

Production-Ready: Structured codebase with error handling, caching, and cross‑platform compatibility.

Easy Customization: Adaptable to any CSV dataset with minimal code changes – no front‑end development skills required.

🛠️ Environment Setup
Option 1: Python Native venv (Recommended)
Works on Windows, macOS, and Linux with no additional software required.

Clone the repository

bash
git clone https://github.com/GengQiankun087/pandas_streamlit_iris_dashboard.git
cd your-repo-name
Create and activate a virtual environment

bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt

# Optional: Upgrade pip if installation fails
pip install --upgrade pip
Run the dashboard

bash
streamlit run iris_visualization.py
Option 2: Conda Environment (Alternative)
For data science workflows using Anaconda/Miniconda:

Create the Conda environment

bash
conda env create -f environment.yml
Activate the environment

bash
conda activate iris-dashboard
Launch the app

bash
streamlit run iris_visualization.py