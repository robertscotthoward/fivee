import unittest

if __name__ == '__main__':
  testsuite = unittest.TestLoader().discover('.')
  
  # This statement does not trigger break points in Visual Studio:
  # unittest.TextTestRunner(verbosity=1).run(testsuite)
  # See: https://developercommunity.visualstudio.com/t/python-unittests-cannot-be-debugged-breakpoints-ig/1237937

  # So we'll write our own test runner that does hit breakpoints:
  for suite in testsuite:
    for test in suite:
      for t in test._tests:
        print(f"{type(t).__module__}.{type(t).__name__}.{t._testMethodName}")
        getattr(t, t._testMethodName)()
