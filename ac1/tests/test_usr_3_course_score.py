from app.game_plat import CoursePlatform


def testScoreToCourse():
    platform = CoursePlatform()
    platform.RegisterUser()
    assert platform.ScoreToCourse(
        ruler_number=12), "O Usuário não possui curso ou a quantidade \
            de cursos é superior/inferior que o ruler_number"
