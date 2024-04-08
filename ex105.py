
def notas(*num, sit=False):
    """
    ->Função para avaliar notas e situações de vários alunos.
    :param num: Notas dos alunos avaliados (Aceita uma ou varias notas).
    :param sit: Opcional, devendo ser indicado se quer ou não adicinar a situação.
    :return: Retorna um dicionário com várias informações sobre as notas e a a situação do aluno.
    """
    dados = dict()
    dados['notas'] = num
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    dados['Média'] = sum(num) / len(num)
    if sit:
        if dados['Média'] < 5:
            dados['Situação'] = 'Reprovado'
        elif dados['Média'] < 7:
            dados['Situação'] = 'Em Recuperação'
        elif dados['Média'] >= 7:
            dados['Situação'] = 'Aprovado'
    return dados


resp = notas(5.5, 2.5, 10, 3, 5, 3.5, sit=True)
print(resp)


