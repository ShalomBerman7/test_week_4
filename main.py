

from fastapi import FastAPI
import uvicorn
import json


app = FastAPI()
items = []
abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher_encrypt(abc, txt):
    result = ''
    txt = txt.replace(' ','')
    for i in range(len(txt)):
        for j in range(len(abc)):
            if txt[i] == abc[j]:
                result += abc[(j + 16) % 25]
    return result


def caesar_cipher_decrypt(abc, txt):
    result = ''
    for i in range(len(txt)):
        for j in range(len(abc)):
            if txt[i] == abc[j]:
                result += abc[(j - 16) % 25]
    return result



def fence_cipher_endpoints(txt):
    txt = txt.replace(' ', '')
    res = ''
    res1 = ''
    for i in range(len(txt)):
        if i % 2 == 0:
            res += txt[i]
        else:
            res1 += txt[i]
    return res + res1


def fence_cipher_dedpoints(txt):
    x = len(txt) // 2
    res = txt[ :x]
    res1 = txt[x: ]
    result = ''
    for i in range(len(res)):
        result += res[i]
        result += res1[i]
    return result



def load_data():
    with open('data_json/data.json', 'r') as f:
        data1 = json.load(f)
    return data1


def save_data(data):
    with open('data_json/data.json', 'w') as f:
        json.dump(data, f)



@app.get("/test")
def get_test():
    response = load_data()
    return response


@app.get("/test/{name}")
def get_test_name(name: str):
    with open("names_file.txt", "a") as f:
        f.write(name)


@app.post("/caesar")
def post_data(text: str, offset: int):
    json_data = caesar_cipher_encrypt(abc_list, load_data())
    body = {"text": text, "offset": offset,  "mode": "encrypt"}
    save_data(body)
    return json_data



if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)