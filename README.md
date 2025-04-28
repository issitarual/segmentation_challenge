# LuminaLab Segmentation API 🖼️
> Image segmentation pipeline exposed as an API using FastAPI!

## About 🔎
This project implements an API for image segmentation, capable of detecting and isolating structures (e.g., walls, rooms) from floor plans or similar images. The solution uses classic image processing techniques and exposes endpoints to process images easily.

### Implemented features ✅
- [x] Pre-processing with grayscale and thresholding
- [x] Noise removal and morphological operations
- [x] Distance transform and marker generation
- [x] Watershed segmentation
- [x] API endpoint to upload and segment images

### Future improvements 🔮
- [ ] Post-processing to refine boundaries
- [ ] Improve segmentation with ML-based approaches
- [ ] Add unit and integration tests

## Technologies
The following tools and frameworks were used in the construction of the project:
<p>
  <img style='margin: 5px;' src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'>
  <img style='margin: 5px;' src='https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white'>
  <img style='margin: 5px;' src='https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white'>
  <img style='margin: 5px;' src='https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white'>
</p>

## How to run
1. Clone this repository
```bash
git clone https://github.com/[your-username]/lumina_lab.git
```
2. Navigate to the project directory
```bash
cd lumina_lab
```
3. Build the Docker image
```bash
docker build -t lumina-lab-segmentation .
```
4. Run the Docker container
```bash
docker run -it --rm -p 8000:8000 lumina-lab-segmentation
```
5. Access the API
```bash
http://localhost:8000/segmentation/segment/
```
