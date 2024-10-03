# Smoke and Fire Detection using YOLOv11

This project utilizes the YOLOv11 model to detect smoke and fire in videos. 
The detection results are displayed in real-time and saved to a new video file.
  
이 프로젝트는 YOLOv11 모델을 사용하여 비디오에서 화재와 연기를 감지합니다.  
전기 차량의 화재 전조 증상을 감지하는 것이 최종 목표입니다.  
  
  
<img src="https://raw.githubusercontent.com/bsy0317/yolov11_FireSmokeDetect/refs/heads/sample/detected_IMG_0181.gif"/>  
  
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Training](#training)
  - [Detection](#detection)
- [Configurations](#configurations)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project uses the YOLOv11 object detection model to detect fire and smoke in videos.  
The model can be trained on a custom dataset or used for detection on a given video file.

## Features

- **Real-time Detection**: Detects fire and smoke in videos using the YOLOv11 model.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bsy0317/yolov11_FireSmokeDetect.git
   cd smoke-fire-detection
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install YOLOv11**:
   Make sure you have the Ultralytics YOLO library installed. You can install it via pip:
   ```bash
   pip install ultralytics
   ```

## Usage

### 1. Training

To train the YOLO model with a datasets:
Download the dataset and update the `data.yaml` file with the dataset details.

```bash
python main.py --train
```

### 2. Detection

To perform fire and smoke detection on a video:

```bash
python main.py --detect --file "path_to_input_video.mp4"
```
  
## Configurations

### `config.py`

The configuration settings for training and detection are defined in the `config.py` file. Here are the key configurations:

- `model_architecture`: The model architecture to use (e.g., yolov11.pt).
- `epochs`: Number of epochs to train the model.
- `batch`: Batch size for training.
- `save_dir`: Directory where model checkpoints and results will be saved.
- `data_yaml_path`: Path to the `data.yaml` file that defines the dataset.

You can modify the configurations to suit your specific requirements.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and make your changes. Once your changes are ready, submit a pull request, and we will review it.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

