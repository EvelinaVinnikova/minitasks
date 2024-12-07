from setuptools import setup, Extension

module = Extension("foreign", sources=["foreign_module.c"])

setup(
    name="foreign",
    version="1.0",
    description="C-extension for raising matrices to a power",
    ext_modules=[module],
)