from fastapi import FastAPI, UploadFile, File
import cv2


def extract_characters(img):
    pass


app = FastAPI()

@app.get('/')
async def test():
    return {"message: ": "Endpoint is working"}


@app.post("/uploadfile")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
        

        img = cv2.imread(file.filename)
        chars = extract_characters(img)
        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        return {"message": "File Uploaded Successfully"}