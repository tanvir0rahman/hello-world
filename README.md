# Image-to-Image Generation with Google Gemini API

A Python implementation for transforming images using text prompts with Google's Gemini 2.5 Flash Image model.

## Milestone 2: Image-to-Image Generation

This milestone implements image-to-image transformation capabilities using the Gemini API, allowing you to:
- Transform images with text descriptions
- Apply artistic styles (watercolor, anime, vintage, etc.)
- Modify backgrounds and objects
- Colorize black and white photos
- Blur backgrounds and enhance features
- Batch process multiple transformations

## Features

- **Simple API**: Easy-to-use Python class for image transformations
- **Multiple Use Cases**: Style transfer, object modification, color adjustments, and more
- **Batch Processing**: Generate multiple variations with different prompts
- **Configurable**: Manage API keys and settings through config file
- **Command-line Interface**: Direct usage from terminal

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tanvir0rahman/hello-world.git
cd hello-world
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key in `config.py` or set as environment variable

## Project Structure

```
hello-world/
├── image_to_image.py     # Main implementation
├── examples.py           # Usage examples
├── config.py             # Configuration file
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
├── output/              # Generated images (auto-created)
└── README.md            # This file
```

## Usage

### Basic Command-line Usage

```bash
python image_to_image.py <input_image_path> <prompt>
```

Example:
```bash
python image_to_image.py photo.jpg "convert to watercolor painting style"
```

### Python API Usage

```python
from image_to_image import ImageToImageGenerator

# Initialize generator
generator = ImageToImageGenerator()

# Transform an image
generator.generate(
    input_image_path="input.jpg",
    prompt="Make it look like a Van Gogh painting"
)

# Batch processing
prompts = [
    "Convert to anime style",
    "Apply vintage filter",
    "Make it look futuristic"
]
generator.batch_generate("input.jpg", prompts)
```

### Running Examples

The `examples.py` file contains 6 different use cases:

1. **Basic Transformation**: Simple style conversions
2. **Object Modification**: Change backgrounds and elements
3. **Style Transfer**: Apply famous artistic styles
4. **Color Adjustments**: Colorize and adjust tones
5. **Batch Processing**: Multiple variations at once
6. **Advanced Editing**: Complex multi-step transformations

Run examples:
```bash
python examples.py
```

## API Reference

### ImageToImageGenerator Class

#### `__init__(api_key=None)`
Initialize the generator with your API key.

#### `generate(input_image_path, prompt, output_filename=None)`
Generate a transformed image based on input image and text prompt.

**Parameters:**
- `input_image_path` (str): Path to input image
- `prompt` (str): Text description of desired transformation
- `output_filename` (str, optional): Custom output filename

**Returns:**
- `str`: Path to generated image

#### `batch_generate(input_image_path, prompts)`
Generate multiple variations with different prompts.

**Parameters:**
- `input_image_path` (str): Path to input image
- `prompts` (list): List of transformation prompts

**Returns:**
- `list`: Paths to generated images

## Configuration

Edit `config.py` to customize:
- API key
- Model name (default: gemini-2.5-flash-image)
- Output directory

## Model Information

- **Model**: Gemini 2.5 Flash Image ("Nano Banana")
- **Provider**: Google AI
- **Capabilities**: Image-to-image transformation, style transfer, object modification
- **Pricing**: $0.039 per image (1290 output tokens)

## Example Transformations

Here are some example prompts you can try:

- "Convert this photo to an oil painting"
- "Make the background blurry and keep the subject sharp"
- "Transform into 1980s vintage style"
- "Add warm sunset lighting"
- "Convert to black and white with high contrast"
- "Make it look like a professional studio photo"
- "Transform into pixel art style"
- "Add snow and winter atmosphere"

## Requirements

- Python 3.7+
- google-generativeai >= 0.8.0
- Pillow >= 10.0.0

## Security

- API keys are stored in `config.py` (gitignored for security)
- Consider using environment variables for production
- Never commit API keys to version control

## Troubleshooting

**No image generated?**
- Check that your API key is valid
- Ensure input image exists and is readable
- Verify internet connection
- Check API quota limits

**Installation issues?**
```bash
pip install --upgrade google-generativeai Pillow
```

## Documentation

Official Google Gemini API documentation:
- https://ai.google.dev/gemini-api/docs/image-generation

## License

MIT License

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

---

**Previous Repository Notes:**
Git hub test repository
Tanvir is testing out github. These comments are getting
added in web version.
Thank you.
12/9 9:21pm
adding new line on 4/25
this is cool
changing stuff in branch 
