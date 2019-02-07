from conans import ConanFile, CMake, tools


class PrettyprintConan(ConanFile):
    name = "cxx-prettyprint"
    version = "2016-04-30-9ab26d2"
    license = "Boost Software License"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-prettyprint"
    description = ("A header-only library for C++(0x) that allows automagic pretty-printing"
                   " of any container., "
                   "See https://github.com/louisdx/cxx-prettyprint")
    no_copy_source = True
    homepage = "https://github.com/louisdx/cxx-prettyprint.git"

    def source(self):
        git = tools.Git(folder="cxx-prettyprint")
        commit_sha1 = self.version.split("-")[-1]
        git.clone(self.homepage)
        git.checkout(commit_sha1)

    def package(self):
        self.copy("*.hpp", dst="include", src="cxx-prettyprint/")
