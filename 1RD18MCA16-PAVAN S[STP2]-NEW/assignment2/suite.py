import unittest
import demo1
import drag
import os
import HtmlTestRunner

path = os.getcwd()


# two test cases are run together
class Test_Suite(unittest.TestCase):
    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([unittest.TestLoader().loadTestsFromModule(demo1),
                            unittest.TestLoader().loadTestsFromModule(drag)])

        outfile = open(path + "SmokeSuite.html", "w")

        runner1 = HtmlTestRunner.HTMLTestRunner(
            stream=outfile,
            report_title='Assignment2 Report',
            descriptions='Assignment2',
            combine_reports=True
        )

        runner1.run(self.suite)

        if __name__ == "_main_":
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="file:///home/pavan/PycharmProjects/assignment2/reports"))
