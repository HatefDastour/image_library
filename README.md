# Image Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Images](https://img.shields.io/badge/Images-11-green.svg?style=flat-square)](#images)

A curated collection of personal photography with a Python utility for easy access and description retrieval. All images are personally captured by Dr. Hatef Dastour.

---

## 📸 Overview

This repository provides:
- High-quality photographs from various locations worldwide
- Python interface (`Sample_Images.py`) for programmatic access
- Detailed descriptions and metadata for each image
- Easy integration for educational and demonstration purposes

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/HatefDastour/image_library.git
cd image_library
```

### Usage

```python
from Sample_Images import Sample_Images

# Initialize the image library
images = Sample_Images()

# Read an image
image_matrix = images.read_image('Lake_Como')

# Get image description
description = images.get_description('Lake_Como')

# List all available images
available_images = images.list_images()
```

---

## 🖼️ Image Gallery

### Available Images

| Image Name | Location | Description |
|------------|----------|-------------|
| **Lake_Como** | Lombardy, Italy | Scenic lake in Northern Italy, known for picturesque surroundings and historic villages |
| **Varenna** | Lake Como, Italy | Colorful village with narrow streets and stunning lake views |
| **Northwest_Gate** | Chongqing, China | Significant landmark showcasing the city's cultural and historical landscape |
| **Qiansimen_Bridge** | Chongqing, China | Modern engineering marvel and urban development example |
| **Hong_Kong** | Victoria Harbour | Natural harbour with stunning skyline and bustling port activities |
| **Lunenburg** | Nova Scotia, Canada | Charming port town with well-preserved 18th-century architecture |
| **Waterfront** | Vancouver, BC | Vibrant urban landscape and scenic waterfront |
| **Rabbits** | Jericho Beach Park, Vancouver | Natural beauty and wildlife at the park |
| **Squirrel** | Sea to Sky Gondola, Vancouver | Diverse wildlife and scenic mountain views |
| **Botanical_Garden** | Kunming, China | Diverse plant species and serene natural environment |
| **Calgary_Fall** | Calgary, AB | Autumn colors in a neighborhood park |

---

## 💻 API Reference

### `Sample_Images` Class

**Methods:**

- `read_image(image_name)` - Load and return image as numpy array
- `get_description(image_name)` - Retrieve detailed description of the image
- `list_images()` - Get list of all available image names

**Example:**

```python
import matplotlib.pyplot as plt
from Sample_Images import Sample_Images

images = Sample_Images()

# Display an image
img = images.read_image('Varenna')
plt.imshow(img)
plt.title(images.get_description('Varenna'))
plt.axis('off')
plt.show()
```

---

## 📁 Repository Structure

```plaintext
image_library/
├── Sample_Images.py        # Python interface for image access
├── images/                 # Directory containing all images
│   ├── Lake_Como.jpg
│   ├── Varenna.jpg
│   └── ...
├── LICENSE.md             # License information
└── README.md              # This file
```

---

## ⚠️ Copyright Notice

**All images in this repository are copyrighted.**

© 2025 Hatef Dastour. All rights reserved.

These images may **not** be used, reproduced, or distributed without express written permission from the copyright holder.

---

## 📄 License

This repository contains both open-source code and copyrighted images:

- **Code** (`Sample_Images.py`): Licensed under the [MIT License](LICENSE.md)
- **Images**: Copyrighted by Hatef Dastour - All rights reserved

See [LICENSE.md](LICENSE.md) for complete details.

---

## 📧 Contact

**Dr. Hatef Dastour**  
University of Missouri, Columbia

- 🌐 **Website:** [hatefdastour.github.io](https://hatefdastour.github.io/)
- 📧 **Email:** [dastourh@missouri.edu](mailto:dastourh@missouri.edu)
- 🐙 **GitHub:** [@HatefDastour](https://github.com/HatefDastour)

For image usage permissions or inquiries, please contact via email.

---

<div align="center">

**Photography by Dr. Hatef Dastour**

</div>