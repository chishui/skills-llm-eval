from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


search_anomaly_detectors_tool = (Tool().name("SearchAnomalyDetectorsTool")
                                 .description("This is a tool that searches anomaly detectors, it returns the list of "
                                              "anomaly detectors, and the total number of anomaly detectors")
                                 .argument("detectorName",
                                           ArgumentType.OPTIONAL,
                                           "detectorName is the explicit name of the monitor (default is null)",
                                           default_value="null")
                                 .argument("detectorNamePattern",
                                           ArgumentType.OPTIONAL,
                                           "detectorNamePattern is a wildcard query to match detector name "
                                           "(default is null)",
                                           default_value="null")
                                 .argument("indices",
                                           ArgumentType.OPTIONAL,
                                           "indices defines the index being detected (default is null)",
                                           default_value="null")
                                 .argument("highCardinality",
                                           ArgumentType.OPTIONAL,
                                           "highCardinality defines whether the anomaly detector is high cardinality "
                                           "(default is null)",
                                           default_value="null")
                                 .argument("lastUpdateTime",
                                           ArgumentType.OPTIONAL,
                                           "lastUpdateTime defines the latest update time of the anomaly detector "
                                           "(default is null)",
                                           default_value="null")
                                 .arguments(sort_arguments)
                                 .arguments(size_start_index_arguments)
                                 .argument("running",
                                           ArgumentType.OPTIONAL,
                                           "running defines whether the anomaly detector is running (default is null, "
                                           "indicating both)",
                                           default_value="null")
                                 .argument("disabled",
                                           ArgumentType.OPTIONAL,
                                           "disabled defines whether the anomaly detector is disabled (default is null, "
                                           "indicating both)",
                                           default_value="null")
                                 .argument("failed",
                                           ArgumentType.OPTIONAL,
                                           "failed defines whether the anomaly detector has failed (default is null, "
                                           "indicating both)",
                                           default_value="null"))
