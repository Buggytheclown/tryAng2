from bs4 import BeautifulSoup
from PiParse.scripts.parsePikabu import PikabuSoup


class MockPikabuCommentsSoup(PikabuSoup):
    @classmethod
    def getParsePage(cls, parseUrl):
        return BeautifulSoup(cls.mockPikabu, "html5lib")

    mockPikabu = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
					<title>Думай наперёд !</title>
					<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
					<meta content="4810d7a06b7443d3" name="yandex-verification"/>
					<meta content="" name="keywords"/>
					<meta content="Думай наперёд !" name="description"/>
					<meta content="SAMEORIGIN" http-equiv="X-FRAME-OPTIONS"/>
					<meta content="100000072189793" property="fb:admins"/>
					<link href="http://pikabu.ru/story/dumay_naperyod__4254058" rel="canonical"/>
					<meta content="586543721489673" property="fb:app_id"/>

				<meta content="summary_large_image" name="twitter:card"/>
				<meta content="@pikabu_vk" name="twitter:site"/>
				<meta content="Думай наперёд !" name="twitter:title"/>
				<meta content="http://pikabu.ru/story/dumay_naperyod__4254058" name="twitter:url"/>

					<meta content="ПереводМиллиардер Дэниел Кэйт Людвиг перед смертью заморозил свой генетический материал, будучи уверенным в том, что дочка его бывшей супруги, проживающая отдельно, будет претендовать на его наследств" name="twitter:description"/>

					<meta content="http://s8.pikabu.ru/post_img/2016/06/07/8/og_og_1465303358222722496.jpg" name="twitter:image:src"/>

				<meta content="http://www.facebook.com/pikabu.ru" property="article:author"/>
				<meta content="http://www.facebook.com/pikabu.ru" property="article:publisher"/>
				<meta content="article" property="og:type"/>
				<meta content="Думай наперёд !" property="og:title"/>
				<meta content="http://pikabu.ru/story/dumay_naperyod__4254058" property="og:url"/>
				<meta content="http://s8.pikabu.ru/post_img/2016/06/07/8/og_og_1465303358222722496.jpg" property="og:image"/>
				<meta content="Пикабу" property="og:site_name"/>

					<meta content="ПереводМиллиардер Дэниел Кэйт Людвиг перед смертью заморозил свой генетический материал, будучи уверенным в том, что дочка его бывшей супруги, проживающая отдельно, будет претендовать на его наследств" property="og:description"/>

				<link href="http://cs.pikabu.ru/favicon2x.ico" id="favicon" rel="shortcut icon" type="image/x-icon"/>
				<link href="http://cs.pikabu.ru/images/icon_ios144.png" rel="apple-touch-icon" sizes="144x144"/>
				<link href="http://cs.pikabu.ru/images/icon_ios114.png" rel="apple-touch-icon" sizes="114x114"/>

				<script type="text/javascript">
					// define initial parameters
					var initParams = {"siteURL":"http:\/\/pikabu.ru\/","imgURL":"http:\/\/cs.pikabu.ru","userID":0,"userName":"","userKarma":0,"sessionID":"tp1sb1vvgol545a3lbr2d2jl39oo31a2","userBanTime":"","isUserBanned":FALSE,"isStoryAnimPreview":TRUE,"isCommAnimPreview":TRUE,"isScrollTopBtn":TRUE,"isAjaxLoadMode":TRUE,"isExpandedMode":TRUE,"isCommentsBranchesHidden":FALSE,"scriptName":"story.php","privateKey":"a2V6MjFZ","uniqueBufferID":"2b851392ff","registrationKey":"22ae636fa9","debugLocation":"","pickedDate":"2016-06-07","pageNumber":1,"environment":225,"developmentMode":FALSE,"filter_name":""};

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
 			<link href="http://cs.pikabu.ru/app/1.1.73/main/style.css" rel="stylesheet" type="text/css"/>

			<script charset="utf-8" src="http://cs.pikabu.ru/app/1.0.17/vendors/jquery/js/jquery.min.js" type="text/javascript"></script>
 			<script charset="utf-8" data-environment="production" data-version="1.1.73" id="applicationMain" src="http://cs.pikabu.ru/app/1.1.72/main/app.js" type="text/javascript"></script>

				<script type="text/javascript">
					$.ajaxSetup({headers: {"X-Csrf-Token" : initParams.sessionID}});
					$.browser = {safari: FALSE, opera: FALSE};
				</script>

					<link href="http://cs.pikabu.ru/css/yadirect/dcomments_new.css?2" rel="stylesheet" type="text/css"/>

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
				                <img attr="http://pikabu.ru/kcaptcha/index.php?PHPSESS=tp1sb1vvgol545a3lbr2d2jl39oo31a2" class="ov-capth_captcha_img" src="http://cs.pikabu.ru/images/loading-spin.svg" style="border-radius: 4px"/>
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

					<li class="active2"><a>Комментарии</a></li>

					<li class="noactive menu-item-default"><a class="no_ch" href="http://pikabu.ru/hot">Горячее</a></li>

					<li class="noactive menu-item-default"><a class="no_ch" href="http://pikabu.ru/best">Лучшее</a></li>

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
				<!-- cached -->
				<div class="page-story" data-user-IN-comments="0">

					<input name="save-cats" type="hidden" value='[{"id":0,"name":"\u041e\u0431\u0449\u0435\u0435","count":0}]'/>

				<!--story_4254058_start-->
				<div class="story" data-story-id="4254058" data-story-long="false" data-visited="false">
					<div class="story__left">

						<div class="story__rating-block" data-can-vote="true" data-story-id="4254058" data-vote="0">
							<div class="story__rating-up" title="Поставить плюсик"></div>
							<div class="story__rating-count">
				3737
							</div>
							<div class="story__rating-down" title="Поставить минус"></div>
						</div>

						<div class="story__scroll-wrapper">
							<div class="story__scroll">
								<div class="story__toggle-button story__toggle-button-scroll" data-story-id="4254058" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
									<i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
								</div>
							</div>
						</div>
					</div>

				<div class="story__main">
					<div class="story__header first_story">
						<div class="story__header-title">

					<a class="story__title-link " href="http://pikabu.ru/story/dumay_naperyod__4254058" target="_blank">Думай наперёд !</a>

				</div>

				<div class="story__header-additional">

					<!--noindex-->
					<div class="story__toggle-button" data-story-id="4254058" data-story-long="false" data-story-type="gtpost" title="Показать/скрыть пост">
						<i class="i-sprite--inline-block i-sprite--feed__gtpost-hide"></i>
					</div>
					<!--/noindex-->

				<div class="story__header-additional-wrapper">
			<a class="story__comments-count story__to-comments" href="http://pikabu.ru/story/dumay_naperyod__4254058#comments">216 Комментариев</a> <img class="story__user-icon" height="11" src="http://cs.pikabu.ru/assets/svg/user.svg" width="10"/><a class="story__author" href="http://pikabu.ru/profile/ukmaksimus">ukmaksimus</a>
				<div class="story__date" title="1465303445">4 часа назад</div> 
				<div class="story__tags">

						<a class="story__tag" href="http://pikabu.ru/tag/%E3%E5%ED%E5%F2%E8%F7%E5%F1%EA%E8%E9%20%EC%E0%F2%E5%F0%E8%E0%EB/hot" target="_blank" title='Поиск по тегу "генетический материал"'>
							генетический материал
						</a>

						<a class="story__tag" href="http://pikabu.ru/tag/%EC%E8%EB%EB%E8%E0%F0%E4%E5%F0/hot" target="_blank" title='Поиск по тегу "миллиардер"'>
							миллиардер
						</a>

						<a class="story__tag" href="http://pikabu.ru/tag/%ED%E0%F1%EB%E5%E4%F1%F2%E2%EE/hot" target="_blank" title='Поиск по тегу "наследство"'>
							наследство
						</a>

						<a class="story__tag" href="http://pikabu.ru/tag/%D5%E8%F2%F0%EE%F1%F2%FC/hot" target="_blank" title='Поиск по тегу "Хитрость"'>
							Хитрость
						</a>

						<a class="story__tag" href="http://pikabu.ru/tag/%E4%F3%EC%E0%E9%20%ED%E0%EF%E5%F0%E5%E4/hot" target="_blank" title='Поиск по тегу "думай наперед"'>
							думай наперед
						</a>

						<a class="story__tag" href="http://pikabu.ru/tag/%F3%EC/hot" target="_blank" title='Поиск по тегу "ум"'>
							ум
						</a>

				</div>

					<div class="story__save i-sprite--comments__save" data-saved="false" data-story-id="4254058" title="Сохранить"></div>

				</div>

							</div>
						</div>
					<div class="story__wrapper" style="display: block">

				<div class="b-story__content b-story-blocks b-story-blocks_with-border" data-expanded="true">
					<div class="b-story-blocks__wrapper" style="">

							<div class="b-story-block b-story-block_type_image">
								<div class="b-story-block__content b-story-block__content_margin">

								<a href="http://cs8.pikabu.ru/post_img/2016/06/07/8/1465303008174149515.jpg" target="_blank"><img alt="Думай наперёд ! генетический материал, миллиардер, наследство, Хитрость, думай наперед, ум" data-height="382" data-large-image="http://cs8.pikabu.ru/post_img/2016/06/07/8/1465303008174149515.jpg" data-viewable="true" src="http://cs8.pikabu.ru/post_img/2016/06/07/8/1465303008174149515.jpg" style=""/></a>

								</div>
							</div>

						<div class="b-story-block b-story-block_type_text">
							<div class="b-story-block__content">
								<p></p><p>Перевод</p><p>Миллиардер Дэниел Кэйт Людвиг перед смертью заморозил свой генетический материал, будучи уверенным в том, что дочка его бывшей супруги, проживающая отдельно, будет претендовать на его наследство. Через сорок лет после смерти Дэниела, дочка  попыталась отсудить его поместье, но проиграла поскольку анализ ДНК определил, что он не был ее отцом.</p><p></p>
							</div>
						</div>

				</div>

				</div>

				<div class="story__footer">
					<ul class="story__rating-block story__rating-block_small" data-story-id="4254058">
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
				<!--story_4254058_end-->

					</div>

					<TABLE cellpadding="0" cellspacing="0" class="inner_wrap">
						<colgroup>
							<col></col>
							<col class="inner_wrap_content"></col>
						</colgroup>
						<tbody>
						<tr>
							<td></td>
							<td>

				<noindex>
				<!--+ social segment frontend-web-pikabu#330 -->
				<div class="b-social" data-description="ПереводМиллиардер Дэниел Кэйт Людвиг перед смертью заморозил свой генетический материал, будучи уверенным в том, что дочка его бывшей супруги, проживающая отдельно, будет претендовать на его наследств" data-image="http://s8.pikabu.ru/post_img/2016/06/07/8/og_og_1465303358222722496.jpg" data-title="Думай наперёд !" data-url="http://pikabu.ru/story/dumay_naperyod__4254058">
					<div class="b-social__buttons">
						<div class="b-social-button b-social-button_type_facebook">
							<div class="fb-like" data-ACTION="like" data-href="http://pikabu.ru/story/dumay_naperyod__4254058" data-layout="button" data-share="false" data-show-faces="false" style="margin-right: -4px;"></div>
							<i class="i-sprite--social__facebook"></i><span class="b-social-button__counter" style="vertical-align: top">0</span>
						</div>
						<div class="b-social-button b-social-button_type_vk">
							<span class="b-social-button__icon"><i class="i-sprite--social__vk"></i></span><span class="b-social-button__counter">0</span>
						</div>
						<div class="b-social-button b-social-button_type_twitter">
							<span class="b-social-button__icon"><i class="i-sprite--social__twitter"></i></span><span class="b-social-button__counter">0</span>
						</div>
						<div class="b-social-button b-social-button_type_save" data-count="107" data-saved="false" data-story-id="4254058">
							<span class="b-social-button__icon-save">
								<span class="b-social-button__icon-in i-sprite--social__save" style=""></span>
								<span class="b-social-button__icon-in i-sprite--social__saved" style="visibility: hidden;"></span>
							</span><span class="b-social-button__counter">0</span>
						</div>
					</div>
					<div class="b-social__widgets">
						<div class="b-social-widget b-social-widget_type_vk" style="display: none">
							<div id="social-vk-widget"></div>
							<a class="b-social-widget__link" href="#">Я уже с вами :)</a>
						</div>
						<div class="b-social-widget b-social-widget_type_twitter" style="display: none">
							<div id="social-twitter-widget">
								<a class="twitter-timeline" data-dnt="true" data-widget-id="568363779285860352" height="320" href="https://twitter.com/pikabu_vk" width="300">Твиты от @pikabu_vk</a>
							</div>
							<a class="b-social-widget__link" href="#">Я уже с вами :)</a>
						</div>
						<div class="b-social-widget b-social-widget_type_facebook" style="display: none" п="">
							<!--div class="b-social-widget__decoration i-sprite--social__decoration"></div-->
							<div class="b-social-widget__wrapper">
								<!--div class="fb-like-box" data-href="https://www.facebook.com/pikabu.ru" data-width="580" data-height="180" data-colorscheme="light" data-show-faces="true" data-header="false" data-stream="false" data-show-border="false"></div-->
								<div class="b-social-widget__facebook-subscribe">Подписаться на Пикабу: </div><div class="fb-like" data-ACTION="like" data-href="https://www.facebook.com/pikabu.ru" data-layout="standard" data-share="false" data-show-faces="false"></div>
							</div>
							<a class="b-social-widget__link b-social-widget__link_type_facebook" href="#">Я уже с вами :)</a>
						</div>
					</div>
				</div>
				<!--- social segment frontend-web-pikabu#330 -->

				<div class="b-story-duplicates" style="display: none;"></div>
				<div class="b-story-info" id="comments">
				<div class="b-story-info__main">
			216 комментариев, по <span class="b-story-info__set-order" title="изменить порядок комментариев">актуальности</span>
						<div class="b-story-info__box-order" style="display: none;">
							<p><label><input name="comment_order" type="radio" value="1"/> Рейтингу</label></p>
							<p><label><input name="comment_order" type="radio" value="2"/> Времени</label></p>
							<p><label><input checked="checked" name="comment_order" type="radio" value="3"/> Актуальности</label></p>
						</div>
					</div>
					<div class="b-story-info__custom">

					<div class="b-story__rating" data-minuses="64" data-pluses="3801">
						<span class="b-story__rating-pluses" style="width: 98%"></span><span class="b-story__rating-minuses" style="width: 2%"></span>
					</div>

					<i class="b-story-info__duplicates i-sprite--page-story__duplicates-no" data-has="false" data-story-id="4254058" title="дубликатов не найдено"></i>

					</div>

				</div>
			</noindex>
				<div class="b-comments_type_main" data-ignored-user="false" data-user-ignored="false">

				<div class="b-comment" data-editable="false" data-id="67082033" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082033">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+563</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LikaSense"><span class="">LikaSense</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465303813">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082033" name="comment_67082033" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							для дочки сюрприз, если она считала по правде его своим отцом. за такой исход спасибо маме)))

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">99</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67084588" data-level="1" data-parent-id="67082033" data-vote="0" id="comment_67084588">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+167</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Ionesoul"><span class="">Ionesoul</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465305818">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084588" name="comment_67084588" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>я думаю задачей был именно сюрприз, иначе он мог просто оставить завещание. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">21</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085758" data-level="2" data-parent-id="67084588" data-vote="0" id="comment_67085758">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+77</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/TackleTart"><img alt="TackleTart" src="http://cs6.pikabu.ru/images/avatars/1236/s1236832-1381398200.jpg"/> <span class="">TackleTart</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306773">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085758" name="comment_67085758" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							завещание он оставил. просто ОП не может в перевод.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">19</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086255" data-level="3" data-parent-id="67085758" data-vote="0" id="comment_67086255">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+51</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/lordalsi"><span class="">lordalsi</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307158">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086255" name="comment_67086255" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ну да - правильней былоб "оспорить завещание" или что-т вроде того?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">17</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089792" data-level="4" data-parent-id="67086255" data-vote="0" id="comment_67089792">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+23</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kincsem"><img alt="kincsem" src="http://cs6.pikabu.ru/images/avatars/1018/s1018943-1388101760.jpg"/> <span class="">kincsem</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465310375">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089792" name="comment_67089792" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Да, challenge his will, где will - последняя воля, завещание. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090502" data-level="5" data-parent-id="67089792" data-vote="0" id="comment_67090502">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/krad213"><span class="">krad213</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311029">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090502" name="comment_67090502" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Кроме того не переведено ключевое слово "estranged" - находящаяся в ссоре.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67093327" data-level="6" data-parent-id="67090502" data-vote="0" id="comment_67093327">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/hoone"><span class="">hoone</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313870">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093327" name="comment_67093327" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Это в каком словаре вы такое нашли?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67097327" data-level="6" data-parent-id="67090502" data-vote="0" id="comment_67097327">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Zaxxon"><img alt="Zaxxon" src="http://cs6.pikabu.ru/images/avatars/1218/s1218905-1640942613.jpg"/> <span class="">Zaxxon</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465318100">52 минуты назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097327" name="comment_67097327" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote><p>дочка его бывшей супруги, <b>проживающая отдельно</b></p></blockquote><p>Скриншот вам вместо пруфа:<b><br/></b></p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465318100155422611.png"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465318100155422611.png" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465318100155422611.png"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098544" data-level="6" data-parent-id="67090502" data-vote="0" id="comment_67098544">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/gusy0nok"><img alt="gusy0nok" src="http://cs6.pikabu.ru/images/avatars/393/s393634.jpg?1294041526"/> <span class="">gusy0nok</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465319369">30 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098544" name="comment_67098544" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>estranged - раздельно проживающий, разобщенный<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67093728" data-level="4" data-parent-id="67086255" data-vote="0" id="comment_67093728">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MorningGlory"><img alt="MorningGlory" src="http://cs6.pikabu.ru/images/avatars/668/s668789-1462175745.jpg"/> <span class="">MorningGlory</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465314242">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093728" name="comment_67093728" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>0_о а разве можно как-то взять и оспорить завещание, которое написал сам человек перед смертью?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">11</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67094214" data-level="5" data-parent-id="67093728" data-vote="0" id="comment_67094214">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Designforfood"><img alt="Designforfood" src="http://cs6.pikabu.ru/images/avatars/748/s748736-1094334019.jpg"/> <span class="">Designforfood</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465314735">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094214" name="comment_67094214" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Да, и чаще пишут не перед смертью. Не все посетили сайт "когда я умру", так что писали давно и в маразме, под давлением, нотариуса подкупили, ложное завещание, заговор рептилойдов и т.д.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095143" data-level="6" data-parent-id="67094214" data-vote="0" id="comment_67095143">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MorningGlory"><img alt="MorningGlory" src="http://cs6.pikabu.ru/images/avatars/668/s668789-1462175745.jpg"/> <span class="">MorningGlory</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315713">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095143" name="comment_67095143" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Люто. Похоже надо в 50 лет завещание писать и всем говорить, что оно настоящее, а иначе как не пиши - всё по-своему сделают))</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">5</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095940" data-level="7" data-parent-id="67095143" data-vote="0" id="comment_67095940">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+14</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/BrimstoneFox"><img alt="BrimstoneFox" src="http://cs6.pikabu.ru/images/avatars/234/s234542-864529641.jpg"/> <span class="">BrimstoneFox</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465316584">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095940" name="comment_67095940" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Да ладно, что ты там завещать собрался, жесткий диск с терабайтами порнухи? ( ͡° ͜ʖ ͡°)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096721" data-level="8" data-parent-id="67095940" data-vote="0" id="comment_67096721">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+9</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Furmi"><span class="">Furmi</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465317425">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096721" name="comment_67096721" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Чем не шикарное наследство

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67097251" data-level="8" data-parent-id="67095940" data-vote="0" id="comment_67097251">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Furystorm"><img alt="Furystorm" src="http://cs6.pikabu.ru/images/avatars/391/s391798-1687122370.jpg"/> <span class="">Furystorm</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465318027">53 минуты назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097251" name="comment_67097251" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>еще и внукам хватит (⌐ ͡■ ͜ʖ ͡■)</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/146531802716918253.jpg"><img class="b-image" data-large-image="" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/146531802716918253.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67098612" data-level="9" data-parent-id="67097251" data-vote="0" id="comment_67098612">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/gDaniCh"><img alt="gDaniCh" src="http://cs6.pikabu.ru/images/avatars/280/s280983-862347614.jpg"/> <span class="">gDaniCh</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465319439">29 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098612" name="comment_67098612" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p><br/>А у меня таких 4штуки скучают... </p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465319438186177889.jpg"><img class="b-image" data-large-image="" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465319438186177889.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67099417" data-level="8" data-parent-id="67095940" data-vote="0" id="comment_67099417">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/IamBaby"><img alt="IamBaby" src="http://cs6.pikabu.ru/images/avatars/1336/s1336994-472804175.jpg"/> <span class="">IamBaby</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465320288">15 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099417" name="comment_67099417" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Я не против такого наследства!</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094254" data-level="5" data-parent-id="67093728" data-vote="0" id="comment_67094254">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kincsem"><img alt="kincsem" src="http://cs6.pikabu.ru/images/avatars/1018/s1018943-1388101760.jpg"/> <span class="">kincsem</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465314782">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094254" name="comment_67094254" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Можно. Всех причин не назову, но точно можно сделать это при подозрении, что человек не был дееспособен на момент написания завещания, впал в слабоумие в силу возраста, тяжело болел и т.д. Надо в ГК заглянуть, там это есть. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094628" data-level="5" data-parent-id="67093728" data-vote="0" id="comment_67094628">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/G0lub"><img alt="G0lub" src="http://cs6.pikabu.ru/images/avatars/613/s613468.jpg?1177846552"/> <span class="">G0lub</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315179">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094628" name="comment_67094628" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>конечно можно. если какой-нибудь чувак завещает все свои средства в приют для кошек, то близкие родственники и сожители имеют право оспорить завещание, так как по закону им полагается не меньше какой-то там части наследства.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67097318" data-level="6" data-parent-id="67094628" data-vote="0" id="comment_67097318">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Furystorm"><img alt="Furystorm" src="http://cs6.pikabu.ru/images/avatars/391/s391798-1687122370.jpg"/> <span class="">Furystorm</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465318091">52 минуты назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097318" name="comment_67097318" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>и РФ и штатах разные законы о наследстве, не путай</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098065" data-level="6" data-parent-id="67094628" data-vote="0" id="comment_67098065">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MrModest"><img alt="MrModest" src="http://cs6.pikabu.ru/images/avatars/995/s995610-1954553404.jpg"/> <span class="">MrModest</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465318878">39 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098065" name="comment_67098065" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Это с какой это стати родне должно что-то полагаться, если сам человек категорически не хочет ей ничего завещать? о_0

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098790" data-level="3" data-parent-id="67085758" data-vote="0" id="comment_67098790">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/WalkingSparrow"><img alt="WalkingSparrow" src="http://cs6.pikabu.ru/images/avatars/1133/s1133841-1427903465.jpg"/> <span class="">WalkingSparrow</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465319612">26 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098790" name="comment_67098790" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Как раз "в перевод" он "может" (вот ведь идиотское выражение). Форма изменена, смысл сохранился - ведь "претендовать на наследство" и означает "пытаться оспорить завещание". Если претензий к завещанию нет, то и претензий на наследство нет, всё логично.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67093079" data-level="2" data-parent-id="67084588" data-vote="0" id="comment_67093079">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Bianchi"><img alt="Bianchi" src="http://cs6.pikabu.ru/images/avatars/687/s687687-1315352311.jpg"/> <span class="">Bianchi</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313598">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093079" name="comment_67093079" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Было бы прикольно, если бы он еще к этому анализу ДНк оставил записку со словами "СЮРПРИЗ!""</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086834" data-level="1" data-parent-id="67082033" data-vote="0" id="comment_67086834">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+30</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/dyuhasil"><img alt="dyuhasil" src="http://cs6.pikabu.ru/images/avatars/603/s603458.jpg?1261351426"/> <span class="">dyuhasil</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307637">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086834" name="comment_67086834" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote> за такой исход спасибо маме)))</blockquote><p>Инфантильные девочки, в таких случаях, да, винят мам. Целеустремлённые девочки знают - кровное родство, не единственный способ получить папкино наследство...</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465307637149561329.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465307637149561329.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465307637149561329.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087699" data-level="2" data-parent-id="67086834" data-vote="0" id="comment_67087699">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+25</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/tarasui"><img alt="tarasui" src="http://cs6.pikabu.ru/images/avatars/525/s525072-2144902939.jpg"/> <span class="">tarasui</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465308435">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087699" name="comment_67087699" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465308434182761584.jpg"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465308434182761584.jpg" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465308434182761584.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096053" data-level="3" data-parent-id="67087699" data-vote="0" id="comment_67096053">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DmitriyNagiev"><img alt="DmitriyNagiev" src="http://cs6.pikabu.ru/images/avatars/1194/s1194198-2089227552.jpg"/> <span class="">DmitriyNagiev</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465316691">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096053" name="comment_67096053" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Их сын.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088671" data-level="2" data-parent-id="67086834" data-vote="0" id="comment_67088671">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Brontozyabra"><img alt="Brontozyabra" src="http://cs6.pikabu.ru/images/avatars/192/s192993.jpg"/> <span class="">Brontozyabra</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465309329">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088671" name="comment_67088671" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Прочитала про его жену и охуела о_О</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090638" data-level="3" data-parent-id="67088671" data-vote="0" id="comment_67090638">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/AnaAnto"><img alt="AnaAnto" src="http://cs6.pikabu.ru/images/avatars/713/s713310-1408642545.jpg"/> <span class="">AnaAnto</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465311166">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090638" name="comment_67090638" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>а что там? я ничего не нашла</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67091294" data-level="4" data-parent-id="67090638" data-vote="0" id="comment_67091294">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Boltin"><img alt="Boltin" src="http://cs6.pikabu.ru/images/avatars/557/s557475-2129058361.jpg"/> <span class="">Boltin</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311816">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091294" name="comment_67091294" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ну... она была его падчерицей.</p><p>На что коммент <noindex><a href="http://pikabu.ru/profile/dyuhasil" rel="nofollow" target="_blank">@dyuhasil</a></noindex> и ссылается.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67093503" data-level="5" data-parent-id="67091294" data-vote="0" id="comment_67093503">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/AnaAnto"><img alt="AnaAnto" src="http://cs6.pikabu.ru/images/avatars/713/s713310-1408642545.jpg"/> <span class="">AnaAnto</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465314026">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093503" name="comment_67093503" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>а, это я знала<br/>к тому же они стали встречаться после того, как он с ее матерью (кстати она девушке тоже не роднёй была) расстались</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084678" data-level="1" data-parent-id="67082033" data-vote="0" id="comment_67084678">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+66</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465305892">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084678" name="comment_67084678" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А КАК В РОССИИ БОРЮТСЯ С БЛЯДСТВОМ!? </p><p>Не переключайтесь - ещё много всего интересного...<noindex><a href="https://youtu.be/djv_XetNfSA" rel="nofollow" target="_blank">https://youtu.be/djv_XetNfSA</a></noindex></p><div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465305892115211144.jpg"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465305892115211144.jpg" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465305892115211144.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">69</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086330" data-level="2" data-parent-id="67084678" data-vote="0" id="comment_67086330">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+26</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DreamSouls"><span class="">DreamSouls</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307217">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086330" name="comment_67086330" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Как я ненавижу таких людей. Одна блядь которая трахается с кем по попало на праздниках, другой выродок, руки распускает. </p><p>И при этом уверены в свой правоте. </p><p><br/></p><p>Хочется такой закон на самом деле, как обязательная генетическая проверка на отцовство. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">7</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089439" data-level="3" data-parent-id="67086330" data-vote="0" id="comment_67089439">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ZamenitelRazuma"><img alt="ZamenitelRazuma" src="http://cs6.pikabu.ru/images/avatars/800/s800719-1052759767.jpg"/> <span class="">ZamenitelRazuma</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310062">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089439" name="comment_67089439" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							Женщины взвоют. В США похожая практика была (подробности просто не помню) и около половины мужчин воспитывали не своих детей)

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092272" data-level="4" data-parent-id="67089439" data-vote="0" id="comment_67092272">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+17</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DreamSouls"><span class="">DreamSouls</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465312823">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092272" name="comment_67092272" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Взвоют не женщины, а бляди. А что их слушать... </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092598" data-level="5" data-parent-id="67092272" data-vote="0" id="comment_67092598">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/visper110"><img alt="visper110" src="http://cs6.pikabu.ru/images/avatars/489/s489904-1964161224.jpg"/> <span class="">visper110</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313110">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092598" name="comment_67092598" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Их же мало так, и в правительстве их нет, ога</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092921" data-level="6" data-parent-id="67092598" data-vote="0" id="comment_67092921">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DreamSouls"><span class="">DreamSouls</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313412">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092921" name="comment_67092921" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Так то можно наверное понять, кто из них кто. Даже не создавая этот закон, а вынеся их на рассмотрения. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67097103" data-level="5" data-parent-id="67092272" data-vote="0" id="comment_67097103">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/BERSERKER13"><img alt="BERSERKER13" src="http://cs6.pikabu.ru/images/avatars/488/s488483-1528062054.jpg"/> <span class="">BERSERKER13</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465317869">55 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097103" name="comment_67097103" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Пока слушают и очень хорошо. Причем везде. Отец не имеет юридического права осуществить ДНК тест твоего ребенка. Женщины намного сильней защищены законом. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098578" data-level="5" data-parent-id="67092272" data-vote="0" id="comment_67098578">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/SteinIsOne"><img alt="SteinIsOne" src="http://cs6.pikabu.ru/images/avatars/622/s622275-12884638.jpg"/> <span class="">SteinIsOne</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465319405">30 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098578" name="comment_67098578" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>вот было-бы круто отбирать права у блядей и создать рынок блядей-рабов. <br/>Из плюсов можно отметить сокращение количества блядей и ностальгию у негров</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67090857" data-level="4" data-parent-id="67089439" data-vote="0" id="comment_67090857">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Vanyushka"><span class="">Vanyushka</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465311365">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090857" name="comment_67090857" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							ага, там ведь даже при просмотре 3D прона залетают )

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085222" data-level="2" data-parent-id="67084678" data-vote="0" id="comment_67085222">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+72</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306330">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085222" name="comment_67085222" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Короткая версия для ЛЛ (зубодробильная) <noindex><a href="https://youtu.be/zSoR5Kv9X7g" rel="nofollow" target="_blank">https://youtu.be/zSoR5Kv9X7g</a></noindex></p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/146530633013829948.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/146530633013829948.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/146530633013829948.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">34</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085669" data-level="3" data-parent-id="67085222" data-vote="0" id="comment_67085669">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+85</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Takedzo"><span class="">Takedzo</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306693">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085669" name="comment_67085669" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Так если я помню , в конце этот чувак оказался не виноват и не его был ребенок :D</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">30</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086232" data-level="4" data-parent-id="67085669" data-vote="0" id="comment_67086232">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+70</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307139">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086232" name="comment_67086232" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ну да. Ребёнок оказался парня, который там же гостем программы был и уже женат был на другой)))</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">28</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086329" data-level="5" data-parent-id="67086232" data-vote="0" id="comment_67086329">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+212</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/suomynona"><span class="">suomynona</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307217">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086329" name="comment_67086329" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Блин, ребят. Я бы не признавался в таком, вот так у всех на виду. Мы теперь знаем, что вы это смотрели.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">26</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086552" data-level="6" data-parent-id="67086329" data-vote="0" id="comment_67086552">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+33</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307416">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086552" name="comment_67086552" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Когда сидишь на дежурстве, то собственно отбирать и тыкать в разные ролики ютуба особо некогда - просто врубаешь плей-лист определённого направления и автоматом выстреливают самые яркие ролики по заданной теме.</p><p>А так как работают в отделе одни женщины, то подобное преобладает в интересах)))</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">21</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089188" data-level="7" data-parent-id="67086552" data-vote="0" id="comment_67089188">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+23</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sent4"><img alt="sent4" src="http://cs6.pikabu.ru/images/avatars/642/s642689-1351481518.jpg"/> <span class="">sent4</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309822">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089188" name="comment_67089188" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А если бы в отделе работали преимущественно геи? Корявая отговорка, если честно :)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">19</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089620" data-level="8" data-parent-id="67089188" data-vote="0" id="comment_67089620">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465310227">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089620" name="comment_67089620" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Извините, Мариванна, виновата. Не буду больше смотреть на то, что общество думает про блядей. В рот я ебла такое общество, которое не любит своих блядей. Буду проводить время в притонах и бухать с кем-попало на деньги с материнского капитала.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">18</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092838" data-level="9" data-parent-id="67089620" data-vote="0" id="comment_67092838">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sent4"><img alt="sent4" src="http://cs6.pikabu.ru/images/avatars/642/s642689-1351481518.jpg"/> <span class="">sent4</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313333">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092838" name="comment_67092838" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Общество? Где Вы, Марьпетровна, общество-то в малаховском сборище застали? Нету там никакого общества, акромя общества копрофилов.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">7</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67093374" data-level="0" data-parent-id="67092838" data-vote="0" id="comment_67093374">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465313906">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093374" name="comment_67093374" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А ты хочешь, чтобы российский народ учился семейным отношениям на примере Владимира и Людмилы Путиных?</p><p>Или на ком ещё?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_expand" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-plus-square"></div>
						<div class="b-comment-toggle__count" style="display: block">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1 b-comments_new-line" style="display: none">

				<div class="b-comment" data-editable="false" data-id="67093967" data-level="1" data-parent-id="67093374" data-vote="0" id="comment_67093967">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sent4"><img alt="sent4" src="http://cs6.pikabu.ru/images/avatars/642/s642689-1351481518.jpg"/> <span class="">sent4</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465314483">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093967" name="comment_67093967" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Господь с Вами. Я решительно ничего не хочу от российского народа. От конкретного человека - может быть. От народа в целом - увольте. Слишком много шарлатанов говорит его, народа, имени.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">5</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095881" data-level="2" data-parent-id="67093967" data-vote="0" id="comment_67095881">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316521">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095881" name="comment_67095881" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Путин - не шарлатан, а представитель всей страны. Не согласен?</p><p>Мне вот муж так и сказал, когда разводился со мной: "Беру пример с Президента".</p><p>Мой муж поступил как шарлатан?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67097950" data-level="3" data-parent-id="67095881" data-vote="0" id="comment_67097950">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sent4"><img alt="sent4" src="http://cs6.pikabu.ru/images/avatars/642/s642689-1351481518.jpg"/> <span class="">sent4</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465318760">41 минуту назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097950" name="comment_67097950" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Да, Ваш муж поступил как шарлатан. Но не потому, что Путин шарлатан. А потому, что не решился взять ответственность за свой поступок на себя.<br/>P.S. Владимир Владимирович по мне - главный шарлатан в стране, но это не имеет отношения к нашей теме).

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67098834" data-level="4" data-parent-id="67097950" data-vote="0" id="comment_67098834">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465319658">26 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098834" name="comment_67098834" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Зато я теперь в Турции и никаких шарлатанов и прочих козлов... )))</p><p>А в ютубе меня пугали - <noindex><a href="https://youtu.be/Is-9MnS66es" rel="nofollow" target="_blank">https://youtu.be/IS-9MnS66es</a></noindex></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098205" data-level="2" data-parent-id="67093967" data-vote="0" id="comment_67098205">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/tinker007"><span class="">tinker007</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465319026">36 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098205" name="comment_67098205" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Краткий пересказ (СПОЙЛЕР) видео</p><p><br/></p><p><br/></p><p>Далее мать - мать двойни</p><p><br/></p><p>Отец - парень на фото/чувак</p><p><br/></p><p><br/></p><p>Что произошло с чуваком </p><p><br/></p><p>1) ушел в армию</p><p><br/></p><p>2) девушка залетела двойней (говорит что от него)</p><p><br/></p><p>3) пришли на телевидение</p><p><br/></p><p>4) Весь зал поддерживает мать и хуесосит отца</p><p><br/></p><p>5) Вышла его тёща, прописала отцу въёбыч</p><p><br/></p><p>6) Весь зал снова поддерживает мать и хуесосит отца </p><p><br/></p><p>7) Вышел его шурин, прописал отцу въёбыч</p><p><br/></p><p>8) Весь зал снова поддерживает мать и хуесосит отца </p><p><br/></p><p>7) В зале показывают ролик с детьми, описывают детей</p><p><br/></p><p><br/></p><p>"вот пальчики/нос/губы/глаза/*вставь своё* прям как у отца "</p><p><br/></p><p><br/></p><p>8) Весь зал ещё больше поддерживает мать и хуесосит отца </p><p><br/></p><p>9) дети оказались не его!! ВОЗМОЖНО она их нагуляла по пьяне на НГ, предполагаемых отцов 2!!!</p><p><br/></p><p>10) Весь зал снова успокаивает мать и хуесосит отца<br/><br/></p><p><br/></p><p></p><div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465319025139793272.png"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465319025139793272.png" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465319025139793272.png"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67099359" data-level="3" data-parent-id="67098205" data-vote="0" id="comment_67099359">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sent4"><img alt="sent4" src="http://cs6.pikabu.ru/images/avatars/642/s642689-1351481518.jpg"/> <span class="">sent4</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465320215">16 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099359" name="comment_67099359" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Спасибо, добрый человек! Прямо как в зоопарке побывал.</p><p>Мне кажется, что пердачу "Пусть говорят" вполне себе можно заменить на зачитывание Малаховым Ваших текстов.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092746" data-level="9" data-parent-id="67089620" data-vote="0" id="comment_67092746">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kadrabkrab"><span class="">kadrabkrab</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465313253">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092746" name="comment_67092746" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote>В рот я ебла такое общество, которое не любит своих блядей</blockquote>пизданул(а) как Карл Маркс, браво. Дайте еще пару таких же, мне скоро детей воспитывать

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">9</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67093296" data-level="0" data-parent-id="67092746" data-vote="0" id="comment_67093296">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465313845">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093296" name="comment_67093296" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не благодари - <noindex><a href="https://youtu.be/VGYu026kVpo" rel="nofollow" target="_blank">https://youtu.be/VGYu026kVpo</a></noindex></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_expand" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-plus-square"></div>
						<div class="b-comment-toggle__count" style="display: block">раскрыть ветвь <span class="b-comment-toggle__count-text">8</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1 b-comments_new-line" style="display: none">

				<div class="b-comment" data-editable="false" data-id="67095294" data-level="1" data-parent-id="67093296" data-vote="0" id="comment_67095294">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kadrabkrab"><span class="">kadrabkrab</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465315851">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095294" name="comment_67095294" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>оу, телевизор, фу гадость. я смотреть не стану, потому поблагодарю</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">7</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095666" data-level="2" data-parent-id="67095294" data-vote="0" id="comment_67095666">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316270">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095666" name="comment_67095666" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>продал уже?</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-04_1/1459853805140236772.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-04_1/1459853805140236772.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-04_1/1459853805140236772.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096663" data-level="3" data-parent-id="67095666" data-vote="0" id="comment_67096663">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kadrabkrab"><span class="">kadrabkrab</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465317359">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096663" name="comment_67096663" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>фотка зацензурена, вот настоящаяя, и нет, не продается</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465317359115249478.png"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465317359115249478.png" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465317359115249478.png"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67095775" data-level="2" data-parent-id="67095294" data-vote="0" id="comment_67095775">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316396">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095775" name="comment_67095775" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не дрочи!</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-03_1/1456853307120299565.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-03_1/1456853307120299565.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-03_1/1456853307120299565.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096081" data-level="3" data-parent-id="67095775" data-vote="0" id="comment_67096081">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kadrabkrab"><span class="">kadrabkrab</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316721">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096081" name="comment_67096081" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>эээ, почему?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096209" data-level="4" data-parent-id="67096081" data-vote="0" id="comment_67096209">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316860">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096209" name="comment_67096209" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Засосёт, не вырвешься! <noindex><a href="https://youtu.be/LhY3mTFEgn4" rel="nofollow" target="_blank">https://youtu.be/LhY3mTFEgn4</a></noindex></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096844" data-level="5" data-parent-id="67096209" data-vote="0" id="comment_67096844">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kadrabkrab"><span class="">kadrabkrab</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465317577">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096844" name="comment_67096844" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>так тут и на на что, даже хрен знает кто из них двоих менее сексуален</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67099165" data-level="6" data-parent-id="67096844" data-vote="0" id="comment_67099165">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465320027">19 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099165" name="comment_67099165" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>нана что?</p><div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/146532002714962471.jpg"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/146532002714962471.jpg" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/146532002714962471.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_1" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089883" data-level="7" data-parent-id="67086552" data-vote="0" id="comment_67089883">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/VeleS40"><img alt="VeleS40" src="http://cs6.pikabu.ru/images/avatars/771/s771675-1254006626.jpg"/> <span class="">VeleS40</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310443">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089883" name="comment_67089883" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Я так практические задания решаю перед сессией</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67095888" data-level="6" data-parent-id="67086329" data-vote="0" id="comment_67095888">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Takedzo"><span class="">Takedzo</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465316525">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095888" name="comment_67095888" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Друг, я и смотрел длительное время(пол года) Дом 2. Эти программы с такими персонажами дают понять, что ты нормальный) . Но если их долго смотреть ,  , то мозг конечно атрофируется.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094371" data-level="6" data-parent-id="67086329" data-vote="0" id="comment_67094371">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/avsst"><img alt="avsst" src="http://cs6.pikabu.ru/images/avatars/136/s136380.jpg"/> <span class="">avsst</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465314904">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094371" name="comment_67094371" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							А что это такое?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091094" data-level="6" data-parent-id="67086329" data-vote="0" id="comment_67091094">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/leff"><img alt="leff" src="http://cs6.pikabu.ru/images/avatars/58/s58804.jpg"/> <span class="">leff</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465311588">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091094" name="comment_67091094" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Вот ты зря, это же сплошной ЖЫРРР! =)

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098150" data-level="6" data-parent-id="67086329" data-vote="0" id="comment_67098150">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/SteinIsOne"><img alt="SteinIsOne" src="http://cs6.pikabu.ru/images/avatars/622/s622275-12884638.jpg"/> <span class="">SteinIsOne</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465318971">37 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098150" name="comment_67098150" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Почему-бы и нет? неплохое фрик-шоу, я считаю.<br/>раньше ведь были цирки уродов, тут как-бы современная версия. А самый смачный кусок это - Фирамир</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67093043" data-level="5" data-parent-id="67086232" data-vote="0" id="comment_67093043">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/makxseem"><img alt="makxseem" src="http://cs6.pikabu.ru/images/avatars/653/s653423-1753836403.jpg"/> <span class="">makxseem</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313547">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67093043" name="comment_67093043" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465313546184086518.png"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465313546184086518.png" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465313546184086518.png"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088151" data-level="4" data-parent-id="67085669" data-vote="0" id="comment_67088151">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/TeslaDC"><img alt="TeslaDC" src="http://cs6.pikabu.ru/images/avatars/1028/s1028306-286492779.jpg"/> <span class="">TeslaDC</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308859">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088151" name="comment_67088151" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Так он не только не будет платить алименты еще и в суд подать может? А то я бы вообще все забрал бы за такую хуйню. Ролик только двухминтный посмотрел.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088822" data-level="3" data-parent-id="67085222" data-vote="0" id="comment_67088822">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+42</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/zhababa"><span class="">zhababa</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309464">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088822" name="comment_67088822" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465309463147469123.png"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465309463147469123.png" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465309463147469123.png"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67091896" data-level="4" data-parent-id="67088822" data-vote="0" id="comment_67091896">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/punker1984"><span class="">punker1984</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312428">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091896" name="comment_67091896" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>нормальная девка, хоть угорнула над выблядками ебаными :-D<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091650" data-level="4" data-parent-id="67088822" data-vote="0" id="comment_67091650">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Kollektor"><img alt="Kollektor" src="http://cs6.pikabu.ru/images/avatars/1064/s1064653-1786233470.jpg"/> <span class="">Kollektor</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465312190">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091650" name="comment_67091650" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Инга?)

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085562" data-level="2" data-parent-id="67084678" data-vote="0" id="comment_67085562">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+13</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/BonartLeo"><span class="">BonartLeo</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306597">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085562" name="comment_67085562" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ниче-се! А я думал, что такое бывало только в шоу "Двери"!</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">23</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086168" data-level="3" data-parent-id="67085562" data-vote="0" id="comment_67086168">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+57</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307083">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086168" name="comment_67086168" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ностальжи))</p><p><br/></p><p>Я у бабушки жила на квартире, которая всё лето на огороде копалась, да за живностью ухаживала...</p><p>Но ровно в 20.00 (или сколько там было) как штык была у телека)))</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465307083140494347.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465307083140494347.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465307083140494347.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">19</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086350" data-level="4" data-parent-id="67086168" data-vote="0" id="comment_67086350">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+68</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/krottavi"><img alt="krottavi" src="http://cs6.pikabu.ru/images/avatars/742/s742182-1069826467.jpg"/> <span class="">krottavi</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465307236">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086350" name="comment_67086350" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А ещё)<br/></p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465307235170650577.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465307235170650577.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465307235170650577.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">18</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087759" data-level="5" data-parent-id="67086350" data-vote="0" id="comment_67087759">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+28</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/rbhubp"><img alt="rbhubp" src="http://cs6.pikabu.ru/images/avatars/1035/s1035879-772755951.jpg"/> <span class="">rbhubp</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308484">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087759" name="comment_67087759" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465308483167563161.jpg"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465308483167563161.jpg" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465308483167563161.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">10</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088982" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67088982">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/monstara"><span class="">monstara</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309634">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088982" name="comment_67088982" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Годнейшая роль, кстати.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088424" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67088424">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+14</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/SuperBBQ"><img alt="SuperBBQ" src="http://cs6.pikabu.ru/images/avatars/709/s709977-1735017011.jpg"/> <span class="">SuperBBQ</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309114">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088424" name="comment_67088424" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Солид снейк?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088784" data-level="7" data-parent-id="67088424" data-vote="0" id="comment_67088784">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+13</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/HitriyZhuk"><img alt="HitriyZhuk" src="http://cs6.pikabu.ru/images/avatars/147/s147928.jpg?1484845484"/> <span class="">HitriyZhuk</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309427">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088784" name="comment_67088784" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Чистилище</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095900" data-level="8" data-parent-id="67088784" data-vote="0" id="comment_67095900">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Slonoeb"><img alt="Slonoeb" src="http://cs6.pikabu.ru/images/avatars/1191/s1191022-1974172110.jpg"/> <span class="">Slonoeb</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316539">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095900" name="comment_67095900" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Жёсткий фильм, особенно в то время когда он вышел.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092385" data-level="7" data-parent-id="67088424" data-vote="0" id="comment_67092385">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Kymapy"><img alt="Kymapy" src="http://cs6.pikabu.ru/images/avatars/1021/s1021206-1295661902.jpg"/> <span class="">Kymapy</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312934">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092385" name="comment_67092385" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>дмитрид нагейк</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089270" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67089270">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MyDefense"><span class="">MyDefense</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309896">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089270" name="comment_67089270" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Эй, полковник... Сугроб чертов! Че ты молчишь? Че ты ничего доброго в радиоэфир не скажешь? Я волнуюсь о тебе, а ты молчишь. А ты как там, а? Тоже, наверное... скучаешь... полковник... на этой войне. Понимаю... Щас я тебя... повеселю немного. Похохочешь хоть... от души...</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089032" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67089032">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/VodkaAbsolute"><img alt="VodkaAbsolute" src="http://cs6.pikabu.ru/images/avatars/190/s190295.jpg"/> <span class="">VodkaAbsolute</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309676">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089032" name="comment_67089032" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Это Чистилище?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089995" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67089995">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/krottavi"><img alt="krottavi" src="http://cs6.pikabu.ru/images/avatars/742/s742182-1069826467.jpg"/> <span class="">krottavi</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465310557">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089995" name="comment_67089995" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Ой, в этой не помню совсем! Это Чистилище, что ли?<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094157" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67094157">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/YATASUKANAKOMODE"><img alt="YATASUKANAKOMODE" src="http://cs6.pikabu.ru/images/avatars/1115/s1115046-859025616.jpg"/> <span class="">YATASUKANAKOMODE</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465314675">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094157" name="comment_67094157" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Вот эта еще</p><div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/big_size_comm/2016-06_2/1465314675167595405.jpg"><img class="b-image" data-large-image="http://s4.pikabu.ru/images/big_size_comm/2016-06_2/1465314675167595405.jpg" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465314675167595405.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088585" data-level="6" data-parent-id="67087759" data-vote="0" id="comment_67088585">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Fake212"><span class="">Fake212</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309256">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088585" name="comment_67088585" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Похож на алконафтера

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087101" data-level="5" data-parent-id="67086350" data-vote="0" id="comment_67087101">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+8</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/TARSjoker"><img alt="TARSjoker" src="http://cs6.pikabu.ru/images/avatars/810/s810339-1348323543.jpg"/> <span class="">TARSjoker</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307856">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087101" name="comment_67087101" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Да вообще прикольный парень был, нынче только в "Кухне" радует, про остальное заикаться страшно

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">5</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089363" data-level="6" data-parent-id="67087101" data-vote="0" id="comment_67089363">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/InfERnuZzZ"><img alt="InfERnuZzZ" src="http://cs6.pikabu.ru/images/avatars/1296/s1296069-2032379682.jpg"/> <span class="">InfERnuZzZ</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309997">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089363" name="comment_67089363" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							а как же реклама МТС?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089392" data-level="6" data-parent-id="67087101" data-vote="0" id="comment_67089392">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/CerbeRus73"><span class="">CerbeRus73</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465310016">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089392" name="comment_67089392" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Я его в первый раз в Чистилище видел. И моментально он для меня стал отрицательным героем. Ненавидел я его героя и как следствие актер он для меня был всегда плохой, но не как актер, а как персонаж. Много времени прошло, пока я привык к его образу крутого парня. Видимо Чистилище много лет не смотрел. И не буду смотреть еще долго. Такие вещи нужно лишь Иногда просматривать, дабы не забывать об этих граблях на которых мы попрыгали.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090505" data-level="7" data-parent-id="67089392" data-vote="0" id="comment_67090505">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Qthe"><span class="">Qthe</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311033">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090505" name="comment_67090505" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Осторожно модерн посмотри. Нет правда. Посмотри.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67098805" data-level="8" data-parent-id="67090505" data-vote="0" id="comment_67098805">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/CerbeRus73"><span class="">CerbeRus73</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465319621">26 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098805" name="comment_67098805" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Я его смотрел уже после чистилища. И ничего смешного не мог найти, потому что таким отрицательным мне казался Нагиев. Хотя в Чистилище он с Ростом играл (танкист мех.вод)

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091600" data-level="8" data-parent-id="67090505" data-vote="0" id="comment_67091600">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/bor59"><span class="">bor59</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465312133">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091600" name="comment_67091600" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Осторожно модерн 2, если только

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094530" data-level="5" data-parent-id="67086350" data-vote="0" id="comment_67094530">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/avsst"><img alt="avsst" src="http://cs6.pikabu.ru/images/avatars/136/s136380.jpg"/> <span class="">avsst</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315067">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094530" name="comment_67094530" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Это полковник как его?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087035" data-level="3" data-parent-id="67085562" data-vote="0" id="comment_67087035">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/HesusKristo"><img alt="HesusKristo" src="http://cs6.pikabu.ru/images/avatars/749/s749891-1914321586.jpg"/> <span class="">HesusKristo</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307796">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087035" name="comment_67087035" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Окна же были с Нагиевым, нет?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67094584" data-level="4" data-parent-id="67087035" data-vote="0" id="comment_67094584">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/avsst"><img alt="avsst" src="http://cs6.pikabu.ru/images/avatars/136/s136380.jpg"/> <span class="">avsst</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315135">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094584" name="comment_67094584" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Так о том и речь

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086038" data-level="3" data-parent-id="67085562" data-vote="0" id="comment_67086038">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/KirovReporting"><img alt="KirovReporting" src="http://cs6.pikabu.ru/images/avatars/258/s258631-1904322967.jpg"/> <span class="">KirovReporting</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306993">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086038" name="comment_67086038" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А это то же самое, только теперь на государственном канале.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67096160" data-level="2" data-parent-id="67084678" data-vote="0" id="comment_67096160">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/mrbrightside9119"><span class="">mrbrightside9119</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316811">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096160" name="comment_67096160" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>ох и курятник...</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098317" data-level="2" data-parent-id="67084678" data-vote="0" id="comment_67098317">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/neyrosmetana"><img alt="neyrosmetana" src="http://cs6.pikabu.ru/images/avatars/647/s647801-577403555.jpg"/> <span class="">neyrosmetana</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465319137">34 минуты назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098317" name="comment_67098317" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Поржал, смотрю вторую часть)))</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083292" data-level="0" data-parent-id="0" data-vote="0" id="comment_67083292">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+180</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Surovman"><span class="">Surovman</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304803">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083292" name="comment_67083292" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465304803142419116.jpg"><img class="b-image" data-large-image="" data-viewable="true" src="http://cs4.pikabu.ru/images/previews_comm/2016-06_2/1465304803142419116.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090409" data-level="1" data-parent-id="67083292" data-vote="0" id="comment_67090409">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+10</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/zona71"><span class="">zona71</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310930">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090409" name="comment_67090409" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Поэтому он и миллиардер) Он даже мухе не позволит на себя сесть.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67097617" data-level="2" data-parent-id="67090409" data-vote="0" id="comment_67097617">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Motuso"><img alt="Motuso" src="http://cs6.pikabu.ru/images/avatars/977/s977688-1558749014.jpg"/> <span class="">Motuso</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465318417">46 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67097617" name="comment_67097617" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Защитил капитал. Теперь стартап какой-нибудь замутит.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083198" data-level="0" data-parent-id="0" data-vote="0" id="comment_67083198">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+180</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/liska93"><img alt="liska93" src="http://cs6.pikabu.ru/images/avatars/507/s507359-588557755.jpg"/> <span class="">liska93</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465304740">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083198" name="comment_67083198" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А не мог он заведомо заморозить не свой генетический материал, чтобы обломать бывшую с дочерью? Мб задрали при жизни</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">24</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67084362" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67084362">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+54</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Pymbo"><span class="">Pymbo</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465305639">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084362" name="comment_67084362" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Таки да.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085789" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67085789">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+16</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/winterheart"><span class="">winterheart</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306797">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085789" name="comment_67085789" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>В таких случаях берут пробу у живого потомка, результаты которой скажут, является ли владелец исходного материала предком контрольного потомка.<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67091320" data-level="2" data-parent-id="67085789" data-vote="0" id="comment_67091320">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+14</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/karastel"><img alt="karastel" src="http://cs6.pikabu.ru/images/avatars/239/s239732.jpg?2112744691"/> <span class="">karastel</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465311840">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091320" name="comment_67091320" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							А является ли этот потомок в действительности потомком?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67094517" data-level="3" data-parent-id="67091320" data-vote="0" id="comment_67094517">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/KamazDebilov"><img alt="KamazDebilov" src="http://cs6.pikabu.ru/images/avatars/1052/s1052821-562104118.jpg"/> <span class="">KamazDebilov</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315051">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094517" name="comment_67094517" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А если все пробы окажутся разными и при этом ни одна из них не будет принадлежать самому папане? Вот это реаьноая Санта Барбара выйдет. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089577" data-level="2" data-parent-id="67085789" data-vote="0" id="comment_67089577">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/psixoy"><img alt="psixoy" src="http://cs6.pikabu.ru/images/avatars/108/s108501.jpg"/> <span class="">psixoy</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310185">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089577" name="comment_67089577" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Умно.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086416" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67086416">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+19</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/krottavi"><img alt="krottavi" src="http://cs6.pikabu.ru/images/avatars/742/s742182-1069826467.jpg"/> <span class="">krottavi</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465307305">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086416" name="comment_67086416" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Теоретически мог, но может это был какой-то нотариально заверенный забор материала.. Прям представляю эту коллегию, наблюдающую, как он потеет над журнальчиком)<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">13</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086952" data-level="2" data-parent-id="67086416" data-vote="0" id="comment_67086952">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+59</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/compwork"><img alt="compwork" src="http://cs6.pikabu.ru/images/avatars/624/s624954-2114380566.jpg"/> <span class="">compwork</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307726">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086952" name="comment_67086952" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							для теста днк не обязательно потеть над журнальчиком.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087782" data-level="3" data-parent-id="67086952" data-vote="0" id="comment_67087782">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+13</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Electroshock"><img alt="Electroshock" src="http://cs6.pikabu.ru/images/avatars/368/s368390.jpg?766178445"/> <span class="">Electroshock</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308497">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087782" name="comment_67087782" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>"Через сорок лет после смерти Дэниела" ©</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088504" data-level="4" data-parent-id="67087782" data-vote="0" id="comment_67088504">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+20</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Red.Tomato"><img alt="Red.Tomato" src="http://cs6.pikabu.ru/images/avatars/700/s700271-644390045.jpg"/> <span class="">Red.Tomato</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465309190">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088504" name="comment_67088504" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>"для теста днк не обязательно потеть над журнальчиком" ©</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088912" data-level="5" data-parent-id="67088504" data-vote="0" id="comment_67088912">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/playermet"><img alt="playermet" src="http://cs6.pikabu.ru/images/avatars/421/s421478.jpg?654659538"/> <span class="">playermet</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465309549">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088912" name="comment_67088912" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Томат дело говорит!

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67098804" data-level="5" data-parent-id="67088504" data-vote="0" id="comment_67098804">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/rockbear"><span class="">rockbear</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465319620">26 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098804" name="comment_67098804" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>а если очень хочется ?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67099338" data-level="6" data-parent-id="67098804" data-vote="0" id="comment_67099338">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Red.Tomato"><img alt="Red.Tomato" src="http://cs6.pikabu.ru/images/avatars/700/s700271-644390045.jpg"/> <span class="">Red.Tomato</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465320194">17 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099338" name="comment_67099338" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не обязательно не значит запрещено. Вперед на добычу генетического материала!</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67094697" data-level="3" data-parent-id="67086952" data-vote="0" id="comment_67094697">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/KamazDebilov"><img alt="KamazDebilov" src="http://cs6.pikabu.ru/images/avatars/1052/s1052821-562104118.jpg"/> <span class="">KamazDebilov</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465315243">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67094697" name="comment_67094697" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Но и не запрещено!<br/></p><div class="b-p b-p_type_image">
						<div class="b-gifx b-gifx_state_new" data-height="258" data-size-gif="6647" data-size-mp4="769" data-size-webm="670" data-size-webp="2718" data-type="comment" data-width="460">
							<div class="b-gifx__state b-gifx__state_loading_yes"><i class="fa fa-circle-o-notch fa-spin"></i></div>
							<div class="b-gifx__state b-gifx__state_waiting_yes" style="visibility: hidden;"><i class="fa fa-play"></i><span class="b-gifx__size">10 Мб</span></div>
							<a class="b-gifx__state b-gifx__state_playing_yes b-gifx__save" href="http://cs5.pikabu.ru/images/big_size_comm_an/2015-10_5/1445780727114530259.gif" style="visibility: hidden;" target="_blank"><i class="fa fa-download"></i></a>
							<div class="b-gifx__preview b-gifx__preview_width_150 b-gifx__preview_show_yes">
								<img class="b-gifx__image" src="http://cs5.pikabu.ru/images/previews_gif_comm/2015-10_5/1445780727114530259.gif"/>
							</div>
							<div class="b-gifx__player" data-height="258" data-size-gif="6647" data-size-mp4="769" data-size-webm="670" data-size-webp="2718" data-src="http://cs5.pikabu.ru/images/big_size_comm_an/2015-10_5/1445780727114530259.gif" data-width="460"></div>
						</div>
					</div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67090571" data-level="2" data-parent-id="67086416" data-vote="0" id="comment_67090571">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+14</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Oforfs"><img alt="Oforfs" src="http://cs6.pikabu.ru/images/avatars/116/s116781.jpg"/> <span class="">Oforfs</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311102">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090571" name="comment_67090571" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Кровь, он сдал на заморозку кровь.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087893" data-level="2" data-parent-id="67086416" data-vote="0" id="comment_67087893">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+15</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ExTempore"><img alt="ExTempore" src="http://cs6.pikabu.ru/images/avatars/4/s4853.jpg"/> <span class="">ExTempore</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308602">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087893" name="comment_67087893" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote>как он потеет над журнальчиком</blockquote><p>Причём здесь маструбация вообще?<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089961" data-level="3" data-parent-id="67087893" data-vote="0" id="comment_67089961">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/krottavi"><img alt="krottavi" src="http://cs6.pikabu.ru/images/avatars/742/s742182-1069826467.jpg"/> <span class="">krottavi</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465310525">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089961" name="comment_67089961" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А какой именно материал забирали? Слюну, что ли? Я уж думала, по старинке..<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092954" data-level="4" data-parent-id="67089961" data-vote="0" id="comment_67092954">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+11</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ExTempore"><img alt="ExTempore" src="http://cs6.pikabu.ru/images/avatars/4/s4853.jpg"/> <span class="">ExTempore</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313449">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092954" name="comment_67092954" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Да что ты о жидкостях только! Может просто ногу отрезали.<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092938" data-level="4" data-parent-id="67089961" data-vote="0" id="comment_67092938">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Dobriyelf"><span class="">Dobriyelf</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465313430">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092938" name="comment_67092938" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Кусок руки, к примеру. Любая часть тела, в том числе и кровь.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091787" data-level="2" data-parent-id="67086416" data-vote="0" id="comment_67091787">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ToksHolmes"><img alt="ToksHolmes" src="http://cs6.pikabu.ru/images/avatars/296/s296599-627628909.jpg"/> <span class="">ToksHolmes</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465312318">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091787" name="comment_67091787" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>&gt;миллиардер</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091036" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67091036">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/kot3gg"><img alt="kot3gg" src="http://cs6.pikabu.ru/images/avatars/745/s745401-1555615716.jpg"/> <span class="">kot3gg</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311534">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091036" name="comment_67091036" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А ведь могло случиться и так, что он взял генетический материал у друга/соседа/коллеги и потом БАЦ, по результатам анализов дочь настоящая.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086851" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67086851">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Avir"><img alt="Avir" src="http://cs6.pikabu.ru/images/avatars/619/s619717-2000732602.jpg"/> <span class="">Avir</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307652">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086851" name="comment_67086851" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>мог другой член семьи, претендующий на миллиарды Дэни поделиться парой миллиончиков с теми, кто проводил анализ ДНК</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092063" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67092063">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/HobbitSam"><img alt="HobbitSam" src="http://cs6.pikabu.ru/images/avatars/837/s837284-2130070241.jpg"/> <span class="">HobbitSam</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312603">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092063" name="comment_67092063" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							в присутствии нотариуса сдавал))

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089442" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67089442">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/InfERnuZzZ"><img alt="InfERnuZzZ" src="http://cs6.pikabu.ru/images/avatars/1296/s1296069-2032379682.jpg"/> <span class="">InfERnuZzZ</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310063">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089442" name="comment_67089442" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							теперт найдут настоящего наследника и все ему отдадут

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084882" data-level="1" data-parent-id="67083198" data-vote="0" id="comment_67084882">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-9</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/sinyoritta"><span class="">sinyoritta</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306045">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084882" name="comment_67084882" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							<div class="b-p b-p_type_image">
						<div class="b-gifx b-gifx_state_new" data-height="263" data-size-gif="2484" data-size-mp4="88" data-size-webm="550" data-size-webp="413" data-type="comment" data-width="350">
							<div class="b-gifx__state b-gifx__state_loading_yes"><i class="fa fa-circle-o-notch fa-spin"></i></div>
							<div class="b-gifx__state b-gifx__state_waiting_yes" style="visibility: hidden;"><i class="fa fa-play"></i><span class="b-gifx__size">10 Мб</span></div>
							<a class="b-gifx__state b-gifx__state_playing_yes b-gifx__save" href="http://cs8.pikabu.ru/images/big_size_comm_an/2016-03_3/1457790465152138900.gif" style="visibility: hidden;" target="_blank"><i class="fa fa-download"></i></a>
							<div class="b-gifx__preview b-gifx__preview_width_150 b-gifx__preview_show_yes">
								<img class="b-gifx__image" src="http://cs8.pikabu.ru/images/previews_gif_comm/2016-03_3/1457790465152138900.gif"/>
							</div>
							<div class="b-gifx__player" data-height="263" data-size-gif="2484" data-size-mp4="88" data-size-webm="550" data-size-webp="413" data-src="http://cs8.pikabu.ru/images/big_size_comm_an/2016-03_3/1457790465152138900.gif" data-width="350"></div>
						</div>
					</div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084885" data-level="0" data-parent-id="0" data-vote="0" id="comment_67084885">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+50</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465306046">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084885" name="comment_67084885" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Мне, как профану в юриспруденции, стало интересно вот что. Если он значился в документах как ее отец (т.е. не отказался сразу по результатам теста, допустим), то играет ли роль тут анализ ДНК? Ведь таким образом можно лишать наследства приемных детей, а судя куче недавних историй, некоторые родственнички и родным готовы поднасрать, не то что усыновленным. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">13</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085297" data-level="1" data-parent-id="67084885" data-vote="0" id="comment_67085297">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+34</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DzirtDoYein"><img alt="DzirtDoYein" src="http://cs6.pikabu.ru/images/avatars/150/s150134.jpg"/> <span class="">DzirtDoYein</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306401">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085297" name="comment_67085297" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Имеется в виду как я понимаю тот факт, что она пыталась отсудить что-то у тех людей, которым по завещанию досталось  какое-то имущество. <br/>И  давила на то, что она, как наследник, имеет больше прав.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">11</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085759" data-level="2" data-parent-id="67085297" data-vote="0" id="comment_67085759">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+26</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465306773">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085759" name="comment_67085759" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Собственно, как "официальная" дочь она и имеет больше прав. На самом деле, мне это видится довольно запутанным случаем, особенно потому что в Штатах прецедентное право, и после такого решения суда все усыновленные могут довольствоваться пинком под зад вместо наследства. Ну или просто в посте опустили всю скучную часть )))</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">9</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086769" data-level="3" data-parent-id="67085759" data-vote="0" id="comment_67086769">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+38</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465307582">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086769" name="comment_67086769" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>В общем, он сам в течение жизни не признавал её своей дочерью, и на момент её рождения Дэниел уже не жил вместе с женой (развелись они, правда, чуть позже), вполне вероятно, что и в документах он тоже не фигурирует как отец. Дело закрыто! :)</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465307582124561033.jpg"><img class="b-image" data-large-image="" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465307582124561033.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086495" data-level="3" data-parent-id="67085759" data-vote="0" id="comment_67086495">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+9</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/bond43"><img alt="bond43" src="http://cs6.pikabu.ru/images/avatars/1292/s1292694-1624291590.jpg"/> <span class="">bond43</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307365">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086495" name="comment_67086495" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote>Ну или просто в посте опустили всю скучную часть )))</blockquote><p>Зришь в корень.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087385" data-level="3" data-parent-id="67085759" data-vote="0" id="comment_67087385">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ashen"><span class="">ashen</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465308131">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087385" name="comment_67087385" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							В оригинале говорится "challenge his will", то есть было составлено завещание. Дочь попыталась через суд получить то, что по завещанию отошло другому. По идее, у нее не должно быть больше прав в этом плане. Плюс, ситуация не идентичная с усыновленными детьми, вряд ли можно использовать в качестве прецедента.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087717" data-level="4" data-parent-id="67087385" data-vote="0" id="comment_67087717">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465308450">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087717" name="comment_67087717" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не знаю, как в Америке, а в России дети могут оспорить завещание, если оно прямо ущемляет их интересы. Т.е. что бы там кто не назавещал, у некоторых категорий наследников есть право оспорить в свою пользу. Типа если между двумя наследниками первого порядка завещание составлено так, что все остается только одному, то второй идет в суд и преспокойно получает свою половину</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">5</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088539" data-level="5" data-parent-id="67087717" data-vote="0" id="comment_67088539">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/BuHoGPaD"><img alt="BuHoGPaD" src="http://cs6.pikabu.ru/images/avatars/89/s89879.jpg"/> <span class="">BuHoGPaD</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465309214">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088539" name="comment_67088539" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А если я скажем завещаю все свое имущество благотворительному фонду, вот абсолютно всё. Ни копейки не оставив ни единому человеку - даже в этом случае могут оспорить?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67089662" data-level="6" data-parent-id="67088539" data-vote="0" id="comment_67089662">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465310268">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089662" name="comment_67089662" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Насколько я понимаю - да. Правда, сейчас мне уже кажется, что в моем примере не очень корректный вывод - оспоривший получит не половину, а четверть. Это т.н. обязательная доля, т.е. доля, которая отходила бы наследнику при отсутствии завещания. Собственно, я, как уже говорилось, не знаток, просто хватаю что на глаза попадется - там почитал, тут почитал - и оп, уже диванный эксперт :) Ну и мое мнение - нет ничего лучше дарения, тут гарантированно достается тому, кому подарил, и никто уже ничего не сделает. Вот хороший пост на эту тему <noindex><a href="http://pikabu.ru/story/_3764322" rel="nofollow" target="_blank">http://pikabu.ru/story/_3764322</a></noindex></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67089126" data-level="6" data-parent-id="67088539" data-vote="0" id="comment_67089126">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/playermet"><img alt="playermet" src="http://cs6.pikabu.ru/images/avatars/421/s421478.jpg?654659538"/> <span class="">playermet</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465309766">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67089126" name="comment_67089126" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Я знаю верный неоспариваемый способ. Завещай все какому нибудь чиновнику/судье/прокурору.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67090490" data-level="6" data-parent-id="67088539" data-vote="0" id="comment_67090490">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465311015">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090490" name="comment_67090490" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>У меня уже голова кипит, чем больше я читаю, тем сложнее становится, и тем больше понятно, что фигню я какую-то про доли пишу. Можно попытать счастья и позвать <noindex><a href="http://pikabu.ru/profile/IzyaLokin" rel="nofollow" target="_blank">@IzyaLokin</a></noindex> из упомянутого выше поста, вдруг он здесь и всё-всё нам объяснит :)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67099300" data-level="5" data-parent-id="67087717" data-vote="0" id="comment_67099300">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/fdhg"><span class="">fdhg</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465320156">17 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099300" name="comment_67099300" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Оспорить-то могут, но вероятность выиграть дело просто мизерная, тем более - если завещатель не состоял на учете в дурке\наркологии и т.д. Так что в описанном вами случае 2 наследник почти гаратнтированно получит известным местом по губам. В то же время, обязательная доля в завещании положена несовершеннолетним либо недееспособным детям, нетрудоспособным родителям, супругу или любому иждивенцу наследодателя.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085426" data-level="2" data-parent-id="67085297" data-vote="0" id="comment_67085426">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306496">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085426" name="comment_67085426" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>да да, именно так! </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085670" data-level="1" data-parent-id="67084885" data-vote="0" id="comment_67085670">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Atlash"><span class="">Atlash</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306694">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085670" name="comment_67085670" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							думаю,тут ещё роль играет в каком государстве происходит это, наверняка не во всех странах единый закон о наследстве

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083910" data-level="0" data-parent-id="0" data-vote="0" id="comment_67083910">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+26</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/George58"><img alt="George58" src="http://cs6.pikabu.ru/images/avatars/950/s950855-584368732.jpg"/> <span class="">George58</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465305295">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083910" name="comment_67083910" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Неудивительно, что при такой дальновидности он сколотил себе приличное состояние.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083389" data-level="0" data-parent-id="0" data-vote="0" id="comment_67083389">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/oplkill"><img alt="oplkill" src="http://cs6.pikabu.ru/images/avatars/940/s940804-451306337.jpg"/> <span class="">oplkill</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304876">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083389" name="comment_67083389" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							40 лет? Разве не через несколько лет если наследники не объявятся, то все уходит госу

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">15</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67083645" data-level="1" data-parent-id="67083389" data-vote="0" id="comment_67083645">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+31</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465305085">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083645" name="comment_67083645" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Я думаю что наследников хватает просто она решила отсудить через 40 лет в надежде что он уже давно превратился в прах а вскрывать могилу и проводить анализ ДНК не станут</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">13</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088050" data-level="2" data-parent-id="67083645" data-vote="0" id="comment_67088050">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+11</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/elenhil"><span class="">elenhil</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465308757">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088050" name="comment_67088050" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>просто кто-то не умеет в английский</p><p>он умер через 40 лет, а  не через 40 лет после его смерти полезли проверять<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090531" data-level="3" data-parent-id="67088050" data-vote="0" id="comment_67090531">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Oforfs"><img alt="Oforfs" src="http://cs6.pikabu.ru/images/avatars/116/s116781.jpg"/> <span class="">Oforfs</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311056">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090531" name="comment_67090531" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Я в целом с вами согласен конечно, но меня самого смутила формулировка "prior to passing away" Она, всеже, в первую очередь наводит на мысль что сделано это было непосредставенно перед кончиной, хоть и буквально на это не указывает. Хотя позже в этом тексте речевой оборот наводит на то что смерть так же случилась много позже чем забор ген. материалов :)</p><p><br/></p><p>А вообще текст взятый в посте очень плох на определене времени. Фигурирует цифра в 40 лет, непонятно откуда взятая. Этот мужчина в 70х сдал кровь на сохранение, скончался в 92м, и в 90ых же "дочка" дочка пыталась подрезать имение, тут ~20-25 лет промежуток, никак не 40.</p><p><br/></p><p>Ваш англоговорящий пикабущникъ.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084155" data-level="2" data-parent-id="67083645" data-vote="0" id="comment_67084155">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LoBBeast"><span class="">LoBBeast</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465305472">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084155" name="comment_67084155" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не в этом дело. Просто существует срок вступления в наследство. Например, у нас, если не ошибаюсь, три года. Если ты в течение трех лет не заявил себя наследником, то потом уже не можешь ни на что претендовать. Как-то так.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">9</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085566" data-level="3" data-parent-id="67084155" data-vote="0" id="comment_67085566">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Gnevrin"><img alt="Gnevrin" src="http://cs6.pikabu.ru/images/avatars/314/s314838-39185019.jpg"/> <span class="">Gnevrin</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306606">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085566" name="comment_67085566" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Подозреваю, что американские адвокаты давно уже пролоббировали возможность начинать дела по любому поводу )) - Лишь бы клиент платил. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086031" data-level="4" data-parent-id="67085566" data-vote="0" id="comment_67086031">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LoBBeast"><span class="">LoBBeast</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306990">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086031" name="comment_67086031" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не знаю, может появится знаток американского права и прокомментирует. Но мне наш закон кажется вполне здравым.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085004" data-level="3" data-parent-id="67084155" data-vote="0" id="comment_67085004">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LoBBeast"><span class="">LoBBeast</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306153">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085004" name="comment_67085004" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Сомнение меня взяло, погуглил чуток. Похоже не три года, а всего лишь 6 месяцев.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">6</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086172" data-level="4" data-parent-id="67085004" data-vote="0" id="comment_67086172">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/rommini"><img alt="rommini" src="http://cs6.pikabu.ru/images/avatars/605/s605765.jpg?2037691146"/> <span class="">rommini</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465307086">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086172" name="comment_67086172" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Есть понятие "вновь открывшиеся обстоятельства". У меня соседка вступила в наследство через 5 лет после смерти родственников.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">5</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086484" data-level="5" data-parent-id="67086172" data-vote="0" id="comment_67086484">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LoBBeast"><span class="">LoBBeast</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307359">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086484" name="comment_67086484" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Интересно. А что может быть такими обстоятельствами?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086864" data-level="6" data-parent-id="67086484" data-vote="0" id="comment_67086864">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/rommini"><img alt="rommini" src="http://cs6.pikabu.ru/images/avatars/605/s605765.jpg?2037691146"/> <span class="">rommini</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465307659">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086864" name="comment_67086864" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							У нее были братья, у братьев была комната в коммуналке. Братьев убили (подробностей не знаю), то, что есть еще сестра, никто не знал. Сама она тоже не знала, что с ними, живы или нет.  Комната каким-то образом продалась-перепродалась несколько раз. Сестра, т.е. соседка, узнала о смерти братьев, узнала, что комнату кто-то прихапал, пошла в суд, отменила все продажи и перепродажи и вступила в наследство, как единственный наследник. Конец.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087070" data-level="7" data-parent-id="67086864" data-vote="0" id="comment_67087070">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LoBBeast"><span class="">LoBBeast</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307822">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087070" name="comment_67087070" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Офигеть. Вот так живешь себе. А кто-то придет и скажет, что хата его.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087513" data-level="7" data-parent-id="67086864" data-vote="0" id="comment_67087513">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/strelokhalfer"><span class="">strelokhalfer</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308251">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087513" name="comment_67087513" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Если квартира перепродалась, то её уже нельзя вернуть, на сколько я помню

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67087882" data-level="8" data-parent-id="67087513" data-vote="0" id="comment_67087882">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/rommini"><img alt="rommini" src="http://cs6.pikabu.ru/images/avatars/605/s605765.jpg?2037691146"/> <span class="">rommini</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465308594">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087882" name="comment_67087882" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Может быть. Но соседка смогла, и именно "по вновь открывшимся обстоятельствам", я у нее специально спрашивала, как так, столько времени прошло.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67090866" data-level="2" data-parent-id="67083645" data-vote="0" id="comment_67090866">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Oforfs"><img alt="Oforfs" src="http://cs6.pikabu.ru/images/avatars/116/s116781.jpg"/> <span class="">Oforfs</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311375">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090866" name="comment_67090866" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Он заморозил кровь в 70х годах, скончался в 92м, и в 90ых же после его смерти "дочка пыталась подрезать имение. Алсо, вообще не понятно откуда взялась цифра в 40 лет в тексте который вы использовали.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085141" data-level="1" data-parent-id="67083389" data-vote="0" id="comment_67085141">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465306253">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085141" name="comment_67085141" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>В википедии сказано, что он сам образец заморозил в 70х, а родство проверяли уже в после его смерти в 1992</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087919" data-level="0" data-parent-id="0" data-vote="0" id="comment_67087919">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/1pauc1"><span class="">1pauc1</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308628">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087919" name="comment_67087919" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Как вариант: он мог вообще чужой генетический материал оставить заместо своего, если не любил бывшую и дочь</p><div class="b-p b-p_type_image"><a href="http://cs5.pikabu.ru/images/big_size_comm/2015-10_2/1444415478151165141.jpg"><img class="b-image" data-large-image="http://s5.pikabu.ru/images/big_size_comm/2015-10_2/1444415478151165141.jpg" data-viewable="true" src="http://cs5.pikabu.ru/images/previews_comm/2015-10_2/1444415478151165141.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082287" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082287">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+12</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/boris22"><img alt="boris22" src="http://cs6.pikabu.ru/images/avatars/265/s265799-201176619.jpg"/> <span class="">boris22</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304023">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082287" name="comment_67082287" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>прохаваный дедан! хуй те доченька</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67083006" data-level="1" data-parent-id="67082287" data-vote="0" id="comment_67083006">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+18</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/VinniThePuh"><img alt="VinniThePuh" src="http://cs6.pikabu.ru/images/avatars/235/s235577.jpg"/> <span class="">VinniThePuh</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304592">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083006" name="comment_67083006" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>вот хер с маслом как раз таки и НЕдоченьке)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084967" data-level="0" data-parent-id="0" data-vote="0" id="comment_67084967">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Puni"><span class="">Puni</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306115">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084967" name="comment_67084967" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Разве он просто не мог указать в завещании пункт о том, чтоб эта "дочь" не могла претендовать?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085233" data-level="1" data-parent-id="67084967" data-vote="0" id="comment_67085233">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465306336">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085233" name="comment_67085233" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Где-то натыкалась на то, что наследники первого порядка - дети, родители, супруги - могут оспаривать завещание в свою пользу</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082619" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082619">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Highvoltage380"><img alt="Highvoltage380" src="http://cs6.pikabu.ru/images/avatars/664/s664806-220822002.jpg"/> <span class="">Highvoltage380</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304281">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082619" name="comment_67082619" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<span style="color: #888888;">Комментарий удален. Причина: комментарий содержит непотребный контент.</span>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">8</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67085376" data-level="1" data-parent-id="67082619" data-vote="0" id="comment_67085376">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-18</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/marelbul"><span class="">marelbul</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306462">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085376" name="comment_67085376" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							<noindex><a href="http://pikabu.ru/profile/moderator" rel="nofollow" target="_blank">@moderator</a></noindex> жесть

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">7</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086544" data-level="2" data-parent-id="67085376" data-vote="0" id="comment_67086544">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+15</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/DeilaWa"><img alt="DeilaWa" src="http://cs6.pikabu.ru/images/avatars/672/s672754-2000889236.jpg"/> <span class="">DeilaWa</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307411">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086544" name="comment_67086544" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>скатина! я жесть не посмотрел!</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087801" data-level="2" data-parent-id="67085376" data-vote="0" id="comment_67087801">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/JackPsyX"><img alt="JackPsyX" src="http://cs6.pikabu.ru/images/avatars/109/s109812.jpg"/> <span class="">JackPsyX</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308509">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087801" name="comment_67087801" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Рассказывай теперь, что там было.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090208" data-level="3" data-parent-id="67087801" data-vote="0" id="comment_67090208">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Ardius"><span class="">Ardius</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310742">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090208" name="comment_67090208" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Предположу что там было выражение лица "дочери", когда ей сообщили о результатах анализа.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085839" data-level="2" data-parent-id="67085376" data-vote="0" id="comment_67085839">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/TrueFighter"><span class="">TrueFighter</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465306842">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085839" name="comment_67085839" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Где жесть?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67086396" data-level="3" data-parent-id="67085839" data-vote="0" id="comment_67086396">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+12</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/bond43"><img alt="bond43" src="http://cs6.pikabu.ru/images/avatars/1292/s1292694-1624291590.jpg"/> <span class="">bond43</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307291">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086396" name="comment_67086396" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Здесь.<br/></p><p><br/></p><p></p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/previews_comm/2016-03_3/1457685629198657251.jpg"><img class="b-image" data-large-image="" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-03_3/1457685629198657251.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67090384" data-level="4" data-parent-id="67086396" data-vote="0" id="comment_67090384">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/NeverAgain"><img alt="NeverAgain" src="http://cs6.pikabu.ru/images/avatars/232/s232842-813329878.jpg"/> <span class="">NeverAgain</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465310905">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090384" name="comment_67090384" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Не факт. Может это всего лишь рулон металлизированного скотча. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67092022" data-level="5" data-parent-id="67090384" data-vote="0" id="comment_67092022">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/bond43"><img alt="bond43" src="http://cs6.pikabu.ru/images/avatars/1292/s1292694-1624291590.jpg"/> <span class="">bond43</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312560">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092022" name="comment_67092022" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Скотч, так скотч.<br/></p><p><br/></p><p></p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465312559177825662.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465312559177825662.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465312559177825662.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67090951" data-level="0" data-parent-id="0" data-vote="0" id="comment_67090951">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Azcinor"><img alt="Azcinor" src="http://cs6.pikabu.ru/images/avatars/437/s437121-335527721.jpg"/> <span class="">Azcinor</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465311458">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67090951" name="comment_67090951" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Заебись перевод с искажением смысла. Не через 40 лет после его смерти, а через 40 лет после заморозки, когда он умер.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67091341" data-level="1" data-parent-id="67090951" data-vote="0" id="comment_67091341">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Oforfs"><img alt="Oforfs" src="http://cs6.pikabu.ru/images/avatars/116/s116781.jpg"/> <span class="">Oforfs</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465311867">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091341" name="comment_67091341" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Если что текст взятый в посте весьма крив на определения в целом, "prior to passing away" действительно сбивает с толку наводя на мысль что кровь сдана на заморозку "перед" смертью в 70х. Алсо, 40 лет вообще неясно от куда взятая цифра, в 70х сдал кровь, в 92м умер, следом в 90ых же "дочка" пыталась подрезать имущество. А там 40 годами в промежутке и не пахнет.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67085710" data-level="0" data-parent-id="0" data-vote="0" id="comment_67085710">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/UncleYosya"><span class="">UncleYosya</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306739">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67085710" name="comment_67085710" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Поэтому и богатый

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67095172" data-level="0" data-parent-id="0" data-vote="0" id="comment_67095172">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Ubertin"><img alt="Ubertin" src="http://cs6.pikabu.ru/images/avatars/914/s914877-598201491.jpg"/> <span class="">Ubertin</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465315739">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095172" name="comment_67095172" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/1465315738191967407.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/1465315738191967407.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/1465315738191967407.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67095580" data-level="0" data-parent-id="0" data-vote="0" id="comment_67095580">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/FormatGvm"><span class="">FormatGvm</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316157">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095580" name="comment_67095580" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Многоходовочка однако)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086050" data-level="0" data-parent-id="0" data-vote="0" id="comment_67086050">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/TackleTart"><img alt="TackleTart" src="http://cs6.pikabu.ru/images/avatars/1236/s1236832-1381398200.jpg"/> <span class="">TackleTart</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465307006">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086050" name="comment_67086050" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>might challenge his will = может оспорить его завещание</p><p>sue the estate = судиться за наследство<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67099155" data-level="0" data-parent-id="0" data-vote="0" id="comment_67099155">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/GolubDerzki"><span class="">GolubDerzki</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465320021">20 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099155" name="comment_67099155" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>в этом не было необходимости тащем-то</p><p>тело можно эксгумировать и также сделать анализ днк ;)</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67099838" data-level="0" data-parent-id="0" data-vote="0" id="comment_67099838">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Alexsan1k"><span class="">Alexsan1k</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465320756">7 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099838" name="comment_67099838" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Скорее всего он знал что жена ему изменяла

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082293" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082293">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ceotcndj2015"><span class="">ceotcndj2015</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304027">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082293" name="comment_67082293" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>а у кого она пыталась отсудить?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">3</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67082398" data-level="1" data-parent-id="67082293" data-vote="0" id="comment_67082398">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+9</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304115">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082398" name="comment_67082398" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>видимо у его родственников, коих я думаю находится немало ))) </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083352" data-level="1" data-parent-id="67082293" data-vote="0" id="comment_67083352">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+4</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/BlueZ"><img alt="BlueZ" src="http://cs6.pikabu.ru/images/avatars/210/s210119-1626631135.jpg"/> <span class="">BlueZ</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304845">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083352" name="comment_67083352" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Там говорится, что была бывшая жена, а не вдова. Так что вероятно была и новая. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67084953" data-level="2" data-parent-id="67083352" data-vote="0" id="comment_67084953">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Tak.04"><span class="">Tak.04</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465306106">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084953" name="comment_67084953" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>А вдова разве не когда муж помер пока семья целой была? Не может ведь жена лишиться мужа, если они и так разведены)<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67099670" data-level="0" data-parent-id="0" data-vote="0" id="comment_67099670">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/stepandko"><span class="">stepandko</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465320554">11 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67099670" name="comment_67099670" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Тот кто делал экспертизу и наварился.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092818" data-level="0" data-parent-id="0" data-vote="0" id="comment_67092818">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Edblin"><img alt="Edblin" src="http://cs6.pikabu.ru/images/avatars/1000/s1000862-102223391.jpg"/> <span class="">Edblin</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465313314">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092818" name="comment_67092818" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Шах и мат. Шлюха.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67092508" data-level="0" data-parent-id="0" data-vote="0" id="comment_67092508">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LeVatnique"><span class="">LeVatnique</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465313047">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67092508" name="comment_67092508" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Он умер в 1992 году, 40 лет с его смерти будет только в 2032 году. </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087920" data-level="0" data-parent-id="0" data-vote="0" id="comment_67087920">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MrLightningRod"><img alt="MrLightningRod" src="http://cs6.pikabu.ru/images/avatars/813/s813858-1285150739.jpg"/> <span class="">MrLightningRod</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308629">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087920" name="comment_67087920" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Я вот думаю наперед, поэтому уже сейчас во время сессии поставил на загрузку Ведьмака 3, чтобы после сдачи последнего экзамена сразу сесть в него играть.<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67088145" data-level="1" data-parent-id="67087920" data-vote="0" id="comment_67088145">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/LyInJuly"><img alt="LyInJuly" src="http://cs6.pikabu.ru/images/avatars/379/s379217-1222562478.jpg"/> <span class="">LyInJuly</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465308854">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088145" name="comment_67088145" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<blockquote><i>после сдачи последнего экзамена</i></blockquote><p>Так мы тебе и поверили! Ну как, шевелится Плотва уже?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67098680" data-level="2" data-parent-id="67088145" data-vote="0" id="comment_67098680">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария"><i class="i-sprite--comments__rating-lock i-sprite--inline-block" title="Рейтинг скрыт в течение 45 минут после добавления комментария"></i></div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/MrLightningRod"><img alt="MrLightningRod" src="http://cs6.pikabu.ru/images/avatars/813/s813858-1285150739.jpg"/> <span class="">MrLightningRod</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465319506">28 минут назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67098680" name="comment_67098680" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>С общажным интернетом ведьмак докачается аккурат к последнему к экзамену. Может быть докачается.<br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67091901" data-level="0" data-parent-id="0" data-vote="0" id="comment_67091901">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Yakynchenkov"><span class="">Yakynchenkov</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312431">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091901" name="comment_67091901" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Он просто был из тех кто вовремя высовывает. <br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67088517" data-level="0" data-parent-id="0" data-vote="0" id="comment_67088517">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Soarelescu"><img alt="Soarelescu" src="http://cs6.pikabu.ru/images/avatars/1260/s1260652-2088989801.jpg"/> <span class="">Soarelescu</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465309203">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67088517" name="comment_67088517" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							А как его генетический материал помешал бы ей оспорить завещание?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67091508" data-level="1" data-parent-id="67088517" data-vote="0" id="comment_67091508">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Oforfs"><img alt="Oforfs" src="http://cs6.pikabu.ru/images/avatars/116/s116781.jpg"/> <span class="">Oforfs</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465312040">2 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67091508" name="comment_67091508" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Нуэ, родная дочь претендует на долю в наследстве. Не родная не претендует. Он её не знал никогда, и как свою не признавал считая что не от него. Вот и замесил бэкап днк на всякий случай. Алсо, забавно учитывать что "дочери" было уже 56+ лет после его смерти.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086622" data-level="0" data-parent-id="0" data-vote="0" id="comment_67086622">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ultranagibator"><img alt="ultranagibator" src="http://cs6.pikabu.ru/images/avatars/998/s998342-1876427280.jpg"/> <span class="">ultranagibator</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307471">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086622" name="comment_67086622" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Он не свой оставил:)

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082739" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082739">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/qqqGhOsTppp"><span class="">qqqGhOsTppp</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304370">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082739" name="comment_67082739" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p><noindex><a href="https://www.youtube.com/watch?v=TYEvJonTEbs" rel="nofollow" target="_blank">https://www.youtube.com/watch?v=TYEvJonTEbs</a></noindex><br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67083251" data-level="1" data-parent-id="67082739" data-vote="0" id="comment_67083251">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304776">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083251" name="comment_67083251" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Спасибо, вы правы. проверочное имя Кит Ричардс ))) </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087535" data-level="0" data-parent-id="0" data-vote="0" id="comment_67087535">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-3</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/avsst"><img alt="avsst" src="http://cs6.pikabu.ru/images/avatars/136/s136380.jpg"/> <span class="">avsst</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465308266">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087535" name="comment_67087535" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							ΛαΛ.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082513" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082513">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-6</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/dimoheha"><img alt="dimoheha" src="http://cs6.pikabu.ru/images/avatars/242/s242691.jpg"/> <span class="">dimoheha</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304213">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082513" name="comment_67082513" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							<p>Рогатый олень-миллиардер)) <br/></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082040" data-level="0" data-parent-id="0" data-vote="0" id="comment_67082040">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-8</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Ltsmb"><span class="">Ltsmb</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465303818">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082040" name="comment_67082040" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							То есть мужик предполагал, что она не его дочь?

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">2</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67082350" data-level="1" data-parent-id="67082040" data-vote="0" id="comment_67082350">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+23</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304069">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082350" name="comment_67082350" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>мужик предполагал что его вырастят в пробирке в будущем, явно же )) </p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083904" data-level="1" data-parent-id="67082040" data-vote="0" id="comment_67083904">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+5</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/alakazam90"><img alt="alakazam90" src="http://cs6.pikabu.ru/images/avatars/936/s936880-559427938.jpg"/> <span class="">alakazam90</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465305292">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083904" name="comment_67083904" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Знал, не зря же написано: <i><b>дочка</b> его <b>бывшей супруги.</b></i></p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67081745" data-level="0" data-parent-id="0" data-vote="0" id="comment_67081745">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-17</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/montanov"><img alt="montanov" src="http://cs6.pikabu.ru/images/avatars/731/s731423-1581674673.jpg"/> <span class="">montanov</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465303576">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67081745" name="comment_67081745" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" style="display: none" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" style="display: none" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle">показать комментарий</span>
						</noindex>
						<div class="b-comment__content" style="display: none">
							<p>Вот крыса</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">13</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67081986" data-level="1" data-parent-id="67081745" data-vote="0" id="comment_67081986">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+13</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/keksveks"><img alt="keksveks" src="http://cs6.pikabu.ru/images/avatars/647/s647871-965466611.jpg"/> <span class="">keksveks</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465303766">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67081986" name="comment_67081986" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Кто именно?</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">12</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67082190" data-level="2" data-parent-id="67081986" data-vote="0" id="comment_67082190">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+87</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/stepan1987"><span class="">stepan1987</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465303944">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082190" name="comment_67082190" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Сплинтер.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">10</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67082265" data-level="3" data-parent-id="67082190" data-vote="0" id="comment_67082265">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+24</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/ukmaksimus"><span class=" b-comment__user_author_story">ukmaksimus</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304005">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082265" name="comment_67082265" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Cell</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">8</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67082625" data-level="4" data-parent-id="67082265" data-vote="0" id="comment_67082625">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+7</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/stahlhammer"><img alt="stahlhammer" src="http://cs6.pikabu.ru/images/avatars/276/s276329-895351385.jpg"/> <span class="">stahlhammer</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304286">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082625" name="comment_67082625" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Blacklist

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">7</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67083152" data-level="5" data-parent-id="67082625" data-vote="0" id="comment_67083152">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+8</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Kaskad"><img alt="Kaskad" src="http://cs6.pikabu.ru/images/avatars/101/s101327.jpg?1257199038"/> <span class="">Kaskad</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304705">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083152" name="comment_67083152" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Пфф, Теория хаоса лучше</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">4</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67083325" data-level="6" data-parent-id="67083152" data-vote="0" id="comment_67083325">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Aventar"><img alt="Aventar" src="http://cs6.pikabu.ru/images/avatars/53/s53366.jpg?1522842561"/> <span class="">Aventar</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465304827">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083325" name="comment_67083325" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Теория Хаоса</p><div class="b-p b-p_type_image"><a href="http://cs8.pikabu.ru/images/big_size_comm/2016-06_2/146530482713772119.jpg"><img class="b-image" data-large-image="http://s8.pikabu.ru/images/big_size_comm/2016-06_2/146530482713772119.jpg" data-viewable="true" src="http://cs8.pikabu.ru/images/previews_comm/2016-06_2/146530482713772119.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67096222" data-level="7" data-parent-id="67083325" data-vote="0" id="comment_67096222">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/frontierguard"><span class="">frontierguard</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465316877">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67096222" name="comment_67096222" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<div class="b-p b-p_type_image"><a href="http://cs5.pikabu.ru/images/big_size_comm/2015-10_3/1444846021198813527.jpg"><img class="b-image" data-large-image="http://s5.pikabu.ru/images/big_size_comm/2015-10_3/1444846021198813527.jpg" data-viewable="true" src="http://cs5.pikabu.ru/images/previews_comm/2015-10_3/1444846021198813527.jpg"/></a></div>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67087173" data-level="6" data-parent-id="67083152" data-vote="0" id="comment_67087173">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">+1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/HesusKristo"><img alt="HesusKristo" src="http://cs6.pikabu.ru/images/avatars/749/s749891-1914321586.jpg"/> <span class="">HesusKristo</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307924">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67087173" name="comment_67087173" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Дабл Эджент ван лав. Реально кооперативные миссии тащили.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67084612" data-level="6" data-parent-id="67083152" data-vote="0" id="comment_67084612">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Engah"><img alt="Engah" src="http://cs6.pikabu.ru/images/avatars/792/s792283-565769538.jpg"/> <span class="">Engah</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465305835">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67084612" name="comment_67084612" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Поддержу. Лучшая часть серии.<br/>А Blacklist сильно оказуален.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67083682" data-level="5" data-parent-id="67082625" data-vote="0" id="comment_67083682">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-1</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/alakazam90"><img alt="alakazam90" src="http://cs6.pikabu.ru/images/avatars/936/s936880-559427938.jpg"/> <span class="">alakazam90</span></a>
								<span>отправил</span>
								<time class="b-comment__time" DATETIME="1465305109">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67083682" name="comment_67083682" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>К сожалению, из памяти выветрилось много чего и я не помню. Почему Реддингтон носится с агентом Кин? Вроде бы в первом сезоне жирно намекали на его отцовство.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: inline-block">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">1</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: block">

				<div class="b-comment" data-editable="false" data-id="67095013" data-level="6" data-parent-id="67083682" data-vote="0" id="comment_67095013">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Inokanoana"><img alt="Inokanoana" src="http://cs6.pikabu.ru/images/avatars/199/s199977-1074879937.jpg"/> <span class="">Inokanoana</span></a>
								<span>отправила</span>
								<time class="b-comment__time" DATETIME="1465315599">1 час назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67095013" name="comment_67095013" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							В одной из последних серий это объяснили. И в самом начале Ред прямо сказал что он не ее отец.

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67086811" data-level="3" data-parent-id="67082190" data-vote="0" id="comment_67086811">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">0</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Switzer"><span class="">Switzer</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465307620">3 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67086811" name="comment_67086811" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							<p>Twin.</p>

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

				<div class="b-comment" data-editable="false" data-id="67082410" data-level="2" data-parent-id="67081986" data-vote="0" id="comment_67082410">
					<div class="b-comment__body ">
						<div class="b-comment__header">
							<div class="b-comment__rating-count" title="Рейтинг комментария">-2</div>
							<ul class="b-comment__rating">
								<li class="b-comment__rating-up" data-rating="up">
									<i class="i-sprite--comments__rating-up"></i>
								</li>
								<li class="b-comment__rating-down" data-rating="down">
									<i class="i-sprite--comments__rating-down"></i>
								</li>
							</ul>
							<div class="b-comment__user">
								<a href="http://pikabu.ru/profile/Nable"><img alt="Nable" src="http://cs6.pikabu.ru/images/avatars/414/s414304.jpg?179183771"/> <span class="">Nable</span></a>
								<span>отправлено</span>
								<time class="b-comment__time" DATETIME="1465304123">4 часа назад</time>
							</div>
							<noindex>
								<div class="b-comment__tools">
									<div class="b-comment__tool b-comment__tool-link" title="Ссылка на комментарий"><a class="" href="http://pikabu.ru/story/dumay_naperyod__4254058#comment_67082410" name="comment_67082410" title="">#</a></div>

									<div class="b-comment__tool b-comment__tool-root i-sprite--comments__root" title="Показать родительский комментарий"></div>
									<div class="b-comment__tool b-comment__tool-root-back i-sprite--comments__root-back" style="display: none" title="Вернуться обратно"></div>
									<div class="b-comment__tool b-comment__tool-branch i-sprite--comments__branch" title="Показать/скрыть ветку комментариев"></div>
									<div class="b-comment__tool b-comment__tool-save i-sprite--comments__save" title="Сохранить"></div>

								</div>
							</noindex>
						</div>
						<noindex>
							<span class="b-comment__content-toggle" style="display: none">показать комментарий</span>
						</noindex>
						<div class="b-comment__content">
							Сплинтер

						</div>
						<noindex>
							<div class="b-comment__controls" style="display: block">
								<button class="b-button b-comment__control b-comment__control-reply " data-ignored-user="false" data-user-ignored="false">ответить</button>
								<button class="b-button b-comment__control b-comment__control-edit" style="display: none">редактировать</button>
								<button class="b-button b-comment__control b-comment__control-remove" style="display: none">удалить</button>
								<span class="b-comment__control-error" style="display: none"></span>
							</div>
							<div class="b-comment__reply-wrapper" style="display: none"></div>
						</noindex>
					</div>
					<div class="b-comment-toggle b-comment-toggle_type_collapse" style="display: none">
						<div class="b-comment-toggle__icon fa fa-minus-square-o"></div>
						<div class="b-comment-toggle__count" style="display: none">раскрыть ветвь <span class="b-comment-toggle__count-text">0</span> <i class="i-sprite--inline-block i-sprite--comments__show"></i></div>
					</div>
					<div class="b-comments b-comments_level_0" style="display: none">

					</div>
				</div>

					</div>
				</div>

					</div>
				</div>

				</div>

						<TABLE>
							<tbody><tr>
								<td>
									<div class="story__gag-container" style="margin-left: 91px; margin-top: 5px; width: 530px">

				<div class="story__gag story__gag_relative">
					<div data-ad="yandex_ctx_story" id="yandex_ad_1465321221_16824"></div>
				</div>
				<script type="text/javascript">
					(function(w, d, n, s, t) {
						w[n] = w[n] || [];
						w[n].push(function() {
							Ya.Direct.insertInto(
								56459,
								"yandex_ad_1465321221_16824",
								{"site_charset":"windows-1251","stat_id":"4","ad_format":"direct","font_size":0.8,"font_family":"tahoma","type":"horizontal","border_type":"none","limit":1,"title_font_size":3,"site_bg_color":"FFFFFF","header_bg_color":"FFFFFF","bg_color":"FFFFFF","title_color":"217CB6","url_color":"777777","all_color":"777777","text_color":"444444","sitelinks_color":"777777","hover_color":"777777"}
							);
						});
						t = d.documentElement.firstChild;
						s = d.createElement("script");
						s.type = "text/javascript";
						s.src = "http://an.yandex.ru/system/context.js";
						s.setAttribute("async", "true");
						t.insertBefore(s, t.firstChild);
					})(window, document, "yandex_context_callbacks");
				</script>

									</div>
								</td>
							</tr>
						</tbody></TABLE>

				<div class="b-comments__reply"></div>

					<!-- RELATED STORIES BLOCK -->
					<div data-count="2" data-id="4254058" id="related-stories">
						<div class="b-related-stories">

						<div class="rs-title">Похожие посты</div>

					<div class="rs-stories"></div>
					<a class="rs-more-btn" target="_blank">показать ещё</a>

						<div class="b-related-stories-tags">
							<div>Похожие посты закончились. Возможно, вас заинтересуют другие посты по тегам:</div>

							<a href="/tag/генетический материал/hot" style="text-decoration: none">
								<span class="tag no_ch">генетический материал</span>
							</a>

							<a href="/tag/миллиардер/hot" style="text-decoration: none">
								<span class="tag no_ch">миллиардер</span>
							</a>

							<a href="/tag/наследство/hot" style="text-decoration: none">
								<span class="tag no_ch">наследство</span>
							</a>

							<a href="/tag/Хитрость/hot" style="text-decoration: none">
								<span class="tag no_ch">Хитрость</span>
							</a>

							<a href="/tag/думай наперед/hot" style="text-decoration: none">
								<span class="tag no_ch">думай наперед</span>
							</a>

							<a href="/tag/ум/hot" style="text-decoration: none">
								<span class="tag no_ch">ум</span>
							</a>

						</div>

						</div>
					</div>


								</td>
							</tr>
						</tbody>
					</TABLE>

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
										<input autocomplete="off" class="b-input" data-additional="_T8f7hN" data-name="password" id="signup-p" maxlength="255" type="password" value=""/>

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
					<a href="http://pikabu.ru/story/vot_yeto_povorot__4252741">Вот это поворот =)</a>
				</div>
				<div class="info info_c menu-comm-head">
                    <h6>+2560</h6> 
                    <a href="http://pikabu.ru/profile/RapTor25">RapTor25</a>; <a class="detailDate" href="javascript:void(0)" style="text-decoration: none;" title="1465273612">13 часов назад</a>
                    <a href="http://pikabu.ru/story/vot_yeto_povorot__4252741#comment_67053149" title="ссылка на данный комментарий">#</a>
				</div>
                <div class="comment_msg comment_desc menu-comm-desc">

				<div class="b-comment__body comment_desc" style="max-width: 260px; overflow: hidden">
					Эх, теперь я завидую мотоциклисту. Отмудохать личинку депутата - бесценно)
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

					<div class="right_menu_ads">

				<div class="story__gag story__gag_relative">
					<div data-ad="yandex_ctx_menu" id="yandex_ad_1465321229_80922"></div>
				</div>
				<script type="text/javascript">
					(function(w, d, n, s, t) {
						w[n] = w[n] || [];
						w[n].push(function() {
							Ya.Direct.insertInto(
								56459,
								"yandex_ad_1465321229_80922",
								{"site_charset":"windows-1251","stat_id":"3","ad_format":"direct","font_size":1,"font_family":"tahoma","type":"posterVertical","border_type":"block","limit":2,"title_font_size":3,"site_bg_color":"FFFFFF","header_bg_color":"FFFFFF","bg_color":"FFFFFF","title_color":"5190B8","url_color":"008900","text_color":"676767","sitelinks_color":"777777","hover_color":"5190B8","border_color":"D7D7D7","favicon":TRUE,"no_sitelinks":FALSE}
							);
						});
						t = d.documentElement.firstChild;
						s = d.createElement("script");
						s.type = "text/javascript";
						s.src = "http://an.yandex.ru/system/context.js";
						s.setAttribute("async", "true");
						t.insertBefore(s, t.firstChild);
					})(window, document, "yandex_context_callbacks");
				</script>

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
							<span class="tag_count">528</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/видео/hot"><span class="tag no_ch">видео</span>
							<span class="tag_count">345</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/аниме/hot"><span class="tag no_ch">аниме</span>
							<span class="tag_count">116</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/сообщество/hot"><span class="tag no_ch">сообщество</span>
							<span class="tag_count">111</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/арт/hot"><span class="tag no_ch">арт</span>
							<span class="tag_count">100</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/кот/hot"><span class="tag no_ch">кот</span>
							<span class="tag_count">97</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/anime art/hot"><span class="tag no_ch">anime art</span>
							<span class="tag_count">90</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Россия/hot"><span class="tag no_ch">Россия</span>
							<span class="tag_count">78</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Игры/hot"><span class="tag no_ch">Игры</span>
							<span class="tag_count">76</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/моё/hot"><span class="tag no_ch">моё</span>
							<span class="tag_count">64</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/история/hot"><span class="tag no_ch">история</span>
							<span class="tag_count">59</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/собака/hot"><span class="tag no_ch">собака</span>
							<span class="tag_count">58</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/рисунок/hot"><span class="tag no_ch">рисунок</span>
							<span class="tag_count">41</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Игра престолов/hot"><span class="tag no_ch">Игра престолов</span>
							<span class="tag_count">37</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Интересное/hot"><span class="tag no_ch">Интересное</span>
							<span class="tag_count">37</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/авто/hot"><span class="tag no_ch">авто</span>
							<span class="tag_count">37</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/работа/hot"><span class="tag no_ch">работа</span>
							<span class="tag_count">35</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Фильмы/hot"><span class="tag no_ch">Фильмы</span>
							<span class="tag_count">35</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/музыка/hot"><span class="tag no_ch">музыка</span>
							<span class="tag_count">31</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/фотография/hot"><span class="tag no_ch">фотография</span>
							<span class="tag_count">29</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Животные/hot"><span class="tag no_ch">Животные</span>
							<span class="tag_count">28</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/космос/hot"><span class="tag no_ch">космос</span>
							<span class="tag_count">27</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/coub/hot"><span class="tag no_ch">coub</span>
							<span class="tag_count">25</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/еда/hot"><span class="tag no_ch">еда</span>
							<span class="tag_count">24</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Природа/hot"><span class="tag no_ch">Природа</span>
							<span class="tag_count">23</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Создайте сообщество/hot"><span class="tag no_ch">Создайте сообщество</span>
							<span class="tag_count">21</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/steam/hot"><span class="tag no_ch">steam</span>
							<span class="tag_count">21</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Москва/hot"><span class="tag no_ch">Москва</span>
							<span class="tag_count">21</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/книги/hot"><span class="tag no_ch">книги</span>
							<span class="tag_count">20</span></a>
						</div>

						<div class="allMenuTags" style="">
							<a class="no_ch" href="http://pikabu.ru/tag/Санкт-Петербург/hot"><span class="tag no_ch">Санкт-Петербург</span>
							<span class="tag_count">20</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Любовь/hot"><span class="tag no_ch">Любовь</span>
							<span class="tag_count">20</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Warhammer 40k/hot"><span class="tag no_ch">Warhammer 40k</span>
							<span class="tag_count">19</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/женщина/hot"><span class="tag no_ch">женщина</span>
							<span class="tag_count">19</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Anime Original/hot"><span class="tag no_ch">Anime Original</span>
							<span class="tag_count">18</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/сериалы/hot"><span class="tag no_ch">сериалы</span>
							<span class="tag_count">18</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/япония/hot"><span class="tag no_ch">япония</span>
							<span class="tag_count">18</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/отношения/hot"><span class="tag no_ch">отношения</span>
							<span class="tag_count">18</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/лето/hot"><span class="tag no_ch">лето</span>
							<span class="tag_count">17</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/дорога/hot"><span class="tag no_ch">дорога</span>
							<span class="tag_count">17</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/перевод/hot"><span class="tag no_ch">перевод</span>
							<span class="tag_count">16</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/vocaloid/hot"><span class="tag no_ch">vocaloid</span>
							<span class="tag_count">15</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/полиция/hot"><span class="tag no_ch">полиция</span>
							<span class="tag_count">15</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/авария/hot"><span class="tag no_ch">авария</span>
							<span class="tag_count">15</span></a>
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
							<a class="no_ch" href="http://pikabu.ru/tag/ДТП/hot"><span class="tag no_ch">ДТП</span>
							<span class="tag_count">15</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/спойлер/hot"><span class="tag no_ch">спойлер</span>
							<span class="tag_count">14</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/армия/hot"><span class="tag no_ch">армия</span>
							<span class="tag_count">14</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Наука/hot"><span class="tag no_ch">Наука</span>
							<span class="tag_count">14</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/путешествия/hot"><span class="tag no_ch">путешествия</span>
							<span class="tag_count">14</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/творчество/hot"><span class="tag no_ch">творчество</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/рассказ/hot"><span class="tag no_ch">рассказ</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/kantai collection/hot"><span class="tag no_ch">kantai collection</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/доктор кто/hot"><span class="tag no_ch">доктор кто</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/ведьмак/hot"><span class="tag no_ch">ведьмак</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Hatsune Miku/hot"><span class="tag no_ch">Hatsune Miku</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/машина/hot"><span class="tag no_ch">машина</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/лига Лени/hot"><span class="tag no_ch">лига Лени</span>
							<span class="tag_count">13</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Франция/hot"><span class="tag no_ch">Франция</span>
							<span class="tag_count">12</span></a>
						</div>

						<div class="allMenuTags" style="display:none">
							<a class="no_ch" href="http://pikabu.ru/tag/Искусство/hot"><span class="tag no_ch">Искусство</span>
							<span class="tag_count">12</span></a>
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
				<a href="http://pikabu.ru/story/_2740794">
					<img id="brov" src="http://cs.pikabu.ru/images/fun/metal_masyanyarus.png" style="" title="Печенюх [by Masyanyarus]"/>
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



			</body></html>
"""
