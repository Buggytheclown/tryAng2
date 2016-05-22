System.register([], function(exports_1) {
    var PostsHelper;
    return {
        setters:[],
        execute: function() {
            PostsHelper = (function () {
                function PostsHelper() {
                    //onScroll check if viewed post is changed
                    //if viewed post changed - change viwedPost
                    this.posts = [];
                    this.currentPost = {
                        get: function () {
                        }, set: function () {
                        }
                    };
                }
                return PostsHelper;
            })();
            exports_1("PostsHelper", PostsHelper);
        }
    }
});
//# sourceMappingURL=posts2.js.map