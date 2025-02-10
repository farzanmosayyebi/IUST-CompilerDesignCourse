class DatasetCleanerCodeGenerator:
    def __init__(self):
        self.commands = []

    def generate_code(self, post_order_traversal):
        for node in post_order_traversal:
            label = node.get('label')
            if label:
                if label.startswith('CLEAN'):
                    c = []
                    c.append(f'# Cleaning dataset: {label.split()[1]}')
                    c.append("import pandas as pd")
                    c.append(f'df = pd.read_csv({label.split()[1]})')
                    self.commands = c + self.commands

                elif label.startswith('REMOVE'):
                    self.commands.append('df.drop_duplicates(inplace=True)')

                elif label.startswith('DROP'):
                    self.commands.append('df.dropna(inplace=True)')

                elif label.startswith('FILL'):
                    _, _, column, _, value = label.split()
                    self.commands.append(f'df[{column}].fillna({value}, inplace=True)')

                elif label.startswith('FILTER'):
                    _, column, op, value = label.split()
                    self.commands.append(f'df = df[df[{column}] {op} {value}]')

                elif label.startswith('RENAME'):
                    _, old_column, _, new_column = label.split()
                    self.commands.append(f'df.rename(columns={{{old_column}: {new_column}}}, inplace=True)')

        return '\n'.join(self.commands)
