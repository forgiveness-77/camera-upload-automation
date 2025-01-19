import os
import time
import shutil
import subprocess

# Configuration
WATCH_FOLDER = "capture"
UPLOADED_FOLDER = "uploads"
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
UPLOAD_ATTRIBUTE = "imageFile"
CHECK_INTERVAL = 5  # Time in seconds to wait between folder checks
UPLOAD_DELAY = 30   # Time in seconds before uploading new files

def upload_file(file_path):
    """Uploads a file using the curl command."""
    try:
        command = [
            "curl", "-X", "POST",
            "-F", f"{UPLOAD_ATTRIBUTE}=@{file_path}",
            UPLOAD_URL
        ]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"[SUCCESS] Uploaded: {file_path}")
            return True
        else:
            print(f"[ERROR] Failed to upload {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] Exception occurred while uploading {file_path}: {e}")
        return False

def monitor_and_upload():
    """Monitors the folder, uploads new files, and moves them to another folder."""
    if not os.path.exists(UPLOADED_FOLDER):
        os.makedirs(UPLOADED_FOLDER)

    print(f"[INFO] Monitoring folder: {WATCH_FOLDER}")
    uploaded_files = set()

    while True:
        try:
            files = [
                os.path.join(WATCH_FOLDER, f)
                for f in os.listdir(WATCH_FOLDER)
                if os.path.isfile(os.path.join(WATCH_FOLDER, f))
            ]

            for file_path in files:
                if file_path not in uploaded_files:
                    print(f"[INFO] New file detected: {file_path}")
                    time.sleep(UPLOAD_DELAY)

                    if upload_file(file_path):
                        # Move file to uploaded folder
                        shutil.move(file_path, os.path.join(UPLOADED_FOLDER, os.path.basename(file_path)))
                        uploaded_files.add(file_path)
                        print(f"[INFO] Moved {file_path} to {UPLOADED_FOLDER}")

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("[INFO] Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")

if __name__ == "__main__":
    monitor_and_upload()
