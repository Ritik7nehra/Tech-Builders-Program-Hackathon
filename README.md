# PowerOpt AI: NextGen Power Predictor ⚡

[Combined Cycle Power Plant]

**PowerOpt AI** is a cutting-edge, machine-learning-powered web dashboard designed to predict the electrical energy output of a Combined Cycle Power Plant (CCPP) in real-time. Built specifically for the  insights and analysis, this project takes raw sensor data and transforms it into actionable insights to help grid operators optimize power dispatch and reduce operational waste.

---

## ✨ Key Features

1. **Real-Time Prediction Engine:** Input live environmental parameters (Temperature, Vacuum, Pressure, Humidity) and instantly receive high-accuracy energy output predictions.
2. **AI-Native Dashboard:** A stunning, modern UI built with Glassmorphism aesthetics, featuring interactive data visualizations and smooth micro-animations.
3. **Comprehensive Analytics:** Deep dive into the dataset with automated exploratory data analysis, showing feature correlations and historical ranges.
4. **Model Transparency:** A dedicated view to evaluate the performance of 5 different regression models, highlighting the production deployment of the Random Forest Regressor.
5. **Dynamic Visualizations:** Dual-chart system including a line chart for tracking prediction trends and a bar chart for current parameter distribution.

---

## 🧠 Machine Learning Architecture

The prediction engine relies on a highly optimized **Random Forest Regressor** built with Scikit-Learn.

- **Dataset:** 9,568 data points collected over 6 years (2006-2011) when the plant was operating under full load.
- **Features Evaluated:**
  - `T`: Ambient Temperature (°C)
  - `AP`: Ambient Pressure (mbar)
  - `RH`: Relative Humidity (%)
  - `V`: Exhaust Vacuum (cm Hg)
- **Target Variable:** `PE`: Electrical Energy Output (MW)
- **Production Model Accuracy:** **96.16% R² Score**

Other models evaluated during the research phase include Multiple Linear Regression (93.25%), Polynomial Regression (94.58%), Support Vector Regression (94.80%), and Decision Tree Regression (92.28%).

---

## 💻 Tech Stack

- **Backend:** Python, Flask, Scikit-Learn, Joblib, Pandas, NumPy
- **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism), Vanilla JavaScript, Chart.js, Lucide Icons

---

## 🚀 Installation & Setup

Follow these steps to run the PowerOpt AI dashboard locally on your machine.

### Prerequisites
- Python 3.8+
- `pip` package manager

### 1. Clone the Repository
Extract the `TechBuilder_PowerOpt_Project.zip` file or clone this repository, then navigate into the project directory:
```bash
cd Combined-Cycle-Power-Plant_Regs-main
```

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install flask scikit-learn pandas numpy joblib
```

### 3. (Optional) Retrain the Model
If you want to train the model from scratch using the provided `Data.csv`:
```bash
python train_model.py
```
*This will generate a new `rf_model.joblib` file in your root directory.*

### 4. Start the Application
Boot up the Flask web server:
```bash
python app.py
```

### 5. Access the Dashboard
Open your web browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 📊 Practical Application

This solution has direct real-world application in the **Energy, Sustainability, and Climate Technology** sectors. By providing operators with highly accurate output forecasts based on atmospheric conditions, plants can:
- Avoid the economic penalties of under-generation or over-generation.
- Dynamically adjust supplementary power sources to maintain grid stability.
- Maximize fuel efficiency, subsequently reducing greenhouse gas emissions.

---

## 👥 Contributors

- **Ritik Nehra** ([@Ritik7nehra](https://github.com/Ritik7nehra)) - Lead Developer & AI Engineer

*Created for the Tech Builder Program Hackathon 2026. Dataset provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/).*
