(function (angular) {
    "use strict";
    angular.module("BankFinder", [
        "ngResource",
        "ngRoute"
    ]);
})(angular);

(function (angular) {
    "use strict";
    angular.module("BankFinder").config(["$routeProvider", "$resourceProvider",
        function ($routeProvider, $resourceProvider) {

            $resourceProvider.defaults.stripTrailingSlashes = false;

            $routeProvider.when("/", {
                name: "Landing",
                controller: "AppLandingController",
                controllerAs: 'vm',
                templateUrl: "/static/bank/app_landing.html"
            }).otherwise({
                redirectTo: '/'
            });
        }
    ]);
})(angular);
