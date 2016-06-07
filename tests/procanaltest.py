# coding=utf-8
import unittest

import volacommander


class ProcAnalTestCase(unittest.TestCase):
    """ 프로세스 분석 모듈 테스트 """

    def setUp(self):
        self.target_path = "/Users/J/Documents/ExampleImage/1.vmem"
        self._commander = volacommander.VolaCommander(self.target_path)
        self._profile = ['WinXPSP0x86', 'WinXPSP1x86', 'WinXPSP2x86', 'WinXPSP3x86']

    def test_volacommander_singleton(self):
        """ 볼라틸리티 명령을 수행하는 클래스의 싱글톤 확인 테스트 """
        commanders = []

        for i in range(0, 5):
            commanders.append(volacommander.VolaCommander(self.target_path))

        for commander in commanders:
            self.assertEqual(self._commander, commander, "VolaCommander is not Singleton")
