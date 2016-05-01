System.register(["angular2/core", "../../static", "./logger.service"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, logger_service_1;
    var LoggerComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (logger_service_1_1) {
                logger_service_1 = logger_service_1_1;
            }],
        execute: function() {
            LoggerComponent = (function () {
                function LoggerComponent(_loggerService) {
                    this._loggerService = _loggerService;
                    this.logs = [];
                    this._logs = [];
                }
                LoggerComponent.prototype.ngOnInit = function () { };
                ;
                LoggerComponent.prototype.getLogs = function () {
                    var _this = this;
                    this._loggerService.getLog()
                        .subscribe(function (logs) {
                        _this.addMeta(logs);
                        //Array.prototype.push.apply(this.logs, logs);
                        _this.logs = logs;
                    }, function (error) { return console.error('Error to load Log: ' + error); });
                };
                ;
                LoggerComponent.prototype.stringAsDate = function (dateStr) {
                    return new Date(dateStr);
                };
                ;
                LoggerComponent.prototype.filterLog = function () {
                    this.getLogs();
                    //this.logs = this._logs.slice().filter((val)=>{
                    //    //if (val.type==='info' && info || val.type==='warning' && warning || val.type==='error' && error  ){
                    //    if(true){
                    //        return true
                    //    }
                    //})
                };
                LoggerComponent.prototype.addMeta = function (logs) {
                    for (var i = 0; i < logs.length; i++) {
                        var curLogs = logs[i];
                        curLogs['Meta'] = {
                            'doTrunk': true,
                            'errorCount': this.countIt('error', curLogs.logs),
                            'infoCount': this.countIt('info', curLogs.logs),
                            'warningCount': this.countIt('warning', curLogs.logs),
                        };
                    }
                };
                ;
                LoggerComponent.prototype.countIt = function (string, logs) {
                    return logs.filter(function (val) {
                        if (val.type === string) {
                            return true;
                        }
                    }).length;
                };
                //CHANGE tag DATE, unsupported
                LoggerComponent.prototype.parseIt = function (page, rating, date) {
                    if (date) {
                        var year = date.slice(0, 4);
                        var month = date.slice(5, 7);
                        var day = date.slice(8, 10);
                        date = day + '-' + month + '-' + year;
                    }
                    console.log('page:', page, 'rating:', rating, 'date:', date);
                };
                LoggerComponent.prototype.getTimeDelta = function (log) {
                    var len = log.logs.length;
                    var firstLogs = new Date(log.logs[0].timestamp);
                    var lastLogs = new Date(log.logs[len - 1].timestamp);
                    return lastLogs - firstLogs;
                };
                LoggerComponent = __decorate([
                    core_1.Component({
                        selector: 'my-logger',
                        templateUrl: static_1.SrcURL + 'logger/logger.html',
                        styleUrls: [static_1.SrcURL + 'logger/logger.css'],
                        directives: [],
                        providers: [logger_service_1.LoggerService],
                    }), 
                    __metadata('design:paramtypes', [logger_service_1.LoggerService])
                ], LoggerComponent);
                return LoggerComponent;
            })();
            exports_1("LoggerComponent", LoggerComponent);
        }
    }
});
//# sourceMappingURL=logger.component.js.map