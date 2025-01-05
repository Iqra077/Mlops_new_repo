---
title: Sentiment Analysis App
emoji: 💬
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.9.1
app_file: app.py
pinned: false
---


# Sentiment Analysis with Hugging Face and Gradio

This app performs sentiment analysis using a pre-trained model from Hugging Face's Transformers library. Built with Gradio, it provides an easy-to-use interface for predicting whether the sentiment of the input text is **positive**, **negative**, or **neutral**.

## Features
- Predicts sentiment (positive, negative, or neutral) based on the input text.
- Provides confidence scores for each prediction.
- Built with MLOps principles for easy updates and continuous deployment.

## How to Use
1. **Enter your text** in the input box.
2. Click **"Submit"** to analyze the sentiment and view the predicted result along with the confidence score.

## Example Inputs:
- **"I love spending time with my family!"** → Positive
- **"This weather is terrible."** → Negative
- **"The movie was okay, not great but not bad."** → Neutral

## Deployment
This app is continuously deployed using **GitHub Actions**. Every time changes are pushed to the `main` branch, the app will automatically update on this Hugging Face Space.

## How It Works
The app uses a pre-trained model from Hugging Face’s `transformers` library to classify the sentiment of any input text. It leverages Gradio to build an interactive web interface.

## Tech Stack
- **Hugging Face**: For the pre-trained sentiment analysis model.
- **Gradio**: For building the interactive web interface.
- **GitHub Actions**: For Continuous Integration and Continuous Deployment (CI/CD).

---

Feel free to test the app by entering text and analyzing its sentiment.

