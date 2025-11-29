
## CODESENSE AI 
![App Preview](https://github.com/Tharunes/CodeSense-AI/blob/main/c99b11bc-0928-4d11-9b55-e8fa68e84d65.png?raw=true)


## 🎥 Demo Video

Click below to watch the prototype demo:
[▶ Watch Demo](Prototype_Demo/Screen%20Recording%202025-11-29%20185258.mp4)

# CodeSense AI - AI-Powered Code Analysis

A powerful web application that helps developers understand code through AI-powered analysis. Simply paste your Python, JavaScript, or C code and get detailed explanations, step-by-step breakdowns, time complexity analysis, beginner-friendly versions, and error predictions.


## Features
- **Multi-Language Support**: Analyze Python, JavaScript, and C code  
- **Simple Explanations**: Get clear, concise explanations of what your code does  
- **Step-by-Step Analysis**: Break down code execution into logical steps  
- **Complexity Analysis**: Understand time and space complexity with Big O notation  
- **Beginner-Friendly Rewrites**: Get simplified versions of complex code  
- **Error Prediction**: Identify potential bugs and issues before they happen  
- **Modern UI**: Beautiful, responsive interface with animations and smooth interactions  
- **Syntax Highlighting**: Professional code editor with syntax highlighting  
- **Language Auto-Detection**: Automatically detects the programming language  


## Installation

### 1. Install Ollama and Mistral Model
Install Ollama by following instructions at https://ollama.com/.

Then pull the Mistral model:

```bash

ollama pull mistral

```


## Requirements
- Python 3.8+  
- Django 4.2+  
- Ollama with Mistral model installed  
- Modern web browser with JavaScript enabled  


## Install dependencies

pip install django requests


## Run the application

python AI_reviewer.py runserver


Open the application at:
http://127.0.0.1:8000/

## Usage

1.Open your browser and go to http://127.0.0.1:8000/

2.Paste your Python, JavaScript, or C code into the code editor

3.Select the programming language or choose auto-detect

4.Choose the analysis type

5.Click the analysis button

6.View the AI generated explanation in the results panel







