# GuardianEcho

GuardianEcho is a desktop assistant that listens for ambient sounds and can trigger emergency alerts. It uses **Kivy** for the interface and relies on **TensorFlow** and **scikit-learn** for sound classification.

## Features
- Real-time sound detection and classification
- Optional location and WhatsApp message alerts
- GUI built with Kivy
- Supports SVM and neural network models
- Dataset tools for custom training

## Installation
```bash
git clone https://github.com/Adityarajsingh2904/GuardianEcho
cd GuardianEcho
python -m venv .venv  # optional
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
Start the application:
```bash
python main.py
```

Classify a single file:
```bash
python sound_classifier_nueral.py --file path/to/audio.wav
```

## Contributing
Contributions are welcome! Fork the repository, create a new branch for your changes and open a pull request when ready.

## License
Distributed under the **MIT License**. See the `LICENSE` file for details.
