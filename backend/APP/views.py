from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .mathematics import *
# Create your views here.

@api_view(['POST'])
def newton_list(request):

    if request.method == 'POST':

        deserialized = Function_Integer_Integer(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            answer = Newton_Method(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.error_messages)


@api_view(['POST'])
def diff_list(request):

    if request.method == 'POST':

        deserialized = Function(data=request.data)
        
        if deserialized.is_valid():

            equation = deserialized.data['equation']
            answer = Differentiating_Calculator(equation)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)
    

@api_view(['POST'])
def taylor_list(request):
    
    if request.method == "POST":

        deserialized = Function_Integer_Integer(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            
            answer = Taylor_Series(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)



    # if request.method == 'GET':
    #     answer = {
    #         "equation":"x",
    #         "first":200,
    #         "second":300
    #     }

    #     serializer = NewtonSerializer(data=answer)
    #     serializer.is_valid()
    #     return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)
    
