# Base image with Python
FROM python:3.12-slim

# Set working directory
WORKDIR /project_root

# Install system dependencies including Pango and other required libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the working directory
COPY . .

# Replacement of the Stearmlit index.html with their unbreakable logo and title
RUN cp app/style/index.html \
    $(python -c "import sysconfig; print(sysconfig.get_paths()['purelib'])")/streamlit/static/index.html

# Expose the port for Streamlit
# EXPOSE 00000

# Add a health check for Streamlit app
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app
# ENTRYPOINT ["streamlit", "run", "app/01_Home.py", "--server.port=0000", "--server.address=0.0.0.0"]
