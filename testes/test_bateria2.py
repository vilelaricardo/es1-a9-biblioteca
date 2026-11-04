"""Bateria 2.

Casos que Renata, colega de João, escreveu depois da entrega,
procurando situações que o programa poderia tratar mal.
"""

from datetime import date

from biblioteca import calcular_multa, calcular_prazo, pode_emprestar, renovar


def test_leitor_com_3_livros_nao_pode_emprestar():
    """RQ1: quem já está com três livros não pode levar o quarto."""
    assert pode_emprestar(3, 0.0) is False


def test_leitor_com_multa_de_50_centavos_nao_pode_emprestar():
    """RQ2: qualquer multa pendente impede o empréstimo, mesmo pequena."""
    assert pode_emprestar(0, 0.50) is False


def test_prazo_de_lancamento_de_7_dias():
    """RQ3: lançamento emprestado em 03/11 deve voltar até 10/11."""
    assert calcular_prazo(date(2026, 11, 3), True) == date(2026, 11, 10)


def test_devolucao_no_ultimo_dia_sem_multa():
    """RQ4: devolver na própria data prevista não gera multa."""
    assert calcular_multa(date(2026, 11, 16), date(2026, 11, 16)) == 0.0


def test_devolucao_com_12_dias_de_atraso():
    """RQ4: doze dias de atraso custam R$ 6,00."""
    assert calcular_multa(date(2026, 11, 16), date(2026, 11, 28)) == 6.00


def test_multa_limitada_a_10_reais():
    """RQ4: trinta dias de atraso custariam R$ 15,00, mas a multa para em R$ 10,00."""
    assert calcular_multa(date(2026, 11, 16), date(2026, 12, 16)) == 10.00


def test_renovacao_recusada_quando_ha_reserva():
    """RQ5: livro reservado por outro leitor não pode ser renovado."""
    assert renovar(date(2026, 11, 16), 0, True) == date(2026, 11, 16)


def test_segunda_renovacao_permitida():
    """RQ5: quem renovou uma vez ainda pode renovar a segunda."""
    assert renovar(date(2026, 11, 30), 1, False) == date(2026, 12, 14)
