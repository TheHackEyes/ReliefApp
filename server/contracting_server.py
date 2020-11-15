# server/contracting_server.py

from sanic import Sanic, response

from sanic_cors import CORS


app = Sanic("contracting server")
CORS(app)

@app.route("/ping")
async def ping(request,response):
    return response.json({'status': 'online'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3737)





# server/contracting_server.py
from sanic import Sanic, response

from contracting.client import ContractingClient
client = ContractingClient()

with open('my_token.py') as f:
    code = f.read()
    client.submit(code, name='my_token')

app = Sanic("contracting server")
CORS(app)
@app.route("/ping")


