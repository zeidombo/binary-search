import time
# from alice_bsort import (locate_card, tests)

def evaluate_test_cases(func, tests):
    """Return execution time and details about a test"""
    summary = []
    total_test = len(tests)
    passed = 0
    failed = 0
    for index, test in enumerate(tests, start=1):
        start_time = time.time()
        out = func(**test["input"])
        if out == test["output"]:
            print(f"Test #{index}: PASSED")
            status = True
            passed += 1
        else:
            print(f"Test #{index}: FAILED")
            failed += 1
            status = False
            print(f"cards: {test['input']['cards']}\nquery: {test['input']['query']}")
        exec_time = time.time() - start_time
        exec_time = float(f"{exec_time*1000:.3f}")

        summary.append((out, status, exec_time))

        print(f"Executed in: {exec_time} ms")
        print()

    print("*"*60)
    print("SUMMARY\n")
    print(f"TOTAL: {total_test}, PASSED: {passed}, FAILED: {failed}")

    print(summary)




