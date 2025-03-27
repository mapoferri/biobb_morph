import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_radiospineomicsw",
    version="5.0.2",
    author="Biobb developers",
    author_email="mferri@bsc.es",
    description="biobb_radiospineomics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_radiospineomics",
    project_urls={
        "Documentation": "http://biobb-radiospineomics.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_radiospineomics": ["py.typed"]},
    include_package_data=True,
    install_requires=[
        "biobb_common==5.0.0",
        "torch",
        "numpy-stl",
        "numpy",
        "trimesh",
        "matplotlib",
        "scikit-learn",
        "scipy",
        "meshio",
        "Rtree",
    ],
    python_requires=">=3.9",
    entry_points={"console_scripts": ["radiospineomics = biobb_radiospineomics.radiospineomics.radiospineomics:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
