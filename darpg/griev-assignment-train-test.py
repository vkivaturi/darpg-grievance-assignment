import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator
import logging

filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance_truncated.csv'

print('## Model training and testing script has started')

h2o.init()

print('## h2o is initialized')

# Import the grievance dataset
grievance_dataset = h2o.import_file(filename_csv)

print('## h2o grievance_dataset_full frame is loaded')

print(grievance_dataset.nrows)

print('## grievance_dataset frame is created')

# convert columns to factors
grievance_dataset['SEX'] = grievance_dataset['SEX'].asfactor()
#grievance_dataset['ORG_CODE'] = grievance_dataset['ORG_CODE'].asfactor()
#grievance_dataset['PINCODE'] = grievance_dataset['PINCODE'].asfactor()

# set the predictor and response columns
predictors = ["ORG_CODE", "PINCODE"]
response_col = "SEX"

print('## predictors and responses are set')

# split into train and testing sets
train, test = grievance_dataset.split_frame(ratios = [0.9], seed = 1234)

# set GLM modeling parameters
# and initialize model training
glm_model = H2OGeneralizedLinearEstimator(family= "auto"
                                          #lambda_ = 0,
                                          #compute_p_values = True
                                          )

glm_model.train(predictors, response_col, training_frame= grievance_dataset)

# predict using the model and the testing dataset
predict = glm_model.predict(test)
print("Printing predictions")
print(predict)

# View a summary of the prediction
predict.head()



