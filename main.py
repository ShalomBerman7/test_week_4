from encrypt_decrypt import abc_list, caesar_encrypt, caesar_decrypt, fence_encrypt, fence_decrypt

from fastapi import FastAPI
import uvicorn
import json


app = FastAPI()
items = []



def load_data():
    with open('data_json/data.json', 'r') as f:
        data1 = json.load(f)
    return data1


def save_data(data):
    with open('data_json/data.json', 'w') as f:
        json.dump(data, f)



@app.get("/test")
def get_test():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def get_test_name(name: str):
    with open("names_file.txt", "a") as f:
        f.write(name)
    return {"msg": "saved user"}


@app.post("/caesar")
def post_data(text: str, offset: int, mode:str):
    if mode == "encrypt":
        result = caesar_encrypt(abc_list, offset, text)
        return {"encrypted_text": result}
    else:
        result = caesar_decrypt(abc_list, offset, text)
        return {"decrypted_text": result}


@app.get("/fence/encrypt")
def fence_encrypt(text: str):
    result = fence_encrypt(text)
    return {"encrypted_text": result}


@app.post("/fence/decrypt")
def fence_decrypt(text: str):
    result = fence_decrypt(text)
    return {"decrypted_text": result}



if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)