from setuptools import setup


PACKAGES = [
    "loyalpy",
]


def setup_package():
    setup(
        name="loyalpy",
        version="0.1.0",
        description="Joshua Loyal's Personal Python Package",
        author="Joshua D. Loyal",
        url="https://github.com/joshloyal/loyalpy",
        license="MIT",
        install_requires=["numpy", "scipy", "matplotlib"],
        packages=PACKAGES
    )


if __name__ == "__main__":
    setup_package()
