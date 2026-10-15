# Deployment Notes

## NVIDIA Jetson

Typical deployment considerations:

- validate the exact JetPack / CUDA / PyTorch / Ultralytics compatibility set
- prefer hardware-accelerated decode where the camera pipeline supports it
- benchmark model latency on the target device rather than quoting desktop results
- keep stream acquisition separate from inference to avoid stale-frame buildup

## Raspberry Pi 5 + Hailo AI HAT

The professional project also included edge-inference work using a **Raspberry Pi 5 with a Hailo AI HAT accelerator**.

Deployment considerations include:

- use a model and runtime supported by the installed Hailo software stack
- validate the model conversion / compiled artifact against the exact accelerator and runtime version
- benchmark end-to-end video processing on the target Raspberry Pi rather than transferring desktop or Jetson results
- keep camera acquisition, preprocessing, inference, tracking, and visualization timing separate when profiling
- monitor CPU load, memory, thermals, dropped frames, and accelerator utilization
- keep private compiled model artifacts and production deployment configuration outside the public repository unless they are explicitly distributable

The repository does not claim a Hailo-specific FPS result without a reproducible model, runtime, input-size, and hardware configuration.

## Raspberry Pi

For Raspberry Pi-class hardware without the Hailo path:

- use a model/runtime appropriate for the available accelerator
- keep resolution and image size aligned with the latency target
- monitor temperature, CPU load, memory, and dropped frames

## Network streams

Never commit real RTSP usernames, passwords, private IPs, or camera URLs. Use environment variables or local configuration outside Git for credentials.
