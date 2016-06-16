export class mockPostChildren {
    _offsetHeight:number;
    _yPosition:number;

    public constructor(public yPosition:number, public offsetHeight:number ) {
        this._offsetHeight = offsetHeight;
        this._yPosition = yPosition;
    }

    getNativeElement() {
        return {
            'offsetHeight': this._offsetHeight,
            'y': this._yPosition,
        };
    }
}

