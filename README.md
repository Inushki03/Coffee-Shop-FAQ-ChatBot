# Coffee Shop FAQ Chatbot

A simple FAQ chatbot for a coffee shop built using Python.

## Description

This chatbot answers frequently asked questions (FAQs) related to a coffee shop. It uses fuzzy string matching to find the best matching question from a set of predefined FAQs stored in a JSON file.

## Libraries Used

- **Flask**: To create the web interface and backend server.
- **FuzzyWuzzy**: For fuzzy string matching to handle approximate user queries.

## Features

- Users can type their questions about the coffee shop.
- The chatbot finds the closest matching question from the FAQ database.
- Provides relevant answers based on stored FAQs.

## Project Structure

- `app.py` — main Flask application.
- `faqs.json` — JSON file containing FAQs.
- `templates/` — HTML templates for the chatbot interface.
- `static/` — static files like CSS and images.




