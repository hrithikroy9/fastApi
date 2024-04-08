from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"go to /lodawear for wears": "/pokemondump for pokemons"}



@app.get("/lodawear")
async def get_products(search_queryy: str = None):
    products = [    
                {
                "category":"clothing",    
                "brand":"Nike",
                "colortype":"multicolor",
                "item_type":"shoe",
                },                
                
                
                {
                "category":"clothing",    
                "brand":"Adidas",
                "colortype":"stock", 
                "item_type":"shoe",
                }, 
                
                {
                "category":"electronic",   
                "brand":"Asus",
                "colortype":"Matt Black",
                "item_type":"laptop",
                },
                
                
                {
                "category":"bigbanglauda",
                "brand":"myslong",
                "colortype":"Dark matter",
                "item_type":"longkong",
                },
                
                
                {
                "category":"electronic",
                "brand":"Oppo",
                "colortype":"lime green",
                "item_type":"mobile phone"  
                },
                
                
                {
                    "category":"electronic",
                    "brand":"Apple",
                    "colortype":"weird yellow",
                    "item_type":"airmax"
                }
                
                ]
    
    if search_queryy:
        productResults = [x for x in products if x['category'] == search_queryy]
        
        lingo = f"I would like to have one {productResults.get('item_type')} of {productResults.get('brand')} with {productResults.get('colortype')} color"

        # for product in products:
        #     if product['brand'] == search_queryy:
        #         lingo = f"I would like to have one {product.get('brand')} of {product.get('colortype')}"
        #         return lingo  # Return 
        # return {"message": "Ae Macha Product not found"}  #error catcha
    
        return productResults
    else:
        return {"message":"Aey macha nothing is here"}#error      
    
    
    
@app.get("/testing_AREA")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



@app.get("/pokemondump/{name}")
async def get_pokemons(search_query: str = None):
    
    
    pokemons =[
                {'type':'Light',
                'name':'pikachu',
                'power': 6.99,
                'origin': 'India'},
                
                
                {'type':'cock',
                'name':'laudachu',
                'power': 999969,
                'origin':'Pakistan'},
                
                
                {'type':'rock',
                'name':'onix', 
                'power': 29,
                'origin':'UP'},
                
                
                {'type':'cock',
                'name':'laudaonix',
                'power': 70029,
                'origin':'mortyland'},
                
                
                
                {'type':'water',
                'name':'waterpuzz',
                'power': 6963,
                'origin':'mexico'},
                
                
                {'type':'water',
                'name':'aquamon',
                'power':55,
                'origin':'Zdivland'
                }] 
    
    
    if search_query:
        results = [x for x in pokemons if x['type'] == search_query]
        
        # for pokemon in pokemons:
        #     if pokemon['type'] == search_query:
        #         # outs = f"Hi My name is {pokemon.get('name')} I am from {pokemon.get('origin')} with power {pokemon.get('power')}"
        #         return outs  # Return 
        # return {"message": "Anna Pokemon ille not found"}  #error catcha
        
        return results
    else:
        return {"message":"Aey macha nothing is here"}#error                  
        






@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price}