# Quick Start Guide - Image-to-Image Generation

Get started with image-to-image generation in 3 simple steps!

## Step 1: Install Dependencies

```bash
pip install google-generativeai Pillow
```

## Step 2: Prepare Your Image

Place an image file in the current directory or specify the full path.

## Step 3: Transform Your Image

### Option A: Command Line

```bash
python image_to_image.py my_photo.jpg "convert to watercolor painting"
```

### Option B: Python Script

Create a file `my_transform.py`:

```python
from image_to_image import ImageToImageGenerator

# Create generator
gen = ImageToImageGenerator()

# Transform image
gen.generate("my_photo.jpg", "make it look like an anime drawing")
```

Run it:
```bash
python my_transform.py
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
