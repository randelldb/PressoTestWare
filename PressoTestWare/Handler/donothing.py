from PressoTestWare.models import CalibrationModel
from PressoTestWare import session


class testHandler:

    @staticmethod
    def create():
        testCommit = CalibrationModel('testing')

        session.add(testCommit)
        session.commit()

        return testCommit


