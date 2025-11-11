"""
Milestone 2: Image-to-Image Generation using Google Gemini API
This module provides functionality to transform images using text prompts
with the Gemini 2.5 Flash Image model.
"""

import google.generativeai as genai
from PIL import Image
import os
import sys
from datetime import datetime
from config import API_KEY, MODEL_NAME, OUTPUT_DIR


class ImageToImageGenerator:
    """
    A class to handle image-to-image generation using Google Gemini API.

    This class enables:
    - Loading and processing input images
    - Applying text-based transformations to images
    - Saving generated images with timestamps
    """

    def __init__(self, api_key=None):
        """
        Initialize the ImageToImageGenerator.

        Args:
            api_key (str, optional): Google API key. Uses config.API_KEY if not provided.
        """
        self.api_key = api_key or API_KEY
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(MODEL_NAME)
        print(f"✓ Initialized with model: {MODEL_NAME}")

    def load_image(self, image_path):
        """
        Load an image from file path.

        Args:
            image_path (str): Path to the input image

        Returns:
            PIL.Image: Loaded image object

        Raises:
            FileNotFoundError: If image file doesn't exist
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        image = Image.open(image_path)
        print(f"✓ Loaded image: {image_path} ({image.size[0]}x{image.size[1]})")
        return image

    def generate(self, input_image_path, prompt, output_filename=None):
        """
        Generate a new image based on the input image and text prompt.

        Args:
            input_image_path (str): Path to the input image
            prompt (str): Text description of the desired transformation
            output_filename (str, optional): Custom output filename

        Returns:
            str: Path to the generated image file
        """
        print(f"\n{'='*60}")
        print(f"Starting Image-to-Image Generation")
        print(f"{'='*60}")

        # Load input image
        input_image = self.load_image(input_image_path)

        # Prepare prompt for image-to-image transformation
        full_prompt = f"Transform this image: {prompt}"
        print(f"✓ Prompt: {prompt}")

        # Generate image
        print("⏳ Generating image...")
        try:
            response = self.model.generate_content([full_prompt, input_image])

            # Check if response contains image data
            if not hasattr(response, 'images') or not response.images:
                print("✗ No image generated. Response:", response.text if hasattr(response, 'text') else "No response")
                return None

            # Save generated image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if output_filename is None:
                output_filename = f"image_to_image_{timestamp}.png"

            output_path = os.path.join(OUTPUT_DIR, output_filename)

            # Save the first generated image
            generated_image = response.images[0]
            generated_image.save(output_path)

            print(f"✓ Image saved to: {output_path}")
            print(f"{'='*60}\n")

            return output_path

        except Exception as e:
            print(f"✗ Error during generation: {str(e)}")
            raise

    def batch_generate(self, input_image_path, prompts):
        """
        Generate multiple variations of an image using different prompts.

        Args:
            input_image_path (str): Path to the input image
            prompts (list): List of text prompts for different transformations

        Returns:
            list: List of paths to generated images
        """
        results = []
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[Batch {i}/{len(prompts)}]")
            output_filename = f"batch_{i}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            try:
                result = self.generate(input_image_path, prompt, output_filename)
                results.append(result)
            except Exception as e:
                print(f"✗ Failed to generate image {i}: {str(e)}")
                results.append(None)

        return results


def main():
    """
    Main function for command-line usage.
    """
    if len(sys.argv) < 3:
        print("Usage: python image_to_image.py <input_image_path> <prompt>")
        print("Example: python image_to_image.py photo.jpg 'make it look like a watercolor painting'")
        sys.exit(1)

    input_image_path = sys.argv[1]
    prompt = " ".join(sys.argv[2:])

    generator = ImageToImageGenerator()
    generator.generate(input_image_path, prompt)


if __name__ == "__main__":
    main()
