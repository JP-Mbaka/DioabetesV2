"""
@author: Mbaka JohnPaul
"""

from pydantic import BaseModel

class Darb(BaseModel):
    preg: int
    plas: int
    pres: int
    skin: int
    insu: int
    mass: float
    pedi: float
    age:  int