import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA


# * id_cliente => df_bill_atm
# * limit_credito => df_bill_atm
# * nivel de educacion => df_card_pay_atm
#  * sexo => df_bill_atm
# * state_civil => df_card_paynext
print("inicando")
#ver columnaas
print(df.columns.tolist())