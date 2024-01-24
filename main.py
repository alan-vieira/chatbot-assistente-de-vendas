"""Módulo para criar e treinar um chatbot de vendas de curso em português.

Este módulo utiliza a biblioteca ChatterBot para criar um chatbot chamado Rose,
treiná-lo com um corpus em português e dados personalizados de vendas de curso,
e executar um loop de interações com o usuário.

"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


def criar_bot():
    """Cria uma instância do chatbot Rose.

    Returns:
        ChatBot: Instância do chatbot Rose configurado.
    """
    bot = ChatBot(
        'Rose',
        logic_adapters=['chatterbot.logic.BestMatch'],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3?check_same_thread=False',
        preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html']
        )
    return bot


def treinar_bot(bot):
    """Treina o chatbot com corpus em português e dados personalizados.

    Args:
        bot (ChatBot): Instância do chatbot Rose.
    """
    # Treinamento do corpus em português
    conversa_corpus = ChatterBotCorpusTrainer(bot)
    conversa_corpus.train('chatterbot.corpus.portuguese')

    # Treinamento personalizado com mensagens de vendas de curso
    conversa_lista = ListTrainer(bot)
    conversa_lista.train([
    'Olá, tudo bem?',
    'Olá! Sim, tudo bem, obrigado. E com você? Como posso ajudar?',
    'Estou interessado em seu curso de Análise de Dados. Poderia me fornecer \
    mais informações?',
    'Claro! O curso de Análise de Dados é um treinamento completo que aborda \
    todos os aspectos do tema. Ele é composto por 3 módulos e \
    60 aulas, abordando tópicos como ETL. Além disso, oferecemos suporte \
    individualizado para todos os alunos durante o curso.',
    'Qual o preço do curso?',
    'O preço do curso é de R$ 720,00. No entanto, oferecemos descontos para \
    grupos de 10 ou mais. Além disso, atualmente \
    estamos oferecendo um desconto especial de 10% para quem se inscrever até \
    o final do mês.',
    'O curso é reconhecido por empresas líderes em análise de dados?',
    'Sim, o curso é reconhecido por empresas líderes em análise de dados. \
    Além disso, oferecemos um certificado de conclusão do curso para aqueles \
    que concluírem o curso com sucesso.',
    'Posso experimentar o curso antes de me inscrever?',
    'Sim, oferecemos um período de 7 dias para que você possa experimentar o \
    curso antes de se comprometer.',
    'Não tenho conhecimento prévio em análise de dados. O curso é adequado \
    para mim?',
    'Sim, o curso é adequado para iniciantes e pessoas com alguma experiência\
    em análise de dados. Nosso conteúdo é progressivo, começando pelos \
    conceitos básicos e indo até os tópicos mais avançados.',
    'Muito obrigado pela informação. Vou considerar minha inscrição.',
    'Fico feliz em ajudar! Se você tiver alguma outra pergunta, não hesite \
    em perguntar. Estamos aqui para ajudar. Boa sorte com sua decisão!',
    'Quais são os métodos de pagamento disponíveis para o curso?',
    'Aceitamos pagamentos via cartão de crédito, transferência bancária e \
    boleto. Você pode escolher o método de pagamento que for mais conveniente \
    para você.',
    'Qual é a carga horária total do curso?',
    'O curso tem uma carga horária total de 40 horas, distribuídas pelos \
    três módulos. Cada aula tem a duração média de 40 minutos.',
    'Gostaria de saber mais sobre os instrutores do curso.',
    'Nossos instrutores são profissionais experientes na área de análise de \
    dados, com ampla experiência prática. Eles estão comprometidos em \
    proporcionar uma experiência de aprendizado de alta qualidade.',
    'Posso baixar as aulas para assistir offline?',
    'Sim, todas as aulas são disponibilizadas para download, permitindo que \
    você as assista offline a qualquer momento.',
    'Qual é a política de reembolso em caso de desistência?',
    'Oferecemos reembolso total para cancelamentos feitos até 7 dias após a \
    inscrição. Após esse período, o reembolso é feito de acordo com nossa \
    política. Recomendamos que você leia nossos termos e condições.',
    'O curso oferece certificado de conclusão?',
    'Sim, ao concluir o curso com sucesso, você receberá um certificado de \
    conclusão reconhecido pela nossa instituição.'
    ])


def executar_chat(bot):
    """Executa um loop de interações com o usuário.

    Args:
        bot (ChatBot): Instância do chatbot Rose.
    """
    print("Bem-vindo à assistente Rose! Como posso ajudar?")
    while True:
        try:
            resposta = bot.get_response(input("Cliente: "))
            if resposta.confidence > 0.2:
                print("Rose:", resposta)
            else:
                print("Desculpe, não entendi. Pode reformular a pergunta?")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Até logo!")
            break

if __name__ == "__main__":
    bot = criar_bot()
    treinar_bot(bot)
    executar_chat(bot)
