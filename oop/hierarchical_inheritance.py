class Software:
    def getinfo(self):
        print("Software is a logical implementation of real world things")

class SystemSoftware(Software):
    def getSystemSoftware(self):
        print("System Software is a software that allows the operations in computer")
        print('Examples - Windows, Linux and Mac')


class ApplicationSoftware(Software):
    def getApplicationSoftware(self):
        print("Application Software is a software that allows the user to perform daily tasks in computer")
        print('Examples - MS Word, MS Excel, Whatsapp, Instagram')


s = SystemSoftware()
a = ApplicationSoftware()

s.getinfo()
s.getSystemSoftware()
print("_____________________")
a.getinfo()
a.getApplicationSoftware()
