import h2o
from h2o.estimators import H2ORandomForestEstimator
import logging

filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\grievance_merged_history_full_truncated.csv'

print('## Model training and testing script has started')

h2o.init()

print('## h2o is initialized')

# Import the grievance dataset
grievance_dataset = h2o.import_file(filename_csv)

print('## h2o grievance_dataset_full frame is loaded')

print(grievance_dataset.nrows)

print('## grievance_dataset frame is created')

# convert columns to factors
#grievance_dataset['history_officer_detail'] = grievance_dataset['history_officer_detail'].asfactor()
grievance_dataset['org_code'] = grievance_dataset['org_code'].asfactor()
grievance_dataset['pincode'] = grievance_dataset['pincode'].asfactor()

# set the predictor and response columns
predictors = ["pincode"]
response_col = "org_code"

print('## predictors and responses are set')

# split into train and testing sets
train, test = grievance_dataset.split_frame(ratios = [0.9], seed = 1234)

# set GLM modeling parameters
# and initialize model training
drf_model = H2ORandomForestEstimator(ntrees=10,
                                    max_depth=5,
                                    min_rows=10,
                                    #calibrate_model=True,
                                    calibration_frame=test,
                                    binomial_double_trees=True)

drf_model.train(predictors, response_col, training_frame= grievance_dataset)

# predict using the model and the testing dataset
predict = drf_model.predict(test)
print("Printing predictions")
print(predict)

# View a summary of the prediction
predict.head()

modelfile = drf_model.download_mojo(path="../build/", get_genmodel_jar=True)
print("Model saved to " + modelfile)



