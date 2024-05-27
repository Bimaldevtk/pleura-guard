import argparse
import time
from pathlib import Path
import torch
import torch.backends.cudnn as cudnn
from numpy import random
from vid_conv import *
import sys
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size,
    check_requirements,
    check_imshow,
    non_max_suppression,
    apply_classifier,
    scale_coords,
    xyxy2xywh,
    strip_optimizer,
    set_logging,
    increment_path,
)
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

##############################Space to Edit##########################################
#####################################################################################
# dirpath=input("Please provide input data path")
# mdl_weight=input("Please provide yolo5s weight file in .pt format")
dirpath = "./data"  ####Please provide your input data path
mdl_weight = "best.pt"  ############Please provide yolo5s weight file in .pt format

###Output will be saved to runs/detect/exp*

######################################################################################
######################################################################################


def make_paths_files():
    for f in os.listdir(dirpath):
        fpath = os.path.join(dirpath, f)
        if os.path.isfile(fpath) and f.endswith(
            (".png", ".jpg", ".jpeg", ".bmp", ".pbm", ".ppm")
        ):
            inp_path = dirpath
        elif os.path.isfile(fpath) and f.endswith((".avi", ".mp4")):
            inp_path = dirpath
        elif os.path.isfile(fpath) and f.endswith((".DCM", ".dcm")):
            dicom2avi(dirpath)
            inp_path = dirpath
        elif os.path.isfile(fpath) and f.endswith(("")):
            unknown2dicom(dirpath, dirpath)
            dicom2avi(dirpath)
            inp_path = dirpath


def detect(save_img=False):
    source, weights, view_img, save_txt, imgsz = (
        opt.source,
        opt.weights,
        opt.view_img,
        opt.save_txt,
        opt.img_size,
    )
    webcam = (
        source.isnumeric()
        or source.endswith(".txt")
        or source.lower().startswith(("rtsp://", "rtmp://", "http://"))
    )

    # Directories
    