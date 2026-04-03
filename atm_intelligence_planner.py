# ==============================
# 🚀 ATM AI FINAL DASHBOARD (ALL-IN-ONE FILE)
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression

from datetime import timedelta
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ==============================
# ⚙️ PAGE CONFIG
# ==============================
st.set_page_config(layout="wide", page_title="ATM AI Dashboard")

# ==============================
# 🎨 STYLING
# ==============================
st.markdown("""
<style>
body { background-color: #0f172a; color: white; }
.block-container { animation: fadeIn 0.8s ease-in; }
@keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

st.title("🏦 ATM AI Dashboard - FINAL VERSION")

# ==============================
# 📂 LOAD DATA (SAFE)
# ==============================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("atm_data_200.csv")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.dropna(inplace=True)
        return df
    except:
        st.error("❌ File 'atm_data_200.csv' not found. Please keep it in same folder.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# ==============================
# 🌍 API SIMULATION
# ==============================
st.header("🌍 Live Bank API Simulation")

if st.button("Fetch Live Data"):
    st.dataframe(df.sample(min(10, len(df))))

# ==============================
# 📊 KPIs
# ==============================
st.header("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Withdrawals", int(df["Total_Withdrawals"].sum()))
col2.metric("Average Withdrawals", int(df["Total_Withdrawals"].mean()))
col3.metric("Max Withdrawals", int(df["Total_Withdrawals"].max()))

# ==============================
# 📈 EDA
# ==============================
st.header("📊 Exploratory Data Analysis")

st.plotly_chart(px.histogram(df, x="Total_Withdrawals"), use_container_width=True)
st.plotly_chart(px.box(df, y="Total_Withdrawals"), use_container_width=True)

# ==============================
# 🗺️ HEATMAP
# ==============================
st.header("🗺️ ATM Location Heatmap")

coords = {
    "Navrangpura": (23.03,72.56),
    "Satellite": (23.02,72.51),
    "Maninagar": (22.99,72.60),
    "Bopal": (23.03,72.47),
    "Vastrapur": (23.04,72.53),
    "Chandkheda": (23.11,72.58),
    "SG Highway": (23.07,72.52),
    "Ellisbridge": (23.02,72.57),
    "Gota": (23.09,72.54),
    "Thaltej": (23.05,72.50)
}

df["lat"] = df["Area"].map(lambda x: coords.get(x, (np.nan, np.nan))[0])
df["lon"] = df["Area"].map(lambda x: coords.get(x, (np.nan, np.nan))[1])

map_df = df.dropna(subset=["lat", "lon"])

st.plotly_chart(
    px.scatter_mapbox(
        map_df,
        lat="lat",
        lon="lon",
        size="Total_Withdrawals",
        color="Total_Withdrawals",
        mapbox_style="open-street-map",
        zoom=10
    ),
    use_container_width=True
)

# ==============================
# 🤖 CLUSTERING
# ==============================
st.header("🤖 ATM Segmentation (Clustering)")

features = ["Total_Withdrawals","Total_Deposits","Nearby_Competitor_ATMs"]
X = df[features]

scaled = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df["Cluster"] = kmeans.fit_predict(scaled)

means = df.groupby("Cluster")["Total_Withdrawals"].mean().sort_values()
labels = {
    means.index[0]:"Low",
    means.index[1]:"Medium",
    means.index[2]:"High"
}

df["Cluster_Label"] = df["Cluster"].map(labels)

st.plotly_chart(
    px.scatter(df, x="Total_Withdrawals", y="Total_Deposits", color="Cluster_Label"),
    use_container_width=True
)

# ==============================
# ⚠️ ANOMALY DETECTION
# ==============================
st.header("⚠️ Anomaly Detection")

iso = IsolationForest(contamination=0.05, random_state=42)
df["Anomaly"] = iso.fit_predict(X)

st.plotly_chart(
    px.scatter(df, x="Total_Withdrawals", y="Total_Deposits",
               color=df["Anomaly"].astype(str)),
    use_container_width=True
)

# ==============================
# 💰 SALARY SIMULATION
# ==============================
st.header("💰 Salary Day Simulation")

salary_day = st.slider("Select Salary Day", 1, 31, 1)

df["Simulated"] = df["Total_Withdrawals"]
df.loc[df["Date"].dt.day == salary_day, "Simulated"] *= 1.5

st.plotly_chart(
    px.line(df.sort_values("Date"), x="Date", y="Simulated"),
    use_container_width=True
)

# ==============================
# 📈 ML PREDICTION
# ==============================
st.header("📈 Cash Demand Prediction")

model = LinearRegression()
model.fit(X, df["Cash_Demand_Next_Day"])

df["Predicted"] = model.predict(X)

st.plotly_chart(
    px.scatter(df, x="Cash_Demand_Next_Day", y="Predicted"),
    use_container_width=True
)

# ==============================
# 📊 FORECAST
# ==============================
st.header("📊 7-Day Forecast")

ts = df.groupby("Date")["Total_Withdrawals"].sum().reset_index()
ts = ts.sort_values("Date")

ts["lag1"] = ts["Total_Withdrawals"].shift(1)
ts.dropna(inplace=True)

model_ts = LinearRegression()
model_ts.fit(ts[["lag1"]], ts["Total_Withdrawals"])

future = []
last_val = ts.iloc[-1]["Total_Withdrawals"]

for _ in range(7):
    pred = model_ts.predict([[last_val]])[0]
    future.append(pred)
    last_val = pred

future_dates = [ts["Date"].max() + timedelta(days=i+1) for i in range(7)]

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Forecast": future
})

st.plotly_chart(
    px.line(forecast_df, x="Date", y="Forecast"),
    use_container_width=True
)

# ==============================
# 📄 PDF GENERATION
# ==============================
st.header("📄 Generate Report")

def create_pdf():
    doc = SimpleDocTemplate("ATM_Report.pdf")
    styles = getSampleStyleSheet()
    content = [
        Paragraph("ATM AI Dashboard Report", styles['Title']),
        Paragraph("Auto-generated summary of ATM performance.", styles['BodyText'])
    ]
    doc.build(content)

if st.button("Generate PDF"):
    create_pdf()
    st.success("✅ PDF Generated Successfully!")

# ==============================
# 📥 DOWNLOAD
# ==============================
st.download_button(
    "Download Processed Data",
    df.to_csv(index=False),
    "atm_final_output.csv"
)

st.success("🚀 DASHBOARD READY!")
