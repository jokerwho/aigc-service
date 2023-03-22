import grpc
from concurrent import futures
from proto import aigc_pb2
from proto import aigc_pb2_grpc

from bots._openai import OpenAIClient


class OpenAIServer(aigc_pb2_grpc.OpenAIServicer):
    def Completion(self, request, context):
        prompt = request.prompt
        max_tokens = request.max_tokens or 2000
        temperature = request.temperature or 1.0
        top_p = request.top_p or 0.8
        openai_client = OpenAIClient()
        res = openai_client.completion(
            prompt,
            max_tokens=max_tokens,
            temperature=round(temperature, 1),
            top_p=round(top_p, 1),
        )
        response = aigc_pb2.OpenAICompletionResponse(
            id=res["id"],
            answer=res["choices"][0]["text"],
            usage=res["usage"]["total_tokens"],
        )
        return response

    def Chat(self, request, context):
        messages = request.messages
        max_tokens = request.max_tokens or 2000
        temperature = request.temperature or 0.7
        top_p = request.top_p or 0.8
        character = {0: "system", 1: "user", 2: "assistant"}
        messages = [
            {"role": character[msg.role], "content": msg.content} for msg in messages
        ]
        openai_client = OpenAIClient()
        res = openai_client.chat_completion(
            messages,
            max_tokens=max_tokens,
            temperature=round(temperature, 1),
            top_p=round(top_p, 1),
        )
        response = aigc_pb2.OpenAIChatResponse(
            id=res["id"],
            message=res["choices"][0]["message"],
            usage=res["usage"]["total_tokens"],
        )
        return response

    def StreamCompletion(self, request, context):
        prompt = request.prompt
        max_tokens = request.max_tokens or 2000
        temperature = request.temperature or 1.0
        top_p = request.top_p or 0.8
        openai_client = OpenAIClient()
        for res in openai_client.completion(
            prompt,
            max_tokens=max_tokens,
            temperature=round(temperature, 1),
            top_p=round(top_p, 1),
            stream=True,
        ):
            response = aigc_pb2.OpenAICompletionResponse(
                id=res["id"],
                answer=res["choices"][0]["text"],
                usage=0,  # HACK: change proto file
            )
            yield response

    def StreamChat(self, request, context):
        messages = request.messages
        max_tokens = request.max_tokens or 2000
        temperature = request.temperature or 0.7
        top_p = request.top_p or 0.8
        character = {0: "system", 1: "user", 2: "assistant"}
        messages = [
            {"role": character[msg.role], "content": msg.content} for msg in messages
        ]
        openai_client = OpenAIClient()
        for res in openai_client.chat_completion(
            messages,
            max_tokens=max_tokens,
            temperature=round(temperature, 1),
            top_p=round(top_p, 1),
            stream=True,
        ):
            response = aigc_pb2.OpenAIChatResponse(
                id=res["id"],
                message=res["choices"][0]["delta"],
                usage=0,  # HACK: change proto file
            )
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aigc_pb2_grpc.add_OpenAIServicer_to_server(OpenAIServer(), server)
    server.add_insecure_port("[::]:9000")
    server.start()
    print("Server started at [::]:9000")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
