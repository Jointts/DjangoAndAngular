"use strict";
var app = angular.module('ToDoList', []);

app.config(function ($interpolateProvider) {
    // Hello django, meet angular
    $interpolateProvider.startSymbol('{|{');
    $interpolateProvider.endSymbol('}|}');
});

app.controller('PostListController', function PostListController($scope, $http) {

    //  Function to retrieve all the posts
    $scope.postList = function () {
        $http.get('/api/posts/').success(function (data) {
            $scope.posts = data;
            $scope.posts.reverse();
        });
    };

    //  Function to save the post
    $scope.saveItem = function () {
        //  Check if all form fields are filled, if not, dont post
        if ($scope.postForm.$valid) {
            var in_data = {title: $scope.newPost.title, description: $scope.newPost.description};
            $http.post('/api/posts/', in_data).success(function () {
                $scope.postList();
            });
        }
    };

    //  Function to delete the post
    $scope.deleteItem = function (id) {
        $http.delete('/api/posts/' + id).success(function () {
            $scope.postList();
        })
    };

    //  Populate the list on first load, otherwise page would be empty
    $scope.postList();

});

