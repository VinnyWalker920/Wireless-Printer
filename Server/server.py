#This Python script serves as the main script for the server side program
import subprocess
#-o XXXX
#coll - collate
#sid1 - one-sided
#sid2L - two-sided-long-edge
#sid2S - two-sided-short-edge

#papLet - media=letter
#papLeg - media=legal
#papA4 - media=A4
#papA3 - media=A3
#papTab - media=tabloid
#papExec - media=executive

class Options():
    def __init__(self, *argv):
        self.ValidCodeHash ={
        'coll': 'collate',
        'sid1': 'sides=one-sided',
        'sid2L': 'sides=two-sided-long-edge',
        'sid2S': 'sides=two-sided-short-edge',
        'papLet': 'media=letter',
        'papLeg': 'media=legal',
        'papA4': 'media=A4',
        'papA3': 'media=A3',
        'papTab': 'media=tabloid',
        'papExec': 'media=executive'
        }
        self.codeList = []
        self.cmdList = []
        for arg in argv:
            if arg in self.ValidCodeHash:
                self.codeList.append(arg)
                self.cmdList.append(self.ValidCodeHash[arg])
            else:
                continue
    def addCode(self,*argv):
        for arg in argv:
            if arg in self.ValidCodeHash:
                self.codeList.appened(arg)
                self.cmdList.append(self.ValidCodeHash[arg])
            else:
                continue
    
    #be careful that it is an actual valid LPR command otherwise no worky. Also doesnt need -o attached because it will be appened later as it is the Options object
    def addCmd(self, *argv):
        for arg in argv:
            self.cmdList.append(arg)#bypasses valid Code checks bc 1, not a code, and 2, this is intended for internal use in a controlled manner
    
    def pullCmdSectionString(self):
        cmdSectionString = ""
        for cmd in self.cmdList:
            cmdSectionString = cmdSectionString + " -o " + cmd
        return cmdSectionString



def print_document(filelocal, options, ppid=None, copies=1):
    lprCmd = "lpr "
    lprCmd = lprCmd + "-# " + str(copies)
    if ppid:
        options.addCmd(("job-id="+str(ppid)))
    lprCmd = lprCmd + options.pullCmdSectionString()
    print(lprCmd)#for testing purposes
    subprocess.run(lprCmd + " " + filelocal, shell=True)
    subprocess.run("lpq")#for testing purposes

ops = Options("sid2L")
#NtS UnSANITIZE FILE PATHHH b4 use
print_document(filelocal="WirelessPrinter/Server/test2.pdf", options=ops, ppid="222", copies=2)
