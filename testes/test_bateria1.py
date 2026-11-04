"""Bateria 1.

Casos que João apresentou à bibliotecária no dia da entrega,
um para cada regra do balcão.
"""

from datetime import date

from biblioteca import (
    calcular_multa,
    calcular_prazo,
    pode_emprestar,
    renovar,
    situacao_do_emprestimo,
)


def test_leitor_sem_livros_e_sem_multa_pode_emprestar():
    """RQ1 e RQ2: quem não tem livros nem multa pode levar um livro."""
    assert pode_emprestar(0, 0.0) is True


def test_leitor_com_multa_nao_pode_emprestar():
    """RQ2: quem tem multa pendente não pode levar outro livro."""
    assert pode_emprestar(1, 2.50) is False


def test_prazo_comum_de_14_dias():
    """RQ3: livro comum emprestado em 03/11 deve voltar até 17/11."""
    assert calcular_prazo(date(2026, 11, 3), False) == date(2026, 11, 17)


def test_devolucao_antes_do_prazo_sem_multa():
    """RQ4: livro devolvido antes da data prevista não gera multa."""
    assert calcular_multa(date(2026, 11, 16), date(2026, 11, 10)) == 0.0


def test_devolucao_com_3_dias_de_atraso():
    """RQ4: três dias de atraso custam R$ 1,50."""
    assert calcular_multa(date(2026, 11, 16), date(2026, 11, 19)) == 1.50


def test_primeira_renovacao_acrescenta_14_dias():
    """RQ5: a renovação acrescenta 14 dias à data prevista."""
    assert renovar(date(2026, 11, 16), 0, False) == date(2026, 11, 30)


def test_situacao_de_emprestimo_no_prazo():
    """Tela do balcão: empréstimo que vence daqui a três dias está no prazo."""
    assert situacao_do_emprestimo(date(2026, 11, 16), date(2026, 11, 13)) == "no prazo"
