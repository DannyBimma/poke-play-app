import requests
import random
from typing import List, Optional
import sys
from dataclasses import dataclass

"""Class to hold Pokemon data"""
@dataclass
class Pokemon:
    name: str
    id: int
    types: List[str]