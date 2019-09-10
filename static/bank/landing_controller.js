(function (angular) {
    "use strict";
    angular.module("BankFinder")
        .controller("AppLandingController", AppLandingController);

    AppLandingController.$inject = ["BranchIFSCResource", "BankBranchResource"];


    function AppLandingController(BranchIFSCResource, BankBranchResource) {

        var vm = this;
        initPage();

        vm.getBranchesByIFSC = getBranchesByIFSC;
        vm.getBranchesByBankCity = getBranchesByBankCity;

        function initPage() {
            vm.banks = [];
            vm.bankIFSC = {};
            vm.cityBank = {};
            vm.errorMessage = null;

        }

        function getBranchesByBankCity() {
            /*
            Gives list of Banks by City and Bank Name
             */
            vm.errorMessage = null;
            BankBranchResource.query(vm.cityBank, function (success_data) {
                vm.banks = success_data;
            }, function (error_data) {
                initPage();
                vm.errorMessage = error_data.data.detail;
            });
        }

        function getBranchesByIFSC() {
            /*
           Gives Bank by IFSC code
            */
            vm.errorMessage = null;
            BranchIFSCResource.get(vm.bankIFSC, function (success_data) {
                vm.banks = [success_data];
            }, function (error_data) {
                initPage();
                vm.errorMessage = error_data.data.detail;
            });
        }

    }
})(angular);

