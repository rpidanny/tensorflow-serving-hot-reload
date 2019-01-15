# tensorflow-serving-hot-reload

A script to dynamically load / unload tensorflow models in serving using serving config file.

## Requirements

- `tensorflow===1.12.0`
- `tensorflow-serving-api===1.12.0`

## Usage

`python reload.py -c /home/user/models.config -H 192.168.2.2:8500`

### Example serving config file

```
model_config_list: {
  config: {
    name:"FLOWER_5flowers",
    base_path: "/serving/models/FLOWER/serving/FLOWER_5flowers",
    model_platform: "tensorflow"
  },
  config: {
    name:"FLOWER_alpha",
    base_path: "/serving/models/FLOWER/serving/FLOWER_alpha",
    model_platform: "tensorflow"
  },
  config: {
    name:"FLOWER_test",
    base_path: "/serving/models/FLOWER/serving/FLOWER_test",
    model_platform: "tensorflow"
  }
}
```