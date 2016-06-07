# coding=utf-8
import meta


class VolaCommander:
    __metaclass__ = meta.Singleton

    def __init__(self, target_path):
        # 덤프 파일 경로 설정
        self._target_path = target_path
