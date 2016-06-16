System.register([], function(exports_1) {
    var mockPostChildren;
    return {
        setters:[],
        execute: function() {
            mockPostChildren = (function () {
                function mockPostChildren(yPosition, offsetHeight) {
                    this.yPosition = yPosition;
                    this.offsetHeight = offsetHeight;
                    this._offsetHeight = offsetHeight;
                    this._yPosition = yPosition;
                }
                mockPostChildren.prototype.getNativeElement = function () {
                    return {
                        'offsetHeight': this._offsetHeight,
                        'y': this._yPosition,
                    };
                };
                return mockPostChildren;
            })();
            exports_1("mockPostChildren", mockPostChildren);
        }
    }
});
//# sourceMappingURL=mock-PostsChildren.js.map