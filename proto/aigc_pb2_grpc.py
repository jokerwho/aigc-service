# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import aigc_pb2 as aigc__pb2


class OpenAIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Completion = channel.unary_unary(
            "/aigc.OpenAI/Completion",
            request_serializer=aigc__pb2.OpenAICreateCompletionRequest.SerializeToString,
            response_deserializer=aigc__pb2.OpenAICompletionResponse.FromString,
        )
        self.Chat = channel.unary_unary(
            "/aigc.OpenAI/Chat",
            request_serializer=aigc__pb2.OpenAICreateChatRequest.SerializeToString,
            response_deserializer=aigc__pb2.OpenAIChatResponse.FromString,
        )
        self.StreamCompletion = channel.unary_stream(
            "/aigc.OpenAI/StreamCompletion",
            request_serializer=aigc__pb2.OpenAICreateCompletionRequest.SerializeToString,
            response_deserializer=aigc__pb2.OpenAIStreamCompletionResponse.FromString,
        )
        self.StreamChat = channel.unary_stream(
            "/aigc.OpenAI/StreamChat",
            request_serializer=aigc__pb2.OpenAICreateChatRequest.SerializeToString,
            response_deserializer=aigc__pb2.OpenAIStreamChatResponse.FromString,
        )


class OpenAIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Completion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Chat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamCompletion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OpenAIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Completion": grpc.unary_unary_rpc_method_handler(
            servicer.Completion,
            request_deserializer=aigc__pb2.OpenAICreateCompletionRequest.FromString,
            response_serializer=aigc__pb2.OpenAICompletionResponse.SerializeToString,
        ),
        "Chat": grpc.unary_unary_rpc_method_handler(
            servicer.Chat,
            request_deserializer=aigc__pb2.OpenAICreateChatRequest.FromString,
            response_serializer=aigc__pb2.OpenAIChatResponse.SerializeToString,
        ),
        "StreamCompletion": grpc.unary_stream_rpc_method_handler(
            servicer.StreamCompletion,
            request_deserializer=aigc__pb2.OpenAICreateCompletionRequest.FromString,
            response_serializer=aigc__pb2.OpenAIStreamCompletionResponse.SerializeToString,
        ),
        "StreamChat": grpc.unary_stream_rpc_method_handler(
            servicer.StreamChat,
            request_deserializer=aigc__pb2.OpenAICreateChatRequest.FromString,
            response_serializer=aigc__pb2.OpenAIStreamChatResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "aigc.OpenAI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OpenAI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Completion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/aigc.OpenAI/Completion",
            aigc__pb2.OpenAICreateCompletionRequest.SerializeToString,
            aigc__pb2.OpenAICompletionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Chat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/aigc.OpenAI/Chat",
            aigc__pb2.OpenAICreateChatRequest.SerializeToString,
            aigc__pb2.OpenAIChatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StreamCompletion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/aigc.OpenAI/StreamCompletion",
            aigc__pb2.OpenAICreateCompletionRequest.SerializeToString,
            aigc__pb2.OpenAIStreamCompletionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StreamChat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/aigc.OpenAI/StreamChat",
            aigc__pb2.OpenAICreateChatRequest.SerializeToString,
            aigc__pb2.OpenAIStreamChatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
