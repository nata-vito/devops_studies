from app.main import Contratar

def testMenor():
    contratar = Contratar(idade = 56)
    assert contratar.ContratarPessoa() == False, 'Idade maior que 56'