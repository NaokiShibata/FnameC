import glob, os, sys, shutil, pathlib
import pandas as pd
from tqdm import tqdm



# Defile current directory
current_dir = pathlib.Path.cwd()

# make file path var
In_path = f'{current_dir}/InFile'
Out_path = f'{current_dir}/OutFile'

# Check output folder
if os.path.isdir(Out_path):
    pass
else:
    pathlib.Path(Out_path).mkdir(exist_ok=True)

# make function
def no_duplicate_check(A):
    return len(A) == len(set(A))


print("\n  ===== Check ref.csv and read data =====\n")

# make file path var
refdata = f'{current_dir}/Ref/ref.csv'
# import
reftable = pd.read_csv(refdata)

# Check ref file data
before_boolen = reftable["Before"].isnull().any(axis=0)
after_boolen = reftable["After"].isnull().any(axis=0)


if before_boolen == False and after_boolen == False:
    if no_duplicate_check(reftable["Before"]) == True and no_duplicate_check(reftable["After"]) == True:
        print("  Confirm no missing value and no duplicate value.\n")
    else:
        print("  WARNING! : Ref.csv file has duplicate value.")
        print("  Program is stopped.")        
        sys.exit()
else:
    print("  WARNING! : Ref.csv file has missing value.\n")
    print("  Program is stopped.")
    sys.exit()

# Get all file names in InFile folder by list format.
InList = glob.glob(f'{In_path}/*')

sorted_InList = sorted(InList) # Sort
sortDFB = reftable.sort_values('Before', ascending=True)
num = sortDFB["Before"].nunique() # count

# Searching for filename listed in 'ref.csv' and if it match, rename.
print("\n  ===== Rename =====\n")
for i in tqdm(range(0, num)):

    # Target file name
    target_rename_filename = sortDFB.iloc[i,0]
    # Renamed file name
    re_name = sortDFB.iloc[i,1]

    # Get file path to target files
    try :
        path = os.path.dirname(InList[i])
    except IndexError:
        print(f"\n  WARNING! : Files are not completely match.")
        sys.exit()

    # Confirm file exists
    conf = os.path.exists(f'{path}/{target_rename_filename}')

    if conf == True: # Target file is exists in input folder.
        if os.path.isfile(f"{Out_path}/{re_name}") == True: # Renamed file aleady exists. 
            print(f"\n  '{re_name}' file is aleady exists in output folder.")
            print("  Please remove files in output foler.")
            print("  Please check output folder.")
            sys.exit() # stop
        else:
            # moveing file
            shutil.copyfile(f'{path}/{target_rename_filename}', f'{Out_path}/{re_name}')
    else: # If not exists
        print(f'  {target_rename_filename} not found.')
        print("  Program is stopped.")        
        sys.exit()