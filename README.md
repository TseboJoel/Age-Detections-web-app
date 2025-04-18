
# Age Detection Web App 👦👩🔍

## Overview

**FaceTraitsAnalyzer** is a Django-based web application designed for age and gender detection in images. By utilizing OpenCV and pre-trained models, the application allows users to upload images and receive real-time analysis of facial features. This web app performs precise age and gender detection, overlaying the results on the images, providing users with valuable insights in a simple and interactive manner.

## Key Features

- **Age Detection:** Accurately estimates the age range of individuals in uploaded images. 🎂
- **Gender Detection:** Identifies the gender of faces with high precision. ♂️♀️
- **User-Friendly Interface:** Intuitive web interface for seamless image upload and result presentation. 🌐
- **Visual Insights:** Presents detection results overlaid on the uploaded images for a comprehensive analysis. 📊

## Project Structure 📂

The project has the following structure:

```plaintext
.
├── README.md
├── age_gender_detection_app
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── age_deploy.prototxt
│   ├── age_net.caffemodel
│   ├── apps.py
│   ├── forms.py
│   ├── gender_deploy.prototxt
│   ├── gender_net.caffemodel
│   ├── migrations
│   ├── models.py
│   ├── opencv_face_detector.pbtxt
│   ├── opencv_face_detector_uint8.pb
│   ├── templates
│   │   ├── result.html
│   │   └── upload_image.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── age_gender_detection_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── compose.yaml
├── db.sqlite3
├── manage.py
├── media
│   └── uploads
│       ├── <image-files>
│       └── result.png
└── requirements.txt
```

### Key Files:
- `views.py`: Contains the logic for processing images, detecting faces, estimating age and gender, and saving the result.
- `forms.py`: Handles the image upload form for the web interface.
- `models.py`: Defines the `UploadedImage` model to save user-uploaded images.
- `templates/`: Contains HTML templates for uploading images and displaying results.
- `opencv_face_detector.pbtxt`, `opencv_face_detector_uint8.pb`, `age_deploy.prototxt`, `age_net.caffemodel`, `gender_deploy.prototxt`, `gender_net.caffemodel`: Pre-trained models used for face, age, and gender detection.

## Prerequisites 🛠️

Ensure you have the following software installed:

- **Python 3.x**: The application is developed using Python 3.
- **Django**: Web framework to build and run the app.
- **OpenCV**: Computer vision library used for processing the image and running the pre-trained models.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Getting Started 🚀

To get started with the Age and Gender Detection Web App, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/TseboJoel/Agedetection.git
```

### 2. Install Required Dependencies

Navigate to the project directory and install the required Python packages:

```bash
cd Agedetection
pip install -r requirements.txt
```

### 3. Apply Database Migrations

Run the following command to apply any database migrations:

```bash
python manage.py migrate
```

### 4. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

By default, the app should be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
In case the port is busy (like port `8000`), you can run the server on a different port:

```bash
python manage.py runserver 8001
```

You can then access the app at [http://127.0.0.1:8001/](http://127.0.0.1:8001/).

### 5. Upload Image for Analysis

Once the server is running, you can visit the app in your browser and upload an image. After uploading, the app will analyze the image, detect any faces, and predict their age range and gender. The result will be displayed on the image itself and shown on the results page.

## Usage

- **Upload an Image:** Simply upload an image of a face via the provided interface on the web page.
- **Results:** Once the image is processed, the age and gender of the detected faces will be overlaid on the image. The results will also be shown below the image.
- **Download the Result:** You can download the processed image with the overlayed results.

## Example

1. **Upload an Image**:
   - Example Image:  
     ![Example](media/uploads/example_image.jpg)

2. **Detection Result**:
   - Age: 25-32
   - Gender: Male
   - Result Image:  
     ![Result](media/uploads/result.png)

## Customizing Models

If you wish to use your own pre-trained models, simply replace the model files in the `age_gender_detection_app` directory:

- `age_deploy.prototxt`
- `age_net.caffemodel`
- `gender_deploy.prototxt`
- `gender_net.caffemodel`
- `opencv_face_detector.pbtxt`
- `opencv_face_detector_uint8.pb`

### Model Sources:

- **Face Detection**: [OpenCV Face Detection Model](https://github.com/opencv/opencv)
- **Age and Gender Detection**: You can find pre-trained models for age and gender detection from multiple sources or train your own using frameworks like TensorFlow or PyTorch.

## Technologies Used

- **Django**: For backend development and handling web requests.
- **OpenCV**: For image processing and detecting age and gender from uploaded images.
- **HTML/CSS**: For frontend development to display the web interface.
- **JavaScript (Optional)**: For additional frontend interactions.

## Contributing 🤝

Feel free to fork this project and make contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Create a pull request.

## License 📄

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments 🙏

- **OpenCV**: For providing the powerful computer vision library used in this project.
- **Pre-trained Models**: Used for face detection, age, and gender prediction.

---

This `README.md` file includes the essential details about the project, its features, and instructions for setting up and running the app. It also encourages contributions and provides a brief overview of the technologies used.
