# Camera Upload Automation

## Overview
This repository contains a Python script designed to automate the monitoring, uploading, and organization of images captured by a camera. The script ensures efficient and seamless management of image files for IoT and image processing workflows.

## Features
- **Folder Monitoring:** Automatically detects new image files in a specified folder.
- **Automated Uploading:** Uses `curl` to upload files to a server after a delay.
- **File Management:** Moves successfully uploaded files to a designated folder to avoid redundancy.

## Requirements
1. **Python**: Ensure Python 3.x is installed.
2. **Curl**: Curl must be installed and available in your system's PATH.

## Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/camera-upload-automation.git
cd camera-upload-automation
```

### Step 2: Configure the Script
Open the script and modify the following variables:
- `WATCH_FOLDER`: Path to the folder where the camera saves pictures.
- `UPLOADED_FOLDER`: Path to the folder where uploaded pictures will be moved.
- `UPLOAD_URL`: URL to upload the images.

Example:
```python
WATCH_FOLDER = r"C:\\path\\to\\your\\capture_folder"
UPLOADED_FOLDER = r"C:\\path\\to\\your\\uploaded_folder"
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
```

### Step 3: Install Dependencies
No additional Python libraries are required for this script as it uses built-in modules.

### Step 4: Run the Script
Run the script from the terminal or command prompt:
```bash
python upload_automation.py
```

## How It Works
1. The script continuously monitors the specified folder for new image files.
2. When a new file is detected:
   - It waits for 30 seconds to ensure the file is ready for upload.
   - Uploads the file using a `curl` POST request.
   - If the upload succeeds, the file is moved to the `UPLOADED_FOLDER`.
3. Logs are printed for each operation, indicating success or errors.

## Example Curl Command
```bash
curl -X POST -F imageFile=@/path/to/your/image.jpg <upload_url>
```




