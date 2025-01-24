import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="Water Pollution Dashboard", layout="wide")

# Apply dark mode using Streamlit's config and styling
st.markdown(
    """
    <style>
        .main {
            background-color: #222222;
            color: #f2f2f2;
        }
        .sidebar .sidebar-content {
            background-color: #333333;
            color: #f2f2f2;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            margin-top: 20px;
            color: #f2f2f2;
        }
        .subtitle {
            text-align: center;
            font-size: 1.5em;
            margin-bottom: 40px;
            color: #cccccc;
        }
        .eda-title {
            font-size: 2em;
            font-weight: normal;
        }
        .prediction-result {
            padding: 15px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-top: 20px;
            font-size: 1.2em;
        }
        .clean {
            background-color: #76c7c0;
        }
        .slightly-polluted {
            background-color: #ffcc00;
        }
        .polluted {
            background-color: #ff6f61;
        }
    </style>
    <div class="title">💧 WATER POLLUTION OF KLANG RIVER DASHBOARD 🌊</div>
    <div class="subtitle">Analysis and Prediction</div>
    """,
    unsafe_allow_html=True,
)

# Sidebar menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Water Pollution Prediction"])

if menu == "Home":
    st.markdown("<div class='eda-title'>Exploratory Data Analysis</div>", unsafe_allow_html=True)

    # Example data based on provided table
    data = {
        
        "NH3N": np.random.rand(100) * 10,
        "BOD": np.random.rand(100) * 10,
        "COD": np.random.rand(100) * 10,
        "DO": np.random.rand(100) * 10,
        "pH": np.random.uniform(6.5, 8.5, 100),
        "TSS": np.random.rand(100) * 100,
        "Col": np.random.rand(100) * 100,
        "EC": np.random.rand(100) * 500,
        "Floatables": np.random.rand(100) * 50,
        "Od": np.random.rand(100) * 5,
        "SAL": np.random.rand(100) * 35,
        "Taste": np.random.randint(0, 2, 100),  # 0 or 1
        "TDS": np.random.rand(100) * 200,
        "Temp": np.random.uniform(20, 35, 100),
        "Turb": np.random.rand(100) * 100,
        "FC": np.random.rand(100) * 1000,
        "TC": np.random.rand(100) * 5000,
        "WQC": np.random.choice([0, 1, 2], 100),  # 0=Clean, 1=Slightly Polluted, 2=Polluted
    }

    df = pd.DataFrame(data)

    st.write("### Klang River Data")
    st.dataframe(df.head())

    st.write("### Data Distribution")
    col1, col2 = st.columns(2)

    with col1:
        st.line_chart(df)

    with col2:
        st.bar_chart(df)

    st.write("### Select a Parameter for Visualization")
    column = st.selectbox("Select a parameter to visualize:", df.columns, key="visualize_param")

    col3, col4 = st.columns(2)

    with col3:
        st.write("#### Histogram")
        fig, ax = plt.subplots(facecolor="#333333")
        ax.hist(df[column], bins=10, color="#067c96", edgecolor="white")
        ax.set_title(f"Histogram of {column}", color="white")
        ax.set_xlabel(column, color="white")
        ax.set_ylabel("Frequency", color="white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        st.pyplot(fig)

    with col4:
        st.write("#### Skewness")
        skewness = df[column].skew()
        fig, ax = plt.subplots(facecolor="#333333")
        sns.kdeplot(df[column], ax=ax, color="#9c092b", fill=True)
        ax.set_title(f"Skewness Line of {column} (Skewness: {skewness:.2f})", color="white")
        ax.set_xlabel(column, color="white")
        ax.set_ylabel("Density", color="white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        st.pyplot(fig)

    st.write("### Scatter Plot and Box Plot")
    col5, col6 = st.columns([1, 1], gap="medium")

    with col5:
        st.write("#### Scatter Plot")
        y_axis = st.selectbox("Select Y-axis parameter:", df.columns, key="scatter_y")
        fig, ax = plt.subplots(facecolor="#333333")
        ax.scatter(df[column], df[y_axis], color="#5e0358", alpha=0.7, edgecolor="white")
        ax.set_title(f"Scatter Plot of {column} vs {y_axis}", color="white")
        ax.set_xlabel(column, color="white")
        ax.set_ylabel(y_axis, color="white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        st.pyplot(fig)

    with col6:
        st.write("#### Box Plot")
        st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
        fig, ax = plt.subplots(facecolor="#333333")
        ax.boxplot(df[column], patch_artist=True, boxprops=dict(facecolor="#51136e", color="white"))
        ax.set_title(f"Box Plot of {column}", color="white")
        ax.set_ylabel(column, color="white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        st.pyplot(fig)

    st.write("### Pollution Distribution of Klang River")
    col7, _ = st.columns([1, 1])
    with col7:
        pollution_data = [20, 50, 30]  # Example percentages for Clean, Slightly Polluted, and Polluted
        pollution_labels = ["Clean", "Slightly Polluted", "Polluted"]
        colors = ["#76c7c0", "#ffcc00", "#ff6f61"]
        fig, ax = plt.subplots(facecolor="#333333")
        ax.pie(
            pollution_data,
            labels=pollution_labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            textprops={"color": "white"},
        )
        ax.set_title("Pollution Rate of Klang River", color="white")
        st.pyplot(fig)

elif menu == "Water Pollution Prediction":
    st.title("Water Pollution Prediction")

    st.write("Enter the values for the following parameters:")

    col1, col2, col3 = st.columns(3)
    with col1:
        nh3n = st.number_input("NH3N (mg/L):", min_value=0.0, step=0.1)
        cod = st.number_input("COD (mg/L):", min_value=0.0, step=0.1)
    with col2:
        bod = st.number_input("BOD (mg/L):", min_value=0.0, step=0.1)
        do = st.number_input("DO (mg/L):", min_value=0.0, step=0.1)
    with col3:
        ph = st.number_input("pH:", min_value=0.0, step=0.1)
        tss = st.number_input("TSS (mg/L):", min_value=0.0, step=0.1)

    if st.button("Predict"):
        # Dummy prediction logic
        prediction = "Clean" if nh3n < 3 and bod < 3 else ("Slightly Polluted" if nh3n < 6 else "Polluted")
        color_class = "clean" if prediction == "Clean" else ("slightly-polluted" if prediction == "Slightly Polluted" else "polluted")
        st.markdown(
            f"""
            <div class="prediction-result {color_class}">
                Prediction: <b>{prediction}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )
