import fastapi as _fastapi
import blockchain as _blockchain

bc = _blockchain.Blockchain()
app = _fastapi.FastAPI()


def validade_blockchain():
    if not bc._is_chain_valid():
        return _fastapi.HTTPException(
            status_code= 400, detail="Blockchain nao e valida"
        )

@app.get("/")
def hello():
    return {
        "message":"Bem vindo ao simple python blockchain API, para saber mais acesse /docs"
    }

# EP PARA ADICIONAR UM BLOCO
@app.post("/mine_block/")
def mine_block(data: dict):
    validade_blockchain()
    block = bc.mine_block(data)
    return block

@app.get("/blockchain/")
def get_blockchain():
    validade_blockchain
    chain = bc.chain
    return chain
