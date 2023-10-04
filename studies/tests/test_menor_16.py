from app.main import Contratar

def testMenor():
    contratar = Contratar(idade = 15)
    assert contratar.ContratarPessoa() == False, 'Idade inferior a 16 anos'