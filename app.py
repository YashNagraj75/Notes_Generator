import streamlit as st
import asyncio
import os
from notes_agents import main

st.title("Notes Generator")

if "generated_notes" not in st.session_state:
    st.session_state["generated_notes"] = ""

uploaded_ppt = st.file_uploader("Upload PowerPoint file", type=["ppt", "pptx"])
uploaded_video = st.file_uploader(
    "Upload video file", type=["mp4", "avi", "mov", "mkv"]
)


def save_uploaded_file(uploaded_file, save_dir="assets"):
    if uploaded_file is not None:
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    return None


if st.button("Generate Notes"):
    if uploaded_ppt is None and uploaded_video is None:
        st.warning("Please upload at least one file (PPT or Video).")
    else:
        ppt_path = save_uploaded_file(uploaded_ppt) if uploaded_ppt else None
        video_path = save_uploaded_file(uploaded_video) if uploaded_video else None
        with st.status(
            "Processing files and generating notes...", expanded=True
        ) as status:
            if ppt_path:
                st.write(f"Processing PPT: {os.path.basename(ppt_path)}")
            if video_path:
                st.write(f"Processing Video: {os.path.basename(video_path)}")
            st.write("Generating notes...")
            try:
                notes = asyncio.run(main(ppt_path, video_path))
                st.session_state["generated_notes"] = notes
                status.update(label="Notes generated successfully!", state="complete")
            except Exception as e:
                st.session_state["generated_notes"] = ""
                status.update(
                    label=f"An error occurred during note generation: {e}",
                    state="error",
                )

# Display generated notes preview
if st.session_state["generated_notes"]:
    st.subheader("Generated Notes Preview")
    st.markdown(st.session_state["generated_notes"], unsafe_allow_html=True)
