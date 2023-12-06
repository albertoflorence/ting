from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.find(lambda item: item["nome_do_arquivo"] == path_file):
        return

    data = txt_importer(path_file)
    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(info)
    print(info)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")

    item = instance.dequeue()
    print(f"Arquivo {item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
