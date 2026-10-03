# Dog Breed Image Classifier

## Project goal
This project evaluates pretrained CNNs for dog detection and breed classification. It is a classic image-classification task that compares multiple model architectures to see which one performs best on the provided dataset.

## What is implemented
The repository contains the full Udacity-style image classification workflow:
- `check_images.py` orchestrates the evaluation run
- `get_input_args.py` reads CLI arguments
- `get_pet_labels.py` extracts labels from image filenames
- `classify_images.py` runs the model and compares predictions
- `adjust_results4_isadog.py` checks whether the model correctly identifies dog vs. non-dog images
- `calculates_results_stats.py` summarizes model accuracy
- `print_results.py` prints the evaluation summary

The code evaluates these architectures:
- AlexNet
- VGG
- ResNet

This is a pretrained-model evaluation workflow, not a custom model training pipeline.

## Typical run
```bash
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```

You can also run the batch comparison script:
```bash
sh run_models_batch.sh
```

## Required data
The project expects a `pet_images/` directory and `dognames.txt` in the project root. Those assets are part of the assignment data and are necessary to reproduce the run.

This repository includes recorded output files for the evaluation runs:
- `resnet_pet-images.txt`
- `alexnet_pet-images.txt`
- `vgg_pet-images.txt`

## Recorded results
The repository contains an output file for the ResNet run. The recorded result shows:
- `pct_match`: 82.50
- `pct_correct_dogs`: 100.00
- `pct_correct_breed`: 90.00
- `pct_correct_notdogs`: 90.00

This is a recorded assignment result for the included dataset, not a claim about broader benchmark performance.

## Limitations
- The project does not fine-tune a custom CNN from scratch.
- It relies on pretrained model weights and the provided assignment dataset.
- The `pet_images/` folder is required to reproduce the run locally.

## Tools used
- Python
- PyTorch / pretrained CNNs
- Image classification workflow scripts

## Attribution
This project follows the structure of a standard Udacity-style AI programming assignment and uses a pretrained CNN evaluation workflow.
