# Text-to-Speech
Python implementation for converting text to speech using Google's Text-to-Speech API.

## Overview

This project demonstrates how to convert text to speech in Python using the `gTTS` (Google Text-to-Speech) library. gTTS is a powerful Python library and command-line tool that interfaces with Google Translate's text-to-speech API, enabling you to generate spoken audio from text input.

## Features

- Convert any text to natural-sounding speech
- Generate MP3 audio files from text input
- Support for multiple languages
- Simple and clean implementation with minimal code
- Command-line friendly interface

## What is gTTS?

**gTTS** (Google Text-to-Speech) is a Python library that:
- Interfaces with Google Translate's text-to-speech API
- Converts text into spoken MP3 audio data
- Supports output to files or stdout
- Provides both library and command-line functionality

## Requirements

- Python 3.x
- gTTS library

## Installation

```bash
pip install gTTS
```

## Usage

The implementation is straightforward and requires just a few lines of code:

```python
from gtts import gTTS

text = "Hello, how are you?"
language = 'en'
obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")
```

## Getting Started

1. Clone this repository
2. Install the required dependencies
3. Run the Python script
4. Listen to the generated MP3 file

## About

This project showcases the simplicity and power of Python for text-to-speech conversion, demonstrating how complex functionality can be achieved with minimal code using the right libraries.
