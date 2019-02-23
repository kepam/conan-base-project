from conans import ConanFile, CMake, tools


class ConanbaseprojectConan(ConanFile):
    name = "conan-base-project"
    version = "0.1.0"
    exports = "scripts/*"

    def package(self):
        self.copy("scripts/*")

    def deploy(self):
        self.copy("*", dst=".", src="scripts")
        self.output.warn("This is a warning, should be yellow")
