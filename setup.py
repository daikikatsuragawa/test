import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="df4loop",
    version="0.1.0",
    author="<your name>",
    author_email="daikikatsuragawa@gmail.com",
    description="<short_description>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/<your_github_name>/<repository_name>",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas>=1.0.0"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)