from app.main import Contratar

def testMenor():
    contratar = Contratar(idade = 20)
    assert contratar.ContratarPessoa() == True, 'Idade não está entre 18 e 55 anos'