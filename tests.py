import unittest

if __name__ == '__main__':
  testsuite = unittest.TestLoader().discover('.')
  
  # This statement does not trigger break points:
  #unittest.TextTestRunner(verbosity=1).run(testsuite)

  # So we'll write our own test runner that does hit breakpoints:
  for suite in testsuite:
    for test in suite:
      for t in test._tests:
        print(f"{type(t).__module__}.{type(t).__name__}.{t._testMethodName}")
        getattr(t, t._testMethodName)()
