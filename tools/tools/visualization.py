from tools.tool import Tool, ArgumentType


visualization_tool = (Tool().name("VisualizationTool")
                      .description(" This is a tool that finds user created visualizations. "
                                   "The tool returns matching visualizations")
                      .argument("name",
                                ArgumentType.REQUIRED,
                                "It takes 1 required argument named input which defines the visualization name to "
                                "search for"))
