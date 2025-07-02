# AttendEase

A real-time facial recognition attendance system using OpenCV, Keras (CNN), and Streamlit. The system supports attendance marking through both a Convolutional Neural Network (CNN) and K-Nearest Neighbors (KNN) classifier.

---

## 📁 Project Structure

```
.
├── data/                            # Stores face data and models
│   ├── haarcascade_frontalface_default.xml
│   ├── faces_data.pkl
│   ├── names.pkl
│   └── label_encoder.pkl
├── Attendance/                      # Automatically stores daily attendance logs
├── background.png                   # Frame overlay background
├── dashboard_app.py                 # Streamlit dashboard
├── face_data_collection.py          # Collects face images and names
├── train_cnn_model.py               # Trains CNN model
├── test_cnn_attendance.py           # Attendance via CNN
├── test_knn_attendance.py           # Attendance via KNN
└── requirements.txt
```

---

## 🚀 Features

- Collect and label face data via webcam
- Train CNN model to recognize faces
- Mark attendance using CNN or KNN
- Overlay background UI
- Live Streamlit dashboard showing daily logs

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/face-attendance-system.git
cd face-attendance-system
```

### 2. (Optional) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📷 Collect Face Data

Run the following to collect 100 face samples of a person:

```bash
python face_data_collection.py
```

- Enter the name when prompted.
- Press **`q`** to quit early or let it auto-stop after collecting 100 samples.

---

## 🧠 Train CNN Model

After collecting sufficient face data:

```bash
python train_cnn_model.py
```

This creates `face_cnn_model.h5` and `data/label_encoder.pkl`.

---

## 🧪 Test Attendance System

### A. Using CNN

```bash
python test_cnn_attendance.py
```

### B. Using KNN

```bash
python test_knn_attendance.py
```

- Press **`o`** to mark attendance.
- Press **`q`** to quit.

Attendance gets saved in `Attendance/Attendance_<DD-MM-YYYY>.csv`.

---

## 📊 View Dashboard

Use Streamlit to view the attendance records:

```bash
streamlit run dashboard_app.py
```

Ensure you have some entries in the `Attendance/` folder for it to display.

---

## ⚠️ Notes

- Make sure a webcam is available.
- The file `data/haarcascade_frontalface_default.xml` is required for detection.
  Download it here:  
  https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
- Place it in the `data/` directory.
- `background.png` is used as an overlay for UI; it must exist in the root directory.

---

## 📂 Directory Setup

If not present, create these:

```bash
mkdir -p data Attendance
```

And place the necessary `haarcascade_frontalface_default.xml` inside `data/`.

---

## 🙋 FAQ

**Q: I get a ModuleNotFoundError for `win32com.client`?**  
A: This is used for text-to-speech on Windows. It only works on Windows via `SAPI`.  
If you're on Linux/macOS, comment out or remove the `speak()` function and its calls.

---

## 📧 Contact

For issues or enhancements, feel free to open an issue or submit a pull request.
