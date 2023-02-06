from fastapi import FastAPI, UploadFile, File
import cv2
from models.image_segmentation import recognition

app = FastAPI()

@app.get('/')
async def test():
    return {"message: ": "Endpoint is working"}


@app.post("/uploadfile")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        # with open(file.filename, 'wb') as f:
        #     f.write(contents)
        
        with open('temp.png', 'wb') as f:
            f.write(contents)

        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        result = recognition()

        print("result : ", result)
        return {"message": f"Number Plate : '{result}'"}