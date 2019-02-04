from conans import ConanFile, CMake, tools


class PrettyprintConan(ConanFile):
    name = "cxx-prettyprint"
    version = "master"
    license = "Boost Software License"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-prettyprint"
    description = ("A header-only library for C++(0x) that allows automagic pretty-printing"
                   " of any container., "
                   "See https://github.com/louisdx/cxx-prettyprint")
    no_copy_source = True
    homepage = "https://github.com/louisdx/cxx-prettyprint"

    def source(self):
        self.run("git clone https://github.com/louisdx/cxx-prettyprint.git")

    def package(self):
        self.copy("*.hpp", dst="include", src="cxx-prettyprint/")
