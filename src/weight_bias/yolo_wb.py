import wandb
from wandb.integration.ultralytics import add_wandb_callback

from ultralytics import YOLO

# Initialize a Weights & Biases run
wandb.init(project="ultralytics", job_type="training")

# Load a YOLO model
model = YOLO("yolov8n.pt")

# Add W&B Callback for Ultralytics
add_wandb_callback(model, enable_model_checkpointing=True)

# Train and Fine-Tune the Model
model.train(project="ultralytics", data="coco8.yaml", epochs=5, imgsz=640)

# Validate the Model
model.val()

# Perform Inference and Log Results
# model(["path/to/image1", "path/to/image2"])

# Finalize the W&B Run
wandb.finish()