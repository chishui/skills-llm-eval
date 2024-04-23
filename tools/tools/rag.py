from tools.tool import Tool, ArgumentType, sort_arguments, size_start_index_arguments


rag_tool = (Tool().name("RAGTool")
            .description("This is a tool that retrieves OpenSearch related documents from knowledge base index and "
                         "provides context for Large Language Model to answer the user question. It returns the answer "
                         "from Large Language Model for the user question.")
            .argument("input",
                      ArgumentType.REQUIRED,
                      "input is user's question"))
