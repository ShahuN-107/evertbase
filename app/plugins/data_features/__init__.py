from flask_plugins import connect_event
from flask import Blueprint, render_template_string, flash
from manage import AppPlugin
from .extract_reasonable import test_one
from .extract_full import test_two
import os
import glob


__plugin__ = "DataFeatures"

data_features = Blueprint('data_features', __name__)

class DataFeatures(AppPlugin):

    def setup(self):
        connect_event("DataFeatures", test_one)
        connect_event("DataFeatures", test_two)
