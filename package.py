name = "ocio"

version = "2.1.0"

variants = [
    ["platform-linux", "python-3.7"]
]

build_command = "make -f {root}/Makefile {install}"

def commands():
    env.OCIO_ROOT = '{root}'
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append(
        "{root}/lib/python{resolve.python.version.major}.{resolve.python.version.minor}/site-packages"
    )

    if building:
        env.OpenColorIO_ROOT="{root}" # CMake Hint
