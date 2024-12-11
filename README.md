# Image Library

This repository contains a collection of images along with their descriptions. It includes a Python script (`Sample_Images.py`) that provides methods to read and describe these images.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Images](#images)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

This repository is designed to provide a simple way to access and describe a set of images. The `Sample_Images.py` script allows you to read images and retrieve their descriptions.

## Usage

To use the `Sample_Images.py` script, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HatefDastour/image-library.git
   ```

2. **Navigate to the Repository**:
   ```bash
   cd image-library
   ```

3. **Run the Script**:
   ```python
   from Sample_Images import Sample_Images

   images = Sample_Images()
   image_matrix = images.read_image('Lake_Como')
   ```

## Images

The following images are included in this repository:

- Lake_Como.jpg
- Northwest_Gate.jpg
- Qiansimen_Bridge.jpg
- Lunenburg.jpg
- Rabbits.jpg
- Squirrel.jpg
- Varenna.jpg
- Waterfront.jpg

## License

### Code
The Python script (`Sample_Images.py`) is licensed under the [MIT License](LICENSE).

### Images
The images in this repository are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)][cc-by-4.0].

[cc-by-4.0]: https://creativecommons.org/licenses/by/4.0/
