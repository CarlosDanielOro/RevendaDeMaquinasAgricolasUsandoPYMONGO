from pymongo import MongoClient

client = MongoClient('10.0.237.41',
                     username='193315',  
                     password='193315',  
                     authSource='193315',  
                     authMechanism='SCRAM-SHA-256')

db = client["193315"]
collection_maquinas = db["maquinas"]  #Collection referente a tabela Maquinas
collection_clientes = db["clientes"]  #Collection referente a tabela Clientes
collection_marcas = db["marcas"]  #Collection referente a tabela Marcas
collection_vendas = db["vendas"]  #Collection referente a tabela Vendas

# Funções para a tabela de Maquinas
def create_maquinas(data):
    result = collection_maquinas.insert_one(data)
    return result.inserted_id

def read_all_maquinas():
    return list(collection_maquinas.find())

def read_maquinas_by_id(maquina_id):
    return collection_maquinas.find_one({'_id': maquina_id})

def update_maquinas(maquina_id, data):
    result = collection_maquinas.update_one({'_id': maquina_id}, {'$set': data})
    return result.modified_count

def delete_maquinas(maquina_id):
    result = collection_maquinas.delete_one({'_id': maquina_id})
    return result.deleted_count

# Funções para a tabela de Clientes
def create_clientes(data):
    result = collection_clientes.insert_one(data)
    return result.inserted_id

def read_all_clientes():
    return list(collection_clientes.find())

def read_clientes_by_id(cliente_id):
    return collection_clientes.find_one({'_id': cliente_id})

def update_clientes(cliente_id, data):
    result = collection_clientes.update_one({'_id': cliente_id}, {'$set': data})
    return result.modified_count

def delete_clientes(cliente_id):
    result = collection_clientes.delete_one({'_id': cliente_id})
    return result.deleted_count

# Funções para a tabela de Marcas
def create_marcas(data):
    result = collection_marcas.insert_one(data)
    return result.inserted_id

def read_all_marcas():
    return list(collection_marcas.find())

def read_marcas_by_id(marca_id):
    return collection_marcas.find_one({'_id': marca_id})

def update_marcas(marca_id, data):
    result = collection_marcas.update_one({'_id': marca_id}, {'$set': data})
    return result.modified_count

def delete_marcas(marca_id):
    result = collection_marcas.delete_one({'_id': marca_id})
    return result.deleted_count

# Funções para a tabela de Vendas
def incluir_venda(data): 
    result = collection_vendas.insert_one(data) 
    return result.inserted_id


def alterar_vendas(venda_id, data): 
    result = collection_vendas.update_one({'_id': venda_id}, {'$set': data}) 
    return result.modified_count

def read_all_vendas():
    return list(collection_vendas.find())

def read_vendas_by_id(venda_id):
    return collection_vendas.find_one({'_id': venda_id})


def excluir_vendas(venda_id): 
     result = collection_vendas.delete_one({'_id': venda_id})
     return result.deleted_count


