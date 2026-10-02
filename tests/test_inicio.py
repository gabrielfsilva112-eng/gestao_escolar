from app import app

def test_inicio_status_code():
    client = app.test_client()
    resposta = client.get("/")

    assert resposta.status_code == 200

def test_inicio_message():
    client = app.test_client()
    resposta = client.get("/")

    assert resposta.get_data(as_text=True) == "Sistema de Gerenciamento Escolar"
