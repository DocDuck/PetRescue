from fastapi import FastAPI
app = FastAPI()
@app.get("/pets/")
async def get_all_pets():
    """[summary]
    Gets all pets adopted/rescued or not.
    [description]
    Endpoint for all pets.
    """
    fake_pets = [{"name": "Toozik"}, {"name": "Boosya"}]
    return fake_pets