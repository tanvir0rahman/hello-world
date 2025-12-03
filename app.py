"""
Streamlit Web Interface for Image-to-Image Generation
Run with: streamlit run app.py
"""

import streamlit as st
from PIL import Image
import io
import os
from datetime import datetime
from image_to_image import ImageToImageGenerator
from config import OUTPUT_DIR

# Page configuration
st.set_page_config(
    page_title="Image-to-Image Generator",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .creator-text {
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 1.5rem;
        color: #ff6b6b;
        text-align: center;
        margin-bottom: 1rem;
        font-style: italic;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #1557a0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_image_path' not in st.session_state:
    st.session_state.generated_image_path = None
if 'generator' not in st.session_state:
    st.session_state.generator = ImageToImageGenerator()

# Header
st.markdown('<h1 class="main-header">🎨 Image-to-Image Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="creator-text">brought to you by Tanvir</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transform your images with AI using Google Gemini 2.5 Flash Image</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app uses **Google Gemini 2.5 Flash Image** (Nano Banana) to transform images based on text prompts.

    Example: Editorial
    """)

    st.header("💡 Example Prompts")
    example_prompts = [
        "Editorial"
    ]

    for prompt in example_prompts:
        if st.button(f"📝 {prompt}", key=f"example_{prompt}"):
            st.session_state.selected_prompt = prompt

    st.markdown("---")
    st.markdown("**Model:** gemini-2.5-flash-image")
    st.markdown("**Cost:** ~$0.039 per image")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Limit 200MB per file • JPG only",
        type=['jpg', 'jpeg'],
        help="Upload JPG images only (max 200MB)"
    )

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)

        # Show image details
        st.caption(f"Size: {image.size[0]} x {image.size[1]} pixels")

with col2:
    st.subheader("✨ Transform")

    # Prompt input
    if 'selected_prompt' in st.session_state:
        default_prompt = st.session_state.selected_prompt
        del st.session_state.selected_prompt
    else:
        default_prompt = "Editorial"

    prompt = st.text_area(
        "Enter transformation prompt:",
        value=default_prompt,
        height=100,
        placeholder="Example: Convert this photo to a watercolor painting style",
        help="Describe how you want to transform the image"
    )

    # Generate button
    generate_button = st.button("🎨 Generate Image", type="primary")

    if generate_button:
        if uploaded_file is None:
            st.error("⚠️ Please upload an image first!")
        elif not prompt.strip():
            st.error("⚠️ Please enter a transformation prompt!")
        else:
            # Save uploaded file temporarily
            temp_input_path = os.path.join(OUTPUT_DIR, f"temp_input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            os.makedirs(OUTPUT_DIR, exist_ok=True)

            image = Image.open(uploaded_file)
            image.save(temp_input_path)

            # Generate image with progress indicator
            with st.spinner("🔄 Generating your image... This may take a moment."):
                try:
                    output_path = st.session_state.generator.generate(
                        input_image_path=temp_input_path,
                        prompt=prompt
                    )

                    if output_path:
                        st.session_state.generated_image_path = output_path
                        st.success("✅ Image generated successfully!")
                    else:
                        st.error("❌ Failed to generate image. Please try a different prompt.")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

                finally:
                    # Clean up temp file
                    if os.path.exists(temp_input_path):
                        os.remove(temp_input_path)

# Display generated image
if st.session_state.generated_image_path and os.path.exists(st.session_state.generated_image_path):
    st.markdown("---")
    st.subheader("🎉 Generated Result")

    col_result1, col_result2 = st.columns(2)

    with col_result1:
        st.markdown("**Original**")
        if uploaded_file is not None:
            st.image(uploaded_file, use_container_width=True)

    with col_result2:
        st.markdown("**Transformed**")
        generated_image = Image.open(st.session_state.generated_image_path)
        st.image(generated_image, use_container_width=True)

        # Download button
        with open(st.session_state.generated_image_path, "rb") as file:
            btn = st.download_button(
                label="⬇️ Download Generated Image",
                data=file,
                file_name=f"generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                mime="image/png"
            )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with Streamlit • Powered by Google Gemini 2.5 Flash Image</p>
        <p>📚 <a href='https://ai.google.dev/gemini-api/docs/image-generation' target='_blank'>API Documentation</a></p>
    </div>
""", unsafe_allow_html=True)
