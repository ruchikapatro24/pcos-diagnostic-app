# PCOS Diagnostic App

A simple Streamlit web app that predicts the likelihood of **Polycystic Ovary Syndrome (PCOS)** using a trained machine learning model.
## Live Demo

Try out the app live on Streamlit Cloud:

[PCOS Diagnostic App - Live Demo](https://pcos-diagnostic-app-zqodvfwmu9kij4u8n5zk72.streamlit.app/)
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
## Dataset

The dataset used in this project is available on Kaggle:  
[PCOS Dataset on Kaggle](https://www.kaggle.com/datasets/your-dataset-link)


## How to Run Locally?

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
