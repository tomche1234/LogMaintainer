import sys
import os

projRootDir = f"{os.path.dirname(__file__)}/../.."
os.chdir(projRootDir)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LogMaintainer import Log as U


def this_fails():
    x = 1 / 0
    
def main():
   funcName = main.__name__
   try:
      U.running(funcName)
      U.log(funcName, "start run this_fails function")
      this_fails()
   except Exception as e:
      U.exception(funcName, e)

main()