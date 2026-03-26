import logging
import os
from datetime import datetime

# 1. Only define the filename here (no slashes)
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# 2. Define the directory where you want the logs to live
logs_dir = os.path.join(os.getcwd(), "logs")

# 3. Create that directory
os.makedirs(logs_dir, exist_ok=True)

# 4. Join the directory and the filename once
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")