'''
DECORATORS:
      1.Decorators Are The Function Which Used To Enhance The Functionality Of An Another Function.
      2.In Word ,One Function Provides Additional Code To An Another Function.
      3.In Order To Make Use Of Decorators We Have To Use Annotations.
      4.Decoratore Can Be Done With The Help Of Special Symbol Called "@".

RULES FOR CREATING AN DECORATOR FUNCTON:
      1.The Decorator Function Should Always Be An Nexted Function.
      2.The Decorator Function Has Accept The Address Of The Function Which Needs To Be Decorated.
      3.The Decorator Function Must Return The Address Of The Inner Function.

 SYNTAX:

 def deco_name(fun):
       def inner_fun():
             ------------------------
             ----before fun call----
             ------------------------
             fun()
             ------------------------------
             ----ofter fun call----------
             -------------------------------
      return inner_fun()
@deco_name
def fun_name():
      -----------------
      -----------------
      ----------------     
'''
#example for decorators
def FaceBook(fun):
      def inner():
            fid='kittu'
            pas='kittu123'
            if fid== input('enter the user id'):
                  if pas== input('enter the password'):
                        fun()
                  else:
                        print('worng password')
            else:
                  print('worng user id')
            
      return inner()
@FaceBook
def add():
      print('photo is added')
