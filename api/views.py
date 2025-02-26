from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
import requests

@api_view(['GET'])
def get_users(request):
    # users=User.objects.all()

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Convertit la réponse en JSON
        # print(data[1]["title"])
        return Response(data)
    else:
        print("Erreur:", response.status_code)
        return Response([{"id":1,"nom":"Tresors"},{"id":2,"nom":"Perla"}])
@api_view(['POST'])
def create_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(UserSerializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def user_detail(request,pk):
    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("Non trouvé")
    
    if request.method == "PUT":
        serialiser=UserSerializer(user,data=request.data)
        if serialiser.isValid():
            serialiser.save()
            
