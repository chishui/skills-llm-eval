from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


cat_index_tool = (Tool().name("CatIndexTool")
                  .description("This tool lists information related to indexes from the OpenSearch cluster, that is, "
                               "how much disk space they are using, how many shards they have, their health status, "
                               "and so on. It returns the indices information, including `health`, `status`, `index`, "
                               "`uuid`, `pri`, `rep`, `docs.count`, `docs.deleted`, `store.size`, `pri.store. size`, "
                               "`pri.store.size`, `pri.store`")
                  .argument("index",
                            ArgumentType.OPTIONAL,
                            "index is a comma-delimited list of one or more indices to get information from "
                            "(default is an empty list meaning all indices)",
                            default_value=[])
                  .argument("local",
                            ArgumentType.OPTIONAL,
                            "local means whether to return information from the local node only instead of the cluster "
                            "manager node (default is false)",
                            default_value=False))
