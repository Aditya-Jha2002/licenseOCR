import os
import shutil
import pandas as pd
from fastapi import FastAPI, UploadFile, File, Form
from prediction_service.taadhar import get_text

app = FastAPI()

static_dir = 'static'
upload_path = os.path.join(static_dir, "id.png")
data_path = os.path.join(static_dir, "license_data.csv")

@app.post("/")
async def root(name: str = Form(), contact: int = Form(), license_img: str = Form()):
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(license_img.file, buffer)

    name_doc, contact_doc, rci = get_text(upload_path)
    contact_doc = int(contact_doc)

    validation1 = validation2 =  False
    rci_val = contact_val = name_val = False

    if name == name_doc and contact == contact_doc:
        validation1 = True

    df = pd.read_csv(data_path)

    if rci in df['RCI No'].values:
        rci_val = True

    df["Mobile no"] = df["Mobile no"].astype(int)
    if contact in df['Mobile no'].values:
        contact_val = True

    if name in df['NAME'].values:
        name_val = True

    if rci_val and contact_val and name_val:
        validation2 = True

    if validation1 and validation2:
        return {"message": "Valid", "name": name, "contact": contact, "rci": rci}

    return {"message": "Invalid"}