0x03. Unittests and Integration Tests
=====================================

This repo is included in Specializations - Web Stack programming ― Back-end Course of Holberton School. We will cover the `Unittests and Integration Tests` in python language

![Logo](https://www.howtogeek.com/wp-content/uploads/2021/05/laptop-with-terminal-big.png?height=200p&trim=2,2,2,50)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

    $ python -m unittest path/to/test_file.py

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/YPwJ2XFk6SxPAXslU2EK0g "explain to anyone"), **without the help of Google**:

*   The difference between unit and integration tests.
*   Common testing patterns such as mocking, parametrizations and fixtures

Resources
---------

**Read or watch:**

*   [unittest — Unit testing framework](https://intranet.hbtn.io/rltoken/gvyg14PB6pkk6rLIlZfMOw "unittest — Unit testing framework")
*   [unittest.mock — mock object library](https://intranet.hbtn.io/rltoken/IRUwzh16CVuEUH2x3KgDUA "unittest.mock — mock object library")
*   [How to mock a readonly property with mock?](https://intranet.hbtn.io/rltoken/sQRCH33cRr2FpNeI7L828g "How to mock a readonly property with mock?")
*   [parameterized](https://intranet.hbtn.io/rltoken/D1MlxxxgWbJa6rLsJlWTpA "parameterized")
*   [Memoization](https://intranet.hbtn.io/rltoken/oiljWJGvcWuJibuc6cX0ww "Memoization")


### Integration test: fixtures

mandatory

We want to test the `GithubOrgClient.public_repos` method in an integration test. That means that we will only mock code that sends external requests.

Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API.

Use `@parameterized_class` to decorate the class and parameterize it with fixtures found in `fixtures.py`. The file contains the following fixtures:

    org_payload, repos_payload, expected_repos, apache2_repos
    

The `setupClass` should mock `requests.get` to return example payloads found in the fixtures.

Use `patch` to start a patcher named `get_patcher`, and use `side_effect` to make sure the mock of `requests.get(url).json()` returns the correct fixtures for the various values of `url` that you anticipate to receive.

Implement the `tearDownClass` class method to stop the patcher.

### Integration tests

Implement the `test_public_repos` method to test `GithubOrgClient.public_repos`.

Make sure that the method returns the expected results based on the fixtures.

Implement `test_public_repos_with_license` to test the `public_repos` with the argument `license="apache-2.0"` and make sure the result matches the expected value from the fixtures.

## Acknowledgments :mega: 

### **`ALX AFRICA`** (*providing guidance*)
This program was written as part of the curriculum for ALX AFRICA.
ALX AFRICA is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information, visit [ALX AFRICA](https://www.alxafrica.com/).
