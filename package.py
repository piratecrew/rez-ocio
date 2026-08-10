name = "ocio"

version = "2.3.2"

variants = [
    ["platform-linux", "python-3.9"],
    ["platform-linux", "python-3.10"],
    ["platform-linux", "python-3.11"],
]

private_build_requires = [
    "cmake-3.15+<4",
    "gcc-11"
]

build_command = "make -f {root}/Makefile {install}"

def pre_build_commands():
    env.Python_ROOT = env.PYTHON_ROOT
    unsetenv("PYTHON_ROOT")

def commands():
    env.OCIO_ROOT = '{root}'
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PYTHONPATH.append(
        "{root}/lib64/python{resolve.python.version.major}.{resolve.python.version.minor}/site-packages"
    )

    if building:
        env.OpenColorIO_ROOT="{root}" # CMake Hint

tests = {
    "python": {
        "command": """
        python -c "import PyOpenColorIO as ocio; assert ocio.__version__ == '{version}'"
        """,
        "run_on": [
            "pre_install",
            "pre_release",
        ],
        "on_variants": True
    },
}
