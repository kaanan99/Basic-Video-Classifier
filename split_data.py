import os

from sklearn.model_selection import train_test_split
from typing import List

def write_split_file(name:str, video_paths:List, labels:List[str]) -> None:
    # Open file/create new one
    split_file = open(f"./{name}.txt", "w")

    # Write each line
    for idx in range(len(video_paths)):
        line = f"{video_paths[idx]} {labels[idx]}\n"
        split_file.write(line)

    # Close file
    split_file.close()

def main():
    video_base_directory = "./UCF11_updated_mpg/UCF11_updated_mpg"
    video_classes = os.listdir(video_base_directory)


    # Get all video names
    all_video_paths = []
    all_classes = []

    for class_ in video_classes:
        video_folders = [video_folder for video_folder in os.listdir(f"{video_base_directory}/{class_}") if video_folder != "Annotation"]

        for video_folder in video_folders:
            video_names = os.listdir(f"{video_base_directory}/{class_}/{video_folder}")

            for video in video_names:
                video_path = f"{video_base_directory}/{class_}/{video_folder}/{video}"
                all_video_paths.append(video_path)
                all_classes.append(class_)

    # Split into train, validation, and test splits
    training_video, testing_video, training_label, testing_label = train_test_split(all_video_paths, all_classes, train_size=.8)
    training_video, validation_video, training_label, valtidation_label = train_test_split(training_video, training_label, train_size=.8)

    # Save paths and labels
    write_split_file("training", training_video, training_label)
    write_split_file("validation", validation_video, valtidation_label)
    write_split_file("testing", testing_video, testing_label)

if __name__ == "__main__":
    main()