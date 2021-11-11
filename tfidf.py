import os

with open("allcompany.txt","w") as f:
    for root, dirs, files in os.walk(r"Data/Foreign_CSR_txt"):
        for file in files:
            print(os.path.join(root, file))
            with open(os.path.join(root,file),"w"):
                text = f.read()
                cont = text.strip()
                f.writelines(f"")