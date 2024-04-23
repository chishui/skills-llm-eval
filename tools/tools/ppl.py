from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


ppl_tool = (Tool().name("PPLTool")
            .description("This is a tool that generates PPL and execute. it returns the execute result by generated "
                         "PPL query.")
            .argument("index",
                      ArgumentType.REQUIRED,
                      "index defines the index PPL query will be executed")
            .argument("question",
                      ArgumentType.REQUIRED,
                      "question is the user question to generate the PPL query."))
