(function (angular) {
    "use strict";
    angular.module("BankFinder")
        .controller("AppLandingController", AppLandingController);

    AppLandingController.$inject = ["BranchIFSCResource", "BankBranchResource"];


    function AppLandingController(BranchIFSCResource, BankBranchResource) {

        var vm = this;

        vm.banks = [];
        vm.bankIFSC = {};
        vm.cityBranch = {};
        vm.errorMessage = null;

        vm.getBranchesByIFSC = getBranchesByIFSC;
        vm.getBranchesByBankCity = getBranchesByBankCity;


        function getBranchesByBankCity() {
            BankBranchResource.query(vm.cityBranch, function (success_data) {
                vm.banks = success_data;
                vm.errorMessage = null;
            }, function (error_data) {
                vm.errorMessage = error_data.data.detail;
            });
        }

        function getBranchesByIFSC() {
            BranchIFSCResource.get(vm.bankIFSC, function (success_data) {
                vm.banks = [success_data];
                vm.errorMessage = null;
            }, function (error_data) {
                vm.errorMessage = error_data.data.detail;
            });
        }

    }
})(angular);

