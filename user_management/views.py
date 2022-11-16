from rest_framework.response import Response
from rest_framework.views import APIView
from user_management.serializers import AllTask, AllUsersSerializer, AppUserSerializer
from rest_framework.permissions import IsAuthenticated
from task.models import Task
from user_management.models import Profile


class AppUser(APIView):

    def post(self, request, *args, **kwargs):
        try:
            

            user_serializer = AppUserSerializer(context={'request': request}, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                print(user_serializer.data,"oooooooooooo")
                return Response(
                    {'error': '', 'error_code': '', 'data': user_serializer.data}, status=200)
            else:
                return Response({'error': user_serializer.errors, 'error_code': 'HS002', 'data':''}, status=200)
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class ListUsersAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # res = AllUsersPicsSerializer(all_users, many=True)
        return Response({'error': '', 'error_code': '', 'data': 'res.data'}, status=200)



class LoginUser(APIView):
    # permission_classes = []
    permission_classes = (IsAuthenticated,)
    

    def post(self, request, *args, **kwargs):
        try:
            profile_obj = Profile.objects.get(i_user_id=request.user.id).user_type
            if profile_obj == 'A':
                all_task = list(Task.objects.filter(is_active=True).values_list('task',flat=True))
            else:
                all_task = list(Task.objects.filter(i_user=request.user.id).values_list('task',flat=True))
            if all_task:
                return Response(
                        {'error': '', 'error_code': '', 'data': all_task}, status=200)
            else:
                return Response({'message': "No Task is available", 'error_code': 'HS002', 'data':''}, status=200)
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

