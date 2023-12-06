def create_search_by_word(word, instance, line_processor):
    return [
        {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [
                line_processor(i + 1, item["linhas_do_arquivo"][i])
                for i in range(item["qtd_linhas"])
                if word.lower() in item["linhas_do_arquivo"][i].lower()
            ],
        }
        for item in instance
        if any(
            word.lower() in line.lower() for line in item["linhas_do_arquivo"]
        )
    ]


def exists_word(word, instance):
    return create_search_by_word(
        word,
        instance,
        lambda line, _: {
            "linha": line,
        },
    )


def search_by_word(word, instance):
    return create_search_by_word(
        word,
        instance,
        lambda line, content: {
            "linha": line,
            "conteudo": content,
        },
    )
