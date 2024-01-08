#!/usr/bin/python3
from PIL import Image
logo = Image.open("/home/kish/AI-ML-production_optimizer/examples/icon.ico")
logo.save("/home/kish/AI-ML-production_optimizer/examples/icon.ico", format='ICO')
