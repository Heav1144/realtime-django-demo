import zipfile
with zipfile.ZipFile("realtime_project.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
