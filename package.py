name = "ocio"

version = "2.1.0"

variants = [
    ["platform-linux", "python-3.7"]
]

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    from subprocess import check_output
    valid = check_output(r"expr `gcc -dumpversion | cut -f1 -d.` \>= 9 || true", shell=True).strip().decode() == "1"
    if not valid:
        return ["devtoolset-9"]
    return []

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
