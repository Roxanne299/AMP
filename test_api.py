import public_timeseries_testing_util

env = public_timeseries_testing_util.make_env()
iter_test = env.iter_test()

counter = 0
# The API will deliver four dataframes in this specific order:
for (test, test_peptides, test_proteins, sample_submission) in iter_test:
    if counter == 0:
        print(test.head())
        print(test_peptides.head())
        print(test_proteins.head())
        print(sample_submission.head())
        sample_submission['rating'] = 0
    env.predict(sample_submission)
    counter += 1
