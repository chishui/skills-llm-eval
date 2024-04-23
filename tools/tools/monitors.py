from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


search_monitor_tool = (Tool().name("SearchMonitorsTool")
                       .description("This is a tool that searches alerting monitors. It returns a list of monitors, "
                                    "and the total number of monitors.")
                       .argument("monitorId",
                                 ArgumentType.OPTIONAL,
                                 "monitorId defines the monitor ID to filter for (default is null)",
                                 default_value="null")
                       .argument("monitorName",
                                 ArgumentType.OPTIONAL,
                                 "monitorName defines explicit name of the monitor (default is null)",
                                 default_value="null")
                       .argument("monitorNamePattern",
                                 ArgumentType.OPTIONAL,
                                 "monitorNamePattern is a wildcard query to match monitor name (default is null)",
                                 default_value="null")
                       .argument("enabled",
                                 ArgumentType.OPTIONAL,
                                 "enabled defines whether the monitor is enabled (default is null, indicating both)",
                                 default_value="null")
                       .argument("hasTriggers",
                                 ArgumentType.OPTIONAL,
                                 "hasTriggers defines whether the monitor has triggers enabled (default is null, "
                                 "indicating both)",
                                 default_value="null")
                       .argument("indices",
                                 ArgumentType.OPTIONAL,
                                 "indices defines the index being monitored (default is null)",
                                 default_value="null")
                       .arguments(sort_arguments)
                       .arguments(size_start_index_arguments))
