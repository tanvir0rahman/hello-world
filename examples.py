"""
Example usage scripts for Image-to-Image Generation (Milestone 2)

This file demonstrates various use cases for the ImageToImageGenerator class.
"""

from image_to_image import ImageToImageGenerator


def example_1_basic_transformation():
    """
    Example 1: Basic image transformation
    Transforms an image based on a simple text prompt.
    """
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Image Transformation")
    print("="*70)

    generator = ImageToImageGenerator()

    # Example: Transform a photo to a different art style
    generator.generate(
        input_image_path="input/sample.jpg",
        prompt="Convert this image to a watercolor painting style"
    )


def example_2_object_modification():
    """
    Example 2: Modify objects in the image
    Demonstrates changing specific elements in the image.
    """
    print("\n" + "="*70)
    print("EXAMPLE 2: Object Modification")
    print("="*70)

    generator = ImageToImageGenerator()

    # Example: Change background or add/remove objects
    generator.generate(
        input_image_path="input/photo.jpg",
        prompt="Change the background to a sunny beach scene"
    )


def example_3_style_transfer():
    """
    Example 3: Apply artistic styles
    Demonstrates applying different artistic styles to images.
    """
    print("\n" + "="*70)
    print("EXAMPLE 3: Style Transfer")
    print("="*70)

    generator = ImageToImageGenerator()

    # Example: Apply Van Gogh style
    generator.generate(
        input_image_path="input/landscape.jpg",
        prompt="Transform this into Van Gogh's Starry Night painting style",
        output_filename="van_gogh_style.png"
    )


def example_4_color_adjustments():
    """
    Example 4: Color and tone adjustments
    Demonstrates changing colors and tones in images.
    """
    print("\n" + "="*70)
    print("EXAMPLE 4: Color Adjustments")
    print("="*70)

    generator = ImageToImageGenerator()

    # Example: Colorize black and white photo
    generator.generate(
        input_image_path="input/bw_photo.jpg",
        prompt="Add realistic colors to this black and white photograph"
    )


def example_5_batch_processing():
    """
    Example 5: Batch processing with multiple prompts
    Demonstrates generating multiple variations of the same image.
    """
    print("\n" + "="*70)
    print("EXAMPLE 5: Batch Processing")
    print("="*70)

    generator = ImageToImageGenerator()

    prompts = [
        "Make it look like a sunset scene",
        "Convert to anime art style",
        "Apply vintage 1970s filter",
        "Transform into a minimalist line drawing"
    ]

    results = generator.batch_generate("input/sample.jpg", prompts)

    print(f"\n✓ Generated {len([r for r in results if r])} out of {len(prompts)} images")


def example_6_advanced_editing():
    """
    Example 6: Advanced image editing
    Demonstrates complex transformations and edits.
    """
    print("\n" + "="*70)
    print("EXAMPLE 6: Advanced Editing")
    print("="*70)

    generator = ImageToImageGenerator()

    # Example: Complex transformation
    generator.generate(
        input_image_path="input/portrait.jpg",
        prompt="Blur the background, enhance the subject's features, and add warm sunset lighting",
        output_filename="advanced_edit.png"
    )


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║  Image-to-Image Generation Examples - Milestone 2             ║
    ║  Using Google Gemini 2.5 Flash Image Model                    ║
    ╚════════════════════════════════════════════════════════════════╝
    """)

    print("\nNOTE: Make sure you have input images in the 'input/' directory")
    print("before running these examples.\n")

    choice = input("Enter example number (1-6) or 'all' to run all examples: ").strip()

    if choice == "1":
        example_1_basic_transformation()
    elif choice == "2":
        example_2_object_modification()
    elif choice == "3":
        example_3_style_transfer()
    elif choice == "4":
        example_4_color_adjustments()
    elif choice == "5":
        example_5_batch_processing()
    elif choice == "6":
        example_6_advanced_editing()
    elif choice.lower() == "all":
        example_1_basic_transformation()
        example_2_object_modification()
        example_3_style_transfer()
        example_4_color_adjustments()
        example_5_batch_processing()
        example_6_advanced_editing()
    else:
        print("Invalid choice. Please run again and select 1-6 or 'all'")
