# 343-Test-suite

Welcome to the 343-Test-suite! This repository contains a set of tests designed to ensure the robustness and functionality of your application. Follow the instructions below to get started:

## Getting Started

1. **Prerequisites:** Make sure you have Flask up and running on your local environment.

2. **Configuration:** Open the `test343.py` file and locate the `TEST_URL` variable. Update this variable with the URL of your running Flask application.

3. **GitHub Token:** In order to run some of the tests, you'll need to provide a GitHub token. Please follow the steps below to add your token:

   - Visit [GitHub Personal Access Tokens](https://github.com/settings/tokens) to generate a new token with the necessary permissions.
   - Copy the generated token.
   - In the `test343.py` file, locate the `GITHUB_TOKEN` variable. Replace it with your actual GitHub token.

4. **Run Tests:** Open your terminal and navigate to the project directory. Run the following command:

   - python3 test343.py

This will execute the test suite against your application.

## Important Notes

- This test suite is designed to assess various aspects of your application's functionality. However, please be aware that it does not cover the following areas:

1. Test for Status Codes: This suite does not include tests to verify specific HTTP status codes returned by your application.

2. Test for Invalid Users: Testing invalid user scenarios is not included in this suite.

Feel free to customize and expand this test suite according to your application's specific needs. We hope these tests prove helpful in maintaining the quality and reliability of your project.

Happy testing!