# Menu principal
while True:
    print("\nRevenda de Maquinas Agricolas")
    print("1. Maquinas")
    print("2. Clientes")
    print("3. Marcas")
    print("4. Vendas")
    print("9. Sair")

    opcao_classe = int(input("Escolha a classe (1 para Maquinas, 2 para Clientes, 3 para Marcas, 4 para Vendas, 9 para Sair): "))

    if opcao_classe == 9:
        break

    if opcao_classe == 1:  # Operações para maquinas
        while True:
            print("\nOperações para Maquinas:")
            print("1. Inserir nova maquina: ")
            print("2. Alterar maquina: ")
            print("3. Excluir maquina: ")
            print("4. Consultar maquina por id")
            print("5. Listar todas as maquinas")
            print("9. Voltar para o menu principal")

            opcao = int(input("Informe sua opcao: "))

            if opcao == 9:
                break

            match opcao:
                case 1:  # Inserir nova maquina
                    id_maquina = int(input("Informe ID do maquina: "))
                    modelo_maquina = input("Informe o modelo da maquina: ")
                    valor_maquina = int(input("Informe o valor da maquina: "))
                    horas_maquina = int(input("Informe as horas da maquina: "))
                    id_marca_maquina = int(input("Informe o ID da marca da maquina: "))
                    id_gerado_maquina = create_maquinas({"_id": id_maquina, 
                                                         'modelo_maquina':      modelo_maquina, 
                                                         'valor_maquina':       valor_maquina, 
                                                         'horas_maquina':       horas_maquina,
                                                         'id_marca_maquina':    id_marca_maquina})
                    print(f'Nova maquina criada com ID: {id_gerado_maquina}')

                case 2:  # Alterar uma maquina
                    id_maquina = int(input("Informe ID da maquina a ser alterada: "))
                    novo_modelo = input("Informe novo modelo da maquina (enter para manter): ")
                    novo_valor = input("Informe novo valor da maquina (enter para manter): ")
                    nova_horas = input("Informe nova hora de de uso da maquina (enter para manter): ")
                    novo_id_marca_maquina = input("Informe o ID da nova marca selecionada (enter para manter): ")

                    # Obtendo os dados atuais da maquina
                    maquina_atual = read_maquinas_by_id(id_maquina)

                    # Atualizando os campos se necessário
                    if novo_modelo != 0:
                        maquina_atual['modelo_maquina'] = novo_modelo
                    if novo_valor != 0:
                        maquina_atual['valor_maquina'] = novo_valor
                    if nova_horas != 0:
                        maquina_atual['horas_maquina'] = nova_horas
                    if novo_id_marca_maquina != 0:
                        maquina_atual['id_marca_maquina'] = novo_id_marca_maquina

                    # Realizando a atualização
                    update_result = update_maquinas(id_maquina, maquina_atual)
                    print(f'Número de documentos atualizados: {update_result}')

                case 3:  # Excluir maquina
                    id_maquina = int(input("Informe ID da maquina a ser excluída: "))
                    delete_result = delete_maquinas(id_maquina)
                    print(f'\nNúmero de documentos deletados: {delete_result}')

                case 4:  # Consultar maquina por id
                    id_maquina = int(input("Informe ID da maquina: "))
                    maquina = read_maquinas_by_id(id_maquina)
                    print(f'\nDocumento com ID {id_maquina}: {maquina}')

                case 5:  # Listar todas maquinas
                    maquina = read_all_maquinas()
                    print('\nTodas as maquinas:')
                    for m in maquina:
                        print(m)

                case 9:  # Sair do menu de Maquinas
                    break

    elif opcao_classe == 2:  # Operações para Clientes
        while True:
            print("\nOperações em Clientes")
            print("1. Incluir novo Cliente")
            print("2. Alterar Cliente")
            print("3. Excluir Cliente")
            print("4. Consultar Cliente por id")
            print("5. Listar todos Cliente")
            print("9. Voltar para o menu principal")

            opcao = int(input("Informe sua opcao: "))

            if opcao == 9:
                break

            match opcao:
                 case 1:  # Inserir novo Cliente
                        id_cliente = int(input("Informe o ID da Cliente: "))
                        cpf_cliente = int(input("Informe o CPF do cliente: ")) 
                        nome_cliente = input("Informe o nome do cliente: ") 
                        telefone_cliente = int(input("Informe o telefone do cliente: "))
                        cidade_cliente = input("Informe a cidade do cliente: ")
                        id_gerado_cliente = create_clientes({"_id": id_cliente,
                                                             'cpf_cliente':         cpf_cliente,
                                                             'nome_cliente':        nome_cliente,
                                                             'telefone_cliente':    telefone_cliente,
                                                             'cidade_cliente':      cidade_cliente})
                        print(f'Nova locacao criada com ID: {id_gerado_cliente}')
                 case 2:  # Alterar cliente
                        novo_id_cliente = int(input("Informe o ID do cliente a ser alterada: "))
                        novo_cpf_cliente = input("Informe o novo CPF do cliente (0 para manter): ")
                        novo_nome_cliente = input("Informe o novo nome do cliente (0 para manter): ")
                        novo_telefone_cliente = input("Informe o novo telefone do cliente (enter para manter): ")
                        nova_cidade = input("Informe a nova cidade do cliente (enter para manter): ")

                        # Obtendo os dados atuais do cliente
                        cliente_atual = read_clientes_by_id(id_cliente)

                        # Atualizando os campos se necessário
                        if novo_cpf_cliente != 0:
                            cliente_atual['cpf_cliente'] = novo_cpf_cliente
                        if novo_nome_cliente != 0:
                            cliente_atual['nome_cliente'] = novo_nome_cliente
                        if novo_telefone_cliente != 0:
                            cliente_atual['telefone_cliente'] = novo_telefone_cliente
                        if nova_cidade != 0:
                            cliente_atual['cidade_cliente'] = nova_cidade

                        # Realizando a atualização
                        update_result = update_clientes(id_cliente, cliente_atual)
                        print(f'Número de documentos atualizados: {update_result}')

                 case 3:  # Excluir cliente
                        id_cliente = int(input("Informe o ID do cliente a ser excluído: "))
                        delete_result = delete_clientes(id_cliente)
                        print(f'\nNúmero de documentos deletados: {delete_result}')

                 case 4:  # Consultar cliente por id
                        id_cliente = int(input("Informe ID do cliente: "))
                        cliente = read_clientes_by_id(id_cliente)
                        print(f'\nDocumento com ID {id_cliente}: {cliente}')

                 case 5:  # Listar todos cliente
                        cliente = read_all_clientes()
                        print('\nTodos os clientes:')
                        for c in cliente:
                            print(c)

                 case 9:  # Sair do menu de cliente
                        break
                
    elif opcao_classe == 3:  # Operações para marcas
        while True:
            print("\nOperações para Marcas")
            print("1. Incluir nova Marca")
            print("2. Alterar Marca")
            print("3. Excluir Marca")
            print("4. Consultar Marca por id")
            print("5. Listar todas Marca")
            print("9. Voltar para o menu principal")

            opcao = int(input("Informe sua opcao: "))

            if opcao == 9:
                break

            match opcao:
                 case 1:  # Inserir nova Marca
                    id_marca = int(input("Informe o ID da marca: "))
                    nome_marca = input("Informe o nome da marca: ")
                    id_gerado_marca = create_marcas({"_id":id_marca,
                                                     'nome_marca':  nome_marca})
                    print(f'Nova Marca criado com ID: {id_gerado_marca}')

                 case 2:  # Alterar Marca
                    id_marca = int(input("Informe o id da marca a ser alterado: "))
                    novo_nome_marca = input("Informe o novo nome da marca (enter para manter): ")

                    # Obtendo os dados atuais da marca
                    marca_atual = read_marcas_by_id(id_marca)

                    # Atualizando os campos se necessário
                    if novo_nome_marca != 0:
                        marca_atual['nome_marca'] = novo_nome_marca

                    # Realizando a atualização
                    update_result = update_marcas(id_marca, marca_atual)
                    print(f'Número de documentos atualizados: {update_result}')

                 case 3:  # Excluir marcas
                    id_marca = int(input("Informe o ID da marca a ser excluída: "))
                    delete_result = delete_marcas(id_marca)
                    print(f'Número de documentos deletados: {delete_result}')

                 case 4:  # Consultar marcas por id
                    id_marca = int(input("Informe o ID da marca: "))
                    marca = read_marcas_by_id(id_marca)
                    print(f'Documento com ID {id_marca}: {marca}')

                 case 5:  # Listar todas marcas
                    marcas = read_all_marcas()
                    print('\nTodas as marcas:')
                    for m in marcas:
                        print(m)


    elif opcao_classe == 4:  # Operações para venda
        while True:
            print("\nOperações para vendas")
            print("1. Incluir nova venda")
            print("2. Alterar venda")
            print("3. Excluir venda")
            print("5. Listar todas vendas")
            print("9. Voltar para o menu principal")

            opcao = int(input("Informe sua opcao: "))

            if opcao == 9:
                break

            match opcao:
                 case 1:  # Inserir novas vendas
                    id_venda = int(input("Informe o ID da venda: "))
                    data_venda = int(input("Informe a data da venda: "))
                    id_maquina_venda = int(input("Informe o ID da maquina vendida: "))
                    id_cliente_venda = int(input("Informe o ID do comprador: "))
                    id_gerado_venda = incluir_venda({"_id":                 id_venda,
                                                     'data_venda':          data_venda,
                                                     'id_maquina_venda':    id_maquina_venda,
                                                     'id_cliente_venda':    id_cliente_venda})
                    print(f'Nova venda criada com ID: {id_gerado_venda}')

                 case 2:  # Alterar vendas
                    id_venda = int(input("Informe o ID da venda a ser alterada: "))
                    nova_data_venda = input("Informe a nova data da venda (enter para manter): ")
                    novo_id_maquina_venda = input("Informe o ID da maquina vendida (enter para manter): ")
                    novo_id_cliente_venda = input("Informe o ID do comprador (enter para manter): ")

                    # Obtendo os dados atuais do vendas
                    venda_atual = read_vendas_by_id(id_venda)

                    # Atualizando os campos se necessário
                    if nova_data_venda != 0:
                        venda_atual['data_venda'] = nova_data_venda
                    if novo_id_maquina_venda != 0:
                        venda_atual['id_maquina_venda'] = novo_id_maquina_venda
                    if novo_id_cliente_venda != 0:
                        venda_atual['id_cliente_venda'] = novo_id_cliente_venda

                    # Realizando a atualização
                    update_result = alterar_vendas(id_venda, venda_atual)
                    print(f'Número de documentos atualizados: {update_result}')

                 case 3:  # Excluir venda
                    id_venda = int(input("Informe o ID da venda a ser excluída: "))
                    delete_result = excluir_vendas(id_venda)
                    print(f'Número de documentos deletados: {delete_result}')

                 case 4:  # Consultar venda por id
                    id_venda = int(input("Informe o ID da venda: "))
                    venda = read_vendas_by_id(id_venda)
                    print(f'Documento com ID {id_venda}: {venda}')

                 case 5:  # Listar todas Vendas
                    venda = read_all_vendas()
                    print('\nTodas as vendas:')
                    for v in venda:
                        print(v)

                 case 9:  # Sair do menu de vendas
                    break
                
            

    
