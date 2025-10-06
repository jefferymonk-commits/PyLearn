class ListCombiner:
    def __init__(self):
        self.list_a = []
        self.list_b = []
        self.list_c = []

    def generate_list_a(self):
        self.list_a = [1, 2, 3]
        return self.list_a

    def generate_list_b(self):
        self.list_b = ['x', 'y', 'z']
        return self.list_b

    def generate_list_c(self):
        self.list_c = [True, False]
        return self.list_c

    def combine_all_lists(self):
        # Call the functions to ensure the lists are populated
        self.generate_list_a()
        self.generate_list_b()
        self.generate_list_c()

        # Combine the lists using the '+' operator
        combined_list = self.list_a + self.list_b + self.list_c
        return combined_list

# Usage
combiner = ListCombiner()
final_list = combiner.combine_all_lists()
print(final_list)