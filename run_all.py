import os
import  unittest

from common import HTMLTestRunner_cn

curpath = os.path.dirname(os.path.realpath(__file__))  #当前操作的文件夹的路径
print(curpath)
casePath = os.path.join(curpath,"case")
print(casePath)

# start_dir = r"F:\jiekou\testCase"     #展示原型
pattern = "test_*.py"
discover = unittest.defaultTestLoader.discover(start_dir = casePath, pattern = pattern)
print(discover)  #看有没有找到测试的用例

# runner = unittest.TextTestRunner()
# runner.run(discover)

report_path = os.path.join(curpath, "report", "report.html")

fp = open(report_path, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(
                                            stream= fp,
                                            title= "活动平台测试用例报告",
                                            description= "测试用例详情描述",
                                            retry = 1,
                                            verbosity= 2
                                                        )

runner.run(discover)
fp.close()















