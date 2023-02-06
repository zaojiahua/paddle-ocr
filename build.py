import os

cmd = "git clone -b gpus http://myj:god1095god@10.0.0.57:8251/backend/coral-ocr.git && " \
      "cd coral-ocr && " \
      "docker-compose up --build"

if "coral_ocr" in os.listdir("."):
    cmd = "cd ~/coral-ocr && " \
          "docker-compose down && " \
          "cd .. && " \
          "rm -rf coral-ocr/ && " + cmd

os.system(cmd)
