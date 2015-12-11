# -*- coding: utf-8 -*-
import os
import random
import json
import logging

dbgMode = int()
dbgLogName = str()




class hServLexicProcessor:
    def __init__(self, jstr = 0, logClass = 0):
        self.logmsg = logging.getLogger( dbgLogName )
        self.logmsg.setLevel(dbgMode)
        self.logfil = logging.FileHandler(dbgLogName+'.log')
        self.logfil.setlevel(logging.DEBUG)
        self.logcon = logging.StreamHandler()
        self.logfil.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logcon.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

        if jstr is 0:

        else:
            if type( jstr ) is str:
                self.procString( jstr )
            else:
                print("It is not string")


    def procString(self, prStr):
        self.deString   = json.loads( prStr )
        self.deLen      = len( self.deString )

        if self.deLen is 0:
            print("String len is Zero")
            return

        if self.deString[0] == 'WannaBeServer':
            self.procAddNew( self.deString[1] )

        if self.deString[0] == 'WannaBeCli':
            self.procConnectExist( self.deString[ 1 ] )


    def procAddNew(self, params):
        print("Wanna Create :\t " + str( params['RoomName'] ))

    def procConnectExist(self, params ):
        print("Wanna Connect :\t "+ str( params['RoomName'] ))


    def stuff(self):

        alphaCh = json.loads(teststr)
        alphaLen = len(alphaCh)
        if alphaLen is 0:
            print("That's bad, coz len is:\tZERO")
        else:
            print("That's good, coz len is:\t"+str(alphaLen))

        alphaLen = 0
        if alphaLen is 0:
            print("That's bad, coz len is:\tZERO")
        else:
            print("That's good, coz len is:\t"+str(alphaLen))

    def logAdd(self,msg,dbgLvl=logging.DEBUG):
        self.logfil.


def current_test():
    teststr = json.dumps(["WannaBeServer", {'RoomName':('PenisDominator')}])
    hello = hServLexicProcessor(teststr)
    teststr = json.dumps(["WannaBeCli", {'RoomName':('PenisDominator')}])
    goodbye = hServLexicProcessor(teststr)



if __name__ == "__main__":
    dbgMode = logging.DEBUG
    dbgLogName = 'hatLog'
    print("_MBegin HatServer Module")
    current_test()
    print("_MEnd HatServer Module")
