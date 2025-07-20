import smartpy as sp

@sp.module
def main():
    """
    A simple counter contract.
    """
    class Counter(sp.Contract):
        def __init__(self, initial_value):
            """
            Initializes the contract's storage.
            
            Args:
                initial_value (sp.TInt): The starting number for the counter.
            """
            self.data.value = initial_value

        @sp.entrypoint
        def increment(self, amount):
            """
            Increments the stored value by a given amount.
            
            Args:
                amount (sp.TInt): The number to add to the counter.
            """
            assert amount > 0, "Increment amount must be positive"
            self.data.value += amount

        @sp.entrypoint
        def decrement(self, amount):
            """
            Decrements the stored value by a given amount.
            
            Args:
                amount (sp.TInt): The number to subtract from the counter.
            """
            assert amount > 0, "Decrement amount must be positive"
            self.data.value -= amount

# --- Test Scenario ---
@sp.add_test()
def test():
    scenario = sp.test_scenario("Counter Test")

    admin = sp.test_account("Admin")

    c1 = main.Counter(initial_value=10)
    scenario += c1

    # --- Test an increment ---
    scenario.h2("Testing Increment")
    scenario.p("Initial value is 10.")
    c1.increment(5, _sender=admin)
    scenario.verify(c1.data.value == 15)
    scenario.p("Value is now 15.")

    # --- Test a decrement ---
    scenario.h2("Testing Decrement")
    c1.decrement(3, _sender=admin)
    scenario.verify(c1.data.value == 12)
    scenario.p("Value is now 12.")
    
    # --- Test a failing condition ---
    scenario.h2("Testing Failing Condition")
    scenario.p("Decrementing by 0 should fail.")
    # This is the corrected line. We now call with an amount (0)
    # that will correctly trigger the contract's assertion.
    c1.decrement(0, _sender=admin, _valid=False)