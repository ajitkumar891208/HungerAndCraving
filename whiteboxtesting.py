# White Box Testing Demonstration Code
# Each section simulates a real test scenario for that concept

# -----------------------------
# 1. UNIT TESTING
# -----------------------------
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# -----------------------------
# 2. STATEMENT COVERAGE
# -----------------------------
def statement_example(x):
    if x > 0:
        y = x * 2
    print("Done")

def test_statement_coverage():
    statement_example(5)   # Executes both lines
    statement_example(-3)  # Only "Done" executed

# -----------------------------
# 3. BRANCH COVERAGE
# -----------------------------
def branch_example(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

def test_branch_coverage():
    assert branch_example(2) == "Even"  # True branch
    assert branch_example(3) == "Odd"   # False branch

# -----------------------------
# 4. PATH COVERAGE
# -----------------------------
def path_example(a, b):
    if a > 0:
        if b > 0:
            return "Both positive"
        else:
            return "a positive only"
    else:
        return "a not positive"

def test_path_coverage():
    assert path_example(1, 1) == "Both positive"       # Path 1
    assert path_example(1, -1) == "a positive only"    # Path 2
    assert path_example(-1, 5) == "a not positive"     # Path 3

# -----------------------------
# 5. CONDITION COVERAGE
# -----------------------------
def condition_example(x, y):
    if x > 0 and y > 0:
        return "Both positive"
    return "Not both positive"

def test_condition_coverage():
    assert condition_example(1, 1) == "Both positive"      # True, True
    assert condition_example(1, -1) == "Not both positive" # True, False
    assert condition_example(-1, 1) == "Not both positive" # False, True

# -----------------------------
# 6. LOOP TESTING
# -----------------------------
def loop_example(n):
    total = 0
    for i in range(n):
        total += i
    return total

def test_loop_testing():
    assert loop_example(0) == 0    # 0 iteration
    assert loop_example(1) == 0    # 1 iteration
    assert loop_example(5) == 10   # multiple iterations

# -----------------------------
# 7. CONTROL FLOW TESTING
# -----------------------------
def control_flow_example(x):
    y = 0
    if x > 0:
        y = x
    else:
        y = -x
    return y

def test_control_flow():
    assert control_flow_example(3) == 3
    assert control_flow_example(-4) == 4

# -----------------------------
# 8. DATA FLOW TESTING
# -----------------------------
def data_flow_example(x):
    y = x + 1  # define
    z = y * 2  # use
    return z

def test_data_flow():
    assert data_flow_example(3) == 8  # definition-use path checked

# -----------------------------
# 9. MUTATION TESTING
# -----------------------------
def mutation_original(x):
    return x * 2

def mutation_variant(x):
    return x * 3  # Mutation: *3 instead of *2

def test_mutation():
    assert mutation_original(4) == 8
    # If the test fails for mutation_variant, mutation was detected
    assert mutation_variant(4) != mutation_original(4)

# -----------------------------
# 10. BASIS PATH TESTING
# -----------------------------
def basis_path_example(a, b, c):
    if a > 0 and b > 0:
        c = c + 1
    elif a > 0 or b > 0:
        c = c - 1
    return c

def test_basis_path():
    assert basis_path_example(1, 1, 5) == 6  # Path 1
    assert basis_path_example(1, -1, 5) == 4 # Path 2
    assert basis_path_example(-1, -1, 5) == 5 # Path 3

# -----------------------------
# RUN ALL TESTS
# -----------------------------
if __name__ == "__main__":
    test_add()
    test_statement_coverage()
    test_branch_coverage()
    test_path_coverage()
    test_condition_coverage()
    test_loop_testing()
    test_control_flow()
    test_data_flow()
    test_mutation()
    test_basis_path()
    print("✅ All white-box test demonstrations executed successfully!")
