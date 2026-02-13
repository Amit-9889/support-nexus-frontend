import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"

def send_query(question:str ,user_id:str):

    try:
        response = requests.post(
            f"{BASE_URL}/query/query",
            json={
                "question":question,
                "user_id":user_id
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        if data.get("status")=="success":
            return data["messages"]["answer"]
        
        else:
            return "Request faild"
    
    except Exception as e:
        return f"Error :{str(e)}"
    

def upload_document(file):
    try:

        files = {
            "file": (file.name, file.getvalue(), file.type)
        }

        response =  requests.post(
            f"{BASE_URL}/upload/upload",
            files=files,
            timeout=60
        )

        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        return {"status":"failed","message":str(e)}
