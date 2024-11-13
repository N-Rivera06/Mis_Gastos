from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from Users.models               import User
from Users.api.serializers      import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

class RegisterView (APIView):
    def post(self, resquest):
        #print('Registro de usuario')
        #return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer=UserRegisterSerializer(data=resquest.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#obtener los datos del usuario logeado

class UserView(APIView):
    Permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    #sobreescribir para modificar los datos del usuario logeado
    def put(self, request):
        user = User.objects.get(id=request.user.id) 
        serializer =  UserUpdateSerializer(user, request.data)

        #para guardar el rerializer
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)