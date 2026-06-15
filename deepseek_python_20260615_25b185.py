#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 2
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 41 a 63)
"""

import random
import os

# Banco de questões do TEMA 2
questoes_tema2 = [
    # ===================== TÓPICO 1.1 - HISTÓRICO DA CONSULTORIA (p.43-46) =====================
    {
        "topico": "1.1 Histórico da consultoria e assessoria organizacional",
        "subt": "Origem da consultoria",
        "pergunta": "A consultoria como atividade profissional de auxílio à gestão começou a se desenvolver a partir da metade do século XIX e início do XX, principalmente nos Estados Unidos, em função de:",
        "tipo": "mc",
        "opcoes": {
            "a": "A Revolução Industrial e a expansão das indústrias.",
            "b": "A Primeira Guerra Mundial e a necessidade de reestruturação militar.",
            "c": "A Grande Depressão de 1929.",
            "d": "O surgimento da internet e da globalização.",
            "e": "A criação da Organização das Nações Unidas."
        },
        "correta": "a",
        "pagina": "43",
        "explicacao": "Página 43: 'A consultoria, como atividade profissional de auxílio à gestão, acompanhou a evolução das organizações em tamanho e complexidade, a partir da metade do século XIX e início do XX, em função da grande expansão das indústrias, nos Estados Unidos (DONADONE, 2001).'"
    },
    {
        "topico": "1.1 Histórico da consultoria",
        "subt": "Consultoria no setor público",
        "pergunta": "Qual período histórico foi importante para dar força ao papel da consultoria no setor público, especialmente no auxílio ao gerenciamento militar e à administração federal?",
        "tipo": "mc",
        "opcoes": {
            "a": "Guerra do Vietnã.",
            "b": "Período da Segunda Guerra Mundial.",
            "c": "Crise de 1929.",
            "d": "Guerra Fria.",
            "e": "Revolução Russa."
        },
        "correta": "b",
        "pagina": "44",
        "explicacao": "Página 44: 'No ambiente governamental, também surgiram situações em que foi necessário contratar especialistas... com destaque para o período da Segunda Guerra Mundial... Esse momento foi importante para dar força ao papel da consultoria no setor público (DONADONE, 2003).'"
    },
    {
        "topico": "1.1 Histórico da consultoria",
        "subt": "Década de 1990",
        "pergunta": "Para Donadone (2005), a década de 1990 foi um período de grandes mudanças tecnológicas, reestruturação produtiva e modernas formas de gestão, marcado principalmente pela:",
        "tipo": "mc",
        "opcoes": {
            "a": "Revolução Industrial.",
            "b": "Globalização.",
            "c": "Crise do petróleo.",
            "d": "Criação da Embrapa.",
            "e": "Abolição da escravatura."
        },
        "correta": "b",
        "pagina": "44",
        "explicacao": "Página 44: 'Para Donadone (2005), o período da década de 1990 foi um tempo de grandes mudanças tecnológicas, de reestruturação produtiva e modernas formas de gestão, uma vez que foi um período marcado pela globalização.'"
    },
    {
        "topico": "1.1 Histórico da consultoria",
        "subt": "Setores com inovação tecnológica expressiva no Brasil",
        "pergunta": "De acordo com Scolari (2006), quais setores da economia brasileira apresentaram expressiva inovação tecnológica?",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas o setor industrial.",
            "b": "Automação bancária, aviação comercial, exploração de petróleo em águas profundas e agronegócio.",
            "c": "Somente o agronegócio.",
            "d": "Setor de serviços e comércio varejista.",
            "e": "Mineração e siderurgia."
        },
        "correta": "b",
        "pagina": "45",
        "explicacao": "Página 45: 'Há setores na economia brasileira onde ocorreu expressiva inovação tecnológica, como na automação bancária, na aviação comercial, na exploração de petróleo em águas profundas e no agronegócio (SCOLARI, 2006).'"
    },
    {
        "topico": "1.1 Histórico da consultoria",
        "subt": "Diferença entre consultoria e assessoria",
        "pergunta": "Verdadeiro ou Falso: A assessoria organizacional surgiu após a consolidação da consultoria, com a necessidade de profissionais exclusivos e atuação de longo prazo, focando em organizar e reorientar os principais setores funcionais da organização.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "45",
        "explicacao": "Página 45: 'Após a consolidação da prestação de serviços do tipo consultoria, evidenciou-se também a necessidade de contar com profissionais exclusivos e que atuem em longo prazo. É quando surge, de forma mais clara, os serviços de assessoria.'"
    },

    # ===================== TÓPICO 1.2 - EVOLUÇÕES E ESTRATÉGIAS (p.47-50) =====================
    {
        "topico": "1.2 Evoluções empresariais a partir dos métodos de consultoria",
        "subt": "Definição de estratégia",
        "pergunta": "Segundo Mintzberg e Quinn (1991), estratégia é definida como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Um conjunto de metas financeiras de curto prazo.",
            "b": "Um modelo ou plano que integra os objetivos, as políticas e as ações sequenciais de uma organização em um todo coeso.",
            "c": "Apenas o plano de marketing da empresa.",
            "d": "A redução de custos operacionais.",
            "e": "A alocação de recursos sem planejamento."
        },
        "correta": "b",
        "pagina": "48",
        "explicacao": "Página 48 - Glossário: 'Estratégia: é um modelo ou plano que integra os objetivos, as políticas e as ações sequenciais de uma organização em um todo coeso (MINTZBERG e QUINN, 1991).'"
    },
    {
        "topico": "1.2 Evoluções empresariais",
        "subt": "Tipos de estratégia - Sobrevivência",
        "pergunta": "Qual tipo de estratégia deve ser adotado quando a empresa não tem mais alternativas e se encontra em situação caótica, com dívidas e problemas graves?",
        "tipo": "mc",
        "opcoes": {
            "a": "Estratégia de manutenção.",
            "b": "Estratégia de desenvolvimento.",
            "c": "Estratégia de sobrevivência.",
            "d": "Estratégia de crescimento.",
            "e": "Estratégia de marketing."
        },
        "correta": "c",
        "pagina": "49",
        "explicacao": "Página 49: 'Estratégia de sobrevivência: Adotada quando a empresa não tem mais alternativas e se encontra em uma situação caótica.'"
    },
    {
        "topico": "1.2 Evoluções empresariais",
        "subt": "Tipos de estratégia - Manutenção",
        "pergunta": "A estratégia de manutenção é indicada para empresas que:",
        "tipo": "mc",
        "opcoes": {
            "a": "Estão em situação caótica.",
            "b": "Já têm pontos fortes e querem manter a posição conquistada, mas precisam se reinventar constantemente.",
            "c": "Estão em ambiente extremamente favorável com grandes oportunidades.",
            "d": "Não têm concorrência.",
            "e": "Desejam encerrar as atividades."
        },
        "correta": "b",
        "pagina": "49",
        "explicacao": "Página 49: 'Estratégia de manutenção: a empresa já têm pontos fortes, os quais são maximizados para tentar manter a posição conquistada até o momento... é preciso mesclar ações de manutenção e de diferenciação competitiva.'"
    },
    {
        "topico": "1.2 Evoluções empresariais",
        "subt": "Tipos de estratégia - Desenvolvimento",
        "pergunta": "Verdadeiro ou Falso: A estratégia de desenvolvimento é indicada para empresas que estão diante de um ambiente repleto de situações favoráveis, com oportunidades de crescimento, como a produção de frutas exóticas (pitaia) em franca expansão.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "50",
        "explicacao": "Página 50: 'Esse tipo de estratégia [desenvolvimento] é indicado para empresas que estão diante um ambiente repleto de situações favoráveis e que podem se tornar oportunidades de crescimento se aproveitadas efetivamente. Podemos citar como exemplo... a pitaia.'"
    },

    # ===================== TÓPICO 2 - TENDÊNCIAS DAS ÁREAS DE ASSESSORIA E CONSULTORIA (p.51-55) =====================
    {
        "topico": "2. Tendências das áreas de assessoria e consultoria",
        "subt": "Tendências tecnológicas",
        "pergunta": "De acordo com o material, qual das seguintes NÃO é citada como tendência para os serviços de assessoria e consultoria no agronegócio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Treinamento e desenvolvimento por meio de metodologias EaD e aplicativos multimídia.",
            "b": "Técnicas de programação para agricultura de precisão.",
            "c": "Desenvolvimento de aplicativos para rastreabilidade de alimentos.",
            "d": "Substituição completa do produtor rural por robôs.",
            "e": "Novos hábitos de consumo, como a carne vegetal."
        },
        "correta": "d",
        "pagina": "52",
        "explicacao": "Página 52 lista várias tendências: Treinamento e desenvolvimento, Técnicas de programação, Métodos de gerenciamento, Aplicativos e softwares, Novos hábitos de consumo. Não há menção à 'substituição completa do produtor por robôs'."
    },
    {
        "topico": "2. Tendências das áreas de assessoria e consultoria",
        "subt": "Digitalização da decisão do agricultor",
        "pergunta": "No contexto da 'digitalização da decisão do agricultor' (Prado et al., 2020), qual atividade adicional pós-disrupção digital é citada na fase de 'reconhecimento das necessidades'?",
        "tipo": "mc",
        "opcoes": {
            "a": "Ligar para distribuidor agrícola para cotar preços.",
            "b": "Sensores de diagnóstico da lavoura e conectividade por meio de IoT.",
            "c": "Processo de compra tradicional no horário comercial.",
            "d": "Avaliação do desempenho dos produtos localmente.",
            "e": "Compartilhamento de experiências por redes sociais."
        },
        "correta": "b",
        "pagina": "53",
        "explicacao": "Página 53, quadro: Na fase 'Reconhecimento das necessidades', as atividades adicionais pós-disrupção digital incluem 'Sensores de diagnóstico da lavoura' e 'Conectividade por meio de IoT, gerando mais informações'."
    },
    {
        "topico": "2. Tendências das áreas de assessoria e consultoria",
        "subt": "Dados do Censo Agropecuário 2017",
        "pergunta": "Segundo o último Censo Agropecuário de 2017, qual percentual de produtores declarou não receber orientação técnica?",
        "tipo": "mc",
        "opcoes": {
            "a": "39,9%",
            "b": "59,9%",
            "c": "79,8%",
            "d": "89,2%",
            "e": "49,7%"
        },
        "correta": "c",
        "pagina": "55",
        "explicacao": "Página 55: 'No último Censo Agropecuário de 2017 foi identificado que 79,8% dos produtores, nos estabelecimentos levantados pelo Censo, declararam não receber orientação técnica.'"
    },

    # ===================== TÓPICO 3 - TÉCNICOS EM AGRONEGÓCIO COMO ASSESSORES E CONSULTORES (p.55-63) =====================
    {
        "topico": "3. Os técnicos em agronegócio como assessores e consultores",
        "subt": "Competências do técnico em agronegócio",
        "pergunta": "De acordo com Borrás e Batalha (1998), o profissional para atuar na gestão do agronegócio deve unir:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas conhecimentos em tecnologia da informação.",
            "b": "Conhecimentos técnicos da produção agropecuária e sólida formação em gestão.",
            "c": "Somente habilidades em marketing e vendas.",
            "d": "Formação exclusiva em direito ambiental.",
            "e": "Experiência prática sem necessidade de estudo teórico."
        },
        "correta": "b",
        "pagina": "56",
        "explicacao": "Página 56: 'Um profissional, para atuar na gestão do agronegócio, deve unir conhecimentos técnicos, próprios da atividade da produção agropecuária e do processamento de seus produtos, a uma sólida formação em gestão (BORRÁS; BATALHA, 1998).'"
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Áreas de atuação do técnico em agronegócio",
        "pergunta": "Assinale a alternativa que NÃO corresponde a uma área de atuação típica do técnico em agronegócio, conforme o material:",
        "tipo": "mc",
        "opcoes": {
            "a": "Gestão da produção.",
            "b": "Gestão financeira e de custos.",
            "c": "Aplicação de insumos na lavoura (operações manuais).",
            "d": "Logística e cadeia de suprimentos.",
            "e": "Gestão de pessoas e legislação ambiental."
        },
        "correta": "c",
        "pagina": "57",
        "explicacao": "Página 57: 'Os técnicos em agronegócio poderão atuar mais diretamente nas áreas de gestão da produção, financeira e de custos, logística, pessoas, legislação ambiental, marketing e vendas.' A aplicação de insumos é mais típica de técnicos agrícolas/agropecuários."
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Papel do assessor",
        "pergunta": "Segundo Caetano (2000), o assessor é responsável por informar sobre mudanças no ambiente externo (como novas legislações) que impactam diretamente o contexto interno da empresa rural. Verdadeiro ou Falso?",
        "tipo": "vf",
        "correta": "V",
        "pagina": "58-59",
        "explicacao": "Página 58-59: 'O assessor é responsável por informar, por exemplo, sobre a iminência da aprovação de uma nova legislação ambiental que impactará diretamente o modelo de negócio da empresa rural. Para Caetano (2000), nesse cenário, os sistemas e subsistemas sofrem mudanças internas devido ao ambiente externo.'"
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Serviços de assessoria: áreas abrangidas",
        "pergunta": "De acordo com o material, os serviços de assessoria dos técnicos em agronegócio abrangem as áreas de produção, finanças, comercialização e pessoas. Nesse contexto, a área de 'comercialização' é responsável por:",
        "tipo": "mc",
        "opcoes": {
            "a": "Administrar o capital financeiro e fluxos de caixa.",
            "b": "Cuidar dos colaboradores e planejamento de recursos humanos.",
            "c": "Analisar canais de distribuição, negociação de preços e venda dos produtos.",
            "d": "Controlar o uso de insumos e produtividade por hectare.",
            "e": "Gerenciar a compra de sementes e fertilizantes."
        },
        "correta": "c",
        "pagina": "60",
        "explicacao": "Página 60: 'Comercialização: É o setor responsável pela análise e pela identificação dos canais de distribuição, além de negociação de preços com os clientes e venda dos produtos.'"
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Maturidade profissional do consultor",
        "pergunta": "O material afirma que a 'maturidade profissional' para atuar como consultor não se refere à idade, mas sim:",
        "tipo": "mc",
        "opcoes": {
            "a": "Ao tempo de serviço público.",
            "b": "Às competências profissionais obtidas por meio de experiências, estudos, diagnósticos e identificação de problemas.",
            "c": "Ao número de clientes atendidos.",
            "d": "À formação exclusiva em mestrado ou doutorado.",
            "e": "À capacidade de vender serviços a qualquer custo."
        },
        "correta": "b",
        "pagina": "60-61",
        "explicacao": "Página 60-61: 'Quando se fala em maturidade profissional, não nos referimos à idade da pessoa, mas às competências profissionais obtidas durante as experiências profissionais, os desafios superados, além do estudo, e à aplicação dos diagnósticos, bem como à identificação de problemas no mundo do trabalho e nas organizações.'"
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Requisitos do consultor",
        "pergunta": "Segundo o material, além de sólida formação, o consultor em agronegócio precisa ter visão de longo prazo, raciocínio lógico, bom senso e, fundamentalmente:",
        "tipo": "mc",
        "opcoes": {
            "a": "Saber lidar e se comunicar com as pessoas.",
            "b": "Ter um veículo 4x4.",
            "c": "Possuir um escritório em área nobre.",
            "d": "Ter mais de 10 anos de experiência.",
            "e": "Ser filho de produtor rural."
        },
        "correta": "a",
        "pagina": "62",
        "explicacao": "Página 62: 'Outro aspecto fundamental e básico, mas por vezes negligenciado, é o entendimento da importância do profissionalismo no contexto das relações interpessoais. Consultor tem que saber lidar e se comunicar com as pessoas!'"
    },
    {
        "topico": "3. Técnicos em agronegócio",
        "subt": "Ética profissional",
        "pergunta": "Qual associação brasileira orienta consultores organizacionais quanto ao cumprimento de princípios éticos e de conduta profissional?",
        "tipo": "mc",
        "opcoes": {
            "a": "Associação Brasileira de Agronegócio (ABAG)",
            "b": "Associação Brasileira de Consultores (ABCO)",
            "c": "Conselho Federal de Técnicos Agrícolas (CFTA)",
            "d": "Sociedade Brasileira de Administração Rural (SOBER)",
            "e": "Organização das Cooperativas Brasileiras (OCB)"
        },
        "correta": "b",
        "pagina": "63",
        "explicacao": "Página 63 - Saiba mais: 'A Associação Brasileira de Consultores orienta todos os consultores organizacionais brasileiros e exige de seus associados o cumprimento de princípios éticos e de conduta profissional no exercício de suas atividades.'"
    }
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 2)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 2.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 41 a 63) antes da prova.")
    print("="*70)

def fazer_questao(q, num, total):
    print(f"\nQuestão {num} de {total}")
    print(f"Tópico: {q['topico']} | Subtópico: {q['subt']}")
    print("-"*70)
    print(q['pergunta'])
    print()
    if q['tipo'] == 'mc':
        for letra, texto in q['opcoes'].items():
            print(f"   {letra.upper()}) {texto}")
        print()
        while True:
            resp = input("Digite a letra da sua resposta (a, b, c, d, e): ").strip().lower()
            if resp in ['a','b','c','d','e']:
                break
            print("Opção inválida. Digite a, b, c, d ou e.")
        acertou = (resp == q['correta'])
        if acertou:
            print("\n✅ CORRETO!")
        else:
            print(f"\n❌ ERRADO. A alternativa correta é: {q['correta'].upper()}")
    else:  # verdadeiro/falso
        while True:
            resp = input("Digite V (Verdadeiro) ou F (Falso): ").strip().upper()
            if resp in ['V','F']:
                break
            print("Opção inválida. Digite V ou F.")
        acertou = (resp == q['correta'])
        if acertou:
            print("\n✅ CORRETO!")
        else:
            print(f"\n❌ ERRADO. A resposta correta é: {q['correta']}")
    print(f"\n📖 REFERÊNCIA (PDF): Página {q['pagina']}")
    print(f"📘 EXPLICAÇÃO: {q['explicacao']}")
    return acertou

def main():
    limpar_tela()
    print("="*70)
    print("   SIMULADOR DE PREPARAÇÃO PARA PROVA")
    print("   CURSO TÉCNICO EM AGRONEGÓCIO - SENAR")
    print("   MÓDULO: ASSESSORIA, CONSULTORIA E INOVAÇÃO")
    print("   TEMA 2: TENDÊNCIAS E PERSPECTIVAS PARA SERVIÇOS")
    print("          DE ASSESSORIA E CONSULTORIA NO AGRONEGÓCIO")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema2)} questões")
    print("cobrindo todos os tópicos do Tema 2 (páginas 41 a 63).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões
    questoes = random.sample(questoes_tema2, len(questoes_tema2))
    acertos = 0
    total = len(questoes)
    
    for i, q in enumerate(questoes, 1):
        limpar_tela()
        if fazer_questao(q, i, total):
            acertos += 1
        input("\nPressione Enter para a próxima questão...")
    
    limpar_tela()
    mostrar_resultado(acertos, total)

if __name__ == "__main__":
    main()