#Copyright (C) 2022 shadroid
from time import sleep

class color:
      red = '\033[91m'
      green = '\033[92m'
      blue = '\033[94m'
      yellow = '\033[93m'
      magenta = '\033[95m'
      cyan = '\033[96m'
      white = '\033[97m'
      bold = '\033[1m'
      underline = '\033[4m'
      black='\033[30m'

class chop:
	 x_coder = f"""{color.bold}
{color.white} [âŚ] - {color.cyan} đđđđđđđđđđđ {color.yellow} đđđđđđđ  {color.red}1.0.0    

{color.white} [âŚ] - {color.cyan} đđđđđđđđđđđ {color.yellow} đđđđđđđđđ (đ) {color.red} 2022 {color.green}đđđđđ đđđđđ   

{color.white} [âŚ] - {color.cyan} đđđđđđđđđ  {color.yellow} đđđđđđ {color.red} đđđđđđđ : {color.green} @python_java_source

{color.white}âžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâžâźâž
"""
	 print(x_coder)
      
for x in range(3):
    for i in ("â˘ż", "âŁť", "âŁ˝", "âŁž", "âŁˇ", "âŁŻ", "âŁ", "âĄż"):
        sleep(0.1)
        if x == 10:
            print('',end='')
            break
        else:
            print( color.blue+'   đđđđđđđ đđđđ đđđđđđ đđđđđđ đđđđ   ',color.green+i,end='\r')
print(color.white+"\n")
