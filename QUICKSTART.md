# Quick Start Guide - Image-to-Image Generation

Get started with image-to-image generation in 2 simple steps!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Run the App

### Option A: Web Interface (Easiest!)

```bash
streamlit run app.py
```

Then open **http://localhost:8501** in your browser and:
1. Upload an image
2. Enter a transformation prompt
3. Click "Generate Image"
4. Download your result!

### Option B: Command Line

```bash
python image_to_image.py my_photo.jpg "convert to watercolor painting"
```

### Option C: Python Script

```python
from image_to_image import ImageToImageGenerator

gen = ImageToImageGenerator()
gen.generate("my_photo.jpg", "make it look like an anime drawing")
```

## Output

Generated images are saved in the `output/` directory with timestamps.

## Example Prompts to Try

- "convert to oil painting style"
- "make background blurry, focus on subject"
- "add sunset lighting"
- "transform into pixel art"
- "colorize this black and white photo"
- "make it look like a vintage 1970s photo"

## Need Help?

Check the full README.md for:
- API reference
- Batch processing
- Advanced examples
- Troubleshooting

## Reference

Based on Google Gemini API documentation:
https://ai.google.dev/gemini-api/docs/image-generation
