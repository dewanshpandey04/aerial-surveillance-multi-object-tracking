# Performance

## Measured project results

The original project work included:

- custom aerial YOLO detectors with **mAP50 > 0.92**
- optimized live-camera edge inference at **50+ FPS**
- real-time detection and tracking of humans, UAVs, tanks, vehicles, and other ground objects
- deployment work on **NVIDIA Jetson**, **Raspberry Pi 5**, and **Raspberry Pi 5 with Hailo AI HAT acceleration**

These measurements refer to the original project environment. Private datasets, production model weights, camera feeds, compiled Hailo model artifacts, and the exact deployment configuration are not distributed with this repository.

The **50+ FPS** result describes the original optimized live-camera project configuration and is not presented as a Hailo-specific benchmark unless the exact Hailo model/runtime/hardware configuration is stated separately.

## Local benchmarking

Use the included benchmark utility on the target hardware:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

Record the model, input size, device, precision, accelerator/runtime, and source pipeline alongside any FPS or latency result.
