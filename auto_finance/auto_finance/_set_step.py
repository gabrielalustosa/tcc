from auto_finance.models.steps import Step


def definir_steps(
    processo_ctx,
):
    steps = []
    step0 = Step(
        nome='Teste',
        descricao='teste',
        objeto=processo_ctx,
        funcao='teste',
    )

    steps.extend([step0])

    return steps
