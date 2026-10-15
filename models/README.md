# Model Artifacts

Production model weights and private datasets are not stored in this repository.

Use a local model path at runtime:

```powershell
python -m src.surveillance --model path\to\model.pt --source path\to\video.mp4 --show
```

For NVIDIA Jetson, use a PyTorch/runtime build compatible with the target JetPack and CUDA version.

Do not commit employer-owned weights, customer footage, private datasets, credentials, or confidential deployment artifacts.
