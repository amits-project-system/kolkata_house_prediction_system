# 🏡 Kolkata House Price Prediction System

An end-to-end Machine Learning system designed to predict residential property prices in Kolkata, West Bengal. This project leverages historical real estate data, geographical features, and property specifications to deliver highly accurate price estimates for home buyers, sellers, and real estate agents.

## 🚀 Key Features
* **Precise Predictions:** Estimates property values based on location, square footage, configuration (BHK), and amenities.
* **Kolkata-Specific Metrics:** Custom encoding tailored to local property hot spots (e.g., Salt Lake, Newtown, Rajarhat, Garia, Tollygunge).
* **Interactive Web UI:** Simple, intuitive web interface built for quick user inputs and instantaneous price rendering.
* **Exploratory Data Analysis (EDA):** Detailed visualizations highlighting real estate trends, price-per-square-foot variations, and growth corridors in Kolkata.

## 📊 System Architecture
1. **Data Collection & Cleaning:** Outlier removal and handling missing local structural data.
2. **Feature Engineering:** Location clustering, price-per-sqft derivation, and categorical encoding for Kolkata neighborhoods.
3. **Model Training:** Comparative training using Linear Regression, Lasso/Ridge, Decision Trees, and Random Forest/XGBoost regressors.
4. **Deployment:** Model serialized via Pickle/Joblib and served through a lightweight web framework.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
* **Web Framework:** Streamlit 
* **Environment:** Jupyter Notebook / VS Code

## 📁 Repository Structure
```text
├── data/
│   ├── real_estate_properties.csv         # Original scraped/collected dataset
│   └── data.csv     # Cleaned data used for training
├── notebooks/
│   ├── house_prediction.ipynb     # Data visualization & insights
│   └── model_training          # Model selection and tuning
├── models/
│   └── model5.pkl          # Saved/serialized ML model
├── app/
│   ├── app.py                           # Web application code
│   
├── requirements.txt                     # List of dependencies
└── README.md                            # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git-clone https://github.com
   cd kolkata-house-price-prediction
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   * **If using Streamlit:**
     ```bash
     streamlit run app.py
     ```
  

## 📈 Future Enhancements
* Add distance mapping to major Kolkata transit hubs (Metro stations, Sealdah/Howrah stations).
* Incorporate real-time property data scraping from local real estate portals.
* Integrate deep learning models (ANNs) for improved accuracy on luxury premium segments.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
