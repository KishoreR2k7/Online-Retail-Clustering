import pandas as pd
import numpy as np
import pickle
import gradio as gr
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("kmeans_model.pkl", "rb") as f:
    final_model = pickle.load(f)
def cluster_dataset(file):
    try:
        df = pd.read_csv(file.name)
    except UnicodeDecodeError:
        df = pd.read_csv(file.name, encoding='latin1')
        df.columns = df.columns.str.strip()
    col_mapping = {
        'quantity': 'Quantity',
        'unitprice': 'UnitPrice',
    }
    df.rename(columns={k: v for k, v in col_mapping.items() if k in df.columns.str.lower()}, inplace=True)
    if not all(col in df.columns for col in ['Quantity', 'UnitPrice']):
        return f"Error: Dataset must contain 'Quantity' and 'UnitPrice' columns. Found: {df.columns.tolist()}", None    
    df['Total'] = df['Quantity'] * df['UnitPrice']    
    x = df[['Quantity', 'UnitPrice', 'Total']].values
    x_scaled = scaler.transform(x)
    clusters = final_model.predict(x_scaled)
    df["Cluster"] = clusters    
    output_file = "clustered_dataset.csv"
    df.to_csv(output_file, index=False)
    return f"Clustering completed! Found {len(np.unique(clusters))} clusters.", output_file
iface = gr.Interface(
    fn=cluster_dataset,
    inputs=gr.File(label="Upload CSV Dataset"),
    outputs=[gr.Textbox(label="Status"), gr.File(label="Download Clustered Dataset")],
    title="Retail Dataset Clustering",
    description="Upload a CSV file containing 'Quantity' and 'UnitPrice'. The app will calculate 'Total', assign K-Means clusters, and provide a downloadable CSV."
)
if __name__ == "__main__":
    iface.launch()
