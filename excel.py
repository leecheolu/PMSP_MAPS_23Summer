import pandas as pd
import pickle
import module

pickle_file_path = 'problem1.pickle'
with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)
ptime_df = pd.DataFrame(data.ptime)
setup_dfs = {f'Machine {i+1}': pd.DataFrame(machine_setup) for i, machine_setup in enumerate(data.setup)}

# 인덱스를 다른이름으로 추가하고 싶으면 아래 코드 이용
"""ptime_df.index = [i for i in range(data.numMch)]
for machine_name, df in setup_dfs.items():
    df.index = df.columns"""

excel_file_path = 'result.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    ptime_df.to_excel(writer, sheet_name='Processing Time')
    for machine_name, df in setup_dfs.items():
        df.to_excel(writer, sheet_name=machine_name)

