import unittest
from solutions.find_all_possible_recipes_from_given_supplies import Solution


class TestFindAllPossibleRecipesFromGivenSupplies(unittest.TestCase):
    def test_find_all_possible_recipes_from_given_supplies(self):
        solution = Solution()
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["yeast", "flour", "corn"]
        expect = ["bread"]
        actual = solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(expect, actual)

        recipes = ["bread", "sandwich"]
        ingredients = [["yeast", "flour"], ["bread", "meat"]]
        supplies = ["yeast", "flour", "meat"]
        expect = ["bread", "sandwich"]
        actual = solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(expect, actual)

        recipes = ["bread", "sandwich", "burger"]
        ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
        supplies = ["yeast", "flour", "meat"]
        expect = ["bread", "sandwich", "burger"]
        actual = solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(expect, actual)
