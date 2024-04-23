from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


search_alerts_tool = (Tool().name("SearchAlertsTool")
                      .description("This is a tool that finds alert trigger information. "
                                   "The tool returns a list of alerts, and the total number of alerts.")
                      .arguments(sort_arguments)
                      .arguments(size_start_index_arguments)
                      .argument("searchString",
                                ArgumentType.OPTIONAL,
                                "searchString defines the search string to use for searching a specific alert "
                                "(default is an empty String)",
                                "")
                      .argument("severityLevel",
                                ArgumentType.OPTIONAL,
                                "severityLevel defines the severity level to filter for (default is ALL)",
                                "ALL")
                      .argument("alertState",
                                ArgumentType.OPTIONAL,
                                "alertState defines the alert state to filter for (default is ALL)",
                                "ALL")
                      .argument("monitorId",
                                ArgumentType.OPTIONAL,
                                "monitorId defines the monitor ID to filter for",
                                "null")
                      .argument("alertIndex",
                                ArgumentType.OPTIONAL,
                                "alertIndex defines the alert index to search from (default is null)",
                                "null")
                      .argument("monitorIds",
                                ArgumentType.OPTIONAL,
                                "monitorIds defines the list of monitor IDs to filter for",
                                "null")
                      .argument("workflowIds",
                                ArgumentType.OPTIONAL,
                                "workflowIds defines the list of workflow IDs to filter for（default is null)",
                                "null")
                      .argument("alertIds",
                                ArgumentType.OPTIONAL,
                                "alertIds defines the list of alert IDs to filter for (default is null)",
                                "null"))
