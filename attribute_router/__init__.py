def match(path, routes):
    for route in routes:
        match = route.match(path)
        if match is not None:
            return lambda *args, **kwargs: routes[route](*args, **kwargs, _match=match)


class Router:
    def __init__(self, routes={}, join_char="/"):
        self.__routes = routes
        self.__join_char = join_char

    def __getattr__(self, path):
        if path.startswith("__"):
            raise AttributeError(path)

        return Chain(self.__join_char + path, self.__routes, self.__join_char)

    def __call__(self, *paths):
        return Chain(
            self.__join_char + self.__join_char.join(paths),
            self.__routes,
            self.__join_char,
        )


class Chain:
    def __new__(cls, path, routes, join_char):
        method = match(path, routes)
        if method is not None:
            return method

        self = object.__new__(cls)
        self.__path = path
        self.__routes = routes
        self.__join_char = join_char

        return self

    def __getattr__(self, path):
        if path.startswith("__"):
            raise AttributeError(path)

        self.__path += self.__join_char + path

        method = match(self.__path, self.__routes)
        return method if method is not None else self

    def __call__(self, *paths):
        self.__path += self.__join_char + self.__join_char.join(paths)

        return self
