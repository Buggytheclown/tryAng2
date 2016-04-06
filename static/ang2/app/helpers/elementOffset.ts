export class elOffsetY {
    obj:any;

    constructor(obj) {
        this.obj = obj;
        this.findPosY(this.obj);
    }

    findPosY(obj) {
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
