# Deployment Notes

## NVIDIA Jetson

Typical deployment considerations:

- validate the exact JetPack / CUDA / PyTorch / Ultralytics compatibility set
- prefer hardware-accelerated decode where the camera pipeline supports it
- benchmark model latency on the target device rather than quoting desktop results
- keep stream acquisition separate from inference to avoid stale-frame buildup

## Raspberry Pi

For Raspberry Pi-class hardware:

- use a model/runtime appropriate for the available accelerator
- keep resolution and image size aligned with the latency target
- monitor temperature, CPU load, memory, and dropped frames

## Network streams

Never commit real RTSP usernames, passwords, private IPs, or camera URLs. Use environment variables or local configuration outside Git for credentials.
