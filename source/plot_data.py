import numpy as np
from matplotlib import pyplot as plt
import torch
from torch import Tensor
import os

from config import get_system_device, data_path, plot_path


def plot_model_inference(model, test_datasets, n_rows=5, n_cols=10, device=get_system_device()):
    # Get a batch of images and labels from the dataset
    images, labels = next(iter(test_datasets))

    # Convert the tensor to numpy for visualization
    images_numpy = images.cpu().numpy()

    # Move the input tensors to the device
    tensor_images = images.to(device)
    # Plot the images
    fig = plt.figure(figsize=(15, 7))

    # Display n_rows*n_cols images
    for idx in np.arange(n_rows * n_cols):
        ax = fig.add_subplot(n_rows, n_cols, idx + 1, xticks=[], yticks=[])
        ax.imshow(np.squeeze(images_numpy[idx]), cmap='gray')
        # Get the model's prediction
        prediction = model(tensor_images[idx].unsqueeze(0))
        # Print out the predicted label for each image
        ax.set_title(str(prediction.argmax(1).item()),
                     color=("limegreen" if prediction.argmax(1).item() == labels[idx] else "red"), fontsize=25)

    inference_dataset_path = os.path.join(plot_path, 'sample_model_inference.png')
    os.makedirs(plot_path, exist_ok=True)
    plt.savefig(inference_dataset_path, bbox_inches='tight')
    plt.show()


def plot_dataset(datasets: Tensor):
    # Get a batch of images and labels from the dataset
    images, labels = next(iter(datasets))

    # Convert the tensor to numpy for visualization
    images_numpy = images.cpu().numpy()

    # Plot the images
    fig = plt.figure(figsize=(10, 10))

    n_rows = 5
    n_cols = 5
    # Display n_rows*n_cols images
    for idx in np.arange(n_rows * n_cols):
        ax = fig.add_subplot(n_rows, n_cols, idx + 1, xticks=[], yticks=[])
        ax.imshow(np.squeeze(images_numpy[idx]), cmap='gray')
        # Print out the predicted label for each image
        ax.set_title(labels[idx].cpu().numpy(), fontsize=25)

    plt.subplots_adjust(hspace=1)
    plt.suptitle("Dataset", y=0.98, fontsize=25)  # for some reason the title is not showing up
    # in the Pycharm IDE. if you want the best image experience it is recommended to open
    # the image in an image viewer

    # create the sample dataset image directory if it does not exist
    os.makedirs(plot_path, exist_ok=True)

    # save the image to the sample dataset directory
    sample_dataset_path = os.path.join(plot_path, 'sample_dataset.png')
    print(f"Saving the sample dataset image to {sample_dataset_path}")
    plt.savefig(sample_dataset_path, bbox_inches='tight')
    plt.show()
