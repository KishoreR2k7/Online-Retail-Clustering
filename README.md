# Online Retail Clustering

A complete **K-Means clustering solution** for online retail transaction data. Users can upload a CSV with `Quantity` and `UnitPrice`, and the app automatically calculates `Total`, assigns cluster labels, and allows downloading the clustered dataset. Built using **Python**, **scikit-learn**, and **Gradio**.

---

## 🚀 Features

- Upload CSV files containing `Quantity` and `UnitPrice`.
- Automatically calculates `Total = Quantity × UnitPrice`.
- Preprocesses and scales features using a pre-trained `StandardScaler`.
- Assigns clusters using a pre-trained **KMeans** model.
- Download the clustered dataset as CSV.
- Handles CSV encoding issues (`UTF-8` and `Latin1`).
- Easy-to-use web interface using Gradio.

---

## 📂 Project Structure

Online-Retail-Clustering/
├── app.py # Gradio web application
├── model.ipynb # Notebook to train KMeans model
├── scaler.pkl # Pre-trained StandardScaler
├── kmeans_model.pkl # Pre-trained KMeans model
├── OnlineRetail.csv # Raw dataset
├── Cleaned Data.csv # Preprocessed dataset
├── Visuvalisation.ipynb # Data visualization and exploration
├── clustered_dataset.csv # Example clustered output
├── README.md # Project documentation
└── .gitignore # Ignore unnecessary files (optional)

yaml
Copy code

---

## 📊 Dataset

- **Source:** Online Retail Dataset (or your own retail dataset)
- **Columns used for clustering:**  
  - `Quantity` — Number of items purchased  
  - `UnitPrice` — Price per unit  
  - `Total` — Calculated as `Quantity × UnitPrice`  

> Other columns can exist in the CSV, but only these are used for clustering.

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/KishoreR2k7/Online-Retail-Clustering.git
cd Online-Retail-Clustering
Install dependencies:

bash
Copy code
pip install pandas numpy scikit-learn gradio
Ensure scaler.pkl and kmeans_model.pkl are in the project folder.

🏃 How to Run
Start the Gradio app:

bash
Copy code
python app.py
Open the provided local URL (e.g., http://127.0.0.1:7860) in your browser.

Upload a CSV with columns Quantity and UnitPrice.

The app will:

Compute Total automatically

Assign clusters

Provide a download link for the clustered CSV

📈 Model Training Workflow
Load and clean the dataset (model.ipynb).

Sample the data for faster processing (optional).

Scale features using StandardScaler.

Determine optimal K using:

Elbow method (inertia)

Silhouette score

Train KMeans with the selected K.

Save the trained KMeans model and scaler as pickle files (kmeans_model.pkl, scaler.pkl).

📊 Evaluation Metrics
Silhouette Score: Measures how similar an object is to its own cluster compared to other clusters.

Calinski-Harabasz Index: Ratio of between-cluster dispersion to within-cluster dispersion.

Davies-Bouldin Index: Measures similarity between clusters (lower is better).

🖼 Usage Example
Screenshot Placeholder:
Upload CSV → Click Submit → Download clustered CSV

mathematica
Copy code
Quantity,UnitPrice,Total,Cluster
10,5.0,50.0,2
1,200.0,200.0,0
5,12.0,60.0,1
⚙️ Optional .gitignore
markdown
Copy code
*.pkl
*.csv
.gradio/
__pycache__/
This prevents large CSVs and pickle files from being pushed to GitHub.
