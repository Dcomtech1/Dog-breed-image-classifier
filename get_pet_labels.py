#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# get_pet_labels.py
#
# PROGRAMMER: David Gbadamosi
# DATE CREATED: 17/10/2025
# REVISED DATE: 
# PURPOSE: Creates pet labels from image filenames for classification checks.

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function.
    Parameters:
     image_dir - The path to the folder of images (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_label = " ".join([word for word in in_files[idx].lower().split("_") if word.isalpha()]).strip()

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])

    return results_dic
