import setuptools

# Long description
with open("README.md", "r") as fh:
    long_description = fh.read()


# Requirements
def get_requirements():
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()
        return requirements


setuptools.setup(
    name="tweetcaptureplus",
    version="0.3.0",
    author="Abdallah Heidar",
    author_email="abdallahheidar@gmail.com",
    description="Take a tweet screenshot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdallahheidar/tweetcaptureplus",
    packages=setuptools.find_packages(),
    install_requires=get_requirements(),
    data_files=[("", ["requirements.txt"])],
    entry_points={"console_scripts": ["tweetcaptureplus=tweetcaptureplus.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    keywords="tweet screenshot",
    python_requires=">=3.9",
)
