# -*- coding: utf-8 -*-

__author__ = """Christoph Rist"""
__email__ = "c.rist@posteo.de"

from .particles import add_voxels, add_point_cloud, add_flow_mesh, add_boxes
from .scene_setup import setup_scene, add_cameras_default
from .system_setup import setup_system
from .object_spotlight import add_spotlight_ground
from .cli import process_file


__all__ = [
    "add_boxes",
    "add_voxels",
    "add_point_cloud",
    "add_cameras_default",
    "add_flow_mesh",
    "setup_scene",
    "setup_system",
    "add_spotlight_ground",
    "process_file",
]
