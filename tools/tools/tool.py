from enum import Enum


class ArgumentType(Enum):
    OPTIONAL = 1
    REQUIRED = 2


class Argument:
    def __init__(self, name, argument_type, description, default_value=None, options=None):
        self.name = name
        self.description = description
        self.default_value = default_value
        self.argument_type = argument_type
        self.options = options if options else []


class Tool:
    def __init__(self):
        self._name = ""
        self._description = ""
        self._arguments = []

    def name(self, name):
        self._name = name
        return self

    def description(self, description):
        self._description = description
        return self

    def argument(self, name, argument_type, description, default_value=None, options=None):
        self._arguments.append(Argument(name, argument_type, description, default_value, options))
        return self

    def arguments(self, arguments):
        self._arguments.extend(arguments)
        return self

    def generate_prompt(self):
        texts = [self._description, f'It has {len(self._arguments)} '
                                    f'{"arguments" if len(self._arguments) > 0 else "argument"}']
        for argument in self._arguments:
            texts.append(argument.description)

        texts = [text.rstrip().rstrip(".") for text in texts]
        return ". ".join(texts)


# common arguments
sort_arguments = [
    Argument("sortOrder",
             ArgumentType.OPTIONAL,
             "sortOrder defines the order of the results (options are ascending or descending, "
             "and default is ascending)",
             default_value="ascending",
             options=["ascending", "descending"]),
    Argument("sortString",
             ArgumentType.OPTIONAL,
             "sortString defines how to sort the results (default is name.keyword)",
             default_value="name.keyword")
]

size_start_index_arguments = [
    Argument("size",
             ArgumentType.OPTIONAL,
             "size defines the size of the request to be returned (default is 20)",
             20),
    Argument("startIndex",
             ArgumentType.OPTIONAL,
             "startIndex defines the index to start from (default is 0)",
             0)
]


