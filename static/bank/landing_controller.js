(function (angular) {
    "use strict";
    angular.module("BankFinder")
        .controller("AppLandingController", AppLandingController);

    AppLandingController.$inject = ["BranchIFSCResource", "BankBranchResource"];


    function AppLandingController(BranchIFSCResource, BankBranchResource) {

        var vm = this;

        vm.banks = [];
        vm.bankIFSC = {};
        vm.cityBank = {};
        vm.errorMessage = null;

        vm.getBranchesByIFSC = getBranchesByIFSC;
        vm.getBranchesByBankCity = getBranchesByBankCity;


        function getBranchesByBankCity() {
            /*
            Gives list of Banks by City and Bank Name
             */
            BankBranchResource.query(vm.cityBank, function (success_data) {
                vm.banks = success_data;
                vm.errorMessage = null;
            }, function (error_data) {
                vm.errorMessage = error_data.data.detail;
            });
        }

        function getBranchesByIFSC() {
             /*
            Gives Bank by IFSC code
             */
            BranchIFSCResource.get(vm.bankIFSC, function (success_data) {
                vm.banks = [success_data];
                vm.errorMessage = null;
            }, function (error_data) {
                vm.errorMessage = error_data.data.detail;
            });
        }

    }
})(angular);

