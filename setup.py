"""Script para tornar o pacote instalavel."""

from setuptools import setup, find_packages

setup(
    name="desafios-storm",
    version="0.1.0",
    description="Desafio da empresa storm para a vaga de backend",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["wheel"],
)
