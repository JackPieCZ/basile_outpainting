import torch
import torchvision
from outpainting.basile.basile import load_model


def initialize_basile(weights):
    print(f"Initializing basile outpainting (model {weights.split('/')[-1]})...")
    return load_model(weights)
