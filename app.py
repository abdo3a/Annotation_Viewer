import streamlit as st
import pandas as pd
import numpy as np

# Define the main function
def main():
    # Set title
    st.title("Interactive Table Viewer")

    # File uploader
    file = st.file_uploader("Upload TSV file", type=["tsv"])
    if file:
        # Read TSV file
        df = pd.read_csv(file, sep='\t')
        
        # Display search bar
        search_query = st.text_input("Search", "")
        
        # Filter data based on search query
        if search_query:
            df = df[df.apply(lambda row: search_query.lower() in ' '.join(map(str, row)).lower(), axis=1)]
        
        # Calculate table height based on screen size
        table_height = st.session_state.get('table_height', 600)
        
        # Paginate the table
        page_num = st.number_input("Page Number", min_value=1, value=1)
        start_index = (page_num - 1) * 100
        end_index = min(start_index + 100, len(df))
        
        # Display table with half of the page height and no index
        st.dataframe(df.iloc[start_index:end_index].reset_index(drop=True), height=table_height, hide_index=True)
        
        # Update session state with new table height
        st.session_state['table_height'] = table_height
        
        # Display pagination controls below the table
        st.write(f"Page {page_num}/{int(np.ceil(len(df) / 100))}")

# Run the app
if __name__ == "__main__":
    main()
