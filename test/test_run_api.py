# coding: utf-8

"""
    Autotab API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from autotab.api.run_api import RunApi


class TestRunApi(unittest.IsolatedAsyncioTestCase):
    """RunApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = RunApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_cancel(self) -> None:
        """Test case for cancel

        Cancel
        """
        pass

    async def test_list(self) -> None:
        """Test case for list

        List Runs
        """
        pass

    async def test_retrieve(self) -> None:
        """Test case for retrieve

        Retrieve
        """
        pass

    async def test_start(self) -> None:
        """Test case for start

        Start
        """
        pass


if __name__ == '__main__':
    unittest.main()
