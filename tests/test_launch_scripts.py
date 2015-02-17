#!/usr/bin/python2.7

import unittest
import subprocess
import os

# Get the directory of this module so the tests can be ran from any cwd
testDirectory = os.path.dirname(os.path.abspath(__file__))

class LaunchScriptTests(unittest.TestCase):
	def testSimulationRuns(self):
		"""
	    Test the simulation script returns an exit code of 0, implying it ran successfully.
	    """
		self.failIf(self.runScript("../simulator.py") != 0)

	def testPlayRuns(self):
		"""
		Test the play script returns an exit code of 0, implying it ran successfully.
		"""
		self.failIf(self.runScript("../play.py") != 0)

	def runScript(self, scriptPath):
		"""
		Run a script relative to this module's directory.

		Returns:
			the return code of the script.
		"""
		process = subprocess.Popen(os.path.join(testDirectory, scriptPath), stdout = subprocess.PIPE)
		process.communicate()
		return process.returncode

def main():
	unittest.main()

if __name__ == '__main__':
	main()