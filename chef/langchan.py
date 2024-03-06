from decouple import config
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


def chef_model(recipe):
    SECRET_KEY = config("OPEN_API_KEY")
    chat = ChatOpenAI(openai_api_key = SECRET_KEY)
    SystemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "You are Chef so First intriduce You self. you can type any type of food recipe which can cooked in 5 minutes. you are only allowd to related food answer. if you don't know the answer then tell i don't know the answer."
    )
    HumanMessagePrompt = HumanMessagePromptTemplate.from_template(
        '{asked_recipe}'
    )
    chatPrompt = ChatPromptTemplate.from_messages([SystemMessagePrompt, HumanMessagePrompt])
    formatedChatPrompt = chatPrompt.format_messages(
        asked_recipe = recipe
    )
    response = chat.invoke(formatedChatPrompt)
    return response.content

