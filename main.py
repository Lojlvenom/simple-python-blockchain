import fastapi as _fastapi
import blockchain as _blockchain

app_desc = {
    'title':'Simple python blockchain API',
    'version':'1.0.0',
    
}

bc = _blockchain.Blockchain()
app = _fastapi.FastAPI(**app_desc)


def validade_blockchain():
    if not bc._is_chain_valid():
        return _fastapi.HTTPException(
            status_code= 400, detail="Blockchain nao e valida"
        )

@app.get("/", tags=["Endpoints"])
def hello():
    return {
        "message":"Bem vindo ao simple python blockchain API, para saber mais acesse /docs"
    }

# EP PARA ADICIONAR UM BLOCO
@app.post("/mine_block/", tags=["Endpoints"])
def mine_block(data: str):
    validade_blockchain()
    block = bc.mine_block(data)
    return block

@app.get("/blockchain/", tags=["Endpoints"])
def get_blockchain():
    validade_blockchain
    chain = bc.chain
    return chain

@app.get('/check_is_valid', tags=["Endpoints"])
def check_is_valid():
    is_valid = validade_blockchain()
    if is_valid:
        return {
            "message": "Is valid"
        }
    else:
        return {
            "message": "Not valid"
        }
