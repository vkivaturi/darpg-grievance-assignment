# Source code of this file is taken from https://docs.h2o.ai/h2o/latest-stable/h2o-docs/training-models.html
import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

h2o.init()

# import the prostate dataset
prostate = h2o.import_file("https://h2o-public-test-data.s3.amazonaws.com/smalldata/prostate/prostate.csv")

# convert columns to factors
prostate['CAPSULE'] = prostate['CAPSULE'].asfactor()
prostate['RACE'] = prostate['RACE'].asfactor()
prostate['DCAPS'] = prostate['DCAPS'].asfactor()
prostate['DPROS'] = prostate['DPROS'].asfactor()

# set the predictor and response columns
predictors = ["AGE", "RACE", "VOL", "GLEASON"]
response_col = "CAPSULE"

# split into train and testing sets
train, test = prostate.split_frame(ratios = [0.8], seed = 1234)

# set GLM modeling parameters
# and initialize model training
glm_model = H2OGeneralizedLinearEstimator(family= "binomial",
                                          lambda_ = 0,
                                          compute_p_values = True)
glm_model.train(predictors, response_col, training_frame= prostate)

# predict using the model and the testing dataset
predict = glm_model.predict(test)
print("Printing predictions")
print(predict)

# View a summary of the prediction
predict.head()
