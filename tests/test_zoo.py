import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):
    
    def setUp(self) -> None:
        self.zoo_1: Zoo = Zoo()
        self.zookeeper_1: ZooKeeper = ZooKeeper('Gianni', 'Rossi', 1)
        self.fence_1: Fence = Fence(100, 25.0, 'Savana')
        self.animal_1: Animal = Animal('Pluto', 'Canide', 5, 200.0, 1.0, 'Savana')
        self.animal_2: Animal = Animal('Franco', 'papera', 40, 20.0, 1,'Savana')
    
    def test_1(self):
        """questo test controlla che animali troppo grandi non vengono aggiunti alla fence"""
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        message: str = f"Error, the function add_animal should not add self.animal_1 i  nto self.fence_1"
        self.assertEqual(result, 0, message)
        
    def test_2(self):
        """questo test controlla se l'animale è stato aggiunto alla fence"""
        check: int = len(self.fence_1.list_of_animals)
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        message: str = f"Error, the function add animal should add self.animal_2 into self.fence_1"
        self.assertNotEqual(result, check, message)
        
    def test_3(self):
        """questo test controlla se l'animale viene rimosso dalla fence"""
        check: int = len(self.fence_1.list_of_animals)
        self.zookeeper_1.remove_animal(self.animal_2, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        self.assertLess()
        
if __name__ == '__main__':
    unittest.main()