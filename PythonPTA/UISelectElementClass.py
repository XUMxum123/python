#Created on 2017/12/24
#@author: meng.xu
#@email: meng.xu@tpv-tech.com

# -*- coding: utf-8 -*-

import string

# text => t
# className => cn
# resourceId => ri

class UISelectElementClass:
    
    TAG = "UISelectElementClass" + ": "
    
    def __init__(self, d):
        self.d = d
        
    def getElementByText(self, t):
        element = self.d(text = str(t))
        return element
    
    def getElementByClassName(self, cn):
        element = self.d(className = str(cn))
        return element
    
    def getElemntByResourceId(self, ri):
        element = self.d(resourceId = str(ri))
        return element
