import streamlit as st
#from notes_agents import main

# Assuming notes_agents.py is in the same directory or accessible in the Python path
# and has a function main(ppt_file=None, video_file=None) that returns the notes as a string.

st.title("Notes Generator")

# Initialize session state for generated notes
if 'generated_notes' not in st.session_state:
    st.session_state['generated_notes'] = ""

# File uploaders
uploaded_ppt = st.file_uploader("Upload PowerPoint file", type=["ppt", "pptx"])
uploaded_video = st.file_uploader("Upload video file", type=["mp4", "avi", "mov", "mkv"])

# Button to generate notes
if st.button("Generate Notes"):
    if uploaded_ppt is None and uploaded_video is None:
        st.warning("Please upload at least one file (PPT or Video).")
    else:
        # Call the main function from notes_agents.py
        # Pass the uploaded file objects directly if main can handle them,
        # otherwise, you might need to save them temporarily and pass paths.
        with st.spinner("Generating notes..."):
            try:
                # Pass uploaded file objects to the main function
                st.session_state['generated_notes'] = "None"
                st.success("Notes generated successfully!")
            except Exception as e:
                st.error(f"An error occurred during note generation: {e}")

# Display generated notes preview
if st.session_state['generated_notes']:
    st.subheader("Generated Notes Preview")
    st.text_area("Notes", st.session_state['generated_notes'], height=300)