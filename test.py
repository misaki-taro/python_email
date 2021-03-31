import pandas as pd

def excel_email(filePath):
    df = pd.read_excel(filePath, usecols=[7], names=None)
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    print(result)
    return df_li

result = excel_email("nameList2.xlsx")