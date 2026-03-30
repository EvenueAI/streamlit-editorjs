from setuptools import find_packages, setup

setup(
    name="streamlit-editorjs",
    version="0.1.0",
    description="Editor.js custom component for Streamlit",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "streamlit_editorjs": [
            "frontend/dist/index.html",
            "frontend/dist/assets/*",
        ],
    },
    install_requires=[
        "streamlit>=1.55",
    ],
)
