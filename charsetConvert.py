# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:48:45 2018

@author: auroch
@github: github.com/ro-auroch
@License: MIT License
"""
import codecs
import getopt
import sys

class charset_conv:
    def __init__(self):
        self.BLOCKSIZE = 1048576 
        self.sourceFileName=None
        self.targetFileName=None
        self.srcEnc=None
        self.outEnc=None
        return
    def convert(self):
        with codecs.open(self.sourceFileName, "r", self.srcEnc) as sourceFile:
            with codecs.open(self.targetFileName, "w", self.outEnc) as targetFile:
                while True:
                    contents = sourceFile.read(self.BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)
    def get_ops(self):
        try:
            opt,args=getopt.getopt(sys.argv[1:], 'x', ['src='
                                   , 'out='
                                   , 'srcenc='
                                   , 'outenc='])
        except getopt.GetoptError as err:
            print(err)
            
        for o, a in opt:
            if o=="--src":
                self.sourceFileName=a
            elif o=="--out":
                self.targetFileName=a
            elif o=="--srcenc":
                self.srcEnc=a
            elif o=="--outenc":
                self.outEnc=a                
            else:
                print("Opción no reconocida")
        return 
    def set_ops(self,src_n, out_n, srcenc, outenc):
        self.sourceFileName=src_n
        self.targetFileName=out_n
        self.srcenc=srcenc
        self.outenc=outenc
        return
    
if __name__=="__main__":
    conv=charset_conv()
    conv.get_ops()
    conv.convert()
    