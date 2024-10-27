import unittest

from heap_draw import create_heap, draw_heap


class TestBinaryHeapVisualization(unittest.TestCase):

    def setUp(self):
        """Sets up a simple binary heap for testing."""
        self.heap_root = create_heap()

    def test_node_creation(self):
        """Tests the creation of nodes in the binary heap."""
        self.assertIsNotNone(self.heap_root)
        self.assertEqual(self.heap_root.val, 10)
        self.assertIsNotNone(self.heap_root.left)
        self.assertEqual(self.heap_root.left.val, 20)
        self.assertIsNotNone(self.heap_root.right)
        self.assertEqual(self.heap_root.right.val, 30)

    def test_heap_structure(self):
        """Tests the structure of the binary heap."""
        self.assertIsNotNone(self.heap_root.left.left)
        self.assertEqual(self.heap_root.left.left.val, 40)
        self.assertIsNotNone(self.heap_root.left.right)
        self.assertEqual(self.heap_root.left.right.val, 50)
        self.assertIsNotNone(self.heap_root.right.left)
        self.assertEqual(self.heap_root.right.left.val, 60)
        self.assertIsNotNone(self.heap_root.right.right)
        self.assertEqual(self.heap_root.right.right.val, 70)

    def test_draw_heap(self):
        """Tests if draw_heap function runs without error."""
        try:
            draw_heap(self.heap_root)
        except Exception as e:
            self.fail(f"draw_heap raised an exception: {str(e)}")


if __name__ == "__main__":
    unittest.main()
