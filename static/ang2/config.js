System.config({
  baseURL: "static/ang2",
  defaultJSExtensions: true,
  transpiler: "typescript",
  typescriptOptions: {
    "module": "commonjs",
    "emitDecoratorMetadata": true
  },
  paths: {
    "github:*": "jspm_packages/github/*",
    "npm:*": "jspm_packages/npm/*"
  },
  bundles: {
    "build.js": [
      "app/boot.js",
      "npm:angular2-jwt@0.1.9.js",
      "npm:angular2-jwt@0.1.9/angular2-jwt.js",
      "npm:rxjs@5.0.0-beta.2/Observable.js",
      "npm:rxjs@5.0.0-beta.2/util/errorObject.js",
      "npm:rxjs@5.0.0-beta.2/util/tryCatch.js",
      "npm:rxjs@5.0.0-beta.2/util/toSubscriber.js",
      "npm:rxjs@5.0.0-beta.2/symbol/rxSubscriber.js",
      "npm:rxjs@5.0.0-beta.2/util/SymbolShim.js",
      "npm:rxjs@5.0.0-beta.2/util/root.js",
      "npm:rxjs@5.0.0-beta.2/Subscriber.js",
      "npm:rxjs@5.0.0-beta.2/Observer.js",
      "npm:rxjs@5.0.0-beta.2/Subscription.js",
      "npm:rxjs@5.0.0-beta.2/util/isFunction.js",
      "npm:rxjs@5.0.0-beta.2/util/isObject.js",
      "npm:rxjs@5.0.0-beta.2/util/isArray.js",
      "npm:angular2@2.0.0-beta.12/http.js",
      "npm:angular2@2.0.0-beta.12/src/http/url_search_params.js",
      "npm:angular2@2.0.0-beta.12/src/facade/collection.js",
      "npm:angular2@2.0.0-beta.12/src/facade/lang.js",
      "npm:angular2@2.0.0-beta.12/src/http/enums.js",
      "npm:angular2@2.0.0-beta.12/src/http/headers.js",
      "npm:angular2@2.0.0-beta.12/src/facade/exceptions.js",
      "npm:angular2@2.0.0-beta.12/src/facade/exception_handler.js",
      "npm:angular2@2.0.0-beta.12/src/facade/base_wrapped_exception.js",
      "npm:angular2@2.0.0-beta.12/src/http/interfaces.js",
      "npm:angular2@2.0.0-beta.12/src/http/static_response.js",
      "npm:angular2@2.0.0-beta.12/src/http/http_utils.js",
      "npm:angular2@2.0.0-beta.12/src/http/static_request.js",
      "npm:angular2@2.0.0-beta.12/src/http/base_response_options.js",
      "npm:angular2@2.0.0-beta.12/core.js",
      "npm:angular2@2.0.0-beta.12/src/core/reflection/reflection.js",
      "npm:angular2@2.0.0-beta.12/src/core/reflection/reflection_capabilities.js",
      "npm:angular2@2.0.0-beta.12/src/core/reflection/reflector.js",
      "npm:angular2@2.0.0-beta.12/src/core/application_common_providers.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/dynamic_component_loader.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view_manager.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view_type.js",
      "npm:angular2@2.0.0-beta.12/src/core/application_tokens.js",
      "npm:angular2@2.0.0-beta.12/src/core/di.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/opaque_token.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/exceptions.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/key.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/forward_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/provider.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/metadata.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/injector.js",
      "npm:angular2@2.0.0-beta.12/src/core/di/decorators.js",
      "npm:angular2@2.0.0-beta.12/src/core/util/decorators.js",
      "npm:angular2@2.0.0-beta.12/src/core/profile/profile.js",
      "npm:angular2@2.0.0-beta.12/src/core/profile/wtf_impl.js",
      "npm:angular2@2.0.0-beta.12/src/core/render/api.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view.js",
      "npm:angular2@2.0.0-beta.12/src/core/render/util.js",
      "npm:angular2@2.0.0-beta.12/src/core/pipes/pipes.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/pipes.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/element.js",
      "npm:angular2@2.0.0-beta.12/src/core/pipes/pipe_provider.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/query_list.js",
      "npm:angular2@2.0.0-beta.12/src/facade/async.js",
      "npm:rxjs@5.0.0-beta.2/operator/toPromise.js",
      "npm:rxjs@5.0.0-beta.2/observable/PromiseObservable.js",
      "npm:rxjs@5.0.0-beta.2/Subject.js",
      "npm:rxjs@5.0.0-beta.2/util/ObjectUnsubscribedError.js",
      "npm:rxjs@5.0.0-beta.2/util/throwError.js",
      "npm:rxjs@5.0.0-beta.2/subject/SubjectSubscription.js",
      "npm:angular2@2.0.0-beta.12/src/facade/promise.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/change_detection.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/change_detection_util.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/directive_record.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/constants.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/binding_record.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/pipe_lifecycle_reflector.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/change_detector_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/dynamic_change_detector.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/proto_record.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/abstract_change_detector.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/parser/locals.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/exceptions.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/jit_proto_change_detector.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/change_detection_jit_generator.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/proto_change_detector.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/coalesce.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/event_binding.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/parser/ast.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/codegen_facade.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/codegen_logic_util.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/codegen_name_util.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/interfaces.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/parser/parser.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/parser/lexer.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/differs/default_keyvalue_differ.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/differs/keyvalue_differs.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/differs/default_iterable_differ.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection/differs/iterable_differs.js",
      "npm:angular2@2.0.0-beta.12/src/core/metadata/directives.js",
      "npm:angular2@2.0.0-beta.12/src/core/change_detection.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/template_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view_container_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/element_ref.js",
      "npm:angular2@2.0.0-beta.12/src/core/metadata/di.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/compiler.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/pipe_resolver.js",
      "npm:angular2@2.0.0-beta.12/src/core/metadata.js",
      "npm:angular2@2.0.0-beta.12/src/core/metadata/view.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/directive_resolver.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/view_resolver.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/resolved_metadata_cache.js",
      "npm:angular2@2.0.0-beta.12/src/core/platform_common_providers.js",
      "npm:angular2@2.0.0-beta.12/src/core/testability/testability.js",
      "npm:angular2@2.0.0-beta.12/src/core/zone/ng_zone.js",
      "npm:angular2@2.0.0-beta.12/src/core/zone/ng_zone_impl.js",
      "npm:angular2@2.0.0-beta.12/src/core/console.js",
      "npm:angular2@2.0.0-beta.12/src/core/platform_directives_and_pipes.js",
      "npm:angular2@2.0.0-beta.12/src/core/debug/debug_node.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker.js",
      "npm:angular2@2.0.0-beta.12/src/core/render.js",
      "npm:angular2@2.0.0-beta.12/src/core/zone.js",
      "npm:angular2@2.0.0-beta.12/src/core/application_ref.js",
      "npm:angular2@2.0.0-beta.12/src/facade/facade.js",
      "npm:angular2@2.0.0-beta.12/src/core/prod_mode.js",
      "npm:angular2@2.0.0-beta.12/src/core/util.js",
      "npm:angular2@2.0.0-beta.12/src/http/base_request_options.js",
      "npm:angular2@2.0.0-beta.12/src/http/backends/browser_jsonp.js",
      "npm:angular2@2.0.0-beta.12/src/http/backends/browser_xhr.js",
      "npm:angular2@2.0.0-beta.12/src/http/backends/jsonp_backend.js",
      "npm:angular2@2.0.0-beta.12/src/http/backends/xhr_backend.js",
      "npm:angular2@2.0.0-beta.12/src/http/http.js",
      "npm:angular2@2.0.0-beta.12/router.js",
      "npm:angular2@2.0.0-beta.12/src/router/router_providers.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/platform_location.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/browser_platform_location.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/dom_adapter.js",
      "npm:angular2@2.0.0-beta.12/src/router/router_providers_common.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/location.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/location_strategy.js",
      "npm:angular2@2.0.0-beta.12/src/router/route_registry.js",
      "npm:angular2@2.0.0-beta.12/src/router/url_parser.js",
      "npm:angular2@2.0.0-beta.12/src/router/route_config/route_config_normalizer.js",
      "npm:angular2@2.0.0-beta.12/src/router/route_config/route_config_decorator.js",
      "npm:angular2@2.0.0-beta.12/src/router/route_config/route_config_impl.js",
      "npm:angular2@2.0.0-beta.12/src/router/instruction.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/rule_set.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/route_paths/regex_route_path.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/route_paths/route_path.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/route_paths/param_route_path.js",
      "npm:angular2@2.0.0-beta.12/src/router/utils.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/route_handlers/sync_route_handler.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/route_handlers/async_route_handler.js",
      "npm:angular2@2.0.0-beta.12/src/router/rules/rules.js",
      "npm:angular2@2.0.0-beta.12/src/router/router.js",
      "npm:angular2@2.0.0-beta.12/src/router/lifecycle/route_lifecycle_reflector.js",
      "npm:angular2@2.0.0-beta.12/src/router/lifecycle/lifecycle_annotations_impl.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/path_location_strategy.js",
      "npm:angular2@2.0.0-beta.12/src/router/lifecycle/lifecycle_annotations.js",
      "npm:angular2@2.0.0-beta.12/src/router/route_definition.js",
      "npm:angular2@2.0.0-beta.12/src/router/location/hash_location_strategy.js",
      "npm:angular2@2.0.0-beta.12/src/router/directives/router_link.js",
      "npm:angular2@2.0.0-beta.12/src/router/directives/router_outlet.js",
      "app/main.component.js",
      "app/temp-study/votes/votes.component.js",
      "npm:angular2@2.0.0-beta.12/common.js",
      "npm:angular2@2.0.0-beta.12/src/common/common_directives.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/core_directives.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_plural.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_switch.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_style.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_if.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_for.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/ng_class.js",
      "npm:angular2@2.0.0-beta.12/src/common/directives/observable_list_diff.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/radio_control_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_control.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/abstract_control_directive.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/control_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/form_builder.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/model.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/validators.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/validators.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/select_control_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_control_status.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/number_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/checkbox_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/default_value_accessor.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_form.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/shared.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/normalize_validator.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/control_container.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_form_model.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_control_group.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_model.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_form_control.js",
      "npm:angular2@2.0.0-beta.12/src/common/forms/directives/ng_control_name.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/common_pipes.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/i18n_select_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/invalid_pipe_argument_exception.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/i18n_plural_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/replace_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/number_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/facade/intl.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/date_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/slice_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/json_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/lowercase_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/uppercase_pipe.js",
      "npm:angular2@2.0.0-beta.12/src/common/pipes/async_pipe.js",
      "app/temp-study/votes/votes.service.js",
      "npm:rxjs@5.0.0-beta.2/add/operator/map.js",
      "npm:rxjs@5.0.0-beta.2/operator/map.js",
      "static.js",
      "app/temp-study/blocknote/blocknote.component.js",
      "app/helpers/headersUnsafe.js",
      "app/logger/logger.component.js",
      "app/logger/logger.service.js",
      "npm:rxjs@5.0.0-beta.2/add/operator/delay.js",
      "npm:rxjs@5.0.0-beta.2/operator/delay.js",
      "npm:rxjs@5.0.0-beta.2/Notification.js",
      "npm:rxjs@5.0.0-beta.2/util/isDate.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/asap.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/AsapScheduler.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/QueueScheduler.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/FutureAction.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/QueueAction.js",
      "npm:rxjs@5.0.0-beta.2/scheduler/AsapAction.js",
      "npm:rxjs@5.0.0-beta.2/util/Immediate.js",
      "github:jspm/nodelibs-process@0.1.2.js",
      "github:jspm/nodelibs-process@0.1.2/index.js",
      "npm:process@0.11.5.js",
      "npm:process@0.11.5/browser.js",
      "app/posts/posts.component.js",
      "app/friendlist/friendlist.component.js",
      "app/friendlist/friendlist.service.js",
      "app/header/header.js",
      "app/header/login/login.component.js",
      "app/header/login/login.service.js",
      "app/helpers/elementInView.js",
      "app/searchbar/searchbar.component.js",
      "app/posts/post/post.component.js",
      "app/helpers/copyTextToClipboard.js",
      "app/comments/comments.component.js",
      "app/comments/comment/comment.js",
      "app/helpers/dateFromUTC.js",
      "app/comments/comments.service.js",
      "app/comments/mock-comments.js",
      "app/posts/post/content/content.component.js",
      "app/helpers/sb_windowToolsY.js",
      "app/posts/posts.service.js",
      "npm:angular2@2.0.0-beta.12/platform/browser.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/xhr_impl.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/xhr.js",
      "npm:angular2@2.0.0-beta.12/compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/url_resolver.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/schema/dom_element_schema_registry.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/schema/element_schema_registry.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/html_tags.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/runtime_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/template_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/util.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/runtime_metadata.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/interfaces.js",
      "npm:angular2@2.0.0-beta.12/src/core/linker/directive_lifecycle_reflector.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/directive_metadata.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/selector.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/template_normalizer.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/template_preparser.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/html_parser.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/parse_util.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/html_lexer.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/html_ast.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/style_url_resolver.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/template_parser.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/template_ast.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/proto_view_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/source_module.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/view_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/style_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/shadow_css.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/change_detector_compiler.js",
      "npm:angular2@2.0.0-beta.12/src/transform/template_compiler/change_detector_codegen.js",
      "npm:angular2@2.0.0-beta.12/src/compiler/change_definition_factory.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser_common.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/tools/tools.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/tools/common_tools.js",
      "npm:angular2@2.0.0-beta.12/src/facade/browser.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/title.js",
      "npm:angular2@2.0.0-beta.12/platform/common_dom.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/debug/ng_probe.js",
      "npm:angular2@2.0.0-beta.12/src/core/debug/debug_renderer.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/dom_renderer.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/util.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/dom_tokens.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/events/event_manager.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/shared_styles_host.js",
      "npm:angular2@2.0.0-beta.12/src/animate/animation_builder.js",
      "npm:angular2@2.0.0-beta.12/src/animate/browser_details.js",
      "npm:angular2@2.0.0-beta.12/src/facade/math.js",
      "npm:angular2@2.0.0-beta.12/src/animate/css_animation_builder.js",
      "npm:angular2@2.0.0-beta.12/src/animate/animation.js",
      "npm:angular2@2.0.0-beta.12/src/animate/css_animation_options.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/debug/by.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/events/dom_events.js",
      "npm:angular2@2.0.0-beta.12/src/core/profile/wtf_init.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/testability.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/browser_adapter.js",
      "npm:angular2@2.0.0-beta.12/src/platform/browser/generic_browser_adapter.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/events/hammer_gestures.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/events/hammer_common.js",
      "npm:angular2@2.0.0-beta.12/src/platform/dom/events/key_events.js",
      "npm:angular2@2.0.0-beta.12/src/core/angular_entrypoint.js",
      "github:es-shims/es6-shim@0.35.1.js",
      "github:es-shims/es6-shim@0.35.1/es6-shim.js",
      "npm:reflect-metadata@0.1.3.js",
      "npm:reflect-metadata@0.1.3/Reflect.js",
      "github:jspm/nodelibs-crypto@0.1.0.js",
      "github:jspm/nodelibs-crypto@0.1.0/index.js",
      "npm:crypto-browserify@3.11.0.js",
      "npm:crypto-browserify@3.11.0/index.js",
      "npm:public-encrypt@4.0.0.js",
      "npm:public-encrypt@4.0.0/browser.js",
      "npm:public-encrypt@4.0.0/privateDecrypt.js",
      "github:jspm/nodelibs-buffer@0.1.0.js",
      "github:jspm/nodelibs-buffer@0.1.0/index.js",
      "npm:buffer@3.6.0.js",
      "npm:buffer@3.6.0/index.js",
      "npm:isarray@1.0.0.js",
      "npm:isarray@1.0.0/index.js",
      "npm:ieee754@1.1.6.js",
      "npm:ieee754@1.1.6/index.js",
      "npm:base64-js@0.0.8.js",
      "npm:base64-js@0.0.8/lib/b64.js",
      "npm:public-encrypt@4.0.0/withPublic.js",
      "npm:bn.js@4.11.4.js",
      "npm:bn.js@4.11.4/lib/bn.js",
      "npm:create-hash@1.1.2.js",
      "npm:create-hash@1.1.2/browser.js",
      "npm:cipher-base@1.0.2.js",
      "npm:cipher-base@1.0.2/index.js",
      "github:jspm/nodelibs-string_decoder@0.1.0.js",
      "github:jspm/nodelibs-string_decoder@0.1.0/index.js",
      "npm:string_decoder@0.10.31.js",
      "npm:string_decoder@0.10.31/index.js",
      "npm:inherits@2.0.1.js",
      "npm:inherits@2.0.1/inherits_browser.js",
      "github:jspm/nodelibs-stream@0.1.0.js",
      "github:jspm/nodelibs-stream@0.1.0/index.js",
      "npm:stream-browserify@1.0.0.js",
      "npm:stream-browserify@1.0.0/index.js",
      "npm:readable-stream@1.1.14/passthrough.js",
      "npm:readable-stream@1.1.14/lib/_stream_passthrough.js",
      "npm:core-util-is@1.0.2.js",
      "npm:core-util-is@1.0.2/lib/util.js",
      "npm:readable-stream@1.1.14/lib/_stream_transform.js",
      "npm:readable-stream@1.1.14/lib/_stream_duplex.js",
      "npm:readable-stream@1.1.14/lib/_stream_writable.js",
      "npm:readable-stream@1.1.14/lib/_stream_readable.js",
      "github:jspm/nodelibs-events@0.1.1.js",
      "github:jspm/nodelibs-events@0.1.1/index.js",
      "npm:events@1.0.2.js",
      "npm:events@1.0.2/events.js",
      "npm:isarray@0.0.1.js",
      "npm:isarray@0.0.1/index.js",
      "npm:readable-stream@1.1.14/transform.js",
      "npm:readable-stream@1.1.14/duplex.js",
      "npm:readable-stream@1.1.14/writable.js",
      "npm:readable-stream@1.1.14/readable.js",
      "npm:sha.js@2.4.5.js",
      "npm:sha.js@2.4.5/index.js",
      "npm:sha.js@2.4.5/sha512.js",
      "npm:sha.js@2.4.5/hash.js",
      "npm:sha.js@2.4.5/sha384.js",
      "npm:sha.js@2.4.5/sha256.js",
      "npm:sha.js@2.4.5/sha224.js",
      "npm:sha.js@2.4.5/sha1.js",
      "npm:sha.js@2.4.5/sha.js",
      "npm:ripemd160@1.0.1.js",
      "npm:ripemd160@1.0.1/lib/ripemd160.js",
      "npm:create-hash@1.1.2/md5.js",
      "npm:create-hash@1.1.2/helpers.js",
      "npm:browserify-rsa@4.0.1.js",
      "npm:browserify-rsa@4.0.1/index.js",
      "npm:randombytes@2.0.3.js",
      "npm:randombytes@2.0.3/browser.js",
      "npm:public-encrypt@4.0.0/xor.js",
      "npm:public-encrypt@4.0.0/mgf.js",
      "npm:parse-asn1@5.0.0.js",
      "npm:parse-asn1@5.0.0/index.js",
      "npm:pbkdf2@3.0.4.js",
      "npm:pbkdf2@3.0.4/browser.js",
      "npm:create-hmac@1.1.4.js",
      "npm:create-hmac@1.1.4/browser.js",
      "npm:browserify-aes@1.0.6.js",
      "npm:browserify-aes@1.0.6/browser.js",
      "npm:browserify-aes@1.0.6/modes.js",
      "npm:browserify-aes@1.0.6/decrypter.js",
      "npm:browserify-aes@1.0.6/modes/ctr.js",
      "npm:buffer-xor@1.0.3.js",
      "npm:buffer-xor@1.0.3/index.js",
      "npm:browserify-aes@1.0.6/modes/ofb.js",
      "npm:browserify-aes@1.0.6/modes/cfb1.js",
      "npm:browserify-aes@1.0.6/modes/cfb8.js",
      "npm:browserify-aes@1.0.6/modes/cfb.js",
      "npm:browserify-aes@1.0.6/modes/cbc.js",
      "npm:browserify-aes@1.0.6/modes/ecb.js",
      "npm:evp_bytestokey@1.0.0.js",
      "npm:evp_bytestokey@1.0.0/index.js",
      "npm:browserify-aes@1.0.6/authCipher.js",
      "npm:browserify-aes@1.0.6/ghash.js",
      "npm:browserify-aes@1.0.6/aes.js",
      "npm:browserify-aes@1.0.6/streamCipher.js",
      "npm:browserify-aes@1.0.6/encrypter.js",
      "npm:parse-asn1@5.0.0/fixProc.js",
      "npm:parse-asn1@5.0.0/aesid.json!github:systemjs/plugin-json@0.1.2.js",
      "npm:parse-asn1@5.0.0/asn1.js",
      "npm:asn1.js@4.6.2.js",
      "npm:asn1.js@4.6.2/lib/asn1.js",
      "npm:asn1.js@4.6.2/lib/asn1/encoders/index.js",
      "npm:asn1.js@4.6.2/lib/asn1/encoders/pem.js",
      "npm:asn1.js@4.6.2/lib/asn1/encoders/der.js",
      "npm:asn1.js@4.6.2/lib/asn1/decoders/index.js",
      "npm:asn1.js@4.6.2/lib/asn1/decoders/pem.js",
      "npm:asn1.js@4.6.2/lib/asn1/decoders/der.js",
      "npm:asn1.js@4.6.2/lib/asn1/constants/index.js",
      "npm:asn1.js@4.6.2/lib/asn1/constants/der.js",
      "npm:asn1.js@4.6.2/lib/asn1/base/index.js",
      "npm:asn1.js@4.6.2/lib/asn1/base/node.js",
      "npm:minimalistic-assert@1.0.0.js",
      "npm:minimalistic-assert@1.0.0/index.js",
      "npm:asn1.js@4.6.2/lib/asn1/base/buffer.js",
      "npm:asn1.js@4.6.2/lib/asn1/base/reporter.js",
      "npm:asn1.js@4.6.2/lib/asn1/api.js",
      "github:jspm/nodelibs-vm@0.1.0.js",
      "github:jspm/nodelibs-vm@0.1.0/index.js",
      "npm:vm-browserify@0.0.4.js",
      "npm:vm-browserify@0.0.4/index.js",
      "npm:indexof@0.0.1.js",
      "npm:indexof@0.0.1/index.js",
      "npm:public-encrypt@4.0.0/publicEncrypt.js",
      "npm:create-ecdh@4.0.0.js",
      "npm:create-ecdh@4.0.0/browser.js",
      "npm:elliptic@6.3.1.js",
      "npm:elliptic@6.3.1/lib/elliptic.js",
      "npm:elliptic@6.3.1/lib/elliptic/eddsa/index.js",
      "npm:elliptic@6.3.1/lib/elliptic/eddsa/signature.js",
      "npm:elliptic@6.3.1/lib/elliptic/eddsa/key.js",
      "npm:hash.js@1.0.3.js",
      "npm:hash.js@1.0.3/lib/hash.js",
      "npm:hash.js@1.0.3/lib/hash/hmac.js",
      "npm:hash.js@1.0.3/lib/hash/ripemd.js",
      "npm:hash.js@1.0.3/lib/hash/sha.js",
      "npm:hash.js@1.0.3/lib/hash/common.js",
      "npm:hash.js@1.0.3/lib/hash/utils.js",
      "npm:elliptic@6.3.1/lib/elliptic/ec/index.js",
      "npm:elliptic@6.3.1/lib/elliptic/ec/signature.js",
      "npm:elliptic@6.3.1/lib/elliptic/ec/key.js",
      "npm:elliptic@6.3.1/lib/elliptic/curves.js",
      "npm:elliptic@6.3.1/lib/elliptic/precomputed/secp256k1.js",
      "npm:elliptic@6.3.1/lib/elliptic/curve/index.js",
      "npm:elliptic@6.3.1/lib/elliptic/curve/edwards.js",
      "npm:elliptic@6.3.1/lib/elliptic/curve/mont.js",
      "npm:elliptic@6.3.1/lib/elliptic/curve/short.js",
      "npm:elliptic@6.3.1/lib/elliptic/curve/base.js",
      "npm:elliptic@6.3.1/lib/elliptic/hmac-drbg.js",
      "npm:brorand@1.0.5.js",
      "npm:brorand@1.0.5/index.js",
      "npm:elliptic@6.3.1/lib/elliptic/utils.js",
      "npm:elliptic@6.3.1/package.json!github:systemjs/plugin-json@0.1.2.js",
      "npm:browserify-sign@4.0.0.js",
      "npm:browserify-sign@4.0.0/browser.js",
      "npm:browserify-sign@4.0.0/verify.js",
      "npm:browserify-sign@4.0.0/curves.js",
      "npm:browserify-sign@4.0.0/sign.js",
      "npm:browserify-sign@4.0.0/algos.js",
      "npm:diffie-hellman@5.0.2.js",
      "npm:diffie-hellman@5.0.2/browser.js",
      "npm:diffie-hellman@5.0.2/lib/dh.js",
      "npm:diffie-hellman@5.0.2/lib/generatePrime.js",
      "npm:miller-rabin@4.0.0.js",
      "npm:miller-rabin@4.0.0/lib/mr.js",
      "npm:diffie-hellman@5.0.2/lib/primes.json!github:systemjs/plugin-json@0.1.2.js",
      "npm:browserify-cipher@1.0.0.js",
      "npm:browserify-cipher@1.0.0/browser.js",
      "npm:browserify-des@1.0.0/modes.js",
      "npm:browserify-des@1.0.0.js",
      "npm:browserify-des@1.0.0/index.js",
      "npm:des.js@1.0.0.js",
      "npm:des.js@1.0.0/lib/des.js",
      "npm:des.js@1.0.0/lib/des/ede.js",
      "npm:des.js@1.0.0/lib/des/cbc.js",
      "npm:des.js@1.0.0/lib/des/des.js",
      "npm:des.js@1.0.0/lib/des/cipher.js",
      "npm:des.js@1.0.0/lib/des/utils.js",
      "npm:zone.js@0.6.12.js",
      "npm:zone.js@0.6.12/dist/zone.js"
    ]
  },
  production: true,

  packages: {
    "app": {
      "main": "main",
      "defaultExtension": "js",
      "format": "register"
    }
  },

  map: {
    "angular2": "npm:angular2@2.0.0-beta.12",
    "angular2-jwt": "npm:angular2-jwt@0.1.9",
    "babel": "npm:babel-core@5.8.38",
    "babel-runtime": "npm:babel-runtime@5.8.38",
    "core-js": "npm:core-js@1.2.6",
    "crypto": "github:jspm/nodelibs-crypto@0.1.0",
    "es6-shim": "github:es-shims/es6-shim@0.35.1",
    "reflect-metadata": "npm:reflect-metadata@0.1.3",
    "rxjs": "npm:rxjs@5.0.0-beta.2",
    "typescript": "npm:typescript@1.8.9",
    "zone.js": "npm:zone.js@0.6.12",
    "github:jspm/nodelibs-assert@0.1.0": {
      "assert": "npm:assert@1.4.1"
    },
    "github:jspm/nodelibs-buffer@0.1.0": {
      "buffer": "npm:buffer@3.6.0"
    },
    "github:jspm/nodelibs-constants@0.1.0": {
      "constants-browserify": "npm:constants-browserify@0.0.1"
    },
    "github:jspm/nodelibs-crypto@0.1.0": {
      "crypto-browserify": "npm:crypto-browserify@3.11.0"
    },
    "github:jspm/nodelibs-events@0.1.1": {
      "events": "npm:events@1.0.2"
    },
    "github:jspm/nodelibs-http@1.7.1": {
      "Base64": "npm:Base64@0.2.1",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "inherits": "npm:inherits@2.0.1",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "github:jspm/nodelibs-https@0.1.0": {
      "https-browserify": "npm:https-browserify@0.0.0"
    },
    "github:jspm/nodelibs-net@0.1.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "http": "github:jspm/nodelibs-http@1.7.1",
      "net": "github:jspm/nodelibs-net@0.1.2",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "timers": "github:jspm/nodelibs-timers@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "github:jspm/nodelibs-os@0.1.0": {
      "os-browserify": "npm:os-browserify@0.1.2"
    },
    "github:jspm/nodelibs-path@0.1.0": {
      "path-browserify": "npm:path-browserify@0.0.0"
    },
    "github:jspm/nodelibs-process@0.1.2": {
      "process": "npm:process@0.11.5"
    },
    "github:jspm/nodelibs-querystring@0.1.0": {
      "querystring": "npm:querystring@0.2.0"
    },
    "github:jspm/nodelibs-stream@0.1.0": {
      "stream-browserify": "npm:stream-browserify@1.0.0"
    },
    "github:jspm/nodelibs-string_decoder@0.1.0": {
      "string_decoder": "npm:string_decoder@0.10.31"
    },
    "github:jspm/nodelibs-timers@0.1.0": {
      "timers-browserify": "npm:timers-browserify@1.4.2"
    },
    "github:jspm/nodelibs-url@0.1.0": {
      "url": "npm:url@0.10.3"
    },
    "github:jspm/nodelibs-util@0.1.0": {
      "util": "npm:util@0.10.3"
    },
    "github:jspm/nodelibs-vm@0.1.0": {
      "vm-browserify": "npm:vm-browserify@0.0.4"
    },
    "github:jspm/nodelibs-zlib@0.1.0": {
      "browserify-zlib": "npm:browserify-zlib@0.1.4"
    },
    "npm:agent-base@2.0.1": {
      "events": "github:jspm/nodelibs-events@0.1.1",
      "extend": "npm:extend@3.0.0",
      "http": "github:jspm/nodelibs-http@1.7.1",
      "https": "github:jspm/nodelibs-https@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "semver": "npm:semver@5.0.3",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:angular2-jwt@0.1.9": {
      "angular2": "npm:angular2@2.0.0-beta.12",
      "rxjs": "npm:rxjs@5.0.0-beta.2",
      "typings": "npm:typings@0.7.12",
      "zone.js": "npm:zone.js@0.6.12"
    },
    "npm:angular2@2.0.0-beta.12": {
      "reflect-metadata": "npm:reflect-metadata@0.1.2",
      "rxjs": "npm:rxjs@5.0.0-beta.2",
      "zone.js": "npm:zone.js@0.6.12"
    },
    "npm:any-promise@1.3.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:asn1.js@4.6.2": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "bn.js": "npm:bn.js@4.11.4",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "inherits": "npm:inherits@2.0.1",
      "minimalistic-assert": "npm:minimalistic-assert@1.0.0",
      "vm": "github:jspm/nodelibs-vm@0.1.0"
    },
    "npm:assert@1.4.1": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "util": "npm:util@0.10.3"
    },
    "npm:babel-runtime@5.8.38": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:bluebird@3.4.1": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:bn.js@4.11.4": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0"
    },
    "npm:boxen@0.3.1": {
      "chalk": "npm:chalk@1.1.3",
      "filled-array": "npm:filled-array@1.1.0",
      "object-assign": "npm:object-assign@4.1.0",
      "repeating": "npm:repeating@2.0.1",
      "string-width": "npm:string-width@1.0.1",
      "widest-line": "npm:widest-line@1.0.0"
    },
    "npm:brace-expansion@1.1.5": {
      "balanced-match": "npm:balanced-match@0.4.1",
      "concat-map": "npm:concat-map@0.0.1"
    },
    "npm:browserify-aes@1.0.6": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "buffer-xor": "npm:buffer-xor@1.0.3",
      "cipher-base": "npm:cipher-base@1.0.2",
      "create-hash": "npm:create-hash@1.1.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "evp_bytestokey": "npm:evp_bytestokey@1.0.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "inherits": "npm:inherits@2.0.1",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:browserify-cipher@1.0.0": {
      "browserify-aes": "npm:browserify-aes@1.0.6",
      "browserify-des": "npm:browserify-des@1.0.0",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "evp_bytestokey": "npm:evp_bytestokey@1.0.0"
    },
    "npm:browserify-des@1.0.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "cipher-base": "npm:cipher-base@1.0.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "des.js": "npm:des.js@1.0.0",
      "inherits": "npm:inherits@2.0.1"
    },
    "npm:browserify-rsa@4.0.1": {
      "bn.js": "npm:bn.js@4.11.4",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "constants": "github:jspm/nodelibs-constants@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "randombytes": "npm:randombytes@2.0.3"
    },
    "npm:browserify-sign@4.0.0": {
      "bn.js": "npm:bn.js@4.11.4",
      "browserify-rsa": "npm:browserify-rsa@4.0.1",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-hash": "npm:create-hash@1.1.2",
      "create-hmac": "npm:create-hmac@1.1.4",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "elliptic": "npm:elliptic@6.3.1",
      "inherits": "npm:inherits@2.0.1",
      "parse-asn1": "npm:parse-asn1@5.0.0",
      "stream": "github:jspm/nodelibs-stream@0.1.0"
    },
    "npm:browserify-zlib@0.1.4": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "pako": "npm:pako@0.2.8",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "readable-stream": "npm:readable-stream@2.0.6",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:buffer-xor@1.0.3": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:buffer@3.6.0": {
      "base64-js": "npm:base64-js@0.0.8",
      "child_process": "github:jspm/nodelibs-child_process@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "ieee754": "npm:ieee754@1.1.6",
      "isarray": "npm:isarray@1.0.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:chalk@1.1.3": {
      "ansi-styles": "npm:ansi-styles@2.2.1",
      "escape-string-regexp": "npm:escape-string-regexp@1.0.5",
      "has-ansi": "npm:has-ansi@2.0.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "strip-ansi": "npm:strip-ansi@3.0.1",
      "supports-color": "npm:supports-color@2.0.0"
    },
    "npm:cipher-base@1.0.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "inherits": "npm:inherits@2.0.1",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "string_decoder": "github:jspm/nodelibs-string_decoder@0.1.0"
    },
    "npm:clone@1.0.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "vm": "github:jspm/nodelibs-vm@0.1.0"
    },
    "npm:code-point-at@1.0.0": {
      "number-is-nan": "npm:number-is-nan@1.0.0"
    },
    "npm:columnify@1.5.4": {
      "process": "github:jspm/nodelibs-process@0.1.2",
      "strip-ansi": "npm:strip-ansi@3.0.1",
      "wcwidth": "npm:wcwidth@1.0.1"
    },
    "npm:concat-stream@1.5.1": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "inherits": "npm:inherits@2.0.1",
      "readable-stream": "npm:readable-stream@2.0.6",
      "typedarray": "npm:typedarray@0.0.6"
    },
    "npm:configstore@2.0.0": {
      "dot-prop": "npm:dot-prop@2.4.0",
      "graceful-fs": "npm:graceful-fs@4.1.4",
      "mkdirp": "npm:mkdirp@0.5.1",
      "object-assign": "npm:object-assign@4.1.0",
      "os-tmpdir": "npm:os-tmpdir@1.0.1",
      "osenv": "npm:osenv@0.1.3",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "uuid": "npm:uuid@2.0.2",
      "write-file-atomic": "npm:write-file-atomic@1.1.4",
      "xdg-basedir": "npm:xdg-basedir@2.0.0"
    },
    "npm:constants-browserify@0.0.1": {
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:core-js@1.2.6": {
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:core-util-is@1.0.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0"
    },
    "npm:create-ecdh@4.0.0": {
      "bn.js": "npm:bn.js@4.11.4",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "elliptic": "npm:elliptic@6.3.1"
    },
    "npm:create-error-class@3.0.2": {
      "capture-stack-trace": "npm:capture-stack-trace@1.0.0"
    },
    "npm:create-hash@1.1.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "cipher-base": "npm:cipher-base@1.0.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "inherits": "npm:inherits@2.0.1",
      "ripemd160": "npm:ripemd160@1.0.1",
      "sha.js": "npm:sha.js@2.4.5"
    },
    "npm:create-hmac@1.1.4": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-hash": "npm:create-hash@1.1.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "inherits": "npm:inherits@2.0.1",
      "stream": "github:jspm/nodelibs-stream@0.1.0"
    },
    "npm:crypto-browserify@3.11.0": {
      "browserify-cipher": "npm:browserify-cipher@1.0.0",
      "browserify-sign": "npm:browserify-sign@4.0.0",
      "create-ecdh": "npm:create-ecdh@4.0.0",
      "create-hash": "npm:create-hash@1.1.2",
      "create-hmac": "npm:create-hmac@1.1.4",
      "diffie-hellman": "npm:diffie-hellman@5.0.2",
      "inherits": "npm:inherits@2.0.1",
      "pbkdf2": "npm:pbkdf2@3.0.4",
      "public-encrypt": "npm:public-encrypt@4.0.0",
      "randombytes": "npm:randombytes@2.0.3"
    },
    "npm:debug@2.2.0": {
      "ms": "npm:ms@0.7.1"
    },
    "npm:deep-extend@0.4.1": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0"
    },
    "npm:defaults@1.0.3": {
      "clone": "npm:clone@1.0.2"
    },
    "npm:des.js@1.0.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "inherits": "npm:inherits@2.0.1",
      "minimalistic-assert": "npm:minimalistic-assert@1.0.0"
    },
    "npm:detect-indent@4.0.0": {
      "repeating": "npm:repeating@2.0.1"
    },
    "npm:diffie-hellman@5.0.2": {
      "bn.js": "npm:bn.js@4.11.4",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "miller-rabin": "npm:miller-rabin@4.0.0",
      "randombytes": "npm:randombytes@2.0.3",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:dot-prop@2.4.0": {
      "is-obj": "npm:is-obj@1.0.1"
    },
    "npm:duplexer2@0.1.4": {
      "readable-stream": "npm:readable-stream@2.0.6"
    },
    "npm:elliptic@6.3.1": {
      "bn.js": "npm:bn.js@4.11.4",
      "brorand": "npm:brorand@1.0.5",
      "hash.js": "npm:hash.js@1.0.3",
      "inherits": "npm:inherits@2.0.1",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:error-ex@1.3.0": {
      "is-arrayish": "npm:is-arrayish@0.2.1",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:evp_bytestokey@1.0.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-hash": "npm:create-hash@1.1.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0"
    },
    "npm:fs.realpath@1.0.0": {
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:glob@7.0.5": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "fs.realpath": "npm:fs.realpath@1.0.0",
      "inflight": "npm:inflight@1.0.5",
      "inherits": "npm:inherits@2.0.1",
      "minimatch": "npm:minimatch@3.0.2",
      "once": "npm:once@1.3.3",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "path-is-absolute": "npm:path-is-absolute@1.0.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:got@5.6.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-error-class": "npm:create-error-class@3.0.2",
      "duplexer2": "npm:duplexer2@0.1.4",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "http": "github:jspm/nodelibs-http@1.7.1",
      "https": "github:jspm/nodelibs-https@0.1.0",
      "is-plain-obj": "npm:is-plain-obj@1.1.0",
      "is-redirect": "npm:is-redirect@1.0.0",
      "is-retry-allowed": "npm:is-retry-allowed@1.0.0",
      "is-stream": "npm:is-stream@1.1.0",
      "lowercase-keys": "npm:lowercase-keys@1.0.0",
      "node-status-codes": "npm:node-status-codes@1.0.0",
      "object-assign": "npm:object-assign@4.1.0",
      "parse-json": "npm:parse-json@2.2.0",
      "pinkie-promise": "npm:pinkie-promise@2.0.1",
      "querystring": "github:jspm/nodelibs-querystring@0.1.0",
      "read-all-stream": "npm:read-all-stream@3.1.0",
      "readable-stream": "npm:readable-stream@2.0.6",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2",
      "timed-out": "npm:timed-out@2.0.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "url-parse-lax": "npm:url-parse-lax@1.0.0"
    },
    "npm:graceful-fs@4.1.4": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "constants": "github:jspm/nodelibs-constants@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:has-ansi@2.0.0": {
      "ansi-regex": "npm:ansi-regex@2.0.0"
    },
    "npm:has@1.0.1": {
      "function-bind": "npm:function-bind@1.1.0"
    },
    "npm:hash.js@1.0.3": {
      "inherits": "npm:inherits@2.0.1"
    },
    "npm:http-proxy-agent@1.0.0": {
      "agent-base": "npm:agent-base@2.0.1",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "debug": "npm:debug@2.2.0",
      "extend": "npm:extend@3.0.0",
      "net": "github:jspm/nodelibs-net@0.1.2",
      "tls": "github:jspm/nodelibs-tls@0.1.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:https-browserify@0.0.0": {
      "http": "github:jspm/nodelibs-http@1.7.1"
    },
    "npm:https-proxy-agent@1.0.0": {
      "agent-base": "npm:agent-base@2.0.1",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "debug": "npm:debug@2.2.0",
      "extend": "npm:extend@3.0.0",
      "net": "github:jspm/nodelibs-net@0.1.2",
      "tls": "github:jspm/nodelibs-tls@0.1.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:inflight@1.0.5": {
      "once": "npm:once@1.3.3",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "wrappy": "npm:wrappy@1.0.2"
    },
    "npm:inherits@2.0.1": {
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:ini@1.3.4": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:invariant@2.2.1": {
      "loose-envify": "npm:loose-envify@1.2.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:is-absolute@0.2.5": {
      "is-relative": "npm:is-relative@0.2.1",
      "is-windows": "npm:is-windows@0.1.1"
    },
    "npm:is-finite@1.0.1": {
      "number-is-nan": "npm:number-is-nan@1.0.0"
    },
    "npm:is-fullwidth-code-point@1.0.0": {
      "number-is-nan": "npm:number-is-nan@1.0.0"
    },
    "npm:is-npm@1.0.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:is-relative@0.2.1": {
      "is-unc-path": "npm:is-unc-path@0.1.1"
    },
    "npm:is-unc-path@0.1.1": {
      "unc-path-regex": "npm:unc-path-regex@0.1.2"
    },
    "npm:is-windows@0.1.1": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:isobject@2.1.0": {
      "isarray": "npm:isarray@1.0.0"
    },
    "npm:latest-version@2.0.0": {
      "package-json": "npm:package-json@2.3.2"
    },
    "npm:lockfile@1.0.1": {
      "constants": "github:jspm/nodelibs-constants@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "os": "github:jspm/nodelibs-os@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:loose-envify@1.2.0": {
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "js-tokens": "npm:js-tokens@1.0.3",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:make-error-cause@1.1.1": {
      "make-error": "npm:make-error@1.1.1"
    },
    "npm:miller-rabin@4.0.0": {
      "bn.js": "npm:bn.js@4.11.4",
      "brorand": "npm:brorand@1.0.5"
    },
    "npm:minimatch@3.0.2": {
      "brace-expansion": "npm:brace-expansion@1.1.5",
      "path": "github:jspm/nodelibs-path@0.1.0"
    },
    "npm:mkdirp@0.5.1": {
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "minimist": "npm:minimist@0.0.8",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:nopt@1.0.10": {
      "abbrev": "npm:abbrev@1.0.9",
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:object.pick@1.1.2": {
      "isobject": "npm:isobject@2.1.0"
    },
    "npm:once@1.3.3": {
      "wrappy": "npm:wrappy@1.0.2"
    },
    "npm:os-browserify@0.1.2": {
      "os": "github:jspm/nodelibs-os@0.1.0"
    },
    "npm:os-homedir@1.0.1": {
      "os": "github:jspm/nodelibs-os@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:os-tmpdir@1.0.1": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:osenv@0.1.3": {
      "child_process": "github:jspm/nodelibs-child_process@0.1.0",
      "os-homedir": "npm:os-homedir@1.0.1",
      "os-tmpdir": "npm:os-tmpdir@1.0.1",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:package-json@2.3.2": {
      "got": "npm:got@5.6.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "rc": "npm:rc@1.1.6",
      "registry-url": "npm:registry-url@3.1.0",
      "semver": "npm:semver@5.2.0",
      "url": "github:jspm/nodelibs-url@0.1.0"
    },
    "npm:pako@0.2.8": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:parse-asn1@5.0.0": {
      "asn1.js": "npm:asn1.js@4.6.2",
      "browserify-aes": "npm:browserify-aes@1.0.6",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-hash": "npm:create-hash@1.1.2",
      "evp_bytestokey": "npm:evp_bytestokey@1.0.0",
      "pbkdf2": "npm:pbkdf2@3.0.4",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:parse-json@2.2.0": {
      "error-ex": "npm:error-ex@1.3.0"
    },
    "npm:path-browserify@0.0.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:path-is-absolute@1.0.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:pbkdf2@3.0.4": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "child_process": "github:jspm/nodelibs-child_process@0.1.0",
      "create-hmac": "npm:create-hmac@1.1.4",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:pinkie-promise@2.0.1": {
      "pinkie": "npm:pinkie@2.0.4"
    },
    "npm:popsicle-proxy-agent@1.0.0": {
      "http-proxy-agent": "npm:http-proxy-agent@1.0.0",
      "https-proxy-agent": "npm:https-proxy-agent@1.0.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "url": "github:jspm/nodelibs-url@0.1.0"
    },
    "npm:popsicle-retry@2.0.0": {
      "any-promise": "npm:any-promise@1.3.0"
    },
    "npm:popsicle@5.0.1": {
      "any-promise": "npm:any-promise@1.3.0",
      "arrify": "npm:arrify@1.0.1",
      "concat-stream": "npm:concat-stream@1.5.1",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "http": "github:jspm/nodelibs-http@1.7.1",
      "https": "github:jspm/nodelibs-https@0.1.0",
      "make-error-cause": "npm:make-error-cause@1.1.1",
      "methods": "npm:methods@1.1.2",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "querystring": "github:jspm/nodelibs-querystring@0.1.0",
      "stream": "github:jspm/nodelibs-stream@0.1.0",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "xtend": "npm:xtend@4.0.1",
      "zlib": "github:jspm/nodelibs-zlib@0.1.0"
    },
    "npm:process-nextick-args@1.0.7": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:process@0.11.5": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "vm": "github:jspm/nodelibs-vm@0.1.0"
    },
    "npm:promise-finally@2.2.1": {
      "any-promise": "npm:any-promise@1.3.0"
    },
    "npm:public-encrypt@4.0.0": {
      "bn.js": "npm:bn.js@4.11.4",
      "browserify-rsa": "npm:browserify-rsa@4.0.1",
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "create-hash": "npm:create-hash@1.1.2",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "parse-asn1": "npm:parse-asn1@5.0.0",
      "randombytes": "npm:randombytes@2.0.3"
    },
    "npm:punycode@1.3.2": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:randombytes@2.0.3": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:rc@1.1.6": {
      "deep-extend": "npm:deep-extend@0.4.1",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "ini": "npm:ini@1.3.4",
      "minimist": "npm:minimist@1.2.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "strip-json-comments": "npm:strip-json-comments@1.0.4"
    },
    "npm:read-all-stream@3.1.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "pinkie-promise": "npm:pinkie-promise@2.0.1",
      "readable-stream": "npm:readable-stream@2.0.6",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:readable-stream@1.1.14": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "core-util-is": "npm:core-util-is@1.0.2",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "inherits": "npm:inherits@2.0.1",
      "isarray": "npm:isarray@0.0.1",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "stream-browserify": "npm:stream-browserify@1.0.0",
      "string_decoder": "npm:string_decoder@0.10.31"
    },
    "npm:readable-stream@2.0.6": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "core-util-is": "npm:core-util-is@1.0.2",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "inherits": "npm:inherits@2.0.1",
      "isarray": "npm:isarray@1.0.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "process-nextick-args": "npm:process-nextick-args@1.0.7",
      "string_decoder": "npm:string_decoder@0.10.31",
      "util-deprecate": "npm:util-deprecate@1.0.2"
    },
    "npm:reflect-metadata@0.1.2": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:registry-url@3.1.0": {
      "rc": "npm:rc@1.1.6"
    },
    "npm:repeating@2.0.1": {
      "is-finite": "npm:is-finite@1.0.1"
    },
    "npm:rimraf@2.5.2": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "glob": "npm:glob@7.0.5",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:ripemd160@1.0.1": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:rxjs@5.0.0-beta.2": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:semver-diff@2.1.0": {
      "semver": "npm:semver@5.2.0"
    },
    "npm:semver@5.0.3": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:semver@5.2.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:sha.js@2.4.5": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "inherits": "npm:inherits@2.0.1",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:slide@1.1.6": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:sort-keys@1.1.2": {
      "is-plain-obj": "npm:is-plain-obj@1.1.0"
    },
    "npm:stream-browserify@1.0.0": {
      "events": "github:jspm/nodelibs-events@0.1.1",
      "inherits": "npm:inherits@2.0.1",
      "readable-stream": "npm:readable-stream@1.1.14"
    },
    "npm:string-width@1.0.1": {
      "code-point-at": "npm:code-point-at@1.0.0",
      "is-fullwidth-code-point": "npm:is-fullwidth-code-point@1.0.0",
      "strip-ansi": "npm:strip-ansi@3.0.1"
    },
    "npm:string_decoder@0.10.31": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0"
    },
    "npm:strip-ansi@3.0.1": {
      "ansi-regex": "npm:ansi-regex@2.0.0"
    },
    "npm:strip-bom@2.0.0": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "is-utf8": "npm:is-utf8@0.2.1"
    },
    "npm:strip-json-comments@1.0.4": {
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2"
    },
    "npm:supports-color@2.0.0": {
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:thenify@3.2.0": {
      "any-promise": "npm:any-promise@1.3.0",
      "assert": "github:jspm/nodelibs-assert@0.1.0"
    },
    "npm:timers-browserify@1.4.2": {
      "process": "npm:process@0.11.5"
    },
    "npm:touch@1.0.0": {
      "constants": "github:jspm/nodelibs-constants@0.1.0",
      "fs": "github:jspm/nodelibs-fs@0.1.2",
      "nopt": "npm:nopt@1.0.10",
      "path": "github:jspm/nodelibs-path@0.1.0"
    },
    "npm:typescript@1.8.9": {
      "os": "github:jspm/nodelibs-os@0.1.0"
    },
    "npm:typings-core@0.2.16": {
      "any-promise": "npm:any-promise@1.3.0",
      "array-uniq": "npm:array-uniq@1.0.3",
      "configstore": "npm:configstore@2.0.0",
      "debug": "npm:debug@2.2.0",
      "detect-indent": "npm:detect-indent@4.0.0",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "graceful-fs": "npm:graceful-fs@4.1.4",
      "has": "npm:has@1.0.1",
      "invariant": "npm:invariant@2.2.1",
      "is-absolute": "npm:is-absolute@0.2.5",
      "lockfile": "npm:lockfile@1.0.1",
      "make-error-cause": "npm:make-error-cause@1.1.1",
      "mkdirp": "npm:mkdirp@0.5.1",
      "object.pick": "npm:object.pick@1.1.2",
      "parse-json": "npm:parse-json@2.2.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "popsicle": "npm:popsicle@5.0.1",
      "popsicle-proxy-agent": "npm:popsicle-proxy-agent@1.0.0",
      "popsicle-retry": "npm:popsicle-retry@2.0.0",
      "popsicle-status": "npm:popsicle-status@1.0.2",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "promise-finally": "npm:promise-finally@2.2.1",
      "querystring": "github:jspm/nodelibs-querystring@0.1.0",
      "rc": "npm:rc@1.1.6",
      "rimraf": "npm:rimraf@2.5.2",
      "sort-keys": "npm:sort-keys@1.1.2",
      "string-template": "npm:string-template@1.0.0",
      "strip-bom": "npm:strip-bom@2.0.0",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2",
      "thenify": "npm:thenify@3.2.0",
      "throat": "npm:throat@2.0.2",
      "touch": "npm:touch@1.0.0",
      "typescript": "npm:typescript@1.8.9",
      "url": "github:jspm/nodelibs-url@0.1.0",
      "xtend": "npm:xtend@4.0.1",
      "zip-object": "npm:zip-object@0.1.0"
    },
    "npm:typings@0.7.12": {
      "any-promise": "npm:any-promise@1.3.0",
      "archy": "npm:archy@1.0.0",
      "bluebird": "npm:bluebird@3.4.1",
      "chalk": "npm:chalk@1.1.3",
      "columnify": "npm:columnify@1.5.4",
      "events": "github:jspm/nodelibs-events@0.1.1",
      "listify": "npm:listify@1.0.0",
      "minimist": "npm:minimist@1.2.0",
      "os": "github:jspm/nodelibs-os@0.1.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "systemjs-json": "github:systemjs/plugin-json@0.1.2",
      "typings-core": "npm:typings-core@0.2.16",
      "update-notifier": "npm:update-notifier@0.6.3",
      "wordwrap": "npm:wordwrap@1.0.0",
      "xtend": "npm:xtend@4.0.1"
    },
    "npm:update-notifier@0.6.3": {
      "boxen": "npm:boxen@0.3.1",
      "chalk": "npm:chalk@1.1.3",
      "child_process": "github:jspm/nodelibs-child_process@0.1.0",
      "configstore": "npm:configstore@2.0.0",
      "is-npm": "npm:is-npm@1.0.0",
      "latest-version": "npm:latest-version@2.0.0",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "semver-diff": "npm:semver-diff@2.1.0"
    },
    "npm:url-parse-lax@1.0.0": {
      "prepend-http": "npm:prepend-http@1.0.4",
      "url": "github:jspm/nodelibs-url@0.1.0"
    },
    "npm:url@0.10.3": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "punycode": "npm:punycode@1.3.2",
      "querystring": "npm:querystring@0.2.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:util-deprecate@1.0.2": {
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:util@0.10.3": {
      "inherits": "npm:inherits@2.0.1",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:uuid@2.0.2": {
      "assert": "github:jspm/nodelibs-assert@0.1.0",
      "child_process": "github:jspm/nodelibs-child_process@0.1.0",
      "crypto": "github:jspm/nodelibs-crypto@0.1.0",
      "os": "github:jspm/nodelibs-os@0.1.0",
      "util": "github:jspm/nodelibs-util@0.1.0"
    },
    "npm:vm-browserify@0.0.4": {
      "indexof": "npm:indexof@0.0.1"
    },
    "npm:wcwidth@1.0.1": {
      "defaults": "npm:defaults@1.0.3"
    },
    "npm:widest-line@1.0.0": {
      "string-width": "npm:string-width@1.0.1"
    },
    "npm:write-file-atomic@1.1.4": {
      "graceful-fs": "npm:graceful-fs@4.1.4",
      "imurmurhash": "npm:imurmurhash@0.1.4",
      "process": "github:jspm/nodelibs-process@0.1.2",
      "slide": "npm:slide@1.1.6"
    },
    "npm:xdg-basedir@2.0.0": {
      "os-homedir": "npm:os-homedir@1.0.1",
      "path": "github:jspm/nodelibs-path@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    },
    "npm:zone.js@0.6.12": {
      "buffer": "github:jspm/nodelibs-buffer@0.1.0",
      "process": "github:jspm/nodelibs-process@0.1.2"
    }
  }
});
