System.register([], function(exports_1) {
    var sb_windowToolsY;
    return {
        setters:[],
        execute: function() {
            sb_windowToolsY = (function () {
                function sb_windowToolsY() {
                    this.scrollBarPadding = 17; // padding to assume for scroll bars
                    this._viewportHeight = undefined;
                    this._windowHeightPrevious = undefined;
                    this._windowHeight = undefined;
                    this._verticalOffset = undefined;
                }
                // load the page size, view port position and vertical scroll offset
                sb_windowToolsY.prototype.updateDimensions = function () {
                    this.updateViewportHeight();
                    this.updateWindowHeight();
                    this.updateScrollOffset();
                };
                ;
                sb_windowToolsY.prototype.updateWindowHeight = function () {
                    // document dimensions
                    this._windowHeightPrevious = this._windowHeight;
                    var windowHeight;
                    if (window.innerHeight && window.scrollMaxY) {
                        windowHeight = window.innerHeight + window.scrollMaxY;
                    }
                    else if (document.body.scrollHeight > document.body.offsetHeight) {
                        // all but explorer mac
                        windowHeight = document.body.scrollHeight;
                    }
                    else {
                        // explorer mac...would also work in explorer 6 strict, mozilla and safari
                        windowHeight = document.body.offsetHeight;
                    }
                    this._windowHeight = windowHeight;
                };
                ;
                // load window size information
                sb_windowToolsY.prototype.updateViewportHeight = function () {
                    // view port dimensions
                    var viewportHeight;
                    if (self.innerHeight) {
                        // all except explorer
                        viewportHeight = self.innerHeight;
                    }
                    else if (document.documentElement && document.documentElement.clientHeight) {
                        // explorer 6 strict mode
                        viewportHeight = document.documentElement.clientHeight;
                    }
                    else if (document.body) {
                        // other explorers
                        viewportHeight = document.body.clientHeight;
                    }
                    this._viewportHeight = viewportHeight;
                };
                ;
                // load scroll offset information
                sb_windowToolsY.prototype.updateScrollOffset = function () {
                    // viewport vertical scroll offset
                    var verticalOffset;
                    if (self.pageYOffset) {
                        verticalOffset = self.pageYOffset;
                    }
                    else if (document.documentElement && document.documentElement.scrollTop) {
                        // Explorer 6 Strict
                        verticalOffset = document.documentElement.scrollTop;
                    }
                    else if (document.body) {
                        // all other Explorers
                        verticalOffset = document.body.scrollTop;
                    }
                    this._verticalOffset = verticalOffset;
                };
                ;
                // combined dimensions object with bounding logic
                sb_windowToolsY.prototype.pageHeight = function () {
                    return this._viewportHeight > this._windowHeight ?
                        this._viewportHeight : this._windowHeight;
                };
                ;
                sb_windowToolsY.prototype.windowHeight = function () {
                    return this._windowHeight;
                };
                ;
                sb_windowToolsY.prototype.verticalOffset = function () {
                    return this._verticalOffset;
                };
                ;
                sb_windowToolsY.prototype.scrollPercent = function () {
                    return ((this._viewportHeight + this._verticalOffset) / this.pageHeight());
                };
                ;
                sb_windowToolsY.prototype.isPageHeightChanged = function () {
                    return this._windowHeightPrevious !== this._windowHeight;
                };
                ;
                sb_windowToolsY.prototype.findPosY = function (obj) {
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
                return sb_windowToolsY;
            })();
            exports_1("sb_windowToolsY", sb_windowToolsY);
        }
    }
});
//# sourceMappingURL=sb_windowToolsY.js.map