import pandas as pd


# In the future: Check exist file. If yes: \/, if not: make exception...
# In the future: Check the extension in file name, and take proper function...
def ext_xlsx() -> dict:
    data = pd.read_excel(io='words/czasowniki.xlsx', index_col=0)
    data = data.to_dict('index')
    return data


# Temporary
if __name__ == "__main__":
    ext_xlsx()


# old vision:
def testowa():
    data = pd.read_excel(io='czasowniki.xlsx', index_col=0, nrows=155)

    data = data.to_dict('index')

    for row in data:
        print(data[row]['Meaning'])
