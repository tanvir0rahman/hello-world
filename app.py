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

# Batch processing section
st.markdown("---")
with st.expander("🔄 Batch Processing (Multiple Prompts)"):
    st.markdown("Generate multiple variations of your image with different prompts")

    batch_prompts = st.text_area(
        "Enter prompts (one per line):",
        height=150,
        placeholder="Convert to watercolor\nMake it look like anime\nApply vintage filter\nTransform into pixel art",
        help="Each line will generate a separate image"
    )

    batch_button = st.button("🎨 Generate Batch", key="batch_generate")

    if batch_button:
        if uploaded_file is None:
            st.error("⚠️ Please upload an image first!")
        elif not batch_prompts.strip():
            st.error("⚠️ Please enter at least one prompt!")
        else:
            prompts_list = [p.strip() for p in batch_prompts.split('\n') if p.strip()]

            # Save uploaded file temporarily
            temp_input_path = os.path.join(OUTPUT_DIR, f"temp_batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            os.makedirs(OUTPUT_DIR, exist_ok=True)

            image = Image.open(uploaded_file)
            image.save(temp_input_path)

            # Generate batch
            progress_bar = st.progress(0)
            status_text = st.empty()

            results = []
            for i, prompt in enumerate(prompts_list):
                status_text.text(f"Generating {i+1}/{len(prompts_list)}: {prompt[:50]}...")

                try:
                    output_path = st.session_state.generator.generate(
                        input_image_path=temp_input_path,
                        prompt=prompt,
                        output_filename=f"batch_{i+1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    )
                    results.append((prompt, output_path))
                except Exception as e:
                    st.warning(f"Failed to generate for prompt: {prompt[:50]}... - Error: {str(e)}")
                    results.append((prompt, None))

                progress_bar.progress((i + 1) / len(prompts_list))

            status_text.text(f"✅ Completed {len([r for r in results if r[1]])} out of {len(prompts_list)} images")

            # Display batch results
            if results:
                st.markdown("### Batch Results")
                cols_per_row = 3
                for i in range(0, len(results), cols_per_row):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        if i + j < len(results):
                            prompt, path = results[i + j]
                            with col:
                                st.markdown(f"**{prompt[:30]}...**" if len(prompt) > 30 else f"**{prompt}**")
                                if path and os.path.exists(path):
                                    st.image(path, use_container_width=True)
                                    with open(path, "rb") as file:
                                        st.download_button(
                                            label="⬇️ Download",
                                            data=file,
                                            file_name=os.path.basename(path),
                                            mime="image/png",
                                            key=f"download_batch_{i+j}"
                                        )
                                else:
                                    st.error("Failed to generate")

            # Clean up temp file
            if os.path.exists(temp_input_path):
                os.remove(temp_input_path)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with Streamlit • Powered by Google Gemini 2.5 Flash Image</p>
        <p>📚 <a href='https://ai.google.dev/gemini-api/docs/image-generation' target='_blank'>API Documentation</a></p>
    </div>
""", unsafe_allow_html=True)
