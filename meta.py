# coding=utf-8
class Singleton(type):
    """ 싱글톤 패턴을 구현해주는 메타 클래스 """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args)

        return cls._instances[cls]
