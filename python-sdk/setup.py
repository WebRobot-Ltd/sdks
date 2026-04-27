from setuptools import setup, find_packages

setup(
    name="webrobot-sdk",
    version="0.3.10",
    description="WebRobot Python SDK — REST client for https://api.webrobot.eu (138 endpoints)",
    author="WebRobot Ltd",
    author_email="support@webrobot.eu",
    url="https://github.com/WebRobot-Ltd/webrobot-sdk",
    keywords=["webrobot", "sdk", "api", "etl", "automation"],
    python_requires=">= 3.8",
    install_requires=[],  # stdlib only (urllib, json)
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description="""
# WebRobot Python SDK

REST client for the [WebRobot API](https://api.webrobot.eu) covering all 138 endpoints.

## Install

```bash
pip install webrobot-sdk
```

## Usage

```python
from webrobot import WebRobotClient

client = WebRobotClient(api_key="your-api-key")

# list projects
projects = client.projects_list()

# execute a job
result = client.job_execute("project-id", "job-id")

# datasets
datasets = client.datasets_list()
```

## Auth

Pass `api_key` (X-API-Key) or `jwt` (Bearer token) to the constructor.
""",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
