# RoadSage - Intelligent Driver Assistance System

## Introduction

RoadSage is an advanced driver assistance system designed to enhance driving safety and convenience. It detects objects on the road, identifies drivable areas and lanes, and provides depth information about various objects. Utilizing state-of-the-art machine learning models, RoadSage ensures high accuracy and real-time performance.

## Features

- **Object Detection and Segmentation**: Uses YOLOP for real-time object detection, drivable area segmentation, and lane detection.
- **Depth Estimation**: Integrates Depth Anything for accurate depth information.
- **Performance Optimization**: Achieves 29 FPS on an RTX 4070 GPU with a frame-skipping strategy for depth estimation.

## Methodology

### Object Detection and Segmentation

RoadSage employs YOLOP (You Only Look Once for Panoptic driving), a robust and efficient model for object detection, drivable area segmentation, and lane detection.

### Depth Estimation

Two depth estimation models were evaluated:
1. **Global Local Networks**: Initially tested but resulted in low FPS.
2. **Depth Anything**: Provided better depth estimation results and was integrated into the final system.

### Implementation and Optimization

- **Without Depth Estimation**: 17 FPS on RTX 4070.
- **With Depth Anything**: 8.3 FPS.
- **Optimized Performance**: 29 FPS with frame-skipping strategy, maintaining accurate depth information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RoadSage.git
   cd RoadSage
