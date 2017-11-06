#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

source_data = pd.read_excel("data.xlsx")
source_data.plot.bar()
plt.show()
