# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 16:33:16 2023

@author: arkob
"""

import glassdoor_data_scrapper as gs

import pandas as pd

path = "C:/Users/Public/chromedriver_win32"

df = gs.get_jobs("Data Analyst", 15, False, path, 15)