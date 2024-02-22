"""Methods and classes that are not marked with the @public_api decorator but may appear in our public docs are listed here.

Over time this list should be driven to 0 by either adding the @public_api decorator and an appropriate docstring or
adding an exclude directive to docs/sphinx_api_docs_source/public_api_excludes.py
"""

ITEMS_IGNORED_FROM_PUBLIC_API = [
    "File: great_expectations/checkpoint/actions.py Name: _run",
    "File: great_expectations/compatibility/not_imported.py Name: is_version_greater_or_equal",
    "File: great_expectations/compatibility/typing_extensions.py Name: override",
    "File: great_expectations/core/batch.py Name: head",
    "File: great_expectations/core/batch_spec.py Name: to_json_dict",
    "File: great_expectations/core/expectation_diagnostics/expectation_doctor.py Name: print_diagnostic_checklist",
    "File: great_expectations/core/expectation_diagnostics/expectation_doctor.py Name: run_diagnostics",
    "File: great_expectations/core/expectation_suite.py Name: show_expectations_by_expectation_type",
    "File: great_expectations/core/factory/factory.py Name: add",
    "File: great_expectations/core/factory/factory.py Name: delete",
    "File: great_expectations/core/factory/factory.py Name: get",
    "File: great_expectations/core/util.py Name: convert_to_json_serializable",
    "File: great_expectations/data_asset/data_asset.py Name: DataAsset",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: add_datasource",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: add_expectation_suite",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: add_or_update_checkpoint",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: add_or_update_expectation_suite",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: get_docs_sites_urls",
    "File: great_expectations/data_context/data_context/abstract_data_context.py Name: open_data_docs",
    "File: great_expectations/data_context/data_context/context_factory.py Name: get_context",
    "File: great_expectations/data_context/store/_store_backend.py Name: add",
    "File: great_expectations/data_context/store/_store_backend.py Name: update",
    "File: great_expectations/data_context/store/checkpoint_store.py Name: add_or_update_checkpoint",
    "File: great_expectations/data_context/store/checkpoint_store.py Name: get_checkpoint",
    "File: great_expectations/data_context/store/database_store_backend.py Name: DatabaseStoreBackend",
    "File: great_expectations/data_context/store/expectations_store.py Name: ExpectationsStore",
    "File: great_expectations/data_context/store/metric_store.py Name: MetricStore",
    "File: great_expectations/data_context/store/store.py Name: add",
    "File: great_expectations/data_context/store/store.py Name: update",
    "File: great_expectations/data_context/store/tuple_store_backend.py Name: TupleAzureBlobStoreBackend",
    "File: great_expectations/data_context/store/tuple_store_backend.py Name: TupleFilesystemStoreBackend",
    "File: great_expectations/data_context/store/tuple_store_backend.py Name: TupleGCSStoreBackend",
    "File: great_expectations/data_context/store/tuple_store_backend.py Name: TupleS3StoreBackend",
    "File: great_expectations/data_context/store/validation_results_store.py Name: ValidationResultsStore",
    "File: great_expectations/data_context/types/base.py Name: update",
    "File: great_expectations/data_context/types/resource_identifiers.py Name: GXCloudIdentifier",
    "File: great_expectations/datasource/datasource_dict.py Name: add_dataframe_asset",
    "File: great_expectations/datasource/fluent/config.py Name: get_datasource",
    "File: great_expectations/datasource/fluent/config.py Name: pop",
    "File: great_expectations/datasource/fluent/config.py Name: yaml",
    "File: great_expectations/datasource/fluent/config_str.py Name: ConfigStr",
    "File: great_expectations/datasource/fluent/file_path_data_asset.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/datasource/fluent/fluent_base_model.py Name: dict",
    "File: great_expectations/datasource/fluent/fluent_base_model.py Name: yaml",
    "File: great_expectations/datasource/fluent/pandas_datasource.py Name: dict",
    "File: great_expectations/datasource/fluent/pandas_datasource.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/datasource/fluent/sources.py Name: add_datasource",
    "File: great_expectations/datasource/fluent/sources.py Name: delete_datasource",
    "File: great_expectations/datasource/fluent/spark_datasource.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/datasource/fluent/sql_datasource.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/datasource/new_datasource.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/exceptions/exceptions.py Name: InvalidExpectationConfigurationError",
    "File: great_expectations/expectations/core/expect_column_values_to_match_like_pattern_list.py Name: validate_configuration",
    "File: great_expectations/expectations/core/expect_column_values_to_not_match_like_pattern_list.py Name: validate_configuration",
    "File: great_expectations/expectations/expectation.py Name: validate_configuration",
    "File: great_expectations/expectations/expectation_configuration.py Name: to_domain_obj",
    "File: great_expectations/expectations/metrics/map_metric_provider/column_pair_condition_partial.py Name: column_pair_condition_partial",
    "File: great_expectations/expectations/metrics/map_metric_provider/multicolumn_condition_partial.py Name: multicolumn_condition_partial",
    "File: great_expectations/expectations/regex_based_column_map_expectation.py Name: register_metric",
    "File: great_expectations/expectations/set_based_column_map_expectation.py Name: register_metric",
    "File: great_expectations/expectations/set_based_column_map_expectation.py Name: validate_configuration",
    "File: great_expectations/experimental/datasource/fabric.py Name: build_batch_request",
    "File: great_expectations/experimental/datasource/fabric.py Name: get_batch_list_from_batch_request",
    "File: great_expectations/render/renderer/email_renderer.py Name: EmailRenderer",
    "File: great_expectations/render/renderer/microsoft_teams_renderer.py Name: MicrosoftTeamsRenderer",
    "File: great_expectations/render/renderer/opsgenie_renderer.py Name: OpsgenieRenderer",
    "File: great_expectations/render/renderer/renderer.py Name: renderer",
    "File: great_expectations/render/renderer/site_builder.py Name: DefaultSiteIndexBuilder",
    "File: great_expectations/render/renderer/site_builder.py Name: SiteBuilder",
    "File: great_expectations/render/renderer/slack_renderer.py Name: SlackRenderer",
    "File: great_expectations/rule_based_profiler/data_assistant_result/data_assistant_result.py Name: to_json_dict",
    "File: great_expectations/rule_based_profiler/helpers/util.py Name: build_batch_request",
    "File: great_expectations/rule_based_profiler/rule_based_profiler.py Name: run",
    "File: great_expectations/rule_based_profiler/rule_based_profiler.py Name: to_json_dict",
    "File: great_expectations/validator/validation_graph.py Name: resolve",
    "File: great_expectations/data_context/store/checkpoint_store.py Name: CheckpointStore",
    "File: great_expectations/data_context/store/metric_store.py Name: EvaluationParameterStore",
    "File: great_expectations/data_context/store/query_store.py Name: SqlAlchemyQueryStore",
]
