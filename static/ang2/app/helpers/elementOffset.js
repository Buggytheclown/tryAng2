System.register([], function(exports_1) {
    var elOffsetY;
    return {
        setters:[],
        execute: function() {
            elOffsetY = (function () {
                function elOffsetY(obj) {
                    this.obj = obj;
                    this.findPosY(this.obj);
                }
                elOffsetY.prototype.findPosY = function (obj) {
                    var curtop = 0;
                    if (obj.offsetParent) {
                        while (1) {
                            curtop += obj.offsetTop;
                            if (!obj.offsetParent) {
                                break;
                            }
                            obj = obj.offsetParent;
                        }
                    }
                    else if (obj.y) {
                        curtop += obj.y;
                    }
                    return curtop;
                };
                return elOffsetY;
            })();
            exports_1("elOffsetY", elOffsetY);
        }
    }
});
//# sourceMappingURL=elementOffset.js.map