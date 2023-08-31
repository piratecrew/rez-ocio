name = "ocio"

version = "2.1.2"

variants = [
    ["platform-linux", "python-3.7"],
    ["platform-linux", "python-3.9"],
]

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    requirements = ["cmake-3.15+<4"]
    from subprocess import check_output
    gcc_major = int(check_output(r"gcc -dumpversion | cut -f1 -d.", shell=True).strip().decode())
    if gcc_major < 9:
        requirements.append("devtoolset-9")

    return requirements

build_command = "make -f {root}/Makefile {install}"

def commands():
    env.OCIO_ROOT = '{root}'
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PYTHONPATH.append(
        "{root}/lib64/python{resolve.python.version.major}.{resolve.python.version.minor}/site-packages"
    )

    if building:
        env.OpenColorIO_ROOT="{root}" # CMake Hint
