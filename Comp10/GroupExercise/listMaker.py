import pandas as pd
path = input("Please enter the absolute path of the file to convert:  ")
delimiter = input(r"Please enter the appropriate delimiter type for this file:(Ex: '\\n or \\t')  ")
cabqFile = pd.read_csv(path, encoding="utf-16", delimiter='\t')
asDataFrame = pd.DataFrame(cabqFile)

asDataFrame.to_csv(path, encoding="utf-8", index=False)


#I am no longer restricted by the laws of Encoding.
#I am the encoder now
#Fear me