# This program will generate lyrics for a personalised Jingle Bells carol.

# ----------------
# Constants
# ----------------

BELL_ASCII_ART = """			   			  		
				   _,--._
                                 ,'  _.._`.
                            ,^.,' ,-" _," ;
                   _,----.._\\|( _/,--"  ,<
                 ,'     ____(_))< ___..".  `.
                :  _,-"__,-" (_)-.      ,\\.  \
                :,'..-"  _,-")|(\\ `._.-"_,\\  \
                 `.__ ,-"    '-`'   \\.-"   Y  :
                 /  /:-...______...-:      |  |
                (  ( |-...______...-'      ;  ;_
                 \\ ,\\|              |     /,^/  ;._
                  `  .              .        _,'   ;
                     :              :    _,-'    ,"
                     '              ` ,-'     _,"
                    '                '    _,-"`.
                   ;`--...______,,,--":.-"     ;
                  :                    :  `..."
                  '---....______,,,,---'
                           :     ;
                            `.,."          
"""


noun= input("Enter a noun")
animal = input("Enter an animal")
place = input("Enter a place")
ing= input("Enter a word ending with -ing")
print ("Jingle bells, jingle bells, jingle all the way!\nDashing through the",noun,"On a one-",animal,"-open-sleigh\nO'er the ",place,"we go\n", ing,"all the way")
