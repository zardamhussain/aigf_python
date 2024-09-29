# Ai-Gf Python SDK


This package lets you start Ai-Gf calls directly in your Python application.

## Installation

You can install the package via pip:

```bash
pip install aigf_python
```

On Mac, you might need to install `brew install portaudio` to satisfy `pyaudio`'s dependency requirement.

## Usage

First, import the AIGF class from the package:

```python
from aigf_python import AIGF
```

Then, create a new instance of the AIGF class:

```python
gf = AIGF()
```

You can start a new call by calling the `start` method

```python

gf.start()
```

You can stop the session by calling the `stop` method:

```python
gf.stop()
```

This will stop the recording and close the connection.

