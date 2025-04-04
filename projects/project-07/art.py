hangman_logo = r"""
***************************************************
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _ \ / _  |  _ \ / _  |  _   _ \ / _  |  _ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\____|_| |_|\__  |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

***************************************************
"""

lifes = {
    5: r"""  
  +---+  
  |   |  
  |   O  
  |      
  |      
  |      
=========  
""",
    4: r"""  
  +---+  
  |   |  
  |   O  
  |   |  
  |      
  |      
=========  
""",
    3: r"""  
  +---+  
  |   |  
  |   O  
  |   |\  
  |      
  |      
=========  
""",
    2: r"""  
  +---+  
  |   |  
  |   O  
  |  /|\  
  |      
  |      
=========  
""",
    1: r"""  
  +---+  
  |   |  
  |   O  
  |  /|\  
  |    \  
  |      
=========  
""",
    0: r"""  
  +---+  
  |   |  
  |   O  
  |  /|\  
  |  / \  
  |      
=========  
"""
}
