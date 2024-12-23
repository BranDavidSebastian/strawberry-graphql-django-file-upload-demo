import strawberry
from strawberry.file_uploads import Upload


@strawberry.type
class Query:
    hello: str = "world"


@strawberry.type
class Mutation:
    @strawberry.field
    def read_file(self, file: Upload) -> str:
        return file.read().decode("utf-8")


schema = strawberry.Schema(query=Query, mutation=Mutation)

