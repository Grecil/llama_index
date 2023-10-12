# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class OpenAiEmbedding(pydantic.BaseModel):
    """
    OpenAI class for embeddings.

    Args:
        mode (str): Mode for embedding.
            Defaults to OpenAIEmbeddingMode.TEXT_SEARCH_MODE.
            Options are:

            - OpenAIEmbeddingMode.SIMILARITY_MODE
            - OpenAIEmbeddingMode.TEXT_SEARCH_MODE

        model (str): Model for embedding.
            Defaults to OpenAIEmbeddingModelType.TEXT_EMBED_ADA_002.
            Options are:

            - OpenAIEmbeddingModelType.DAVINCI
            - OpenAIEmbeddingModelType.CURIE
            - OpenAIEmbeddingModelType.BABBAGE
            - OpenAIEmbeddingModelType.ADA
            - OpenAIEmbeddingModelType.TEXT_EMBED_ADA_002

        deployment_name (Optional[str]): Optional deployment of model. Defaults to None.
            If this value is not None, mode and model will be ignored.
            Only available for using AzureOpenAI.
    """

    model_name: typing.Optional[str] = pydantic.Field(
        description="The name of the embedding model."
    )
    embed_batch_size: typing.Optional[int] = pydantic.Field(
        description="The batch size for embedding calls."
    )
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
    deployment_name: typing.Optional[str]
    additional_kwargs: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Additional kwargs for the OpenAI API."
    )
    api_key: typing.Optional[str] = pydantic.Field(description="The OpenAI API key.")
    api_type: typing.Optional[str] = pydantic.Field(description="The OpenAI API type.")
    api_base: str = pydantic.Field(description="The base URL for OpenAI API.")
    api_version: str = pydantic.Field(description="The API version for OpenAI API.")
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}