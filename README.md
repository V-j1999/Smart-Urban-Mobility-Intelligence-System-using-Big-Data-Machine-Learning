**# Smart-Urban-Mobility-Intelligence-System-using-Big-Data-Machine-Learning**
Developed an end-to-end Big Data analytics and machine learning system using real-world NYC Taxi trip data to analyze urban mobility patterns and predict transportation demand. 
## 📌 Overview
This project builds an end-to-end Big Data analytics and machine learning system using real-world NYC Taxi trip data.

It analyzes urban mobility patterns and predicts transportation demand using scalable data processing and predictive modeling techniques.

---

## 🎯 Objectives
- Analyze taxi demand patterns across time
- Identify peak hours and high-demand zones
- Build a machine learning model to predict demand
- Deploy an interactive web application

---

## 🛠 Tech Stack
- Python (Pandas, NumPy)
- PySpark (Big Data Processing)
- Scikit-learn (Machine Learning)
- Streamlit (Deployment)
- SQL

---

## 📊 Features
- 🚕 Demand analysis by hour & day
- 📈 Predictive ML model (Random Forest)
- ⚡ PySpark pipeline for large-scale data
- 🌐 Interactive Streamlit dashboard

---

## 🧠 Machine Learning Model
- Model: Random Forest Regressor  
- Input Features: Hour, Day  
- Output: Predicted Taxi Demand



---

## 📁 Project Structure :

NYC-Taxi-Smart-Mobility/
│
├── data/
│ ├── raw/ # Original NYC taxi dataset (not uploaded)
│ ├── processed/ # Cleaned & aggregated data
│ └── map_data/ # Latitude/Longitude data for heatmap
│
├── pyspark/
│ └── pipeline.py # Big Data processing using PySpark
│
├── ml/
│ ├── train_model.py # ML model training script
│ └── model.pkl # Saved trained model (ignored in Git)
│
├── app/
│ └── streamlit_app.py # Interactive dashboard & prediction app
│
├── utils/
│ └── preprocess.py # Data cleaning functions
│
├── notebooks/
│ ├── eda.ipynb # Exploratory Data Analysis
│ └── feature_engineering.ipynb # Feature creation experiments
│
├── requirements.txt # Project dependencies
├── .gitignore # Ignore large files (data, models)
└── README.md # Project documentation

📌 Note: Large datasets and trained models are excluded from the repository using .gitignore.

            ┌────────────────────────────┐
            │   NYC Taxi Raw Dataset     │
            │  (Parquet / Large Files)   │
            └────────────┬───────────────┘
                         │
                         ▼
            ┌────────────────────────────┐
            │     PySpark Pipeline       │
            │  (Data Cleaning + ETL)     │
            └────────────┬───────────────┘
                         │
                         ▼
            ┌────────────────────────────┐
            │   Processed Data (CSV)     │
            │  Hour, Day, Demand, Geo    │
            └────────────┬───────────────┘
                         │
    ┌────────────────────┼────────────────────┐
    ▼                    ▼                    ▼
┌───────────────┐ ┌────────────────┐ ┌────────────────────┐
│ ML Model │ │ Streamlit App │ │ Map Visualization │
│ (RandomForest)│ │ Dashboard UI │ │ (PyDeck Heatmap) │
└──────┬────────┘ └────────┬───────┘ └────────┬───────────┘
│ │ │
▼ ▼ ▼
┌────────────────────────────────────────────────────────────┐
│ 🚕 Demand Prediction & Business Insights │
└────────────────────────────────────────────────────────────┘


---

## 🔄 Data Pipeline Workflow

```markdown id="1r5l91"
## 🔄 Workflow

1. 📥 Data Ingestion  
   - Load raw NYC Taxi dataset (Parquet format)

2. ⚙️ Data Processing (PySpark)  
   - Clean data  
   - Extract features (hour, day)  
   - Aggregate demand  

3. 🧠 Feature Engineering  
   - Time-based features  
   - Demand grouping  

4. 🤖 Machine Learning  
   - Train Random Forest model  
   - Predict taxi demand  

5. 🌐 Deployment  
   - Streamlit app for real-time predictions  
   - Interactive dashboard  

6. 🗺️ Visualization  
   - Heatmap of taxi demand (Uber-style)  
   - Time-based trend analysis

## 📊 Key Features

- 🚕 Demand analysis by hour & weekday  
- 🤖 Machine Learning-based demand prediction  
- ⚡ Scalable PySpark data pipeline  
- 🗺️ Geospatial heatmap visualization (Uber-style)  
- 📈 Interactive Streamlit dashboard  
- 📊 Real-time prediction interface


## 🎯 End-to-End Pipeline

Raw Data → PySpark Processing → Feature Engineering → ML Model → Streamlit App → Visualization → Business Insights



