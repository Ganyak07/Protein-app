import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="Drug Target Identification", page_icon=":pill:")

# Page Title
st.title("Drug Target Identification")

# Add the necessary components for protein sequence retrieval, structure prediction, etc.
from Bio import Entrez, SeqIO

# Function to retrieve protein sequence from NCBI database
def retrieve_protein_sequence(query):
    try:
        # Configure BioPython Entrez with email (required by NCBI)
        Entrez.email = "your_email@example.com"  # Replace with your email address
        
        # Search for the query term in the NCBI Protein database
        handle = Entrez.esearch(db="protein", term=query)
        record = Entrez.read(handle)
        
        # Get the first protein ID from the search results
        protein_id = record["IdList"][0]
        
        # Fetch the protein sequence using the protein ID
        handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
        sequence_record = SeqIO.read(handle, "fasta")
        
        # Close the handle
        handle.close()
        
        # Return the protein sequence
        return sequence_record.seq
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Input field for gene or protein name
query = st.text_input("Enter gene or protein name")

# Button to trigger sequence retrieval
if st.button("Retrieve Sequence"):
    if query:
        # Retrieve and display the protein sequence
        sequence = retrieve_protein_sequence(query)
        if sequence:
            st.write("### Retrieved Protein Sequence:")
            st.write(sequence)
    else:
        st.warning("Please enter a gene or protein name.")
import streamlit as st
import plotly.graph_objects as go

def visualize_protein_domains_interactive(sequence, domain_annotations):
    fig = go.Figure()

    # Plot the protein sequence as a line
    fig.add_trace(go.Scatter(x=list(range(len(sequence))), y=[0] * len(sequence), mode='lines', name='Protein Sequence'))

    # Plot domain annotations as shaded regions
    for domain in domain_annotations:
        start, end = domain['start'], domain['end']
        fig.add_trace(go.Scatter(x=list(range(start, end + 1)), y=[0.5] * (end - start + 1),
                                 mode='lines', name=domain['name'], fill='toself', fillcolor='blue', line=dict(color='blue')))

    # Update layout with interactive features
    fig.update_layout(
        title='Protein Sequence with Domain Annotations',
        xaxis=dict(title='Residue Position'),
        yaxis=dict(title=''),
        hovermode='closest',
        showlegend=True
    )

    return fig

# Page Title
st.title("Protein Domain Visualization")

# Input field for protein sequence
sequence = st.text_area("Enter protein sequence")

# Example domain annotations
domain_annotations = [{'name': 'Domain1', 'start': 5, 'end': 15}, {'name': 'Domain2', 'start': 25, 'end': 35}]

# Button to trigger domain visualization
if st.button("Visualize Protein Domains"):
    if sequence:
        # Display the interactive plot
        st.plotly_chart(visualize_protein_domains_interactive(sequence, domain_annotations))
    else:
        st.warning("Please enter a protein sequence.")
        import streamlit as st
import requests
import nglview as nv

# Function to predict protein structure using AlphaFold API
# Function to predict protein structure using AlphaFold API
def predict_structure(sequence):
    try:
        # Make a POST request to the AlphaFold API with the protein sequence
        response = requests.post('https://alphafold.ebi.ac.uk/entry', json={'seq': sequence})
        response.raise_for_status()  # Raise an error for non-2xx status codes
        
        # Print the response content for debugging
        print("Response Content:", response.content)
        
        # Parse the response to extract the predicted structure
        predicted_structure = response.json()['prediction']
        return predicted_structure
    except requests.RequestException as e:
        st.error(f"Error occurred while fetching protein structure: {e}")
        return None
    except KeyError as e:
        st.error("Unexpected response format from the AlphaFold API")
        return None



# Page Title
st.title("Protein Structure Prediction")

# Input field for protein sequence
sequence = st.text_area("Enter protein sequence", key="protein_sequence_input")

# Button to trigger structure prediction
# Button to trigger structure prediction
if st.button("Predict Structure"):
    if sequence:
        # Predict protein structure using AlphaFold API
        predicted_structure = predict_structure(sequence)
        if predicted_structure is not None:
            # Display the predicted structure using NGL Viewer
            viewer = nv.show_structure_file(predicted_structure)
            st.write(viewer)
        else:
            st.error("Failed to predict protein structure. Please try again with a different sequence.")
    else:
        st.warning("Please enter a protein sequence.")

