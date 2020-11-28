import grpc
from random import randint
from timeit import default_timer as timer
import random
import argparse

# import the generated classes
import ML_example_pb2
import ML_example_pb2_grpc
from predict_income import predict_sale_price



#
# parser = argparse.ArgumentParser()
# parser.add_argument('--jobType', type=int, help='input:jobType')
# parser.add_argument('--degree', type=int, help='input:degree')
# parser.add_argument('--yearsExperience', type=float, help='input:yearsExperience')
#
# args = parser.parse_args()
# channel = grpc.insecure_channel('localhost:50051')
# stub = ML_example_pb2_grpc.PredictStub(channel)
#
# requestPrediction  = ML_example_pb2.Features(jobType = 1, degree = 2, yearsExperience = 10)
# responsePrediction = stub.predict_sale_price(requestPrediction)
# print('The prediction is :',responsePrediction.Survived)












start_ch = timer()

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = ML_example_pb2_grpc.PredictStub(channel)
end_ch = timer()


jobType   = 2
degree      = 3
yearsExperience    = 10.0

ans_lst = []

start = timer()


    # create a valid request message
requestPrediction  = ML_example_pb2.Features(jobType=jobType,degree=degree,yearsExperience=yearsExperience)

# make the call
responsePrediction = stub.predict_sale_price(requestPrediction)
ans_lst.append(responsePrediction.salary)
print(f'The prediction is : {responsePrediction.salary:.2f} $')
print('Done!')
