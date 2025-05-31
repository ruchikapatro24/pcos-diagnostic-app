# PCOS Diagnostic App

A simple Streamlit web app that predicts the likelihood of **Polycystic Ovary Syndrome (PCOS)** using a trained machine learning model.

## Features

- Upload patient data through sliders and inputs
- Predicts whether PCOS is likely
- Built using Streamlit and a trained RandomForest model
- Clean UI and fast response

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Joblib
- Jupyter Notebook (for model training)

## How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ruchikapatro24/pcos-diagnostic-app.git
   cd pcos-diagnostic-app
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the app**:
   ```bash
   streamlit run app.py
## Model Training

The model was trained in this notebook: [`PCOS_Diagnostic_Project.ipynb`](./PCOS_Diagnostic_Project.ipynb), using real-world PCOS diagnostic datasets with appropriate preprocessing and EDA.
## License

This project is open source and available under the [MIT License](LICENSE).
