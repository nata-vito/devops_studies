from app.main import CoursePlatform


def testPassIdUsers():
    platform = CoursePlatform()
    platform.RegisterUser(plan='Premium')
    assert platform.FindPremiumUsers(), "Não existe usuários premiuns"