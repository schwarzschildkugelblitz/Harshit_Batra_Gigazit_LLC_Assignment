# Pixel to Coordinates Conversion Script

## Overview
This script allows you to convert pixel locations within an image to their corresponding x and y coordinates. It includes an interactive click system(for testing purpose) where you can click on any point in the image to get its pixel coordinates. The script handles various image formats and provides a default image for testing.


## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)


## Run the Code in Google Colab

This link allows you to run the code directly in Google Colab, eliminating the need to install any packages on your local machine. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12mflnYeHycY6JL2qMBIlr81I04UxBU2n?usp=sharing)

## Installation


**Prerequisites**

* **Python:** Ensure you have Python 3.x installed on your system. You can verify this by opening a terminal or command prompt and typing `python --version` or `python3 --version`. If Python is not installed or the version is incompatible, download the latest version from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** pip is the recommended package installer for Python. It usually comes bundled with Python 3.x installations. To check if pip is installed, type `pip --version` in your terminal. If it's not found, follow the instructions on the pip website to install it: [https://www.pypa.io/](https://www.pypa.io/)

**Installation Methods**

**Method 1: Using pip**

1. Open a terminal or command prompt.
2. Run the following command to install the required packages:

   ```bash
   pip install opencv-python numpy
   ```

   This command will download and install the `opencv-python` and `numpy` packages from the Python Package Index (PyPI).

**Method 2: Using requirements.txt**

1. Open a terminal and navigate to your project directory.
2. Run the following command to install the packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```



## Usage
1. Save your image in the same directory as the script or provide the path to your image.
2. Run the script using the following command:
    ```
    python pixel_to_coordinates.py --image your_image.jpg [--interactive]
    ```
    Replace `your_image.jpg` with the path to your image file. If no image is provided, the script will use `default_image.jpg`.

3. If you use the `--interactive` flag, the script will display the image, and you can click on any point to get its pixel coordinates. The coordinates will be printed to the console.

4. If the `--interactive` flag is not used, the script will display a predefined location on the image.

## Examples
## Usage Examples

### Interactive Mode
Run the script in interactive mode to click on the image and get pixel coordinates. In this mode, you can click on multiple points on the image to capture their coordinates. Press 'q' to quit the interactive session.

```sh
python pixel_to_coordinates.py --image sample_image.png --interactive
```

### Predefined Coordinates Mode
Run the script without interactive mode to display the image with a predefined point marked. The default coordinates are (100, 50), but you can specify custom coordinates using the `--location` argument.

```sh
python pixel_to_coordinates.py --image sample_image.png
```

### Custom Predefined Coordinates
Specify custom coordinates to be marked on the image in non-interactive mode by using the `--location` argument followed by the x and y values.

```sh
python pixel_to_coordinates.py --image sample_image.png --location 150 200
```

- Ensure that the path to the input image is correct and the image format is supported by OpenCV.
- In interactive mode, the coordinates of each click will be printed in the console.
- Press 'q' to exit the interactive session.

## Assumptions
- The script assumes the provided image path is valid and the image is in a readable format.
- The default image used is `default_image.jpg`.

## Notes
- The script uses OpenCV for image processing and displaying the image.
- The clicked coordinates are stored in a list and printed to the console after you quit the interactive mode.

## Troubleshooting
- If the image is not displayed, ensure that the image path is correct and the image format is supported by OpenCV.
- If the script does not capture clicks, ensure that the OpenCV window is in focus while clicking.


