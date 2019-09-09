(function (angular) {
    "use strict";
    angular.module("BankFinder").factory("BranchIFSCResource",
        ["$resource", function ($resource) {
            /*
               This resource is used to retrieve Branch details by sending IFSC code
                e.g. /api/branch-ifsc/ABHY0065001/
             */
            return $resource("/api/branch-ifsc/:ifsc_code", {});
        }]);
})(angular);

(function (angular) {
    "use strict";
    angular.module("BankFinder").factory("BankBranchResource",
        ["$resource", function ($resource) {
            /*
                This resource is used to get Branch details by City and Bank name
                e.g. /api/bank-branch/?city=Pune&bank=state bank of india
             */

            return $resource("/api/bank-branch/", {});
        }]);
})(angular);