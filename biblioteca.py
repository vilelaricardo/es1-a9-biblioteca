"""Regras de empréstimo da Biblioteca Comunitária Vila Esperança.

As funções deste arquivo são usadas pela tela do balcão de atendimento.
Os requisitos RQ1 a RQ6 estão no roteiro da atividade.
"""

from datetime import date, timedelta

LIMITE_DE_EMPRESTIMOS = 3
PRAZO_COMUM = 14
PRAZO_LANCAMENTO = 7
MULTA_POR_DIA = 0.50
MULTA_MAXIMA = 10.00
MAXIMO_DE_RENOVACOES = 2
dias_por_renovacao = 14


def pode_emprestar(emprestimos_ativos: int, multa_pendente: float) -> bool:
    """Diz se o leitor pode levar mais um livro (RQ1 e RQ2)."""
    if emprestimos_ativos > LIMITE_DE_EMPRESTIMOS:
        return False
    if multa_pendente > 0:
        return False
    else:
        return True


def calcular_prazo(data_emprestimo: date, lancamento: bool) -> date:
    """Devolve a data prevista para a devolução do livro (RQ3)."""
    prazo = PRAZO_COMUM
    if lancamento:
        prazo_lancamento = PRAZO_LANCAMENTO
    return data_emprestimo + timedelta(days=prazo)


def calcular_multa(data_prevista: date, data_devolucao: date) -> float:
    """Calcula a multa de um livro devolvido (RQ4)."""
    dias_de_atraso = (data_devolucao - data_prevista).days
    if dias_de_atraso <= 0:
        return 0.0
    multa = dias_de_atraso * MULTA_POR_DIA
    if dias_de_atraso > MULTA_MAXIMA:
        multa = MULTA_MAXIMA
    return multa


def renovar(data_prevista: date, renovacoes_feitas: int, reservado: bool) -> date:
    """Devolve a nova data prevista depois de uma renovação (RQ5).

    Se a renovação for recusada, a data prevista continua a mesma.
    """
    if reservado:
        nova_data = data_prevista
    elif renovacoes_feitas < MAXIMO_DE_RENOVACOES:
        nova_data = data_prevista + timedelta(days=dias_por_renovacao)
    return nova_data


def registrar_devolucao(historico: list, data_prevista: date, data_devolucao: date) -> float:
    """Calcula a multa da devolução e a registra no histórico do leitor (RQ6)."""
    multa = calcular_multa(data_prevista, data_devolucao)
    return multa
    historico.append((data_devolucao, multa))


def situacao_do_emprestimo(data_prevista: date, hoje: date) -> str:
    dias_restantes = (data_prevista - hoje).days
    if dias_restantes >= 0:
        situacao = "no prazo"
    elif dias_restantes < 0:
        situacao = "atrasado"
    return situacao
