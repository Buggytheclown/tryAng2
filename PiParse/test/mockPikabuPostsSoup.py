from bs4 import BeautifulSoup

from PiParse.scripts.parsePikabu import PikabuSoup


class MockPikabuPostsSoup(PikabuSoup):

    @classmethod
    def getParsePage(cls, parseUrl):
        return BeautifulSoup(cls.mockPikabu, "html5lib")

    mockPikabu = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html><head>
                        <title>Лучшее</title>
                        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
                        <meta content="4810d7a06b7443d3" name="yandex-verification"/>
                        <meta content="" name="keywords"/>
                        <meta content="" name="description"/>
                        <meta content="SAMEORIGIN" http-equiv="X-FRAME-OPTIONS"/>
                        <meta content="100000072189793" property="fb:admins"/>
                        <link href="http://pikabu.ru/best" rel="canonical"/>
                        <meta content="586543721489673" property="fb:app_id"/>

                    <link href="http://cs.pikabu.ru/favicon2x.ico" id="favicon" rel="shortcut icon" type="image/x-icon"/>
                    <link href="http://cs.pikabu.ru/images/icon_ios144.png" rel="apple-touch-icon" sizes="144x144"/>
                    <link href="http://cs.pikabu.ru/images/icon_ios114.png" rel="apple-touch-icon" sizes="114x114"/>

                    <script type="text/javascript">
                        // define initial parameters
                        var initParams = {"siteURL":"http:\/\/pikabu.ru\/","imgURL":"http:\/\/cs.pikabu.ru","userID":0,"userName":"","userKarma":0,"sessionID":"qor7gdi84ge2et2a6cbocqnq7bd6fv1o","userBanTime":"","isUserBanned":FALSE,"isStoryAnimPreview":TRUE,"isCommAnimPreview":TRUE,"isScrollTopBtn":TRUE,"isAjaxLoadMode":TRUE,"isExpandedMode":TRUE,"isCommentsBranchesHidden":FALSE,"scriptName":"index.php","privateKey":"VEZiWTE3","uniqueBufferID":"0a04644e5e","registrationKey":"1f3ad81a6a","debugLocation":"","pickedDate":"2016-06-06","pageNumber":1,"environment":225,"developmentMode":FALSE,"filter_name":"nbest_24"};

                        /**
                         * Create old global vars for back compatibility
                         */
                        var logined = initParams.userID > 0 ? 1 : 0,
                            uCarma = initParams.userKarma,
                            phpSelf = initParams.scriptName,
                            ppk = initParams.privateKey,
                            bid = initParams.uniqueBufferID,
                            site_url = initParams.siteURL,
                            img_url = initParams.imgURL,
                            tag_str = "",
                            developmentMode = initParams.developmentMode,
                            is_twitmode = initParams.isAjaxLoadMode ? 1 : 0,
                            is_scrollmode = initParams.isExpandedMode ? 1 : 0,
                            regKey = initParams.registrationKey,
                            sessID = initParams.sessionID,
                            picker_date = new DATE(initParams.pickedDate),
                            pl = 0,
                            page_num = initParams.pageNumber,
                            dev = initParams.developmentMode,
                            nextJS = {
                                mv: {
                                    facebookWidget: FALSE
                                },
                                adbix: 0,
                                banned: initParams.isUserBanned,
                                bannedTime: initParams.userBanTime,
                                best: "",
                                listDate: "",
                                gif: {
                                    background: TRUE,
                                    showComment: !initParams.isCommAnimPreview,
                                    showStory: !initParams.isStoryAnimPreview
                                },
                                options: {
                                    autoShowGif: initParams.isCommAnimPreview
                                },
                                filterName: initParams.filter_name,
                                user: {
                                    id: initParams.userID,
                                    name: initParams.userName
                                },
                                scrollToTop: initParams.isScrollTopBtn,
                                hideSaveMenu: initParams.isHideSaveMenu,
                                location: initParams.debugLocation
                            };
                    </script>

                <link href="http://cs.pikabu.ru/app/1.0.17/vendors/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
                <link href="http://cs.pikabu.ru/app/1.1.72/main/style.css" rel="stylesheet" type="text/css"/>

                <script charset="utf-8" src="http://cs.pikabu.ru/app/1.0.17/vendors/jquery/js/jquery.min.js" type="text/javascript"></script>
                <script charset="utf-8" data-environment="production" data-version="1.1.72" id="applicationMain" src="http://cs.pikabu.ru/app/1.1.72/main/app.js" type="text/javascript"></script>

                    <script type="text/javascript">
                        $.ajaxSetup({headers: {"X-Csrf-Token" : initParams.sessionID}});
                        $.browser = {safari: FALSE, opera: FALSE};
                    </script>

                        <link href="http://cs.pikabu.ru/css/yadirect/dall.css?5" rel="stylesheet" type="text/css"/>

                    <link href="http://cs.pikabu.ru/css/style2013_1.css?295" rel="stylesheet" type="text/css"/>
                    <link href="http://cs.pikabu.ru/css/style_new.css?56" rel="stylesheet" type="text/css"/>
                    <script src="http://cs.pikabu.ru/js/jquery.form.js" type="text/javascript"></script>
                    <script src="http://cs.pikabu.ru/js/over_js8.js?73" type="text/javascript"></script>

                    <script defer="" src="http://cs.pikabu.ru/js/select.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/icq.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/jquery.impromptu.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/jquery.scrollTo.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/jquery.color.js" type="text/javascript"></script>

                    <script defer="" src="http://cs.pikabu.ru/js/community.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/dig.js?01" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/main28.js?03" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/ajax_login.js?04" type="text/javascript"></script>

                    <script defer="" src="http://cs.pikabu.ru/js/jquery.ui.core.min.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/jquery-ui-1.10.4.custom.min.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/jquery.ui.datepicker.min.js" type="text/javascript"></script>
                    <script defer="" src="http://cs.pikabu.ru/js/datepicker-ru.js" type="text/javascript"></script>

                    </head>
                    <body style="background-color: white;">

                    <div class="ov-capth ov-capth_bg" style="position: fixed;  top: 0;  left: 0;  width: 100%;  height: 100%; min-height: 100%; z-index: 10000;  background: #000000;  filter:progid:DXImageTransform.Microsoft.Alpha(opacity=45);  -moz-opacity: 0.45;  -khtml-opacity: 0.45;  opacity: 0.45;  display: none;"> </div>
                    <div class="ov-capth ov-capth_wrap" style="position: fixed; z-index: 10001; width: 100%;  top: 200px; display: none;">
                        <div class="ov-capth_inner" style="position: relative; margin: 0 auto; width: 300px; background-color: #ffffff; font-family: Tahoma, Arial, sans-serif; font-size: 12px; text-align: center; border-radius: 3px; border: 1px solid #d7d7d7;">
                            <div class="rating_bl" style=" background-color: #efefef; border-radius: 4px 4px 0 0;">
                                Введите код с картинки <img class="ov-capth_reload" src="http://cs.pikabu.ru/images/reload_captcha.png" style="cursor: pointer; margin-top: -1px; vertical-align: middle;"/>
                                <div class="ov-capth_hide_block" style="position: absolute; top: 6px; right: 10px; cursor: pointer;">x</div>
                            </div>
                            <div style="padding: 20px; font-size: 11px;">

                                <div class="ov-capth_img_warp">
                                    <img attr="http://pikabu.ru/kcaptcha/index.php?PHPSESS=qor7gdi84ge2et2a6cbocqnq7bd6fv1o" class="ov-capth_captcha_img" src="http://cs.pikabu.ru/images/loading-spin.svg" style="border-radius: 4px"/>
                                </div>
                                <input class="ov-capth_value" id="ov-capth_rm_captcha" style="border: 1px solid rgb(195, 195, 195); border-radius: 3px; color: rgb(158, 158, 158); font: 14px Tahoma, Arial, sans-serif; height: 24px; padding: 0 5px; transition: all 0.3s ease-out 0s; width: 150px;" type="text" value=""/>

                                <div class="ov-capth_error" style="color: red; display: none;">Неверный код</div>

                                <div style="margin-top: 10px;">
                                    <input class="ov-capth_submit submit_button" style="width: 100px; height: 22px; padding: 0 0 2px;" type="button" value="отправить"/>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="header-cont">

                        <a href="http://pikabu.ru/go/WT0616" target="_blank">
                            <div id="branding_ad_header" onclick="yaCounter174977.reachGoal('branding_click', {position: 'Шапка'}); return true;" style="
                                    background: url('http://pikabu.ru/images/header_bg_white.png') repeat-x 100% 0, url('http://cs8.pikabu.ru/post_img/2016/06/03/10/146497246890911394.jpg') NO-repeat center;
                                    background-color: #fff;
                                    width: 100%;
                                    height: 264px;
                                    margin-bottom: -64px;
                                    display: block !important;
                                    visibility: visible !important;
                                " title="">
                            </div>
                        </a>

                        <div>
                        <TABLE cellpadding="0" cellspacing="0" class="header-table" id="header_t">
                            <tbody><tr>
                            <td class="header-logo">
                                <a class="no_ch" href="http://pikabu.ru">
                                    <span class="b-logo"></span>
                                </a>
                            </td>
                            <td class="header-nav">
                                <TABLE cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col></col>
                                        <col style="width: 222px;"></col>
                                    </colgroup>
                                    <tbody>
                                    <tr>
                                        <td class="header-nav-top" colspan="2">
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="header-nav-bottom">
                                            <ul class="menu">

                        <li class="noactive menu-item-default"><a class="no_ch" href="http://pikabu.ru/hot">Горячее</a></li>

                        <li class="active menu-item-default"><a class="no_ch" href="http://pikabu.ru/best">Лучшее</a></li>

                        <li class="noactive menu-item-default"><a class="no_ch" href="http://pikabu.ru/new">Свежее</a></li>

                        <li class="noactive menu-item-default large"><a class="no_ch" href="http://pikabu.ru/communities">Сообщества</a></li>

                                                </ul>
                                            </td>
                                            <td class="header-nav-right">
                                            </td>
                                        </tr>
                                        </tbody>
                                        </TABLE>
                                    </td>
                                </tr>
                            </tbody></TABLE>
                        </div>
                    </div>

                        <div id="wrap">

                    <TABLE border="0" cellpadding="0" cellspacing="0" style="width: 100%">
                        <tbody><tr>
                            <td class="main-b" style="vertical-align: top; text-align: center">
                                <TABLE cellpadding="0" cellspacing="0" class="inner_wrap">

                        <colgroup><col></col>
                        <col class="inner_wrap_content"></col>
                        </colgroup><tbody><tr>
                            <td> </td>
                            <td style="padding-left: 0px; padding-right: 0px; text-align: left;">

                    <div class="b-feed-panel" data-mode="best">
                        <div class="b-feed-panel__toolbar">

                        <div>
                            <span>За</span>
                            <a data-type="date" data-value="today" href="javascript: void(0);">сегодня</a>
                        </div>

                    <div class="feed-panel-right" id="feed-panel-hidden-counter">
                        <a data-type="mode" data-value="0" href="javascript: void(0);">показывать</a>
                        <span>просмотренные посты</span>
                    </div>

                        </div>
                    </div>

                        <input name="save-cats" type="hidden" value='[{"id":0,"name":"\u041e\u0431\u0449\u0435\u0435","count":0}]'/>

                            <div style="height: 15px"></div>
                            <div class="b-promo-wrapper b-promo-wrapper_type_hide" style="display: none;"></div>

                            <div style="height: 25px"></div>

                        <div class="stories">

                    <!--story_4250062_start-->
                    <div class="story" data-story-id="4250062" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4250062" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    7377
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4250062" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/splachivanie_kollektiva_4250062" target="_blank">Сплачивание коллектива</a>

                            <a class="story__authors" href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250062" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/splachivanie_kollektiva_4250062#comments">336 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/webpauk">webpauk</a>
                    <div class="story__date" title="1465207921">9 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%EA%EE%EB%EB%E5%EA%F2%E8%E2/hot" target="_blank" title='Поиск по тегу "коллектив"'>
                                коллектив
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%F0%EE%E2%E5%F0%EA%E0%20%ED%E0%20%E2%F8%E8%E2%EE%F1%F2%FC/hot" target="_blank" title='Поиск по тегу "проверка на вшивость"'>
                                проверка на вшивость
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250062" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsplachivanie_kollektiva_4250062" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsplachivanie_kollektiva_4250062" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsplachivanie_kollektiva_4250062&amp;text=%D0%A1%D0%BF%D0%BB%D0%B0%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%B0" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>Поведал друг. Далее с его слов.</p><p><br/></p><p>Работаю на алкобазе, торгую элитным бухлом.</p><p>Назначили нового директора, и чтобы познакомиться с коллективом, директор пригласил всех семерых менеджеров на шашлычки за город.</p><p>Приехали каждый своим ходом. Директор организовал место и уже накрыл стол.</p><p><br/></p><p>На столе стоят семь 200-граммовых стаканов.</p><p>- Значтак, парни! в одном стакане водка, во всех остальных вода. пьем. увижу, кто сморщился после водки - зп на 10% ниже.</p><p>Все поднимают стаканы. И по закону подлости именно у меня водка. Выпиваю, чуть не закашлявшись в конце.</p><p>Директор оглядывает всех орлиным взором. Ни одного сморщившегося!</p><p>- Ну, блядь, и коллектив! У всех была налита водка!</p><p><br/></p><p>вечер только начинался...</p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4250062">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250062_end-->

                    <!--story_4249080_start-->
                    <div class="story" data-story-id="4249080" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249080" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    6096
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249080" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/v_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080" target="_blank">В каком подземелье выбивается данный сет?</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249080" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/v_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080#comments">256 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/MaskedShaco">MaskedShaco</a>
                    <div class="story__date" title="1465154594">23 часа назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%EC%EE%E4%E0/hot" target="_blank" title='Поиск по тегу "мода"'>
                                мода
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%CA%E0%F0%F2%E8%ED%EA%E8/hot" target="_blank" title='Поиск по тегу "Картинки"'>
                                Картинки
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/RPG/hot" target="_blank" title='Поиск по тегу "RPG"'>
                                RPG
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%F0%E8%EA%EE%EB/hot" target="_blank" title='Поиск по тегу "прикол"'>
                                прикол
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249080" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fv_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fv_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fv_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080&amp;text=%D0%92+%D0%BA%D0%B0%D0%BA%D0%BE%D0%BC+%D0%BF%D0%BE%D0%B4%D0%B7%D0%B5%D0%BC%D0%B5%D0%BB%D1%8C%D0%B5+%D0%B2%D1%8B%D0%B1%D0%B8%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F+%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9+%D1%81%D0%B5%D1%82%3F" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/v_kakom_podzemele_vyibivaetsya_dannyiy_set_4249080" target="_blank">
                            <img alt="В каком подземелье выбивается данный сет?" data-bigger-available="true" data-large-image="" data-viewable="true" height="604" src="http://cs8.pikabu.ru/post_img/2016/06/05/11/1465154553191312059.jpg" width="568"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249080">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249080_end-->

                    <!--story_4249778_start-->
                    <div class="story" data-story-id="4249778" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249778" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    5128
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249778" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/devochka_i_stroiteli_4249778" target="_blank">Девочка и строители</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249778" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/devochka_i_stroiteli_4249778#comments">125 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Glover">Glover</a>
                    <div class="story__date" title="1465200019">11 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%E5%E2%EE%F7%EA%E0/hot" target="_blank" title='Поиск по тегу "девочка"'>
                                девочка
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%E5%F2%E8/hot" target="_blank" title='Поиск по тегу "дети"'>
                                дети
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%F2%F0%EE%E8%F2%E5%EB%E8/hot" target="_blank" title='Поиск по тегу "строители"'>
                                строители
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F0%E0%E1%EE%F2%E0/hot" target="_blank" title='Поиск по тегу "работа"'>
                                работа
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EE%E1%F9%E5%ED%E8%E5/hot" target="_blank" title='Поиск по тегу "общение"'>
                                общение
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E1%E0%E9%EA%E0/hot" target="_blank" title='Поиск по тегу "байка"'>
                                байка
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%FE%EC%EE%F0/hot" target="_blank" title='Поиск по тегу "юмор"'>
                                юмор
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249778" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fdevochka_i_stroiteli_4249778" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fdevochka_i_stroiteli_4249778" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fdevochka_i_stroiteli_4249778&amp;text=%D0%94%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B0+%D0%B8+%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D0%B8" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>Молодая семья переехала в дом рядом с пустырем. И однажды там появилась бригада строителей, которым предстояло построить на пустом месте новый дом.</p><p><br/></p><p>Конечно же, 5-летней девочке было очень интересно, что там происходит, поэтому она целыми днями наблюдала за рабочими.</p><p><br/></p><p>В конце концов, она подружилась со строителями, и они стали считать ее своеобразным талисманом проекта. Они постоянно болтали с ней, девочка обедала с ними и даже выполняла маленькие поручения, которые ей давали строители, чтобы она почувствовала себя важной.</p><p><br/></p><p>В конце первой недели ей вручили конверт с заработной платой в 10 долларов. Малышка сразу побежала к маме похвастаться, а женщина предложила дочке открыть собственный сберегательный счет в банке и положить туда эти деньги.</p><p><br/></p><p>Кассир в банке был очень впечатлён. Он спросил у девочки, как она смогла заработать деньги в таком юном возрасте.</p><p><br/></p><p>Малышка с гордостью ответила:</p><p><br/></p><p>— На прошлой неделе я работала с настоящими строителями, которые строят дом по соседству с нами.</p><p><br/></p><p>— Ого! – воскликнул кассир. – А на следующей неделе ты тоже будешь там работать?</p><p><br/></p><p>Девочка ответила:</p><p><br/></p><p>— Да, буду, если, конечно, эти придурки со склада стройматериалов наконец-то пришлют этот еб%чий гипсокартон!</p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249778">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249778_end-->

                    <!--story_4249286_start-->
                    <div class="story" data-story-id="4249286" data-story-long="true" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249286" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    4986
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249286" data-story-long="true" data-story-type="gtpost" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank">Триал спорт испортил жизнь одной деревни</a>

                            <a class="story__authors" href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249286" data-story-long="true" data-story-type="gtpost" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286#comments">395 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/xsidorovx">xsidorovx</a>
                    <div class="story__date" title="1465162696">21 час назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%EF%EE%F0%F2/hot" target="_blank" title='Поиск по тегу "спорт"'>
                                спорт
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%EB%EE%F1%E8%EF%E5%E4/hot" target="_blank" title='Поиск по тегу "велосипед"'>
                                велосипед
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%E5%F0%E5%E2%ED%FF/hot" target="_blank" title='Поиск по тегу "деревня"'>
                                деревня
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%CF%F0%E8%F0%EE%E4%E0/hot" target="_blank" title='Поиск по тегу "Природа"'>
                                Природа
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%EB%E8%ED%ED%EE%EF%EE%F1%F2/hot" target="_blank" title='Поиск по тегу "длиннопост"'>
                                длиннопост
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249286" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Ftrial_sport_isportil_zhizn_odnoy_derevni_4249286" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Ftrial_sport_isportil_zhizn_odnoy_derevni_4249286" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Ftrial_sport_isportil_zhizn_odnoy_derevni_4249286&amp;text=%D0%A2%D1%80%D0%B8%D0%B0%D0%BB+%D1%81%D0%BF%D0%BE%D1%80%D1%82+%D0%B8%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D0%BB+%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C+%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9+%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D0%B8" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story-blocks b-story-blocks_with-border" data-expanded="true">
                        <div class="b-story-blocks__wrapper b-story-blocks__wrapper_slice_yes" style="">

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Дорогие пикабушники! </p><p>Хочу направить свой гнев на соревнования bike-OFF-road, которые прошли в эти выходные в деревне Горки, Волоколамского района.</p><p>Внеазапно, приехав после работы на дачу с женой мы обнаружили толпы машин по дороге к нашей деревне. У нас в деревне 5 домов и такого скопления машин не было никогда.</p><p>До деревни идет дорога по полю, чиним мы ее на свои деньги и на деле это вытоптанная тропа. Стоит ли говорить, что после проезд сотни машин от нее остался фиг ? </p><p>А ровняли и посыпали гравием ее мы на свои деньги.</p><p>Итак, после всех страданий, мы добрались до своего дома (два раза застряв и получил поддержку только от случайно проезжавшего соседа) обнаружили под забором своего дома машины и палатки. Все фото уже с утра, т.к. приехали мы поздно ночью. </p><p>Полночи я пробегал в поисках организаторов. Нашел и узнал, что это соревнование, оно согласовано. Об этом мне сказал подпитый организатор Андрей. Оставшуюся часть ночи я слушал песни, наблюдал фонарики в окно и получал массу удовольствия от пятничной ночи.</p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/0/1465162242177173772.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162242177173772.jpg" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Половину субботнего утра я с супругой ездил по администрациям и пытался найти, кто же согласовал это мероприятие ? Выяснилось, что это управа района. Мероприятие согласовано на 100 человек. По факту на месте было 1500 человек! Никаких правил парковки, которая кстати была размечена. Фото прилагаю. Никакой парковки в деревне, как видите нет, но по факту, смотрим фото.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-blocks__hide-wrapper" style="display: none;">

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="849" data-large-image="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162093112570446.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162093112570446.jpg" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/06/0/146516215411426566.jpg" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/0/146516215411426566.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/0/1465162168130640415.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162168130640415.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/06/0/1465162291183681145.jpg" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/0/1465162291183681145.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Хочу отметить, что участие в этом мероприятии строило 1500 р. с человека! За эти деньги смогли нанять и мусорный контейнер, но он не помог.</p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/0/1465162368114941917.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162368114941917.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/06/0/1465162430136642950.jpg" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/0/1465162430136642950.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Жгли костры без мангалов и поломали елки, разворотили все дороги. Спонсором всего этого безумия выступил магазин Триал Спорт. </p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/0/1465162488166225987.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162488166225987.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/06/0/1465162522118336987.jpg" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/0/1465162522118336987.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286" target="_blank"><img alt="Триал спорт испортил жизнь одной деревни спорт, велосипед, деревня, Природа, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/0/1465162642114755012.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/06/0/1465162642114755012.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>В итоге, одни отдыхали, а другим убирать мусор, чинить дорогу, сажать деревья и вспоминать, как здорово к нам в деревню заглянули спортсмены ! </p><p></p>
                                </div>
                            </div>

                        </div>

                    </div>

                        <a class="b-story__show-all" href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286">
                            <span>Показать полностью</span>
                            9 <i class="b-story__show-all-images"></i>

                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249286">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249286_end-->

                    <!--story_4249520_start-->
                    <div class="story" data-story-id="4249520" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249520" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    4077
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249520" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/labrazavrus_4249520" target="_blank">Лабразаврус</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249520" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/labrazavrus_4249520#comments">43 Комментария</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Rokotgrei">Rokotgrei</a>
                    <div class="story__date" title="1465189515">14 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%D1%EE%E1%E0%EA%E0/hot" target="_blank" title='Поиск по тегу "Собака"'>
                                Собака
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EB%E0%E1%F0%E0%E4%EE%F0/hot" target="_blank" title='Поиск по тегу "лабрадор"'>
                                лабрадор
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%EE%EA%E0%E7%E0%EB%EE%F1%FC/hot" target="_blank" title='Поиск по тегу "показалось"'>
                                показалось
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249520" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Flabrazavrus_4249520" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Flabrazavrus_4249520" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Flabrazavrus_4249520&amp;text=%D0%9B%D0%B0%D0%B1%D1%80%D0%B0%D0%B7%D0%B0%D0%B2%D1%80%D1%83%D1%81" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/labrazavrus_4249520" target="_blank">
                            <img alt="Лабразаврус" data-bigger-available="true" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/06/4/1465189479187270794.jpg" data-viewable="true" height="696" src="http://cs4.pikabu.ru/post_img/2016/06/06/4/1465189479187270794.jpg" width="600"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249520">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249520_end-->

                    <!--story_4249485_start-->
                    <div class="story" data-story-id="4249485" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249485" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    4004
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249485" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/derzhites_podalshe_ot_vyisokoy_quottravyiquot_4249485" target="_blank">Держитесь подальше от высокой "травы"</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249485" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/derzhites_podalshe_ot_vyisokoy_quottravyiquot_4249485#comments">137 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Deathman">Deathman</a>
                    <div class="story__date" title="1465187345">14 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E7%E0%F1%E0%E4%E0/hot" target="_blank" title='Поиск по тегу "засада"'>
                                засада
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%EE%EB%E5/hot" target="_blank" title='Поиск по тегу "поле"'>
                                поле
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E3%E8%F4%EA%E0/hot" target="_blank" title='Поиск по тегу "гифка"'>
                                гифка
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249485" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fderzhites_podalshe_ot_vyisokoy_quottravyiquot_4249485" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fderzhites_podalshe_ot_vyisokoy_quottravyiquot_4249485" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fderzhites_podalshe_ot_vyisokoy_quottravyiquot_4249485&amp;text=%D0%94%D0%B5%D1%80%D0%B6%D0%B8%D1%82%D0%B5%D1%81%D1%8C+%D0%BF%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D1%88%D0%B5+%D0%BE%D1%82+%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D0%B9+%26quot%3B%D1%82%D1%80%D0%B0%D0%B2%D1%8B%26quot%3B" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <div class="b-gifx" data-height="508" data-type="story" data-width="276" style="width: 276px">
                            <div class="b-gifx__state b-gifx__state_loading_yes"><i class="fa fa-circle-o-notch fa-spin"></i></div>
                            <div class="b-gifx__state b-gifx__state_waiting_yes" style="visibility: hidden;"><span class="b-gifx__size">10 Мб</span></div>
                            <a class="b-gifx__state b-gifx__state_playing_yes b-gifx__save" href="http://cs4.pikabu.ru/post_img/2016/06/06/4/1465187296122694469.gif" style="visibility: hidden;" target="_blank"><i class="fa fa-download"></i></a>
                            <div class="b-gifx__preview b-gifx__preview_show_yes">
                                <img alt="Держитесь подальше от высокой &amp;quot;травы&amp;quot;" class="b-gifx__image" src="http://cs4.pikabu.ru/post_img/2016/06/06/4/1465187296122694469.jpg"/>
                                <div class="b-gifx__logo i-sprite--gifx__gifx"></div>
                                <div class="b-gifx__play i-sprite--gifx__play"></div>
                            </div>
                            <div class="b-gifx__player" data-size-gif="9793" data-size-mp4="1467" data-size-webm="2254" data-size-webp="1257" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/4/1465187296122694469.gif"></div>
                        </div>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249485">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249485_end-->

                    <!--story_4249504_start-->
                    <div class="story" data-story-id="4249504" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249504" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3886
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249504" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/ne_plyuy_v_kolodets_4249504" target="_blank">Не плюй в колодец...</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249504" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/ne_plyuy_v_kolodets_4249504#comments">576 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/squeezed">squeezed</a>
                    <div class="story__date" title="1465188706">14 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%E5%EC%FC%FF/hot" target="_blank" title='Поиск по тегу "семья"'>
                                семья
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EC%F3%E6/hot" target="_blank" title='Поиск по тегу "муж"'>
                                муж
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%E2%E5%EA%F0%EE%E2%FC/hot" target="_blank" title='Поиск по тегу "свекровь"'>
                                свекровь
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%E2%E8%ED%F1%F2%E2%EE/hot" target="_blank" title='Поиск по тегу "свинство"'>
                                свинство
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/bash%20im/hot" target="_blank" title='Поиск по тегу "bash im"'>
                                bash im
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%ED%E5%20%EC%EE%E5/hot" target="_blank" title='Поиск по тегу "не мое"'>
                                не мое
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249504" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fne_plyuy_v_kolodets_4249504" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fne_plyuy_v_kolodets_4249504" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fne_plyuy_v_kolodets_4249504&amp;text=%D0%9D%D0%B5+%D0%BF%D0%BB%D1%8E%D0%B9+%D0%B2+%D0%BA%D0%BE%D0%BB%D0%BE%D0%B4%D0%B5%D1%86..." rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>Не мое, взято с баша.</p><p><br/></p><p>Был у нас случай на работе</p><p>У женщины-коллеги сын открыл свой бизнес платил работникам мало, текучка была большая</p><p>С теток сразу же брал заявление об уходе с открытой датой, на случай ухода в декрет, т.е. мог уволить сразу же как только живот становился заметен.</p><p>Его мать попыталась объяснить, что так поступать "в общем-то не по-людски", сын ее попытки живенько пресек, прочитал курс экономики, сказал, что ему пофиг на чужих детей и он их кормить не намерен, если тетка выбрала ребенка то пусть ищет другую работу. и еще попросил не лезть туда, где бабий ум неспособен ничего понять.</p><p><br/></p><p>Мать была женщиной мудрой, более вмешиваться в эти дела не стала.</p><p>Через несколько лет сын женился, сноха забеременела, родила внука.</p><p>Сын со снохой решили дитятко подкинуть бабушке (вроде как пенсионерка уже), чтобы сноха вышла на работу побыстрее.</p><p>На что бабушка сказала, что услуги няни стоят недешево и озвучила сумму.</p><p>Когда ее попытались пристыдить, как так брать денюжку со своего сына и внука, она сказала, что не хрен ее воспитывать, у ребенка есть мать и пусть выбирает "или ребенок или работа".<br/></p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249504">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249504_end-->

                    <!--story_4250018_start-->
                    <div class="story" data-story-id="4250018" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4250018" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3650
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4250018" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/loft_4250018" target="_blank">Лофт!!!</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250018" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/loft_4250018#comments">110 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Bleras">Bleras</a>
                    <div class="story__date" title="1465206666">9 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E8%F1%EA%F3%F1%F1%F2%E2%EE/hot" target="_blank" title='Поиск по тегу "искусство"'>
                                искусство
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/twitter/hot" target="_blank" title='Поиск по тегу "twitter"'>
                                twitter
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%D1%EC%E5%F5/hot" target="_blank" title='Поиск по тегу "Смех"'>
                                Смех
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250018" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Floft_4250018" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Floft_4250018" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Floft_4250018&amp;text=%D0%9B%D0%BE%D1%84%D1%82%21%21%21" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/loft_4250018" target="_blank">
                            <img alt="Лофт!!!" data-bigger-available="true" data-large-image="" data-viewable="true" height="252" src="http://cs4.pikabu.ru/post_img/2016/06/06/6/14652066201100125342.jpg" width="480"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4250018">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250018_end-->

                    <!--story_4250072_start-->
                    <div class="story" data-story-id="4250072" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4250072" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3504
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4250072" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/kto_tam_4250072" target="_blank">Кто там?</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250072" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/kto_tam_4250072#comments">44 Комментария</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/ASer0806">ASer0806</a>
                    <div class="story__date" title="1465208159">8 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E0%ED%E5%EA%E4%EE%F2/hot" target="_blank" title='Поиск по тегу "анекдот"'>
                                анекдот
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%FE%EC%EE%F0/hot" target="_blank" title='Поиск по тегу "юмор"'>
                                юмор
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%F0%E8%EA%EE%EB/hot" target="_blank" title='Поиск по тегу "прикол"'>
                                прикол
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EB%E5%F4%EE%ED%ED%E0%FF%20%E1%F3%E4%EA%E0/hot" target="_blank" title='Поиск по тегу "телефонная будка"'>
                                телефонная будка
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250072" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkto_tam_4250072" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkto_tam_4250072" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkto_tam_4250072&amp;text=%D0%9A%D1%82%D0%BE+%D1%82%D0%B0%D0%BC%3F" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>- Тук, тук.</p><p>- Кто там?</p><p>- Полиция, откройте.</p><p>- Вы должны подождать, я ... какаю.</p><p>- Мы это видим, телефонная будка стеклянная. </p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4250072">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250072_end-->

                    <!--story_4249227_start-->
                    <div class="story" data-story-id="4249227" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249227" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3483
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249227" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/verno_zamecheno_4249227" target="_blank">Верно замечено</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249227" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/verno_zamecheno_4249227#comments">225 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/SeverCo">SeverCo</a>
                    <div class="story__date" title="1465160577">22 часа назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%E5%ED%FC%E3%E8/hot" target="_blank" title='Поиск по тегу "деньги"'>
                                деньги
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E8%E3%F0%FB/hot" target="_blank" title='Поиск по тегу "игры"'>
                                игры
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F0%E0%F1%F1%F3%E4%E8%F2%E5%EB%FC%ED%EE%F1%F2%FC/hot" target="_blank" title='Поиск по тегу "рассудительность"'>
                                рассудительность
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249227" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fverno_zamecheno_4249227" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fverno_zamecheno_4249227" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fverno_zamecheno_4249227&amp;text=%D0%92%D0%B5%D1%80%D0%BD%D0%BE+%D0%B7%D0%B0%D0%BC%D0%B5%D1%87%D0%B5%D0%BD%D0%BE" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>"Я более рассудительно трачу деньги в компьютерных играх, чем в реальной жизни"</p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249227">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249227_end-->

                    <!--story_4249110_start-->
                    <div class="story" data-story-id="4249110" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249110" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3413
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249110" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/vedmaki_byivayut_raznyie_4249110" target="_blank">Ведьмаки бывают разные...</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249110" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/vedmaki_byivayut_raznyie_4249110#comments">117 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/CarzyEj">CarzyEj</a>
                    <div class="story__date" title="1465155594">23 часа назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E0%F0%F2/hot" target="_blank" title='Поиск по тегу "арт"'>
                                арт
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C2%E5%E4%FC%EC%E0%EA/hot" target="_blank" title='Поиск по тегу "Ведьмак"'>
                                Ведьмак
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/Whitcher/hot" target="_blank" title='Поиск по тегу "Whitcher"'>
                                Whitcher
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%E4%FC%EC%E0%EA%203/hot" target="_blank" title='Поиск по тегу "ведьмак 3"'>
                                ведьмак 3
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C8%E3%F0%FB/hot" target="_blank" title='Поиск по тегу "Игры"'>
                                Игры
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%FF%EA%F3%E1%EE%E2%E8%F7/hot" target="_blank" title='Поиск по тегу "якубович"'>
                                якубович
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C3%E5%F0%E0%EB%FC%F2%20%E8%E7%20%D0%E8%E2%E8%E8/hot" target="_blank" title='Поиск по тегу "Геральт из Ривии"'>
                                Геральт из Ривии
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249110" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvedmaki_byivayut_raznyie_4249110" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvedmaki_byivayut_raznyie_4249110" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvedmaki_byivayut_raznyie_4249110&amp;text=%D0%92%D0%B5%D0%B4%D1%8C%D0%BC%D0%B0%D0%BA%D0%B8+%D0%B1%D1%8B%D0%B2%D0%B0%D1%8E%D1%82+%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B5..." rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/vedmaki_byivayut_raznyie_4249110" target="_blank">
                            <img alt="Ведьмаки бывают разные..." data-bigger-available="true" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/05/11/1465155374118497379.jpg" data-viewable="true" height="387" src="http://cs8.pikabu.ru/post_img/2016/06/05/11/1465155374118497379.jpg" width="600"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249110">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249110_end-->

                    <!--story_4249669_start-->
                    <div class="story" data-story-id="4249669" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249669" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3395
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249669" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/shpora_4249669" target="_blank">Шпора</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249669" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/shpora_4249669#comments">50 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/GrayFr">GrayFr</a>
                    <div class="story__date" title="1465196371">12 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%FD%EA%E7%E0%EC%E5%ED/hot" target="_blank" title='Поиск по тегу "экзамен"'>
                                экзамен
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F8%EF%E0%F0%E3%E0%EB%EA%E0/hot" target="_blank" title='Поиск по тегу "шпаргалка"'>
                                шпаргалка
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E5%E3%FD/hot" target="_blank" title='Поиск по тегу "егэ"'>
                                егэ
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249669" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fshpora_4249669" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fshpora_4249669" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fshpora_4249669&amp;text=%D0%A8%D0%BF%D0%BE%D1%80%D0%B0" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/shpora_4249669" target="_blank">
                            <img alt="Шпора" data-bigger-available="true" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/5/1465196327127186644.jpg" data-viewable="true" height="567" src="http://cs8.pikabu.ru/post_img/2016/06/06/5/1465196327127186644.jpg" width="600"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249669">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249669_end-->

                    <!--story_4250466_start-->
                    <div class="story" data-story-id="4250466" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4250466" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3286
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4250466" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/i_botanik_4250466" target="_blank">..И ботаник</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250466" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/i_botanik_4250466#comments">52 Комментария</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/m0rfus">m0rfus</a>
                    <div class="story__date" title="1465212841">7 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%F0%E8%F9/hot" target="_blank" title='Поиск по тегу "дрищ"'>
                                дрищ
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C1%EE%F2%E0%ED/hot" target="_blank" title='Поиск по тегу "Ботан"'>
                                Ботан
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E7%ED%E0%EA%EE%EC%F1%F2%E2%E0%20%E2%20%F1%E5%F2%E8/hot" target="_blank" title='Поиск по тегу "знакомства в сети"'>
                                знакомства в сети
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/forever%20alone/hot" target="_blank" title='Поиск по тегу "forever alone"'>
                                forever alone
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EC%EE%E6%E5%F2%20%E1%FB%F2%FC%20%E1%E0%FF%ED/hot" target="_blank" title='Поиск по тегу "может быть баян"'>
                                может быть баян
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%E5%F0%E5%EF%E8%F1%EA%E0/hot" target="_blank" title='Поиск по тегу "переписка"'>
                                переписка
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250466" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fi_botanik_4250466" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fi_botanik_4250466" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fi_botanik_4250466&amp;text=..%D0%98+%D0%B1%D0%BE%D1%82%D0%B0%D0%BD%D0%B8%D0%BA" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/i_botanik_4250466" target="_blank">
                            <img alt="..И ботаник" data-bigger-available="true" data-large-image="" data-viewable="true" height="480" src="http://cs4.pikabu.ru/post_img/2016/06/06/7/1465212553146966322.jpg" width="480"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4250466">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250466_end-->

                    <!--story_4249385_start-->
                    <div class="story" data-story-id="4249385" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249385" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3259
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249385" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/kogda_3dmodeller_delaet_yeskiz_4249385" target="_blank">Когда 3D-моделлер делает эскиз</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249385" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/kogda_3dmodeller_delaet_yeskiz_4249385#comments">66 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Frontender">Frontender</a>
                    <div class="story__date" title="1465171632">19 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%F0%E8%F1%F3%ED%EE%EA/hot" target="_blank" title='Поиск по тегу "рисунок"'>
                                рисунок
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/3D%20%F0%E8%F1%F3%ED%EE%EA/hot" target="_blank" title='Поиск по тегу "3D рисунок"'>
                                3D рисунок
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E3%E8%F4%EA%E0/hot" target="_blank" title='Поиск по тегу "гифка"'>
                                гифка
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249385" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkogda_3dmodeller_delaet_yeskiz_4249385" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkogda_3dmodeller_delaet_yeskiz_4249385" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkogda_3dmodeller_delaet_yeskiz_4249385&amp;text=%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0+3D-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%BB%D0%B5%D1%80+%D0%B4%D0%B5%D0%BB%D0%B0%D0%B5%D1%82+%D1%8D%D1%81%D0%BA%D0%B8%D0%B7" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <div class="b-gifx" data-height="250" data-type="story" data-width="250" style="width: 250px">
                            <div class="b-gifx__state b-gifx__state_loading_yes"><i class="fa fa-circle-o-notch fa-spin"></i></div>
                            <div class="b-gifx__state b-gifx__state_waiting_yes" style="visibility: hidden;"><span class="b-gifx__size">10 Мб</span></div>
                            <a class="b-gifx__state b-gifx__state_playing_yes b-gifx__save" href="http://cs4.pikabu.ru/post_img/2016/06/06/2/1465171589160220238.gif" style="visibility: hidden;" target="_blank"><i class="fa fa-download"></i></a>
                            <div class="b-gifx__preview b-gifx__preview_show_yes">
                                <img alt="Когда 3D-моделлер делает эскиз" class="b-gifx__image" src="http://cs4.pikabu.ru/post_img/2016/06/06/2/1465171589160220238.jpg"/>
                                <div class="b-gifx__logo i-sprite--gifx__gifx"></div>
                                <div class="b-gifx__play i-sprite--gifx__play"></div>
                            </div>
                            <div class="b-gifx__player" data-size-gif="10443" data-size-mp4="1255" data-size-webm="2139" data-size-webp="5325" data-src="http://cs4.pikabu.ru/post_img/2016/06/06/2/1465171589160220238.gif"></div>
                        </div>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249385">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249385_end-->

                    <!--story_4249567_start-->
                    <div class="story" data-story-id="4249567" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249567" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3221
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249567" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/voyna_sosedey_4249567" target="_blank">Война соседей</a>

                            <a class="story__authors" href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249567" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/voyna_sosedey_4249567#comments">155 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Whisky1">Whisky1</a>
                    <div class="story__date" title="1465192092">13 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%F1%EE%F1%E5%E4%E8/hot" target="_blank" title='Поиск по тегу "соседи"'>
                                соседи
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E3%E0%E2%ED%EE%20%F1%EE%E1%E0%F7%FC%E5/hot" target="_blank" title='Поиск по тегу "гавно собачье"'>
                                гавно собачье
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C6%E8%E2%EE%F2%ED%FB%E5/hot" target="_blank" title='Поиск по тегу "Животные"'>
                                Животные
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249567" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvoyna_sosedey_4249567" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvoyna_sosedey_4249567" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvoyna_sosedey_4249567&amp;text=%D0%92%D0%BE%D0%B9%D0%BD%D0%B0+%D1%81%D0%BE%D1%81%D0%B5%D0%B4%D0%B5%D0%B9" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/voyna_sosedey_4249567" target="_blank">
                            <img alt="Война соседей" data-bigger-available="true" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/4/1465191965156286941.jpg" data-viewable="true" height="800" src="http://cs8.pikabu.ru/post_img/2016/06/06/4/1465191965156286941.jpg" width="600"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249567">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249567_end-->

                    <!--story_4249248_start-->
                    <div class="story" data-story-id="4249248" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249248" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3081
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249248" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/vsego_tretiy_raz_edu_4249248" target="_blank">Всего третий раз еду</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249248" data-story-long="false" data-story-type="text" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__text-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/vsego_tretiy_raz_edu_4249248#comments">104 Комментария</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/TaPaD">TaPaD</a>
                    <div class="story__date" title="1465161203">22 часа назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%CF%EE%EF%F0%EE%F8%E0%E9%EA%E8/hot" target="_blank" title='Поиск по тегу "Попрошайки"'>
                                Попрошайки
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%EE%EA%E7%E0%EB/hot" target="_blank" title='Поиск по тегу "вокзал"'>
                                вокзал
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%CC%E8%ED%F1%EA/hot" target="_blank" title='Поиск по тегу "Минск"'>
                                Минск
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F2%E5%EA%F1%F2/hot" target="_blank" title='Поиск по тегу "текст"'>
                                текст
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249248" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvsego_tretiy_raz_edu_4249248" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvsego_tretiy_raz_edu_4249248" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fvsego_tretiy_raz_edu_4249248&amp;text=%D0%92%D1%81%D0%B5%D0%B3%D0%BE+%D1%82%D1%80%D0%B5%D1%82%D0%B8%D0%B9+%D1%80%D0%B0%D0%B7+%D0%B5%D0%B4%D1%83" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_text" data-expanded="1">
                <p>Вот как раз сегодня был случай (Минск). Иду по подземному переходу на вокзале в наушниках. Боковым зрением вижу стремительно приближающуюся ко мне фигуру, которая приблизившись ко мне дотрагивается до моей руки. Я вынул наушник из уха решив послушать ее вопрос</p><p>ПОПРОШАЙКА: Извините, у Вас случайно не будет 26000 р..... (примерно 1,5$)</p><p>Я: На билет до Могилева?</p><p>Поскольку я живу в пригороде, а работаю в городе, попрошайки ко мне подходят почти каждый день, и эта женщина уже подходила однажды (внешность обычная, не бомжеватая).</p><p>П: Да (удивленно)</p><p>Я: (продолжая свой путь) Когда же вы наконец-то уедете? </p><p>П:(в след обиженно) я всего третий раз еду!!!!</p>
                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249248">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249248_end-->

                    <!--story_4250719_start-->
                    <div class="story" data-story-id="4250719" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4250719" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3087
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4250719" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/myi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719" target="_blank">Мы купили дочери игрушечное яйцо с пингвином, который вылупляется и растёт в воде</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250719" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/myi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719#comments">339 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Frontender">Frontender</a>
                    <div class="story__date" title="1465216606">6 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%E8%ED%E3%E2%E8%ED%FB/hot" target="_blank" title='Поиск по тегу "пингвины"'>
                                пингвины
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%EE%E4%E0/hot" target="_blank" title='Поиск по тегу "вода"'>
                                вода
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E8%E3%F0%F3%F8%EA%E8/hot" target="_blank" title='Поиск по тегу "игрушки"'>
                                игрушки
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%E8%EB%E4%EE/hot" target="_blank" title='Поиск по тегу "дилдо"'>
                                дилдо
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250719" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmyi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmyi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmyi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719&amp;text=%D0%9C%D1%8B+%D0%BA%D1%83%D0%BF%D0%B8%D0%BB%D0%B8+%D0%B4%D0%BE%D1%87%D0%B5%D1%80%D0%B8+%D0%B8%D0%B3%D1%80%D1%83%D1%88%D0%B5%D1%87%D0%BD%D0%BE%D0%B5+%D1%8F%D0%B9%D1%86%D0%BE+%D1%81+%D0%BF%D0%B8%D0%BD%D0%B3%D0%B2%D0%B8%D0%BD%D0%BE%D0%BC%2C+%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9+%D0%B2%D1%8B%D0%BB%D1%83%D0%BF%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F+%D0%B8+%D1%80%D0%B0%D1%81%D1%82%D1%91%D1%82+%D0%B2+%D0%B2%D0%BE%D0%B4%D0%B5" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story-blocks b-story-blocks_with-border" data-expanded="true">
                        <div class="b-story-blocks__wrapper" style="">

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/myi_kupili_docheri_igrushechnoe_yaytso_s_pingvinom_kotoryiy_vyiluplyaetsya_i_rastyot_v_vode_4250719" target="_blank"><img alt="Мы купили дочери игрушечное яйцо с пингвином, который вылупляется и растёт в воде пингвины, вода, игрушки, дилдо" data-height="763" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/8/1465216389147346501.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/06/8/1465216389147346501.jpg" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Выглядит как живой</p><p></p>
                                </div>
                            </div>

                    </div>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4250719">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250719_end-->

                    <!--story_4249639_start-->
                    <div class="story" data-story-id="4249639" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249639" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    3011
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249639" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/muzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639" target="_blank">Мужик пришел устраиваться на работу с такими документами...</a>

                            <a class="story__authors" href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249639" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/muzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639#comments">298 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Junkeee">Junkeee</a>
                    <div class="story__date" title="1465194957">12 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%C4%EE%EA%F3%EC%E5%ED%F2%FB/hot" target="_blank" title='Поиск по тегу "Документы"'>
                                Документы
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%EF%E0%F1%EF%EE%F0%F2/hot" target="_blank" title='Поиск по тегу "паспорт"'>
                                паспорт
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%EE%E4%E8%F2%E5%EB%FC%F1%EA%E8%E5%20%EF%F0%E0%E2%E0/hot" target="_blank" title='Поиск по тегу "водительские права"'>
                                водительские права
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%FD%EC%EC/hot" target="_blank" title='Поиск по тегу "эмм"'>
                                эмм
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/wtf/hot" target="_blank" title='Поиск по тегу "wtf"'>
                                wtf
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%F0%F2%EE%EB%E5%F2-%F1%E0%EC%EE%EB%E5%F2/hot" target="_blank" title='Поиск по тегу "вертолет-самолет"'>
                                вертолет-самолет
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249639" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmuzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmuzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fmuzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639&amp;text=%D0%9C%D1%83%D0%B6%D0%B8%D0%BA+%D0%BF%D1%80%D0%B8%D1%88%D0%B5%D0%BB+%D1%83%D1%81%D1%82%D1%80%D0%B0%D0%B8%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F+%D0%BD%D0%B0+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83+%D1%81+%D1%82%D0%B0%D0%BA%D0%B8%D0%BC%D0%B8+%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8..." rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story-blocks b-story-blocks_with-border" data-expanded="true">
                        <div class="b-story-blocks__wrapper b-story-blocks__wrapper_slice_yes" style="max-height: 750px;">

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/muzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639" target="_blank"><img alt="Мужик пришел устраиваться на работу с такими документами... Документы, паспорт, водительские права, эмм, wtf, вертолет-самолет" data-height="449" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/5/1465194767152366734.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/06/5/1465194767152366734.jpg" style=""/></a>

                                    </div>
                                </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/muzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639" target="_blank"><img alt="Мужик пришел устраиваться на работу с такими документами... Документы, паспорт, водительские права, эмм, wtf, вертолет-самолет" data-height="449" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/06/5/1465194771197110090.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/06/5/1465194771197110090.jpg" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Принимать? =)</p><p></p>
                                </div>
                            </div>

                    </div>

                        <a class="b-story__show-all" href="http://pikabu.ru/story/muzhik_prishel_ustraivatsya_na_rabotu_s_takimi_dokumentami_4249639">
                            <span>Показать полностью</span>
                            1 <i class="b-story__show-all-images"></i>

                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249639">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249639_end-->

                    <!--story_4249741_start-->
                    <div class="story" data-story-id="4249741" data-story-long="true" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249741" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    2869
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249741" data-story-long="true" data-story-type="gtpost" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741" target="_blank">Как я три дня был веганом</a>

                            <a class="story__authors" href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249741" data-story-long="true" data-story-type="gtpost" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741#comments">486 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/qstyler">qstyler</a>
                    <div class="story__date" title="1465198418">11 часов назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%E5%E4%E0/hot" target="_blank" title='Поиск по тегу "еда"'>
                                еда
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C4%E8%E5%F2%E0/hot" target="_blank" title='Поиск по тегу "Диета"'>
                                Диета
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%E3%E0%ED%FB/hot" target="_blank" title='Поиск по тегу "веганы"'>
                                веганы
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%E3%E5%F2%E0%F0%E8%E0%ED%F6%FB/hot" target="_blank" title='Поиск по тегу "вегетарианцы"'>
                                вегетарианцы
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E2%E5%E3%E5%F2%E0%F0%E8%ED%F1%F2%E2%EE/hot" target="_blank" title='Поиск по тегу "вегетаринство"'>
                                вегетаринство
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%F4%E0%EB%E0%F4%E5%EB%FC/hot" target="_blank" title='Поиск по тегу "фалафель"'>
                                фалафель
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%D2%EE%F4%F3/hot" target="_blank" title='Поиск по тегу "Тофу"'>
                                Тофу
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E7%E0%F7%E5%EC%20%F2%E0%EA%20%E6%E8%F2%FC/hot" target="_blank" title='Поиск по тегу "зачем так жить"'>
                                зачем так жить
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%EB%E8%ED%ED%EE%EF%EE%F1%F2/hot" target="_blank" title='Поиск по тегу "длиннопост"'>
                                длиннопост
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249741" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkak_ya_tri_dnya_byil_veganom_4249741" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkak_ya_tri_dnya_byil_veganom_4249741" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fkak_ya_tri_dnya_byil_veganom_4249741&amp;text=%D0%9A%D0%B0%D0%BA+%D1%8F+%D1%82%D1%80%D0%B8+%D0%B4%D0%BD%D1%8F+%D0%B1%D1%8B%D0%BB+%D0%B2%D0%B5%D0%B3%D0%B0%D0%BD%D0%BE%D0%BC" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story-blocks b-story-blocks_with-border" data-expanded="true">
                        <div class="b-story-blocks__wrapper b-story-blocks__wrapper_slice_yes" style="">

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Я всю свою жизнь жру мясо. Я его, мясо, очень люблю. Никогда не мог без него. Но вот как-то <b>исключительно в качестве эксперимента</b> попробовал я питаться так, как питаются веганы. Интересно стало, что в головах у таких людей происходит. Как они себя чувствуют. Почему некоторые так рьяно защищают свою диету и способствуют привлечению новых адептов.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Для полноты эксперимента я решил полностью отказаться от животных белков. Т. е. никакого сыра, молока яиц и т. п.</p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741" target="_blank"><img alt="Как я три дня был веганом еда, Диета, веганы, вегетарианцы, вегетаринство, фалафель, Тофу, зачем так жить, длиннопост" data-height="473" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/05/8/1465133827130259014.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/05/8/1465133827130259014.jpg" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Я пошёл в магазин и накупил себе кучу веганского говна. В основном фалафель и вега-котлетки. Надо сказать, что веганская еда выходит дороже раза в полтора – два, чем нормальная. Но чего не сделаешь ради науки. Дело было в четверг. </p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>На ужин я приготовил себе 250 грамм обычного фалафеля и обычный зелёный салат (огурцы, помидоры, зелёный лучок). Обычно такого объёма еды мне хватает, чтобы наесться от пуза и, немножко переварив еду, приступить к вечерним делам: учёбе и работе. Но не тут-то было. Когда я дожрал всё своё веганское хрючево, я по-прежнему был голоден.</p><p>Это был странный голод: есть я больше не мог, т. к. живот был полон, но организм требовал ещё еды. Но я решил продолжить эксперимент и в таком состоянии лёг спать.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-blocks__hide-wrapper" style="display: none;">

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p><i>Фалафель кстати охуенно вкусный. Я его буду иногда кушать. С мясом конечно.</i></p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741" target="_blank"><img alt="Как я три дня был веганом еда, Диета, веганы, вегетарианцы, вегетаринство, фалафель, Тофу, зачем так жить, длиннопост" data-height="450" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/05/8/1465134200110114482.jpg" data-viewable="true" src="http://cs4.pikabu.ru/post_img/2016/06/05/8/1465134200110114482.jpg" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Проснулся я голодным. На завтрак были фрукты. Почти 300 граммов фруктов. Немного углеводов сбили голод и я смог как-то допедалить до работы. Надо сказать, что это мой обычный завтрак, и мне этого обычно хватает для того, чтобы бодрячком (я программист) доработать до ланча.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Работа — это отдельная опера. Нормально работать у меня не получалось. Во-первых, все мысли были <b>только о еде</b>. Я дико хотел жрать и таскал из офисного холодильника помидорки, но они не спасали. Поэтому я постоянно пил воду, чтобы в желудке хоть чего-нибудь было. </p><p><br/></p><p>Но это только полбеды. Большой проблемой было то, что на меня напал дикий пердёж. Я постоянно бегал в сортир пробздеться: боялся бзднуть с продрисью, потому что консистенция моего говна сильно изменилась.</p><p><br/></p><p>Пообедал я бутербродами без мяса или рыбы. Хумус, авокадо, огурцы, помидоры. Съел я опять же в два раза больше, чем обычно по объёму. Но это не сильно мне помогло.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Для следующего ужина я решил добавить чего-нибудь, что нормально бы забило мой желудок и спасло бы от голода хотя бы на чуть чуть.</p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741" target="_blank"><img alt="Как я три дня был веганом еда, Диета, веганы, вегетарианцы, вегетаринство, фалафель, Тофу, зачем так жить, длиннопост" data-height="424" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/05/8/1465134551160284854.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/05/8/1465134551160284854.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Я купил тофу и фасольку. Ещё купил постные лепёшки-питу. Добавил в это хрючево ещё баклажанов, потому что я их дико люблю. Еды у меня вышло где-то грамм 400.</p><p><br/></p><p>Получилось, надо сказать, очень вкусно. Но под конец я уже не мог это есть. Физически не лезло, но организм по-прежнему требовал еды. Поэтому я просто ложкой доел фасольку из банки. Это немного спасло меня от голода, я смог доделать домашние дела и лечь спать лишь немного голодным.</p><p><br/></p><p>Я даже не смог как следует пообщаться со своей девушкой по телефону, потому что мозг отказывался думать о чём-либо.</p><p><br/></p><p>Так закончилась моя пятница.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Суббота прошла также дико голодной. На завтрак опять были фрукты. До обеда я дотянул на фасоли. На обед съел целую пачку фалафеля вприкуску с питой.</p><p><br/></p><p>Было немного проще под вечер, потому что я пошёл на день рождения, а там подбухнул и забыл про голод.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Утром в Воскресенье я проснулся не только голодным, но ещё и со средней тяжести бодунцом. Оно и понятно: пить на голодный желудок — не самая лучшая идея (я вообще спец по не самым лучшим идеям, ага). Но я набрал в себе остатки воли, чтобы продолжить эксперимент. Доел банку фасоли до конца, пожарил вега-котлетки (с брокколи и шампиньонами), и...</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>...понял, что не могу продолжать эксперимент. Это бесчеловечно. Нахуй так жить. Постоянный голод и пердёж. Непонимающие взгляды людей, когда ты отказываешься от каких-нибудь очевидно вкуснейших штук.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Я сварил все имеющиеся у меня яйца и сожрал их с мазиком. У меня тряслись руки в предвкушении животных белков. А ведь это всего лишь яйца. Мне кажется, ещё чуть-чуть, и я бы кончил, когда делал первый укус.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Пока я писал весь этот пост, в духовке у меня готовилась ветчинка. И это охуенно.</p><p></p>
                                </div>
                            </div>

                                <div class="b-story-block b-story-block_type_image">
                                    <div class="b-story-block__content">

                                    <a href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741" target="_blank"><img alt="Как я три дня был веганом еда, Диета, веганы, вегетарианцы, вегетаринство, фалафель, Тофу, зачем так жить, длиннопост" data-height="450" data-large-image="http://cs8.pikabu.ru/post_img/big/2016/06/05/8/1465134904123366409.jpg" data-src="http://cs8.pikabu.ru/post_img/2016/06/05/8/1465134904123366409.jpg" data-viewable="true" style=""/></a>

                                    </div>
                                </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>Я, глазом не моргнув, проглотил половину этого почти килограммового куска ветчины. Потом понял, что этого мало, и доел оставшуюся половину. Улёгся на диван. Такого кайфа я, кажется, не испытывал за всю свою жизнь. И это не преувеличение. Это на столько круто, что реально не с чем сравнить.</p><p></p>
                                </div>
                            </div>

                            <div class="b-story-block b-story-block_type_text">
                                <div class="b-story-block__content">
                                    <p></p><p>В общем я всем рекомендую веганскую диету. Без неё невозможно в полной мере понять, на сколько это важно и круто: есть нормальную человеческую еду.</p><p></p>
                                </div>
                            </div>

                        </div>

                    </div>

                        <a class="b-story__show-all" href="http://pikabu.ru/story/kak_ya_tri_dnya_byil_veganom_4249741">
                            <span>Показать полностью</span>
                            3 <i class="b-story__show-all-images"></i>

                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249741">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249741_end-->

                    <!--story_4249203_start-->
                    <div class="story" data-story-id="4249203" data-story-long="false" data-visited="false">
                        <div class="story__left">

                            <div class="story__rating-block" data-can-vote="true" data-story-id="4249203" data-vote="0">
                                <div class="story__rating-up" title="Поставить плюсик"></div>
                                <div class="story__rating-count">
                    2792
                                </div>
                                <div class="story__rating-down" title="Поставить минус"></div>
                            </div>

                            <div class="story__scroll-wrapper">
                                <div class="story__scroll">
                                    <div class="story__toggle-button story__toggle-button-scroll" data-story-id="4249203" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                                        <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <div class="story__main">
                        <div class="story__header">
                            <div class="story__header-title">

                        <a class="story__title-link " href="http://pikabu.ru/story/nakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203" target="_blank">Наконец-то фильм "Д-р. Акула" запущен в производство. Спустя 15 лет с написания и сожжения сценария.</a>

                    </div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4249203" data-story-long="false" data-story-type="image" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__image-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/nakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203#comments">130 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/Kyrsor">Kyrsor</a>
                    <div class="story__date" title="1465159577">22 часа назад</div> 
                    <div class="story__tags">

                            <a class="story__tag" href="http://pikabu.ru/tag/%EA%EB%E8%ED%E8%EA%E0/hot" target="_blank" title='Поиск по тегу "клиника"'>
                                клиника
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E4%EE%EA%F2%EE%F0/hot" target="_blank" title='Поиск по тегу "доктор"'>
                                доктор
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%E0%EA%F3%EB%E0/hot" target="_blank" title='Поиск по тегу "акула"'>
                                акула
                            </a>

                            <a class="story__tag" href="http://pikabu.ru/tag/%C7%E0%EA%20%C1%F0%E0%F4%F4/hot" target="_blank" title='Поиск по тегу "Зак Брафф"'>
                                Зак Брафф
                            </a>

                    </div>

                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4249203" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fnakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fnakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fnakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203&amp;text=%D0%9D%D0%B0%D0%BA%D0%BE%D0%BD%D0%B5%D1%86-%D1%82%D0%BE+%D1%84%D0%B8%D0%BB%D1%8C%D0%BC+%26quot%3B%D0%94-%D1%80.+%D0%90%D0%BA%D1%83%D0%BB%D0%B0%26quot%3B+%D0%B7%D0%B0%D0%BF%D1%83%D1%89%D0%B5%D0%BD+%D0%B2+%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE.+%D0%A1%D0%BF%D1%83%D1%81%D1%82%D1%8F+15+%D0%BB%D0%B5%D1%82+%D1%81+%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D1%8F+%D0%B8+%D1%81%D0%BE%D0%B6%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F+%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D1%8F." rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                    </div>

                                </div>
                            </div>
                        <div class="story__wrapper" style="display: block">

                    <div class="b-story__content b-story__content_type_media " data-expanded="1">

                        <a href="http://pikabu.ru/story/nakonetsto_film_quotdr_akulaquot_zapushchen_v_proizvodstvo_spustya_15_let_s_napisaniya_i_sozhzheniya_stsenariya_4249203" target="_blank">
                            <img alt="Наконец-то фильм &amp;quot;Д-р. Акула&amp;quot; запущен в производство. Спустя 15 лет с написания и сожжения сценария." data-bigger-available="true" data-large-image="http://cs4.pikabu.ru/post_img/big/2016/06/05/12/1465159557114875130.jpg" data-viewable="true" height="717" src="http://cs4.pikabu.ru/post_img/2016/06/05/12/1465159557114875130.jpg" width="600"/>
                        </a>

                    </div>

                    <div class="story__footer">
                        <ul class="story__rating-block story__rating-block_small" data-story-id="4249203">
                            <li class="story__rating-up-small " data-rating="up">
                                <i class="i-sprite--comments__rating-up"></i>
                            </li>
                            <li class="story__rating-down-small " data-rating="down">
                                <i class="i-sprite--comments__rating-down"></i>
                            </li>
                        </ul>
                        <div class="story__slide-up">свернуть</div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4249203_end-->

                        <script type="text/javascript">
                            (function(KEY, value, expireSec, domain) {
                                var data = KEY + "=" + value + ";";
                                data += "path=/;";
                                IF (expireSec != 0) {
                                    var d = new DATE();
                                    d.setTime(d.getTime() + (expireSec * 1000));
                                    data += "expires=" + d.toUTCString() + ";";
                                }
                                IF (domain) {
                                    data += "domain=" + domain + ";";
                                }
                                document.cookie = data;
                            })("_Va", "DR.tGTE.NWM1ZB", 12000, "");
                        </script>

                    <!--story_4250688_start-->
                    <div class="story" data-story-id="4250688" data-story-long="false" data-visited="false" style="margin-top: 10px">
                        <div class="story__left">
                            <i class="story__pin-o"></i>
                        </div>
                        <div class="story__main">

                            <div class="story__header">

                                <div class="story__header-title">

                            <a class="story__title-link " data-VIEW-KEY="JDR0cDhUb_qC" href="http://pikabu.ru/story/azaetonop_byota_noekdogoidn_anehct__shcsskchebyi_ranedskoekdogoidn_an_ray_n_4250688" target="_blank">Сергей Кабаргин и чемпион мира по дрифту Daigo Saito</a>

                            <!--noindex--><span class="story__source-domain">[youtube.com]</span><!--/noindex-->

                    </div>

                        <div class="story__description"></div>

                    <div class="story__header-additional">

                        <!--noindex-->
                        <div class="story__toggle-button" data-story-id="4250688" data-story-long="false" data-story-type="video" title="Показать/скрыть пост">
                            <i class="i-sprite--inline-block i-sprite--feed__video-hide"></i>
                        </div>
                        <!--/noindex-->

                    <div class="story__header-additional-wrapper">
                <a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/sergey_kabargin_i_chempion_mira_po_driftu_daigo_saito_4250688#comments">7 Комментариев</a>; <a class="story__sponsor" href="http://pikabu.ru/html.php?id=ad&amp;from=ad_unit">спонсорское видео</a> от <a class="story__author" href="http://pikabu.ru/profile/kxdoom">kxdoom</a>
                        <div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4250688" title="Сохранить"></div>

                        <div class="story__share i-sprite--inline-block i-sprite--feed__share-all"></div>
                        <!--noindex-->
                        <div class="story__share-buttons" style="display: none">

                    <a class="story__share-button story__share-button_type_fb i-sprite--feed__share-fb" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsergey_kabargin_i_chempion_mira_po_driftu_daigo_saito_4250688" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_vk i-sprite--feed__share-vk" href="http://vk.com/share.php?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsergey_kabargin_i_chempion_mira_po_driftu_daigo_saito_4250688" rel="nofollow" target="_blank"></a>
                    <a class="story__share-button story__share-button_type_tw i-sprite--feed__share-tw" href="http://twitter.com/share?url=http%3A%2F%2Fpikabu.ru%2Fstory%2Fsergey_kabargin_i_chempion_mira_po_driftu_daigo_saito_4250688&amp;text=%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9+%D0%9A%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B8%D0%BD+%D0%B8+%D1%87%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD+%D0%BC%D0%B8%D1%80%D0%B0+%D0%BF%D0%BE+%D0%B4%D1%80%D0%B8%D1%84%D1%82%D1%83+Daigo+Saito" rel="nofollow" target="_blank"></a>

                        </div>
                        <!--/noindex-->

                                    </div> <!-- header-additional-wrapper -->
                                </div>
                            </div> <!-- header -->

                            <div class="story__wrapper">

                    <div abbr="0" attr="1" class="b-story__content b-story__content_type_media" id="videoDiv4250688" style="display: block; margin-bottom: 0px; ">
                        <div class="b-video" data-aid="787" data-authors="true" data-callback="true" data-duration="123" data-id="4250688" data-original="true" data-ratio="1.78" data-url="https://www.youtube.com/embed/WGWj6XmlxAQ?version=3&amp;enablejsapi=1&amp;playerapiid=ytplayer">
                            <div class="b-video__player b-video__player_show_yes">
                                <iframe allowfullscreen="1" frameborder="0" src="https://www.youtube.com/embed/WGWj6XmlxAQ?version=3&amp;enablejsapi=1&amp;playerapiid=ytplayer" style="width: 100%; height: 100%"></iframe>
                            </div>
                        </div>
                    </div>

                            </div>
                        </div>
                    </div>
                    <!--story_4250688_end-->

                        </div>

                            <div class="stories__spinner" style="display: none;">
                                <div class="stories__spinner-bounce-1"></div>
                                <div class="stories__spinner-bounce-2"></div>
                                <div class="stories__spinner-bounce-3"></div>
                            </div>
                            <div id="tw_loader" style="margin: 10px 0 0 95px; display: none;">
                                <img height="41" src="http://cs.pikabu.ru/images/loading_new.gif" width="96"/>
                            </div>

                                </td>
                            </tr>
                        </tbody></TABLE>
                    </td>

                        <td class="personal" style="vertical-align: top">
                            <!--[start right menu]-->
                            <div class="menu-cont" id="right_menu">
                                <div class="header_links header-nav-top">
                                    <ul class="header_links" style="margin-right: 1%">
                                        <li><a href="http://pikabu.ru/tag">список тегов</a></li>
                                        <li><a href="http://pikabu.ru/disputed">обсуждаемое</a></li>
                                        <li><a href="http://pikabu.ru/search.php?n=16&amp;r=3">[моё]</a></li>
                                        <li><a href="http://pikabu.ru/html.php?id=faq">FAQ</a></li>
                                        <li><a href="http://pikabu.ru/html.php?id=ad">реклама</a></li>
                                    </ul>
                                </div>
                                <div class="header-search-box" id="serach_block">
                                    <form ACTION="http://pikabu.ru/search.php" method="get" name="form1">
                                        <div>
                                            <input class="search_block" id="search_menu" name="q" placeholder="поиск..." type="text" value=""/><input class="search_btn" src="http://cs.pikabu.ru/images/search_btn4n.png" type="image" value=""/>
                                        </div>
                                    </form>
                                </div>

                    <!--[start auth block]-->
                    <div class="b-sign">
                        <div class="b-tabs b-tabs_type_sign">
                            <ul class="b-tabs__list b-tabs__list_justify_center">
                                <li class="b-tabs_li_active_yes">Авторизация</li>
                                <li>Регистрация</li>
                            </ul>
                            <div class="b-tabs__container">
                                <!-- Войти -->
                                <div class="b-tabs__tab b-tabs__tab_active_yes b-sign__in">
                                    <form>
                                        <input name="mode" type="hidden" value="login"/>

                                        <div class="b-group b-group_margin-bottom_10">
                                            <input autocomplete="username" class="b-input" data-name="username" id="username" maxlength="255" name="username" placeholder="логин" type="text"/>
                                            <input autocomplete="password" class="b-input" data-name="password" id="password" maxlength="255" name="password" placeholder="пароль" type="password"/>
                                        </div>
                                        <div class="b-sign__captcha" style="display: none"></div>
                                        <div class="b-group">
                                            <div class="b-sign__oauth-providers">
                                                <a href="http://pikabu.ru/oauth.php?type=vk">
                                                    <i class="i-sprite--sign__vk i-sprite--inline-block"></i>
                                                </a> <a href="http://pikabu.ru/oauth.php?type=fb">
                                                    <i class="i-sprite--sign__facebook i-sprite--inline-block"></i>
                                                </a> <a href="http://pikabu.ru/oauth.php?type=tw">
                                                    <i class="i-sprite--sign__twitter i-sprite--inline-block"></i>
                                                </a> <a href="http://pikabu.ru/oauth.php?type=google">
                                                    <i class="i-sprite--sign__google i-sprite--inline-block"></i>
                                                </a>
                                            </div>
                                            <button class="b-button b-button_type_default" type="submit">войти</button>
                                        </div>
                                        <div class="b-sign__error" style="display: none">
                                            <div class="b-sign__error-message">Неверный логин или пароль</div>
                                            <a class="b-link b-link_type_primary" href="/login.php?retrieve=1">Восстановить пароль</a>
                                        </div>
                                    </form>
                                </div>
                                <!-- Зарегистрироватся -->
                                <div class="b-tabs__tab b-sign__up">
                                    <div class="b-sign__oauth-label">Через социальную сеть</div>
                                    <div class="b-sign__oauth-providers">
                                        <a href="http://pikabu.ru/oauth.php?type=vk">
                                            <i class="i-sprite--sign__vk i-sprite--inline-block"></i>
                                        </a> <a href="http://pikabu.ru/oauth.php?type=fb">
                                            <i class="i-sprite--sign__facebook i-sprite--inline-block"></i>
                                        </a> <a href="http://pikabu.ru/oauth.php?type=tw">
                                            <i class="i-sprite--sign__twitter i-sprite--inline-block"></i>
                                        </a> <a href="http://pikabu.ru/oauth.php?type=google">
                                            <i class="i-sprite--sign__google i-sprite--inline-block"></i>
                                        </a>
                                    </div>
                                    <div class="b-sign__oauth-hr"></div>
                                    <form id="form2" name="form2">
                                        <span class="b-sign__validate b-sign__validate_state_error" data-name="all"></span>
                                        <div>
                                            <label FOR="signup-u">Логин
                                                <span class="b-sign__validate b-sign__validate_state_error" data-name="username"></span>
                                            </label>
                                        </div>
                                        <div>
                                            <input autocomplete="off" class="b-input" data-name="username" id="signup-u" maxlength="255" type="text" value=""/>
                                        </div>
                                        <div>
                                            <label FOR="signup-e">Email
                                                <span class="b-sign__validate b-sign__validate_state_error" data-name="email"></span>
                                            </label>
                                        </div>
                                        <div>
                                            <input autocomplete="off" class="b-input" data-name="email" maxlength="255" type="email" value=""/>
                                        </div>
                                        <div class="b-sign__password">
                                            <label FOR="signup-p">Пароль
                                                <span class="b-sign__validate b-sign__validate_state_error" data-name="password"></span>
                                            </label>

                                            <div class="b-sign__password-view fa fa-eye"></div>
                                            <input autocomplete="off" class="b-input" data-additional="_k7j5Z9" data-name="password" id="signup-p" maxlength="255" type="password" value=""/>

                                            <div class="b-password-strength">
                                                <div class="b-password-strength__bar"></div>
                                            </div>
                                        </div>
                                        <span class="b-sign__validate b-sign__validate_state_error" data-name="g-recaptcha-response"></span>
                                        <div class="b-sign__captcha"></div>
                                        <button class="b-button b-button_type_create b-button_width_p100" type="submit">Зарегистрироваться</button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!--[end auth block]-->

                    <div class="login_f menu-add-btn">
                        <a href="javascript:void(0)" onclick="show_reg_msg()">
                            <div class="b-button b-button_type_green">
                                <img src="http://cs.pikabu.ru/images/addbutton2014_plus.png"/>
                                <div id="addnews_div">добавить пост</div>
                            </div>
                        </a>
                    </div>

                            <div class="login_f menu-block-branding">

                        <a href="http://pikabu.ru/go/WT0616" target="_blank">
                            <div id="branding_ad_comment" onclick="yaCounter174977.reachGoal('branding_click', {position: 'Комментарий'}); return true;" style="
                                    width: 300px;
                                    height: 100px;
                                    border-radius: 3px 3px 0 0;
                                    background: url('http://cs8.pikabu.ru/post_img/2016/06/03/10/14649725075155776.jpg');
                                    border-bottom: 1px dashed;
                                    border-bottom-color: #777;
                                    display: block !important;
                                    visibility: visible !important;
                                " title="">
                            </div>
                        </a>

                        <TABLE cellspacing="0" class="best_comm">
                            <tbody><tr>
                                <td class="rating_bl menu-block-title">
                                    <div>
                                        Комментарий дня
                                        <span class="menu-block-title-right">
                                            <a href="http://pikabu.ru/top50_comm.php">ТОП 50</a>
                                        </span>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td class="menu-best-comm">

                    <div class="menu-story-link">
                        <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286">Триал спорт испортил жизнь одной деревни</a>
                    </div>
                    <div class="info info_c menu-comm-head">
                        <h6>+1053</h6> 
                        <a href="http://pikabu.ru/profile/3JIouKoMMeHT">3JIouKoMMeHT</a>; <a class="detailDate" href="javascript:void(0)" style="text-decoration: none;" title="1465163938">21 час назад</a>
                        <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286#comment_66984234" title="ссылка на данный комментарий">#</a>
                    </div>
                    <div class="comment_msg comment_desc menu-comm-desc">

                    <div class="b-comment__body comment_desc" style="max-width: 260px; overflow: hidden">
                        Триал-спорт серьезная организация. Если действительно это они проводили мероприятие под своими флагами, предло<span id="show_long_comm">... <a href="http://pikabu.ru/story/trial_sport_isportil_zhizn_odnoy_derevni_4249286#comment_66984234" style="text-decoration: none">весь комментарий</a></span><span id="long_comm" style="display: none;">жите им мирное решение: они за собой подтирают, вы забываете об их существовании, они забывают к вам дорогу. В целом, я рекомендую вам рассказать об их environmentally friendly отношении на международных спортивных форумах. Это будет тотальный крах бренда, с ними ни один более-менее уважающий контрагент/команда/ассоциация работать после такого не будет, репутация дороже. </span>
                    </div>

                    </div>

                                    </td>
                                </tr>
                            </tbody></TABLE>
                        </div>

                    <TABLE border="0" cellpadding="0" cellspacing="0" style="width: 300px; margin: 15px 0 0 5px; padding: 0px; text-align: center">
                        <tbody><tr width="100%">
                        <td style="width: auto; font-size: 13px; text-align: center">

                        <!-- /52555387/pikabu.ru_300x250 -->
                        <div>
                        <script type="text/javascript">
                          var googletag = googletag || {};
                          googletag.cmd = googletag.cmd || [];
                          (function() {
                            var gads = document.createElement("script");
                            gads.async = TRUE;
                            gads.type = "text/javascript";
                            var useSSL = "https:" == document.location.protocol;
                            gads.src = (useSSL ? "https:" : "http:") +
                              "//www.googletagservices.com/tag/js/gpt.js";
                            var node = document.getElementsByTagName("script")[0];
                            node.parentNode.insertBefore(gads, node);
                          })();
                        </script>

                        <script type="text/javascript">
                          googletag.cmd.push(function() {
                            googletag.defineSlot("/52555387/pikabu.ru_300x250", [300, 250], "div-gpt-ad-1460378979199-0").addService(googletag.pubads());
                            googletag.pubads().enableSingleRequest();
                            googletag.enableServices();
                          });
                        </script>
                        </div>
                        <div id="div-gpt-ad-1460378979199-0" style="height:250px; width:300px;">
                        <script type="text/javascript">
                            googletag.cmd.push(function() { googletag.display("div-gpt-ad-1460378979199-0"); });
                        </script>
                        </div>

                            <div id="facebook_page_block" style="display: none"></div>
                            <script src="http://cs.pikabu.ru/files/advert.js"></script>
                            <script>
                                IF (!("ab" IN window)) { window.ab = TRUE; }
                                var result = document.getElementById("facebook_page_block");
                                IF (window.ab == TRUE) {
                                    document.getElementById("facebook_page_block").style.display = "block";
                                    result.innerHTML = '<iframe src="http://pikabu.ru/social_widget.php?i=2" scrolling="no" style="border: none; width: 302px; height: 250px; background-color: white;"></frame>';
                                }
                            </script>
                        </td>
                        </tr>
                    </tbody></TABLE>

                        <div class="login_f menu-block">
                            <TABLE cellpadding="0">
                                <tbody><tr>
                                    <td class="rating_bl menu-block-title">Управление на клавиатуре</td>
                                </tr>
                                <tr style="height:10px">
                                    <td class="small_text menu-block-small-txt">
                                        <img src="http://cs.pikabu.ru/images/keys/keysall_r.png"/>
                                    </td>
                                </tr>
                            </tbody></TABLE>
                        </div>

                        <div class="login_f menu-top-tags">
                            <TABLE cellpadding="0">
                                <tbody><tr>
                                    <td class="rating_bl">Популярные теги за 24 часа</td>
                                </tr>
                                <tr>
                                    <td class="menu-top-tags-cont">

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/длиннопост/hot"><span class="tag no_ch">длиннопост</span>
                                <span class="tag_count">450</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/видео/hot"><span class="tag no_ch">видео</span>
                                <span class="tag_count">311</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/сообщество/hot"><span class="tag no_ch">сообщество</span>
                                <span class="tag_count">201</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Игры/hot"><span class="tag no_ch">Игры</span>
                                <span class="tag_count">103</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/аниме/hot"><span class="tag no_ch">аниме</span>
                                <span class="tag_count">89</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/кот/hot"><span class="tag no_ch">кот</span>
                                <span class="tag_count">81</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/арт/hot"><span class="tag no_ch">арт</span>
                                <span class="tag_count">79</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Россия/hot"><span class="tag no_ch">Россия</span>
                                <span class="tag_count">70</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Anime art/hot"><span class="tag no_ch">Anime art</span>
                                <span class="tag_count">69</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/история/hot"><span class="tag no_ch">история</span>
                                <span class="tag_count">58</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/моё/hot"><span class="tag no_ch">моё</span>
                                <span class="tag_count">51</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Музыка/hot"><span class="tag no_ch">Музыка</span>
                                <span class="tag_count">44</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/собака/hot"><span class="tag no_ch">собака</span>
                                <span class="tag_count">40</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/coub/hot"><span class="tag no_ch">coub</span>
                                <span class="tag_count">39</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Игра престолов/hot"><span class="tag no_ch">Игра престолов</span>
                                <span class="tag_count">37</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/авто/hot"><span class="tag no_ch">авто</span>
                                <span class="tag_count">36</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Фильмы/hot"><span class="tag no_ch">Фильмы</span>
                                <span class="tag_count">33</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Интересное/hot"><span class="tag no_ch">Интересное</span>
                                <span class="tag_count">33</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Создайте сообщество/hot"><span class="tag no_ch">Создайте сообщество</span>
                                <span class="tag_count">32</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/рисунок/hot"><span class="tag no_ch">рисунок</span>
                                <span class="tag_count">32</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/футбол/hot"><span class="tag no_ch">футбол</span>
                                <span class="tag_count">31</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/работа/hot"><span class="tag no_ch">работа</span>
                                <span class="tag_count">30</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/фотография/hot"><span class="tag no_ch">фотография</span>
                                <span class="tag_count">30</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/животные/hot"><span class="tag no_ch">животные</span>
                                <span class="tag_count">29</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/лето/hot"><span class="tag no_ch">лето</span>
                                <span class="tag_count">29</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Overwatch/hot"><span class="tag no_ch">Overwatch</span>
                                <span class="tag_count">26</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Природа/hot"><span class="tag no_ch">Природа</span>
                                <span class="tag_count">25</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/еда/hot"><span class="tag no_ch">еда</span>
                                <span class="tag_count">24</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/Санкт-Петербург/hot"><span class="tag no_ch">Санкт-Петербург</span>
                                <span class="tag_count">24</span></a>
                            </div>

                            <div class="allMenuTags" style="">
                                <a class="no_ch" href="http://pikabu.ru/tag/спорт/hot"><span class="tag no_ch">спорт</span>
                                <span class="tag_count">22</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/steam/hot"><span class="tag no_ch">steam</span>
                                <span class="tag_count">21</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Косплей/hot"><span class="tag no_ch">Косплей</span>
                                <span class="tag_count">21</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/перевод/hot"><span class="tag no_ch">перевод</span>
                                <span class="tag_count">19</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/москва/hot"><span class="tag no_ch">москва</span>
                                <span class="tag_count">19</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/книги/hot"><span class="tag no_ch">книги</span>
                                <span class="tag_count">19</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/спойлер/hot"><span class="tag no_ch">спойлер</span>
                                <span class="tag_count">19</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/космос/hot"><span class="tag no_ch">космос</span>
                                <span class="tag_count">18</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/blizzard/hot"><span class="tag no_ch">blizzard</span>
                                <span class="tag_count">17</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Warhammer 40k/hot"><span class="tag no_ch">Warhammer 40k</span>
                                <span class="tag_count">17</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/путешествия/hot"><span class="tag no_ch">путешествия</span>
                                <span class="tag_count">17</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Photoshop/hot"><span class="tag no_ch">Photoshop</span>
                                <span class="tag_count">17</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Оружие/hot"><span class="tag no_ch">Оружие</span>
                                <span class="tag_count">16</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/ведьмак 3/hot"><span class="tag no_ch">ведьмак 3</span>
                                <span class="tag_count">16</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/сериалы/hot"><span class="tag no_ch">сериалы</span>
                                <span class="tag_count">16</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/халява/hot"><span class="tag no_ch">халява</span>
                                <span class="tag_count">15</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/крипота/hot"><span class="tag no_ch">крипота</span>
                                <span class="tag_count">15</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/ремонт/hot"><span class="tag no_ch">ремонт</span>
                                <span class="tag_count">15</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/вопрос/hot"><span class="tag no_ch">вопрос</span>
                                <span class="tag_count">15</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Искусство/hot"><span class="tag no_ch">Искусство</span>
                                <span class="tag_count">14</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/лига лени/hot"><span class="tag no_ch">лига лени</span>
                                <span class="tag_count">14</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/дтп/hot"><span class="tag no_ch">дтп</span>
                                <span class="tag_count">14</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/отношения/hot"><span class="tag no_ch">отношения</span>
                                <span class="tag_count">14</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Авиация/hot"><span class="tag no_ch">Авиация</span>
                                <span class="tag_count">14</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Компьютерные игры/hot"><span class="tag no_ch">Компьютерные игры</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/творчество/hot"><span class="tag no_ch">творчество</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Ведьмак/hot"><span class="tag no_ch">Ведьмак</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Своими руками/hot"><span class="tag no_ch">Своими руками</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/наука/hot"><span class="tag no_ch">наука</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/Warcraft/hot"><span class="tag no_ch">Warcraft</span>
                                <span class="tag_count">13</span></a>
                            </div>

                            <div class="allMenuTags" style="display:none">
                                <a class="no_ch" href="http://pikabu.ru/tag/объявление/hot"><span class="tag no_ch">объявление</span>
                                <span class="tag_count">13</span></a>
                            </div>

                                </td>
                            </tr>
                            <tr>
                                <td class="menu-top-tags-links">
                                    <div class="tag_all"><a class="showMenuTags dotted" href="" style="margin-right: 10px;">Показать еще 30</a><a href="http://pikabu.ru/tag" style="margin-right: 10px;">все теги</a><a href="http://pikabu.ru/tags_merge">объединение тегов</a>
                                    </div>
                                </td>
                            </tr>
                        </tbody></TABLE>
                        </div>

                    <div style="overflow: hidden; margin-top: 10px; margin-left: 17px;">

                        <!-- /52555387/pikabu.ru_240x400 -->
                        <div>
                        <script type="text/javascript">
                          var googletag = googletag || {};
                          googletag.cmd = googletag.cmd || [];
                          (function() {
                            var gads = document.createElement("script");
                            gads.async = TRUE;
                            gads.type = "text/javascript";
                            var useSSL = "https:" == document.location.protocol;
                            gads.src = (useSSL ? "https:" : "http:") +
                              "//www.googletagservices.com/tag/js/gpt.js";
                            var node = document.getElementsByTagName("script")[0];
                            node.parentNode.insertBefore(gads, node);
                          })();
                        </script>

                        <script type="text/javascript">
                          googletag.cmd.push(function() {
                            googletag.defineSlot("/52555387/pikabu.ru_240x400", [240, 400], "div-gpt-ad-1460378949260-0").addService(googletag.pubads());
                            googletag.pubads().enableSingleRequest();
                            googletag.enableServices();
                          });
                        </script>
                        </div>
                        <div id="div-gpt-ad-1460378949260-0" style="height:400px; width:240px;">
                        <script type="text/javascript">
                            googletag.cmd.push(function() { googletag.display("div-gpt-ad-1460378949260-0"); });
                        </script>
                        </div>

                    </div>
                <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-28292940-1']);
      _gaq.push(['_setDomainName', 'pikabu.ru']);
      _gaq.push(['_setAllowLinker', true]);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = TRUE;
    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>


                    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

                            <!--[end right menu]-->
                            </div>
                            </td>
                            </tr>

                        </tbody></TABLE>
                        <br/><br/>
                    </div>

                    <noindex>
                        <div class="header-message-signup" id="unreg_message">
                            Пожалуйста, <a class="gotoLoginForm" href="#login_block_btn_enter" id="showLogForm">войдите</a>
                            в аккаунт или <a class="gotoLoginForm" href="#login_block_btn_enter" id="showRegForm">зарегистрируйтесь</a>
                        </div>
                        <div class="header-message-err" id="error_message"></div>
                    </noindex>

                    <TABLE class="footer_links footer-table">
                        <tbody><tr>
                        <td class="footer-links" id="footer_links_td">
                            <img src="http://cs.pikabu.ru/images/rss.png"/><a href="http://pikabu.ru/xmlfeeds.php?cmd=popular">RSS</a>

                            <span> </span>
                            <a href="http://m.pikabu.ru">Мобильная версия</a>

                            <span> </span>
                            <a href="http://pikabu.ru/html.php?id=wtf">Правила</a>

                            <span> </span>
                            <a href="http://pikabu.ru/html.php?id=faq">FAQ</a>

                            <noindex>
                                <span> </span>
                                <a href="http://pikabu.ru/banned_users.php" rel="nofollow">Бан</a>
                            </noindex>

                            <span> </span>
                            <a href="http://pikabu.ru/html.php?id=ad">Реклама</a>
                        </td>
                        </tr>
                    </tbody></TABLE>

                    <TABLE class="footer_links2 footer-table">
                        <tbody><tr>
                        <td class="footer-links" id="footer_links_td" style="width: 67%">
                            Партнеры: <img src="http://cs.pikabu.ru/images/partners/blackbears.png"/>
                            <noindex><a href="https://vk.com/blackbearsmobi" rel="nofollow" target="_blank">BlackBears</a></noindex>
                        </td>
                        <td style="width: 15%"></td>
                        <td style="width: 17%">
                            <div class="footer-fornex">
                                <noindex>
                                    <span>Хостинг:</span>
                                    <a href="http://fornex.com/" rel="nofollow" target="_blank">Fornex.com</a>
                                </noindex>
                            </div>
                        </td>
                        </tr>
                    </tbody></TABLE>

                    <TABLE class="footer footer-table footer-table-bottom" style="color: black">
                        <tbody><tr style="color: black">
                        <td class="copy" style="width: 70%; line-height: 1.3;">
                            <div class="footer-social">
                                <span><img src="http://cs.pikabu.ru/images/vk_pikabu.png"/> <a href="http://vk.com/pikabu" style="color: black" target="_blank">Вконтакте</a></span>
                                <span style="margin-left:10px"><img src="http://cs.pikabu.ru/images/fb_3.png"/> <a href="https://www.facebook.com/pikabu.ru" style="color: black" target="_blank">Facebook</a></span>
                                <!-- <span style="margin-left:10px"><img src="http://cs.pikabu.ru/images/tw_3.png"> <a href="https://twitter.com/pikabu_vk" target="_blank"  style="color: black">Twitter</a></span> -->
                            </div>
                            <div class="footer-contact">
                            <div class="footer-contact">
                                Служба поддержки: <a href="mailto:support@pikabu.ru" style="color: black">support@pikabu.ru</a><br/>
                                По вопросам работы сайта: <a href="mailto:admin@pikabu.ru" style="color: black">admin@pikabu.ru</a><br/>
                                По вопросам <a href="http://pikabu.ru/html.php?id=ad" style="color: inherit;">рекламы</a>: <a href="mailto:ads@pikabu.ru" style="color: black">ads@pikabu.ru</a>
                                </div>
                            </div>
                        </td>

                        <td class="copy counter" style="width: 15%">
                            <div class="footer-counter-liveinternet">
                                <noindex>

                                <!--LiveInternet counter--><script type="text/javascript"><!--
                                    new Image().src = "//counter.yadro.ru/hit;Pikabu?r"+
                                    ESCAPE(document.referrer)+((typeof(screen)=="undefined")?"":
                                    ";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
                                    screen.colorDepth:screen.pixelDepth))+";u"+ESCAPE(document.URL)+
                                    ";"+Math.random();//--></script><!--/LiveInternet-->
                                </noindex>
                                <!--LiveInternet logo-->
                                    <a href="http://www.liveinternet.ru/click;Pikabu" target="_blank">
                                        <img alt="" border="0" height="31" src="//counter.yadro.ru/logo;Pikabu?17.2" title="LiveInternet: показано число просмотров за 24 часа, посетителей за 24 часа и за сегодня" width="88"/>
                                    </a>
                                <!--/LiveInternet-->

                            </div>
                        </td>
                        <td class="copy" style="width: 15%">
                            <noindex>
                            <div>
                                <div class="footer-pechenka">
                                    <div id="brovdiv">
                    <a href="http://pikabu.ru/story/_2595592">
                        <img id="brov" src="http://cs.pikabu.ru/images/fun/aksakal.png" style="" title="Печенюх [by maniackz]"/>
                    </a>
                </div>
                                </div>

                                <!-- Yandex.Metrika counter -->
                                <script type="text/javascript">
                                    (function (d, w, c) {
                                        (w[c] = w[c] || []).push(function() {
                                            try {
                                                w.yaCounter174977 = new Ya.Metrika({id:174977});
                                            } catch(e) { }
                                        });

                                        var n = d.getElementsByTagName("script")[0],
                                            s = d.createElement("script"),
                                            f = function () { n.parentNode.insertBefore(s, n); };
                                        s.type = "text/javascript";
                                        s.async = TRUE;
                                        s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

                                        IF (w.opera == "[object Opera]") {
                                            d.addEventListener("DOMContentLoaded", f, FALSE);
                                        } ELSE { f(); }
                                    })(document, window, "yandex_metrika_callbacks");
                                </script>
                                <noscript>
                                    &lt;div&gt;&lt;img src="//mc.yandex.ru/watch/174977" style="position:absolute; left:-9999px;" alt="" /&gt;&lt;/div&gt;
                                </noscript>
                                <!-- /Yandex.Metrika counter -->

                        <script>
                            !function(f,b,e,v,n,t,s){IF(f.fbq)return;n=f.fbq=function(){n.callMethod?
                            n.callMethod.apply(n,arguments):n.queue.push(arguments)};IF(!f._fbq)f._fbq=n;
                            n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;
                            t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
                            document,"script","//connect.facebook.net/en_US/fbevents.js");

                            fbq("init", "250301471808186");
                            fbq("track", "PageView");
                        </script>
                        <noscript>&lt;img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=250301471808186&amp;ev=PageView&amp;noscript=1"/&gt;</noscript>


                            </div>
                            <div style="visibility: hidden">
                                <script type="text/javascript">
                                    (window.Image ? (new Image()) : document.createElement("img")).src = location.protocol
                                        + "//vk.com/rtrg?r=y5YLGMdFGMussDQo9RKwt0ZXBhlVHz9Wk1keHFw1GGi6umhFgCHTD4vYUnpy9t2guau7nCXi4p4lZy6g4RVVeaj0ksWvpbGL8xl53mDcbKBtPgigBg/8OUM2g6lhNPstAMipZiDFYJpEV0LDXYgKucnNBBRu3QHNQbNNZnE/Zmg-";
                                </script>
                            </div>
                            </noindex>
                        </td>
                        </tr>
                    </tbody></TABLE>

                        <a href="http://pikabu.ru/go/WT0616" target="_blank">
                            <div id="branding_ad_footer" onclick="yaCounter174977.reachGoal('branding_click', {position: 'Футер'}); return true;" style="
                                    background: url('http://cs8.pikabu.ru/post_img/2016/06/03/10/146497249339315661.jpg') NO-repeat center;
                                    background-color: #fff;
                                    width: 100%;
                                    height: 285px;
                                    margin-top: -93px;
                                    display: block !important;
                                    visibility: visible !important;
                                " title="">
                            </div>
                        </a>



                </body></html>"""
