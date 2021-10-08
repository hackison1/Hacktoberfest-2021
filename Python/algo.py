# shoting algorithm
def shoting(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

def main():
    print(shoting(1, 2, 3))

def test():
    assert shoting(1, 2, 3) == 3
    assert shoting(1, 3, 2) == 3
    assert shoting(3, 1, 2) == 3

def test_shoting():
    print("shoting test")
    test()
    print("shoting test passed")

class TestShoting(unittest.TestCase):
    def test_shoting(self):
        self.assertEqual(shoting(1, 2, 3), 3)
        self.assertEqual(shoting(1, 3, 2), 3)
        self.assertEqual(shoting(3, 1, 2), 3)

class UnityTestShoting(unittest.TestCase):
    def test_shoting(self):
        self.assertEqual(shoting(1, 2, 3), 3)
        self.assertEqual(shoting(1, 3, 2), 3)
        self.assertEqual(shoting(3, 1, 2), 3)

class advancedTestShoting(unittest.TestCase):
    def test_shoting(self):
        self.assertEqual(shoting(1, 2, 3), 3)
        self.assertEqual(shoting(1, 3, 2), 3)
        self.assertEqual(shoting(3, 1, 2), 3)
