import grpc
from concurrent import futures
import time

# import the generated classes :
import ML_example_pb2
import ML_example_pb2_grpc
import predict_income

# import the function we made :
from predict_income import predict_sale_price


# _ONE_DAY_IN_SECONDS = 60 * 60 * 24
# class PredictServicer(ML_example_pb2_grpc.PredictServicer):
#     def predict_passenger_survived(self, request, context):
#         response = ML_example_pb2.Prediction()
#         response.Survived = predict_sale_price.predict_passenger_survived(request.jobType,request.degree, request.yearsExperience)
#         return response
# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
#     ML_example_pb2_grpc.add_PredictServicer_to_server(
#         PredictServicer(), server)
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     try:
#         while True:
#             time.sleep(_ONE_DAY_IN_SECONDS)
#     except KeyboardInterrupt:
#         server.stop(0)
# if __name__ == '__main__':
#     serve()
#











# create a class to define the server functions, derived from
# usingSKlearn_pb2_grpc.PredictServicer :
class PredictServicer(ML_example_pb2_grpc.PredictServicer):
    def predict_sale_price(self, request, context):
        # define the buffer of the response :
        response = ML_example_pb2.Prediction()
        # get the value of the response by calling the desired function :
        response.salary = predict_income.predict_sale_price(request.jobType,request.degree, request.yearsExperience)
        return response


# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))

ML_example_pb2_grpc.add_PredictServicer_to_server(PredictServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
