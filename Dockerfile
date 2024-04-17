# # Use an official Python runtime as a parent image, specify the exact version
# FROM python:3.9.0

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Run run.py when the container launches
# CMD ["python", "run.py"]

#========================= aws ======================================
# Use an official Python runtime as a parent image, specify the exact version
# FROM python:3.9.0

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application's code
# COPY . .

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable for Flask
# ENV FLASK_APP=run.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=production

# # Run run.py when the container launches
# CMD ["python", "run.py"]


#===============================azure ===========================================

# Use an official Python runtime as a parent image, specify the exact version
# FROM python:3.9.0

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application's code
# COPY . .

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable for Flask
# ENV FLASK_APP=run.py

# # Run Gunicorn with multiple worker processes
# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "run:app"]

#========================== heroku ===============================

FROM python:3.9.0
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]