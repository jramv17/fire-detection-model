# 🔥 Fire Detection Model using YOLOv8

This project is a fire detection system built using the YOLOv8 object detection model. The model was trained using a dataset from [Roboflow](https://roboflow.com/) and is served via a Flask-based API that allows users to detect fire in images through a simple POST request.

## 🚀 Features

- 🔍 Fire detection in images using YOLOv8
- 📊 Returns fire presence, percentage, and result image URL
- 🌐 Flask API endpoint for easy integration

## 🧠 Model Training

- **Model**: YOLOv8 (Ultralytics)
- **Dataset**: Sourced from Roboflow
- **Training**: Conducted using the official Ultralytics YOLOv8 training pipeline

## 🖼️ API Usage

### Endpoint : POST /api/detect-fire

### Request

- **Content-Type**: `multipart/form-data`
- **Body**: An image file under the key `image`

### Example using `curl`

```bash
curl -X POST http://localhost:5000/api/detect-fire \
  -F "image=@path_to_your_image.jpg"
```

### Response
```bash
{
  "fire_detected": true,
  "fire_percentage": 74.5,
  "image_result_url": "http://localhost:5000/static/results/result_123.jpg"
}
```


### ⚙️ Setup & Run
1.**Clone the repository**
```bash
git clone https://github.com/your-jramv17/fire-detection-yolov8.git
cd fire-detection-yolov8
```
2.**Install dependencies**
```bash
pip install -r requirements.txt
```
3.**Run the Flask app**
```bash
python app.py
```


