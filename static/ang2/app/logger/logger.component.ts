import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {LoggerService} from "./logger.service";
import {NgFor} from "angular2/common";


@Component({
    selector: 'my-logger',
    templateUrl:SrcURL+'logger/logger.html',
    styleUrls: [SrcURL + 'logger/logger.css'],
    directives: [],
    providers: [LoggerService],
})

export class LoggerComponent {
    logs:any=[];
    _logs:any=[];

    constructor(private _loggerService:LoggerService) { }


    ngOnInit() {};

    getLogs() {
        this._loggerService.getLog()
            .subscribe
            (logs=> {
                this.addMeta(logs);
                //Array.prototype.push.apply(this.logs, logs);
                this.logs = logs;
            },
            error => console.error('Error to load Log: ' + error));
    };

    stringAsDate(dateStr) {
        return new Date(dateStr);
    };

    filterLog(){
        this.getLogs();
        //this.logs = this._logs.slice().filter((val)=>{
        //    //if (val.type==='info' && info || val.type==='warning' && warning || val.type==='error' && error  ){
        //    if(true){
        //        return true
        //    }
        //})
    }

    addMeta(logs) {
        for (let i = 0; i < logs.length; i++) {
            let curLogs = logs[i];
            curLogs['Meta'] = {
                'doTrunk': true,
                'errorCount': this.countIt('error', curLogs.logs),
                'infoCount': this.countIt('info', curLogs.logs),
                'warningCount': this.countIt('warning', curLogs.logs),
            };
            //for (let i2 = 0; i2 < curLogs.logs.length; i2++){
            //    curLogs.logs[i2]['Meta'] = {
            //    }
            //}
        }
    };

    countIt(string, logs){
        return logs.filter((val)=>{
            if(val.type === string){return true}
        }).length
    }

    //CHANGE tag DATE, unsupported
    parseIt(page, rating, date){
        if (date) {
            let year = date.slice(0, 4);
            let month = date.slice(5, 7);
            let day = date.slice(8, 10);
            date = day + '-' + month + '-' + year;
        }
        console.log('page:',page,'rating:', rating, 'date:', date)
    }

    getTimeDelta(log){
        let len = log.logs.length;
        let firstLogs:any = new Date(log.logs[0].timestamp);
        let lastLogs:any = new Date(log.logs[len-1].timestamp);
        return lastLogs - firstLogs;
    }

}