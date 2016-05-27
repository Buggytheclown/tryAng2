System.register([], function(exports_1) {
    var sb_windowTools;
    return {
        setters:[],
        execute: function() {
            sb_windowTools = (function () {
                function sb_windowTools() {
                    this.scrollBarPadding = 17; // padding to assume for scroll bars
                    this.pageSize = {};
                    this.windowSize = {};
                    this.scrollOffset = {};
                }
                ;
                sb_windowTools.prototype.centerElementOnScreen = function (element) {
                    var pageDimensions = this.updateDimensions();
                    element.style.top = ((this.verticalOffset() + this.windowHeight() / 2) - (this.scrollBarPadding + element.offsetHeight / 2)) + 'px';
                    element.style.left = ((this.windowWidth() / 2) - (this.scrollBarPadding + element.offsetWidth / 2)) + 'px';
                    element.style.position = 'absolute';
                };
                ;
                // load the page size, view port position and vertical scroll offset
                sb_windowTools.prototype.updateDimensions = function () {
                    this.updatePageSize();
                    this.updateWindowSize();
                    this.updateScrollOffset();
                };
                ;
                sb_windowTools.prototype.updatePageSize = function () {
                    // document dimensions
                    var viewportWidth, viewportHeight;
                    if (window.innerHeight && window.scrollMaxY) {
                        viewportWidth = document.body.scrollWidth;
                        viewportHeight = window.innerHeight + window.scrollMaxY;
                    }
                    else if (document.body.scrollHeight > document.body.offsetHeight) {
                        // all but explorer mac
                        viewportWidth = document.body.scrollWidth;
                        viewportHeight = document.body.scrollHeight;
                    }
                    else {
                        // explorer mac...would also work in explorer 6 strict, mozilla and safari
                        viewportWidth = document.body.offsetWidth;
                        viewportHeight = document.body.offsetHeight;
                    }
                    this.pageSize = {
                        viewportWidth: viewportWidth,
                        viewportHeight: viewportHeight
                    };
                };
                ;
                // load window size information
                sb_windowTools.prototype.updateWindowSize = function () {
                    // view port dimensions
                    var windowWidth, windowHeight;
                    if (self.innerHeight) {
                        // all except explorer
                        windowWidth = self.innerWidth;
                        windowHeight = self.innerHeight;
                    }
                    else if (document.documentElement && document.documentElement.clientHeight) {
                        // explorer 6 strict mode
                        windowWidth = document.documentElement.clientWidth;
                        windowHeight = document.documentElement.clientHeight;
                    }
                    else if (document.body) {
                        // other explorers
                        windowWidth = document.body.clientWidth;
                        windowHeight = document.body.clientHeight;
                    }
                    this.windowSize = {
                        windowWidth: windowWidth,
                        windowHeight: windowHeight
                    };
                };
                ;
                // load scroll offset information
                sb_windowTools.prototype.updateScrollOffset = function () {
                    // viewport vertical scroll offset
                    var horizontalOffset, verticalOffset;
                    if (self.pageYOffset) {
                        horizontalOffset = self.pageXOffset;
                        verticalOffset = self.pageYOffset;
                    }
                    else if (document.documentElement && document.documentElement.scrollTop) {
                        // Explorer 6 Strict
                        horizontalOffset = document.documentElement.scrollLeft;
                        verticalOffset = document.documentElement.scrollTop;
                    }
                    else if (document.body) {
                        // all other Explorers
                        horizontalOffset = document.body.scrollLeft;
                        verticalOffset = document.body.scrollTop;
                    }
                    this.scrollOffset = {
                        horizontalOffset: horizontalOffset,
                        verticalOffset: verticalOffset
                    };
                };
                ;
                // INFORMATION CONTAINERS
                // raw data containers
                // combined dimensions object with bounding logic
                sb_windowTools.prototype.pageWidth = function () {
                    return this.pageSize.viewportWidth > this.windowSize.windowWidth ?
                        this.pageSize.viewportWidth :
                        this.windowSize.windowWidth;
                };
                ;
                sb_windowTools.prototype.pageHeight = function () {
                    return this.pageSize.viewportHeight > this.windowSize.windowHeight ?
                        this.pageSize.viewportHeight :
                        this.windowSize.windowHeight;
                };
                ;
                sb_windowTools.prototype.windowWidth = function () {
                    return this.windowSize.windowWidth;
                };
                ;
                sb_windowTools.prototype.windowHeight = function () {
                    return this.windowSize.windowHeight;
                };
                ;
                sb_windowTools.prototype.horizontalOffset = function () {
                    return this.scrollOffset.horizontalOffset;
                };
                ;
                sb_windowTools.prototype.verticalOffset = function () {
                    return this.scrollOffset.verticalOffset;
                };
                ;
                sb_windowTools.prototype.scrollPercent = function () {
                    return ((this.windowSize.windowHeight + this.scrollOffset.verticalOffset) / this.pageHeight());
                };
                ;
                sb_windowTools.prototype.findPosY = function (obj) {
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
                return sb_windowTools;
            })();
            exports_1("sb_windowTools", sb_windowTools);
        }
    }
});
//# sourceMappingURL=sb_windowTools.js.map