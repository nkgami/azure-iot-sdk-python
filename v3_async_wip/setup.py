# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup

setup(
    name="v3_async_wip",
    description="Internal development utilities for Azure IoT. NOT FOR DISTRIBUTION.",
    version="0.0.0a1",  # Alpha Release
    license="MIT License",
    install_requires=[
        # NOTE: there is an optional aiohttp[speedups] install that improves performance
        # but I don't know if we want to bring in extra, optional packages
        "aiohttp",
    ],
)
