from app.main import Contratar

def testMenor():
    contratar = Contratar(idade = 17)
    assert contratar.ContratarPessoa() == True, 'Idade não está entre 16 e 18 anos'