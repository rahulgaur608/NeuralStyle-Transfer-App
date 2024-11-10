import unittest
import contribute
from subprocess import check_output, CalledProcessError
import os
import shutil
import tempfile

class TestContribute(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for a clean test environment
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Clean up the temporary directory after each test
        os.chdir('..')
        shutil.rmtree(self.test_dir)

    def test_arguments(self):
        # Test the argument parsing functionality
        args = contribute.arguments(['-nw'])
        self.assertTrue(args.no_weekends)
        self.assertEqual(args.max_commits, 10)
        self.assertTrue(1 <= contribute.contributions_per_day(args) <= 20)

    def test_contributions_per_day(self):
        # Test the maximum commits per day feature
        args = contribute.arguments(['-mc=15'])
        self.assertTrue(1 <= contribute.contributions_per_day(args) <= 15)

    def test_commit_generation(self):
        # Run the main function with a limited set of arguments
        contribute.main([
            '-nw',
            '--user_name=sampleuser',
            '--user_email=sampleuser@users.noreply.github.com',
            '-mc=5',
            '-fr=100',
            '-db=5',
            '-da=5'
        ])

        # Check the number of commits made
        try:
            commit_count = int(check_output(
                ['git', 'rev-list', '--count', 'HEAD']
            ).decode('utf-8'))
        except CalledProcessError:
            self.fail("Git command failed")

        # Ensure at least one commit was made and at most 5*10 (days) = 50
        self.assertTrue(1 <= commit_count <= 50)

if __name__ == "__main__":
    unittest.main()
