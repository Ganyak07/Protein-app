

# Drug Target Identification

## Overview
This project focuses on identifying drug targets through various processes such as protein sequence retrieval, structure prediction, and visualization of protein domains. It provides a user-friendly interface for retrieving protein sequences, visualizing protein domains, and predicting protein structures.

## Features
- **Protein Sequence Retrieval**: Users can retrieve protein sequences by entering the gene or protein name. The application utilizes the NCBI Protein database to fetch the sequence.
- **Protein Domain Visualization**: The application allows users to visualize protein domains interactively. Users can input the protein sequence and view domain annotations on the sequence.
- **Protein Structure Prediction**: Using the AlphaFold API, the application predicts the 3D structure of proteins based on their amino acid sequences.

## Installation
To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Usage
1. **Run the Application**: Execute the Streamlit application by running the following command:
   ```
   streamlit run protein.py
   ```
2. **Retrieve Protein Sequence**: Enter the gene or protein name in the input field and click "Retrieve Sequence" to fetch the protein sequence.
3. **Visualize Protein Domains**: Input the protein sequence and click "Visualize Protein Domains" to see an interactive plot displaying protein domains.
4. **Predict Protein Structure**: Enter the protein sequence and click "Predict Structure" to obtain a 3D structure prediction using the AlphaFold API.

## Technologies Used
- **Streamlit**: Python library for creating interactive web applications.
- **BioPython**: Python tools for computational molecular biology.
- **Plotly**: Python graphing library for interactive plots.
- **NGLView**: Molecular visualization widget for Jupyter notebooks.

## Contributors
- [Ganiyat Yakub](https://github.com/Ganyak07)

## License
This project is licensed under the [MIT License](LICENSE).

