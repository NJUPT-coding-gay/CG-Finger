from pocsuite.net   import req
from pocsuite.poc   import POCBase,Output
from pocsuite.utils import register


class Joomla_Exec(POCBase):
    vulID      = "1"
    version    = "1"
    author     = "meizj"
    vulDate    = "2015-12-17"
    createDate = "2017-09-24"
    update     = "2017-09-24"
    references = ["http://www.cnblogs.com/milantgh/p/5193723.html"]
    apppowerLink = ""
    appName      = "Joomla!"
    appversion   = "1.5-3.4.5"
    vulType      = "Code Exec"
    def __verify(self):
        result = {}
        target = self.url

    def __attack(self):
        print(2)
    def parser_result(self,result):
        print(3)