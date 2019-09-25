from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView

from bank.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Branch model used for List and Get purpose
    """
    bank = serializers.CharField(source='bank_name',
                                 help_text="bank_name is model property which gives bank name"
                                           "instead of bank id")

    class Meta:
        model = Branch
        # get all the fields and overwrite bank files with serialiser field
        fields = '__all__'


class BranchIFSCView(APIView):
    """
    Info:
      Content-Type: application/json
      url:  <IP_address>/api/branch-ifsc/<desired IFSC code>
      description: BranchIFSCView is used to retrieve Branch details by sending IFSC code
      version: 1.0
      test: tests/TestBranchIFSCView
    Status:
      '200':
         Description: Provided IFSC is found
         Schema:
            type: Dict
            :returns {
                    "ifsc": "<str>: ifsc code" ,
                    "bank": "<str>: bank name",
                    "branch": "<str>: branch name",
                    "address": "<str>: address",
                    "city": "<str>: City name",
                    "district": "<str>: District name",
                    "state": "<str>: state name"
                }
      '404':
         Description: Give IFSC is not present in records
         Schema:
            type: Dict
            :returns {
                    "detail": "Branch not found for given IFSC code"
                    }
    """

    def get(self, request, ifsc_code):
        try:
            branch = Branch.objects.get(ifsc__iexact=ifsc_code)
        except ObjectDoesNotExist:
            # HTTP_404_NOT_FOUND status
            raise NotFound('Branch not found for given IFSC code')
        serializer = BranchSerializer(branch)
        return Response(serializer.data)


class BankBranchView(APIView):
    """
    Info:
      Content-Type: application/json
      url:  <IP_address>/api/bank-branch/?city=<City Name>&bank=<Bank name>
      :arg: city: City Name
      :arg: bank: Bank Name
      description: BankBranchView is used to get Branch details by City and Bank name
      version: 1.0
      test: tests/TestBankBranchView
    Status:
      '200':
         Description: If records found for given City and Bank name
         Schema:
            type: List
            :returns [{
                    "ifsc": "<str>: ifsc code" ,
                    "bank": "<str>: bank name",
                    "branch": "<str>: branch name",
                    "address": "<str>: address",
                    "city": "<str>: City name",
                    "district": "<str>: District name",
                    "state": "<str>: state name"
                }]
      '404':
         Description: If records not found for given City and Bank name
         Schema:
            type: Dict
            :returns {
                    "detail": "No branch found for provided Bank and City."
                    }
      '422':
         Description: If City name or Bank name or both are not provided in API
         Schema:
            type: Dict
            :returns {
                    "detail": "Both City and Bank names are required to get all the branches of the Bank in the City."
                    }

    """

    def get(self, request):
        # Response time:  71 ms for 103 records: size 21 KB

        city = request.GET.get("city")
        bank = request.GET.get("bank")
        if not city or not bank:
            response_data = {"detail": "Both City and Bank names are required "
                                       "to get all the branches of the Bank in the City."}
            return Response(response_data, status=HTTP_422_UNPROCESSABLE_ENTITY)

        branches = Branch.objects.filter(city__iexact=city,
                                         bank__name__iexact=bank).select_related("bank").values("ifsc", "bank__name",
                                                                                                "branch", "address",
                                                                                                "city", "district",
                                                                                                "state")
        if not branches:
            raise NotFound('No branch found for provided Bank and City.')

        data = [{
            "ifsc": branch["ifsc"],
            "bank": branch["bank__name"],
            "branch": branch["branch"],
            "address": branchb["address"],
            "city": branch["city"],
            "district": branch["district"],
            "state": branch["state"]
        } for branch in branches]

        return Response(data)
