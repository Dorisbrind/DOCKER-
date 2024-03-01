# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# add the app.py file to the working directory inside the container
ADD apps/ .

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "--server.port=8501", "app.py"]
