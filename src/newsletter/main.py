#!/usr/bin/env python
import sys
from newsletter.crew import NewsletterCrew
import streamlit as st


def load_html_template(): 
    with open('/Users/germangirod/Documents/newsletter_crew/newsletter/src/newsletter/config/newsletter_template.html', 'r') as file:
        html_template = file.read()
        
    return html_template

st.title("Wellness Newsletter Generator")

# Define available topics
available_topics = [
    "Mental Health", "Fitness", "Nutrition", "Holistic Health", "Meditation", "Yoga", "Wellness Trends"
]

# Topic selection
selected_topics = st.multiselect("Select Topics", available_topics)

# Generate button
if st.button("Generate Newsletter"):
    if selected_topics:
        inputs = [{'topics': topic, 'html_template': load_html_template()} for topic in selected_topics]   
        crewResult = NewsletterCrew().crew().kickoff_for_each(inputs=inputs)
        print(crewResult)
    else:
        st.error("Please select at least one topic.")


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topics': 'Nutrition',
        'personal_message': 'Hola German',
        'html_template': load_html_template()
    }
    NewsletterCrew().crew().kickoff_for_each(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topics': 'Nutrition',
        'personal_message': 'Hola German',
        'html_template': load_html_template()
    }
    try:
        NewsletterCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
