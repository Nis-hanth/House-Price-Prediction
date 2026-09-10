# 🏠 House Price Prediction Using Linear Regression

## 📌 Project Overview

This project predicts house prices using the **Linear Regression Machine Learning algorithm**.

The model is trained using different house-related features such as overall quality, living area, garage capacity, basement area, year built, bathrooms, bedrooms, and lot area.

A **Streamlit web application** is also developed to allow users to enter house details and get a predicted house price.

---

## 🚀 Features

* 📊 Data Analysis and Visualization
* 🧹 Missing Value Checking
* 🔍 Exploratory Data Analysis (EDA)
* 🎯 Feature and Target Selection
* ✂️ Train-Test Split
* 🤖 Linear Regression Model
* 📈 Model Evaluation
* 💾 Model Saving using Pickle
* 🌐 Interactive Streamlit Web Application
* 🏠 House Price Prediction

---

## 🧠 Machine Learning Workflow

```text
House Price Dataset
        ↓
Understand Dataset
        ↓
Check Missing Values
        ↓
EDA / Visualization
        ↓
Remove Unnecessary Columns
        ↓
Select Features (X)
        ↓
Select Target (y)
        ↓
Train-Test Split
        ↓
Linear Regression
        ↓
Model Evaluation
        ↓
MAE / MSE / RMSE / R² Score
        ↓
Save Model using Pickle
        ↓
Streamlit Web Application
        ↓
House Price Prediction
```

---

## 📂 Dataset Features

The dataset contains the following features:

| Feature      | Description                         |
| ------------ | ----------------------------------- |
| OverallQual  | Overall material and finish quality |
| GrLivArea    | Above ground living area            |
| GarageCars   | Garage capacity                     |
| TotalBsmtSF  | Total basement area                 |
| YearBuilt    | Year the house was built            |
| FullBath     | Number of full bathrooms            |
| BedroomAbvGr | Number of bedrooms above ground     |
| LotArea      | Total lot size                      |
| SalePrice    | Target variable – House Sale Price  |

---

## 🤖 Machine Learning Model

The project uses:

**Linear Regression**

```python
model = LinearRegression()
```

Linear Regression is used because the target variable `SalePrice` is a continuous numerical value.

---

## 📊 Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🌐 Streamlit Application

The Streamlit application allows users to enter house details such as:

* Overall Quality
* Living Area
* Garage Capacity
* Basement Area
* Year Built
* Number of Bathrooms
* Number of Bedrooms
* Lot Area

After entering the details, the trained model predicts the estimated house price.

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── house_prediction_sys.ipynb
├── house_prices_practice.csv
├── Hose_price_model.pkl
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle
* Jupyter Notebook

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nis-hanth/House-Price-Prediction.git
```

Go to the project folder:

```bash
cd House-Price-Prediction
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

---

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📌 Project Files

* `app.py` – Streamlit application
* `house_prediction_sys.ipynb` – Data analysis and model training
* `house_prices_practice.csv` – Dataset
* `Hose_price_model.pkl` – Trained Linear Regression model

---

## 🎯 Future Improvements

* Add more house features
* Improve the dataset
* Compare multiple regression algorithms
* Add model performance visualization
* Deploy the Streamlit application online

---

## 👨‍💻 Author

**Nishanth**

BCA Graduate | Aspiring Data Scientist

---

⭐ If you like this project, please consider giving it a star!
