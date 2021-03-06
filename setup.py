from skbuild import setup


if __name__ == "__main__":
    setup(
        # the following config options are not picked up by scikit-build unless they are
        # in the setup() call. This is because scikit-build directly scalps arguments from
        # the setup() call, before calling setuptool's setup().
        packages=['hello'],
        package_dir={'': 'src'},
        cmake_install_dir='src/hello')
