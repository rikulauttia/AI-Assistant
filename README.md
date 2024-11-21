# AI-Powered Conversational Assistant

## Project Overview

The **AI-Powered Conversational Assistant** is a project aimed at building a user-friendly chatbot application powered by AI. It combines cutting-edge technologies such as TensorFlow and Keras for model development, Angular for frontend design, and Firebase for backend services. This project is a perfect way to strengthen your skills in AI/ML, web development, and cloud integration.

---

## Features

- AI-based conversational assistant trained using TensorFlow and Keras.
- Real-time chat interface built with Angular.
- Firebase integration for user authentication and real-time database.
- Backend API using Flask to serve the trained AI model.
- Scalable deployment options with GCP or AWS.

---

## Tools and Technologies

- **Programming Languages:** Python, TypeScript
- **Frameworks:** TensorFlow, Keras, Angular, Flask
- **Cloud Services:** Firebase, GCP (Google Cloud Platform), AWS (Amazon Web Services)
- **Libraries:** pandas, numpy, scikit-learn, Flask-CORS
- **Other Tools:** Node.js, Firebase CLI, Angular CLI

---

## Learning Goals

This project is designed to help you:

1. Understand and apply AI/ML concepts using TensorFlow and Keras.
2. Build a modern web frontend with Angular.
3. Use Firebase for backend services like authentication and database management.
4. Deploy AI models and web apps to scalable cloud platforms like GCP or AWS.
5. Work end-to-end on a real-world AI/ML project.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- Node.js and npm
- Angular CLI (`npm install -g @angular/cli`)
- Firebase CLI (`npm install -g firebase-tools`)
- TensorFlow and Keras libraries

---

## How to Run the Project

### **1. Clone the Repository**

```bash
git clone https://github.com/rikulauttia/AI-Assistant.git
cd AI-Assistant
```

### **2. Install Required Libraries**

```bash
pip install tensorflow keras flask flask-cors pandas numpy scikit-learn
```

### **3. Train the AI Model**

Add your dataset to the data folder.
Run the training script:

```bash
python train_model.py
```

The trained model (chatbot_model.h5) will be saved in the backend folder.

### **4. Start the Flask Backend**

```bash
python app.py
```

## Frontend: Angular Chat Interface

### **Set Up the Frontend**

```bash
cd frontend
npm install
ng serve
```

Access the frontend at http://localhost:4200.

## Firebase: Backend Services

### **Initialize Firebase**

```bash
firebase login
firebase init
```

Deploy Firebase Functions

```bash
firebase deploy --only functions
```

## Project Structure

```bash
AI-Assistant/
├── backend/ # Backend files
│ ├── venv/ # Virtual environment (ignored by .gitignore)
│ ├── train_model.py # Training script
│ ├── app.py # Flask API
│ ├── chatbot_model.h5 # Trained model
│ └── data/ # Dataset folder
├── frontend/ # Angular frontend
│ ├── src/ # Source code for frontend
│ ├── node_modules/ # Node dependencies
│ └── angular.json # Angular config
├── .gitignore # Ignored files
└── README.md # Project documentation
```

## License

This project is licensed under the MIT License.
