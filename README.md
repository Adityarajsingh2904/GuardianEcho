# GuardianEcho 🔊🛡️

*A real-time smart audio-classification engine that listens, understands, and reacts.*

GuardianEcho is an end-to-end **audio-event detection & alerting system**. Using a hybrid of **SVM classifiers** and **deep-learning models** (TensorFlow/Keras), it can distinguish between *speech, screams, shouts, noise* and other categories in real time, then trigger follow-up actions such as notifications, logging or UI cues.

---

## 📚 Table of Contents

1. Features  
2. Architecture & File Map  
3. Branch & Version Strategy  
4. Installation  
5. Quick Start  
6. Usage Examples  
7. Contributing  
8. Roadmap  
9. License  

---

## ✨ Features

- **Real-time Audio Pipeline** – streams microphone input, extracts MFCCs and passes them to the active model.  
- **Dual-Model Support** – choose between fast classical SVMs (`svm_based_model/`) or a Keras CNN (`sound_classifier_nueral.py`).  
- **Dataset Builder** – `datasetmaker.py` lets you curate and label custom WAV datasets.  
- **Extensible UI** – lightweight **Kivy** front-end (`ui.kv`, `main.py`) with live predictions and alert pop-ups.  
- **Configurable Alerts** – trigger sounds, desktop notifications or custom hooks on defined events.  
- **Plug-in Friendly** – drop in a new `saved_model.pb` or additional SVM phases without touching the core logic.  

---

## 🗂️ Architecture & File Map

```text
GuardianEcho/
├── bin/                     # Virtual-env executables (local dev only)
├── config/                  # Log files & runtime configs
├── resources/
│   └── icons/               # UI icon assets
├── svm_based_model/         # Classical SVM classifiers & CSV helpers
├── testing/                 # Sample audio clips for smoke-tests
├── variables/               # Runtime variable storage (pickle / json)
│
├── main.py                  # Kivy entry-point – launches the GUI
├── sound_classifier_nueral.py # CNN-based TF model & inference loop
├── modelloader.py           # Wrapper to load *.pb SavedModels
├── datasetmaker.py          # Command-line dataset creator
├── sound.py                 # Cross-platform audio recording helper
├── requirements.txt         # Python dependencies
└── LICENSE                  # MIT License
```

> **Tip:** See `how_to_use.txt` for a one-page overview.

---

## 🌳 Branch & Version Strategy

| Branch        | Status     | Purpose                                       |
|---------------|------------|-----------------------------------------------|
| `main`        | ✅ Stable   | Production-ready code. All PRs merge here.    |
| `feature/*`   | 🛠️ Active  | For features, bug-fixes or refactors.         |
| `release/*`   | 🚀 Release | Tagged snapshots for versioned builds.        |

---

## 🛠️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/Adityarajsingh2904/GuardianEcho.git
cd GuardianEcho

# 2. (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt
```

> **Note:** TensorFlow and Kivy may require additional system packages.

---

## ⚡ Quick Start

```bash
# Run the GUI application
python main.py

# Directly classify a WAV file
python sound_classifier_nueral.py --file path/to/clip.wav
```

---

## 🖥️ Usage Examples

### 1. Train a New SVM Phase
```bash
python svm_based_model/phase1_speech_vs_noise.py --data /path/to/dataset
```

### 2. Batch-predict WAVs in a folder
```bash
python sound_classifier_nueral.py --folder ./testing --export ./results.csv
```

---

## 🤝 Contributing

1. Fork the repo and create your branch:
```bash
git checkout -b feature/your-feature-name
```
2. Commit your changes and push.
3. Open a Pull Request.

---

## 🗺️ Roadmap

- [ ] Add Voice Activity Detection (VAD) pre-filter  
- [ ] Docker support for containerized deployment  
- [ ] REST API wrapper using FastAPI  
- [ ] Mobile-friendly UI adjustments

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

> Made with ❤️ by **Aditya Raj Singh** – drop a ⭐ if you like the project!