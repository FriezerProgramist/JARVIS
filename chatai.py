import openai

openai.api_key = "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"

models = openai.Model.list()
#print(models)


def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
    )
    return copletion