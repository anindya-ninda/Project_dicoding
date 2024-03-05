# Bike Data Sharing

## Setup environment
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
```

## Run steamlit app
```
pip install streamlit
%%writefile app.py
! wget -q -O - ipv4.icanhazip.com
! streamlit run app.py & npx localtunnel --port 8501
```
