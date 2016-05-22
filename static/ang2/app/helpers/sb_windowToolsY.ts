export class sb_windowToolsY {
    scrollBarPadding:number = 17; // padding to assume for scroll bars
    _viewportHeight:number = undefined;
    _windowHeightPrevious:number = undefined;
    _windowHeight:number = undefined;
    _verticalOffset:number = undefined;

    constructor() {
    };


    // load the page size, view port position and vertical scroll offset
    updateDimensions():void {
        this.updateViewportHeight();
        this.updateWindowHeight();
        this.updateScrollOffset();
    };

    updateWindowHeight():void {
        // document dimensions
        this._windowHeightPrevious = this._windowHeight;
        let windowHeight;
        if (window.innerHeight && window.scrollMaxY) {
            windowHeight = window.innerHeight + window.scrollMaxY;
        } else if (document.body.scrollHeight > document.body.offsetHeight) {
            // all but explorer mac
            windowHeight = document.body.scrollHeight;
        } else {
            // explorer mac...would also work in explorer 6 strict, mozilla and safari
            windowHeight = document.body.offsetHeight;
        }
        this._windowHeight = windowHeight

    };

    // load window size information
    updateViewportHeight():void {
        // view port dimensions
        var viewportHeight;
        if (self.innerHeight) {
            // all except explorer
            viewportHeight = self.innerHeight;
        } else if (document.documentElement && document.documentElement.clientHeight) {
            // explorer 6 strict mode
            viewportHeight = document.documentElement.clientHeight;
        } else if (document.body) {
            // other explorers
            viewportHeight = document.body.clientHeight;
        }

        this._viewportHeight = viewportHeight
    };

    // load scroll offset information
    updateScrollOffset():void {
        // viewport vertical scroll offset
        let verticalOffset;
        if (self.pageYOffset) {
            verticalOffset = self.pageYOffset;
        } else if (document.documentElement && document.documentElement.scrollTop) {
            // Explorer 6 Strict
            verticalOffset = document.documentElement.scrollTop;
        } else if (document.body) {
            // all other Explorers
            verticalOffset = document.body.scrollTop;
        }


        this._verticalOffset = verticalOffset
    };

    // combined dimensions object with bounding logic

    pageHeight():number {
        return this._viewportHeight > this._windowHeight ?
            this._viewportHeight : this._windowHeight;
    };

    windowHeight():number {
        return this._windowHeight;
    };

    verticalOffset():number {
        return this._verticalOffset;
    };

    scrollPercent():number {
        return ((this._viewportHeight + this._verticalOffset) / this.pageHeight())
    };

    isPageHeightChanged():boolean {
        return this._windowHeightPrevious !== this._windowHeight;
    };

    findPosY(obj):number {
        var curtop = 0;
        if (obj.offsetParent) {
            while (1) {
                curtop += obj.offsetTop;
                if (!obj.offsetParent) {
                    break;
                }
                obj = obj.offsetParent;
            }
        } else if (obj.y) {
            curtop += obj.y;
        }
        return curtop;
    }

}