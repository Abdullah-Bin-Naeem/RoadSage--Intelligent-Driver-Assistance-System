
 ``` ```
# RoadSage - Intelligent Driver Assistance System
 ``` ```
## Introduction

RoadSage is an advanced driver assistance system designed to enhance driving safety and convenience. It detects objects on the road, identifies drivable areas and lanes, and provides depth information about various objects. Utilizing state-of-the-art machine learning models, RoadSage ensures high accuracy and real-time performance.
 ```  ```

<video src="videos/foreign.mp4" controls autoplay loop muted width="600">
  Your browser does not support the video tag.
</video>


## Features

- **Object Detection and Segmentation**: Uses YOLOP for real-time object detection, drivable area segmentation, and lane detection.
- **Depth Estimation**: Integrates Depth Anything for accurate depth information.
- **Performance Optimization**: Achieves 29 FPS on an RTX 4070 GPU with a frame-skipping strategy for depth estimation.
 ``` ```
## Methodology
 
### Object Detection and Segmentation

RoadSage employs YOLOP (You Only Look Once for Panoptic driving), a robust and efficient model for object detection, drivable area segmentation, and lane detection.
 ```  ```
### Depth Estimation

Two depth estimation models were evaluated:
1. **Global Local Networks**: Initially tested but resulted in less efficient results in depths.
2. **Depth Anything**: Provided better depth estimation results and was integrated into the final system.
``` ```
### Implementation and Optimization
 
- **With optimizations in Depth Estimation**: 17 FPS on RTX 4070.
- **Without optimizations in Depth Anything**: 8.3 FPS.
- **Optimized Performance**: 29 FPS with frame-skipping strategy, maintaining accurate depth information.
``` ```
## Installation

   
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RoadSage.git
   cd RoadSage
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have the correct versions of PyTorch and torchvision:
   ```bash
   conda install pytorch==1.7.0 torchvision==0.8.0 cudatoolkit=10.2 -c pytorch
   ```

## Usage

### Download these files first

Download these files in the 'RoadSage--Intelligent-Driver-Assistance-System' folder after cloning the repository. Files are: LiheYoung, inference, weights, vinvino02 [Download](https://drive.google.com/drive/folders/1b9jaZK7c9ZVgqjd2WdCt790fueCtz-hQ?usp=sharing)

### Demo Test

We provide two testing methods:

#### Folder

Store the images or videos in the `--source` directory and save the inference results to inference/outputs`:
```bash
python tools/demo.py --source inference/images inference/outputs
```

#### Camera

If there is a camera connected to your computer, set the source as the camera number (default is 0):
```bash
python tools/demo.py --source 0
```

## File Structure

- `main.py`: Main script to run RoadSage.
- `depths.py`: Contains the depth estimation models and related code.
- `tools/demo.py`: Script to run the demo tests.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- YOLOP: [YOLOP GitHub Repository](https://github.com/hustvl/YOLOP)
- Depth Anything: [Depth Anything GitHub Repository](https://github.com/isl-org/DPT)
```

### Additional Steps for GitHub

After updating the `README.md` file, follow these steps to push your changes to GitHub:

1. **Add the updated README.md file to the staging area**:
   ```bash
   git add README.md
   ```
2. **Commit your changes**:
   ```bash
   git commit -m "Added complete README.md with demo test instructions and requirements"
   ```
3. **Push your changes to GitHub**:
   ```bash
   git push origin main
   ```

This will update your project repository on GitHub with the complete `README.md` file, providing all necessary instructions and information.
