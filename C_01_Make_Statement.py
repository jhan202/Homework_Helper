# Functions go here
def make_statement(statement, decoration):
    return f"{decoration*1} {statement} {decoration*1}"


# Main routine goes here

# testing make_statement
print(make_statement("Homework Helper", "✖️➕➗"))
print(make_statement("Instructions", "ℹ️"))
print(make_statement("Results", "--"))

