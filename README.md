# vUtils: Feature-Point-Based Video Stabilization for Fixed Cameras

This project implements a feature-point-based algorithm to calibrate and remove camera shake caused by external factors from fixed camera footage.

## Project Overview

The system focuses on stabilizing videos captured by fixed cameras, compensating for external vibrations and movements by leveraging a feature-point-based method. For more details on the algorithm and code, please visit the project repository: [vUtils GitHub Repository](https://github.com/gaobiaoli/vUtils.git).

## Usage Guide

Follow the steps below to set up and run the project:

### 1. Clone the repository

```bash
git clone https://github.com/gaobiaoli/Sample_VideoCapture.git
cd Sample_VideoCapture
```
### 2. Clone the repository

It's recommended to create a virtual environment to manage dependencies:
```bash
conda create --name demo python=3.x  # Replace `3.x` with your preferred Python version
conda activate demo
```

### 3、Install dependencies

```bash
pip install -r requirements.txt
```

### 4、Run the demo

```bash
python demo.py
```