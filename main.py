from supabase import create_client, Client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# https://docs.render.com/deploy-fastapi

url: str = "https://gqajdjmciuzhiwcqniho.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdxYWpkam1jaXV6aGl3Y3FuaWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE4Mzk2MDQsImV4cCI6MjA1NzQxNTYwNH0.m719elC1ldMX51cBJuv4fhlbPq3jyf5Z_z4relZvVQo"

supabase: Client = create_client(url, key)

app = FastAPI()

class ChocolateBar(BaseModel):
    company: str
    specific_bean_origin_or_bar_name: str
    ref: int
    review_date: int 
    cocoa_percent: str 
    company_location: str 
    rating : float 
    bean_type: str 
    broad_bean_origin: str 
    

@app.post("/chocolatebar/")
def create_chocolate_bar(chocolatebar: ChocolateBar):
    data = supabase.table("chocolate_bars").insert(chocolatebar.dict()).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Item could not be created")
    

@app.get("/chocolatebar/")
def read_chocolate_bars():
    data = supabase.table("chocolate_bars").select("*").execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Items not found")
    

@app.put("/chocolatebar/{id}")
def update_chocolate_bar(chocolatebar_id: int, chocolatebar: ChocolateBar):
    data = supabase.table("chocolate_bars").update(chocolatebar.dict()).eq("id", chocolatebar_id).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/chocolatebar/{id}")
def delete_chocolate_bar(chocolatebar_id: int):
    data = supabase.table("chocolate_bars").delete().eq("id", chocolatebar_id).execute()
    if data.data:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
