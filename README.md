# 🧠 AI Microexpression Stress Analyzer

An **AI-based facial microexpression analyzer** that detects **Calm, Mild Stress, and High Stress** in real time using a webcam.

The system analyzes **subtle facial movements (microexpressions)** such as eyebrow raises, lip tension, blinking rate, and facial symmetry to estimate stress levels.

---

# 🚀 Features

* Real-time **webcam stress detection**
* Detects **3 stress levels**

  * 🟢 Calm
  * 🟡 Mild Stress
  * 🔴 High Stress
* Uses **MediaPipe Face Mesh** for facial landmark detection
* Feature engineering based on **facial muscle movement**
* Lightweight and runs **locally on CPU**
* Simple modular Python architecture

---

# 🧠 How It Works

The system processes webcam frames and extracts **facial landmarks** using MediaPipe Face Mesh.

From these landmarks, the system computes several facial stress indicators:

| Feature            | Description                        |
| ------------------ | ---------------------------------- |
| Eyebrow Raise      | Measures eyebrow movement          |
| Lip Tension        | Measures lip compression           |
| Blink Rate         | Eye closing frequency              |
| Facial Symmetry    | Detects asymmetric stress movement |
| Head Nod Intensity | Measures head motion               |

These features are combined into a **stress score** using weighted calculations.

```
Stress Score =
20 × eyebrow_raise +
18 × lip_tension +
15 × blink_rate +
12 × symmetry_delta +
10 × head_nod_intensity
```

Based on the score:

| Score Range | Stress Level |
| ----------- | ------------ |
| 0 – 3       | Calm         |
| 3 – 6       | Mild Stress  |
| 6 – 10      | High Stress  |

---

# 📂 Project Structure

```
AI-Microexpression-Analyzer
│
├── main.py
├── face_mesh_module.py
├── feature_engineering.py
├── stress_model.py
├── data_logger.py
├── requirements.txt
└── README.md
```

### File Descriptions

| File                     | Purpose                                               |
| ------------------------ | ----------------------------------------------------- |
| `main.py`                | Main program that runs the webcam and stress analysis |
| `face_mesh_module.py`    | Captures facial landmarks using MediaPipe             |
| `feature_engineering.py` | Extracts facial microexpression features              |
| `stress_model.py`        | Calculates stress score and classification            |
| `data_logger.py`         | Logs detected stress values                           |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/AI-Microexpression-Analyzer.git
cd AI-Microexpression-Analyzer
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

Or manually install:

```
pip install opencv-python mediapipe numpy pandas tensorflow
```

---

# ▶️ Run the Project

```
python main.py
```

Optional debug mode:

```
python main.py --verbose
```

---

# 📸 Example Output

```
Stress Score: 2.3
Status: Calm

Stress Score: 4.8
Status: Mild Stress

Stress Score: 7.1
Status: High Stress
```

The system continuously updates based on your **facial microexpressions**.

---

# 🧪 Applications

This project can be used for:

* Stress monitoring
* Human behavior analysis
* Mental health studies
* AI emotion detection research
* Interview stress analysis
* Smart wellness systems

---

# 🔧 Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* TensorFlow
* Computer Vision
* Feature Engineering

---

# 📊 Future Improvements

Possible upgrades:

* Deep learning emotion recognition
* Stress graph visualization
* Streamlit dashboard
* Dataset training with CNN models
* Mobile app integration
* Real microexpression datasets

---

# 👨‍💻 Author

**Priyansu Sikdar**

AI | Computer Vision | Machine Learning Projects

---

# ⭐ If You Like This Project

Give the repository a **star ⭐ on GitHub** and share it with others!
