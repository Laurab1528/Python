from typing import List 
class CostDict():
    def __init__(self):

        self.dictionary =  {'socks':5,'shoes':60, 'sweater':30}
        
    def get_total(self,keys: List[str], tax:float)->float:
        total_cost = 0       
        
        for keys in keys:
            total_cost+=self.dictionary[keys]
        tax_final = total_cost * tax
        abs_cost = total_cost + tax_final

        return abs_cost
    
