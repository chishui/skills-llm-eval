from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


search_anomaly_results_tool = (Tool().name("SearchAnomalyResultsTool")
                               .description("This is a tool that searches anomaly results. It returns a list of "
                                            "anomaly results, and the total number of anomaly result.")
                               .argument("detectorId",
                                         ArgumentType.OPTIONAL,
                                         "detectorId defines the detector ID to filter for (default is null)",
                                         default_value="null")
                               .argument("realtime",
                                         ArgumentType.OPTIONAL,
                                         "realtime defines whether the anomaly is real time (default is null)",
                                         default_value="null")
                               .argument("anomalyGradeThreshold",
                                         ArgumentType.OPTIONAL,
                                         "anomalyGradeThreshold defines the threshold for anomaly grade "
                                         "(a number between 0 and 1 that indicates how anomalous a data point is) "
                                         "(default is 0)",
                                         default_value=0)
                               .argument("dataStartTime",
                                         ArgumentType.OPTIONAL,
                                         "dataStartTime defines the start time of the anomaly query (default is null)",
                                         default_value="null")
                               .argument("dataEndTime",
                                         ArgumentType.OPTIONAL,
                                         "dataEndTime defines the end time of the anomaly query (default is null)",
                                         default_value="null")
                               .arguments(sort_arguments)
                               .arguments(size_start_index_arguments))
