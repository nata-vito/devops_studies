from app.main import CoursePlatform


def testPassStudentScoreToCripto():
    platform = CoursePlatform()
    assert platform.ScoreToCripto(
        3, 5) == 2, "O número de moedas especificadas não passaram no teste!"
