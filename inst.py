import subprocess
import os

subprocess.run(["apt-get", "-y", "install", "build-essential", "python3-dev", "ffmpeg"])

subprocess.run(["pip3", "install", "--upgrade", "setuptools", "wheel"])
subprocess.run(["pip3", "install", "--upgrade", "pip"])  
subprocess.run(["pip3", "install", "faiss-cpu==1.7.2", "fairseq", "gradio==3.14.0", 
               "ffmpeg", "ffmpeg-python", "praat-parselmouth", "pyworld", 
               "numpy==1.23.5", "numba==0.56.4", "librosa==0.9.2"])

subprocess.run(["pip3", "install", "torch", "torchvision", "torchaudio"])

subprocess.run(["mkdir", "rmvpe-ai"])
os.chdir("/kaggle/working/rmvpe-ai")

subprocess.run(["pip", "install", "-r", "requirements.txt"])
