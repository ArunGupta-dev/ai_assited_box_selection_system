from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core_utils.Logger import Logger
from box_manager.utils.box_handler import box_handler 

Log = Logger()


class box_manager(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            handler = box_handler()(data)

            return Response(
                    {'best_box':handler},
                    status=status.HTTP_200_OK
                    )


        except Exception as e:
            Log.Log_Error('box-manager-post-exception', e)
            return Response(
                    {'code':'error'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

