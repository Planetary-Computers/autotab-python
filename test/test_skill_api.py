# coding: utf-8

"""
    Autotab API

    AI that does your repetitive work end to end, with superhuman reliability.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from autotab.api.skill_api import SkillApi


class TestSkillApi(unittest.IsolatedAsyncioTestCase):
    """SkillApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = SkillApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_list(self) -> None:
        """Test case for list

        List
        """
        pass

    async def test_retrieve(self) -> None:
        """Test case for retrieve

        Retrieve
        """
        pass


if __name__ == '__main__':
    unittest.main()
