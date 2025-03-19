import pandas as pd 
import numpy as np
import sqlite3

# %%
# careful to list your path to the file or save it in the same place as your .qmd or .py file
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)

q = 'SELECT * FROM allstarfull LIMIT 5'
results = pd.read_sql_query(q,con)

results

# Select all columns from batting table, limit to two rows
q = "SELECT * FROM batting LIMIT 2"
qr = pd.read_sql_query(q, con)

# Check if 'addybo01' is in the first two rows and extract 'AB'
addybo01_ab = qr.loc[qr['playerID'] == 'addybo01', 'AB']

# Print result
if not addybo01_ab.empty:
    print(f"Addybo01 had {addybo01_ab.values[0]} at-bats.")
else:
    print("Addybo01 is not in the first two rows.")


# Filter for addybo01's row from qr (limited to first two rows)
addybo01_data = qr.loc[(qr['playerID'] == 'addybo01') & (qr['yearID'] == 1871)]

# Extract at-bats (AB) and hits (H)
if not addybo01_data.empty:
    ab = addybo01_data.iloc[0]['AB']
    h = addybo01_data.iloc[0]['H']
    
    # Calculate batting average and round to 3 decimals
    batting_avg = round(h / ab, 3) if ab > 0 else 0
    print(f"Addybo01's batting average for 1871: {batting_avg}")
else:
    print("Addybo01's 1871 stats are not in the limited output.")
