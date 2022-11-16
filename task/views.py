from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from task.serializers import CreateTaskSerializer,UpdateTaskSerializer
from task.models import Task
from rest_framework.permissions import IsAuthenticated
import openpyxl as xl

class createtask(APIView):
    permission_classes = (IsAuthenticated,)
    
    

    def post(self, request, *args, **kwargs):
        try:
            
            task_serializer= CreateTaskSerializer( data=request.data)
            if task_serializer.is_valid():
                
                data_dict = task_serializer.validated_data
                data_dict['i_user_id'] = request.user.id
                
                Task.objects.create(**data_dict)
                
                return Response(
                    {'error': '', 'error_code': '', 'data': data_dict}, status=200)
            else:
                return Response({'error': task_serializer.errors, 'error_code': 'HS002', 'data':''}, status=200)
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)



class UpdateTaskAPI(APIView):
    permission_classes = [IsAuthenticated]
    

    def put(self, request, format=None, pk=None):
        if pk:
            try:
                Task_obj= Task.objects.get(pk=pk)
                serializer = Task_obj(UpdateTaskSerializer,data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {'error': '', 'error_code': '', 'data':serializer.data}, status=200)
                else:
                    return Response({'error': serializer.errors, 'error_code': 'HS002', 'matched': 'N', 'data': {}}, status=400)
            except Exception as e :
                print(repr(e))
                return Response({'error': repr(e), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)





class DeleteTaskAPI(APIView):
    permission_classes = [IsAuthenticated]
    

    def put(self, request, format=None, pk=None):
        if pk:
            try:
                Task_obj= Task.objects.get(pk=pk)
                Task_obj.is_active = False
                Task_obj.save()
                return Response(
                        {'error': '', 'error_code': '', 'data':"Sucessfully Delete"}, status=200)
            except Exception as e :
                print(repr(e))
                return Response({'error': repr(e), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)
        
        

class uploadtaskbulk(APIView):
    permission_classes = (IsAuthenticated,)
    
    

    def post(self, request, *args, **kwargs):
        try:
            file = request.data['file']
            
            wb_obj = xl.load_workbook(file)
            print(wb_obj)


        
            
            return Response(
                {'error': '', 'error_code': '', 'data': 'data_dict'}, status=200)
            
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)