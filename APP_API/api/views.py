from django.http.response import Http404
from rest_framework.views import APIView
from .models import TableCars
from .serializers import TableCarsSerializer
from rest_framework.response import Response

# Create your views here.

class TCAPIView(APIView):

    # READ a single API
    def get_object(self, pk):
        try:
            return TableCars.objects.get(pk=pk)
        except TableCars.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = TableCarsSerializer(data)
        else:
            data = TableCars.objects.all()
            serializer = TableCarsSerializer(data, many=True)

        # Return Response to User
        response = Response()
        response.data = {
            'Pesan': 'List Data Mobil',
            'data': serializer.data
        }
        return response

    def post(self, request):
        data = request.data
        serializer = TableCarsSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create API in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'Pesan': 'Data Mobil Berhasil Ditambahkan',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None):
        # Get the API to update
        todo_to_update = TableCars.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire API object
        serializer = TableCarsSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'Pesan': 'Data Mobil Berhasil Dirubah',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk):
        todo_to_delete =  TableCars.objects.get(pk=pk)

        # delete the todo
        todo_to_delete.delete()

        return Response({
            'Pesan': 'Data Mobil Berhasil Dihapus'
        })