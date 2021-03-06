"""
Runs a model on the CPU on a single node.
"""
import os
from argparse import ArgumentParser

import numpy as np
import torch

import pytorch_lightning as pl
from pl_examples.models.lightning_template import LightningTemplateModel

pl.seed_everything(234)


def main(args):
    """
    Main training routine specific for this project
    :param args:
    """
    # ------------------------
    # 1 INIT LIGHTNING MODEL
    # ------------------------
    model = LightningTemplateModel(**vars(args))

    # ------------------------
    # 2 INIT TRAINER
    # ------------------------
    trainer = pl.Trainer.from_argparse_args(args)

    # ------------------------
    # 3 START TRAINING
    # ------------------------
    trainer.fit(model)


if __name__ == '__main__':
    # ------------------------
    # TRAINING ARGUMENTS
    # ------------------------
    # these are project-wide arguments
    root_dir = os.path.dirname(os.path.realpath(__file__))
    parent_parser = ArgumentParser(add_help=False)

    # each LightningModule defines arguments relevant to it
    parser = LightningTemplateModel.add_model_specific_args(parent_parser, root_dir)
    parser = pl.Trainer.add_argparse_args(parser)
    args = parser.parse_args()

    # ---------------------
    # RUN TRAINING
    # ---------------------
    main(args)
