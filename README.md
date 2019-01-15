# tensorflow-serving-hot-reload

A script to dynamically load / unload tensorflow models in serving using serving config file.

## Requirements

- `tensorflow===1.12.0`
- `tensorflow-serving-api===1.12.0`

## Usage

`python reload.py -c /home/user/models.config -H 192.168.2.2:8500`
