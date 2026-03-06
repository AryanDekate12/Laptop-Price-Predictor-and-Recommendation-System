import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained files
model = pickle.load(open("model.pkl","rb"))
encoders = pickle.load(open("encoders.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

# Load dataset
data = pd.read_csv("dataset.csv")

st.title("💻 AI Laptop Price Predictor")

# -------------------------
# BRAND SELECTION
# -------------------------

brand = st.selectbox(
"Select Brand",
sorted(data["Company"].unique())
)

brand_data = data[data["Company"]==brand]

# -------------------------
# MODEL SELECTION
# -------------------------

model_name = st.selectbox(
"Select Laptop Model",
brand_data["LaptopName"].unique()
)

selected = brand_data[brand_data["LaptopName"]==model_name].iloc[0]

st.subheader("Laptop Configuration")

cpu = st.selectbox(
"CPU",
sorted(data["CPU"].unique()),
index=list(sorted(data["CPU"].unique())).index(selected["CPU"])
)

gpu = st.selectbox(
"GPU",
sorted(data["GPU"].unique()),
index=list(sorted(data["GPU"].unique())).index(selected["GPU"])
)

os = st.selectbox(
"Operating System",
sorted(data["OS"].unique()),
index=list(sorted(data["OS"].unique())).index(selected["OS"])
)

ram_options = [8,16,32]

ram = st.selectbox(
"RAM",
ram_options,
index=ram_options.index(selected["RAM"])
)

ssd_options = [256,512,1024]

ssd = st.selectbox(
"SSD",
ssd_options,
index=ssd_options.index(selected["SSD"])
)

hdd_options = [0,500,1000]

hdd = st.selectbox(
"HDD",
hdd_options,
index=hdd_options.index(selected["HDD"])
)

screen_options = [13.3,14,15.6,16,17]

screen = st.selectbox(
"Screen Size",
screen_options,
index=screen_options.index(selected["ScreenSize"])
)

weight = st.slider(
"Weight",
1.0,
3.0,
float(selected["Weight"])
)

# -------------------------
# PRICE PREDICTION
# -------------------------

if st.button("Predict Price"):

    company_val = encoders["Company"].transform([brand])[0]
    cpu_val = encoders["CPU"].transform([cpu])[0]
    gpu_val = encoders["GPU"].transform([gpu])[0]
    os_val = encoders["OS"].transform([os])[0]

    features = np.array([[company_val,ram,ssd,hdd,cpu_val,gpu_val,screen,weight,os_val]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    st.success(f"Estimated Price ₹{int(prediction[0])}")

# -------------------------
# BUDGET RECOMMENDER
# -------------------------

st.divider()

st.header("💰 Best Laptop Under Budget")

budget = st.slider(
"Select Budget",
30000,
200000,
60000,
5000
)

filtered = data[data["Price"]<=budget]

filtered = filtered.sort_values(by="Price")

if st.button("Recommend Laptops"):

    if len(filtered)==0:

        st.warning("No laptops found.")

    else:

        st.subheader("Top Laptops Within Budget")

        for i,row in filtered.head(5).iterrows():

            st.write(
            f"💻 {row['LaptopName']} — ₹{row['Price']}"
            )