"""
Note: on Linux you need to run this as well: apt-get install portaudio19-dev

pip install kokoro-onnx sounddevice

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin
python examples/with_log.py
"""

import logging
import sounddevice as sd
import kokoro_onnx
from kokoro_onnx import Kokoro

# You can set the environment variable LOG_LEVEL
# Linux: export LOG_LEVEL=DEBUG
# Windows: $env:LOG_LEVEL="DEBUG"

# Or programmatically
logging.getLogger(kokoro_onnx.__name__).setLevel("DEBUG")

kokoro = Kokoro("kokoro-v0_19.onnx", "voices.bin")
samples, sample_rate = kokoro.create(
    "Hello. This audio generated by kokoro!", voice="af_sarah", speed=1.0, lang="en-us"
)
print("Playing audio...")
sd.play(samples, sample_rate)
sd.wait()
