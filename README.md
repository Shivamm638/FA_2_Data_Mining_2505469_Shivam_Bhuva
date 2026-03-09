# 🏦 ATM Intelligence Demand Forecasting with Data Mining

## 📌 Project Overview

This project analyzes ATM transaction data to identify patterns in cash withdrawals and deposits.  
Using **data mining techniques**, the system explores trends, groups ATMs based on demand behavior, and detects unusual withdrawal spikes.

The dashboard provides an **interactive data exploration tool** that helps decision-makers understand ATM usage and improve cash management strategies.

This project was developed for **Formative Assessment 2 (FA-2)** in the **Data Mining course**.

---

# 🌐 Live Application

The interactive dashboard can be accessed here:

🔗 **Web App Link:**  
**ADD YOUR WEBPAGE / STREAMLIT LINK HERE**

Example: https://fa2datamining.streamlit.app/

https://your-streamlit-app-link.streamlit.app

---

# 🎯 Project Objectives

The main objectives of this project are:

- Perform **Exploratory Data Analysis (EDA)** on ATM transaction data
- Identify trends in withdrawal behavior
- Group ATMs using **clustering techniques**
- Detect unusual withdrawal spikes using **anomaly detection**
- Build an **interactive Python dashboard** for data exploration

---

# 📊 Key Features

## 🔎 Exploratory Data Analysis (EDA)

The system includes several visualizations to understand ATM usage:

- Histogram of withdrawals and deposits
- Box plots for identifying outliers
- Withdrawals by day of the week
- Withdrawals by time of day
- Holiday and event impact analysis
- Weather condition impact on ATM usage
- Scatter plot of previous cash level vs next day demand
- Correlation heatmap of numeric features

These visualizations help identify patterns and relationships in the data.

---

## 🤖 ATM Clustering

ATMs are grouped using **K-Means clustering** based on transaction behavior.

Clusters help identify:

- **High-demand ATMs** – busy urban areas
- **Moderate-demand ATMs** – business districts
- **Low-demand ATMs** – residential or rural areas

The model uses:

- **Elbow Method** to determine optimal clusters
- **Silhouette Score** to evaluate cluster quality

---

## ⚠ Anomaly Detection

Unusual ATM withdrawal spikes are detected using:

### Z-Score Method
Identifies withdrawals that significantly deviate from normal values.

### Isolation Forest (Machine Learning)
Detects abnormal patterns in ATM transactions using an unsupervised learning algorithm.

These methods help identify unusual demand during:

- Holidays
- Festivals
- Special events
- Unexpected demand spikes

---

## 🎛 Interactive Dashboard

The dashboard allows users to filter and explore ATM data interactively.

Users can filter data by:

- Area
- Day of the week
- Time of day

The dashboard dynamically updates visualizations based on user selections.

---

# 📁 Project Structure
ATM_Project
│
├── atm_intelligence_planner.py
├── atm_data.csv
├── requirements.txt
└── README.md
---

# ⚙ Installation

Install all required libraries using:
pip install -r requirements.txt

---

# ▶ Running the Application

Run the dashboard using:

After running the command, open the link shown in the terminal (usually):

---

# 🧠 Technologies Used

This project was built using:

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- SciPy

---

# 📈 Dataset Description

The dataset contains ATM transaction information including:

- ATM ID
- Location / Area
- Total withdrawals
- Total deposits
- Day of week
- Time of day
- Holiday flag
- Special event flag
- Weather conditions
- Nearby competitor ATMs
- Previous day cash level
- Next day demand prediction

---

# 📌 Conclusion

This project demonstrates how **data mining techniques can transform raw financial transaction data into actionable insights**.

By combining **EDA, clustering, and anomaly detection**, the system provides valuable insights that can help financial institutions optimize ATM cash management.

---

# 👨‍💻 Author

**Student:** Shivam  
**Course:** Artificial Intelligence – Data Mining  
**Assessment:** Formative Assessment 2 (FA-2)
