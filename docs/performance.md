# Professional Results and Public Benchmarking

## Original professional project

The resume-backed project work includes:

- custom aerial YOLO detectors with **mAP50 above 0.92**
- optimized live-camera edge inference at **50+ FPS**
- real-time detection and tracking of humans, UAVs, tanks, vehicles, and other ground objects
- deployment work on NVIDIA Jetson and Raspberry Pi-class systems

These results refer to the original professional environment and are not automatically reproducible from this public repository because private datasets, trained production weights, and exact deployment configuration are excluded.

## Public benchmarking

Use the included script for your own hardware:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

Record the model, input size, device, precision, and stream pipeline alongside any published FPS number.
